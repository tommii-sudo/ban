
from splinter import Browser
import argparse
import re
from bs4 import BeautifulSoup
import yaml
import os
import time
import csv
from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper



class WebDriver():
    def __init__(self):
        self.browser = Browser('chrome',user_agent="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0)")

    def visit(self, url, text = None):
        print("loading " , url)

        self.browser.visit(url)
        if(not text is None):
            load_done = self.browser.is_text_present(text)
            while(not load_done):
                load_done = self.browser.is_text_present(text)
                time.sleep(0.05)
            print("loading ok" , url)

    @property
    def html(self):
        return self.browser.html
    



class DoubanDriver:
    def __init__(self):
        self.loginDone = False
        self.url = "https://www.douban.com/contacts/list"
        self.contacts_list_url = "https://www.douban.com/contacts/list?tag=0&start="
        self.contacts_list = set()
        self.contacts_page_step = 20

        self.driver = WebDriver()
        self.browser = self.driver.browser

    def login(self):
        if (not self.loginDone):
            print("\n-- try login, wait")
            self.driver.visit(self.url, u"我的豆瓣")
        self.loginDone = True

    def isUserValid(self, url):
        self.driver.visit(url, u"关于豆瓣")
        valid = self.browser.is_text_present(u"广播")
        return valid

    def isGroupValid(self, url):
        self.driver.visit(url, u"关于豆瓣")
        valid = self.browser.is_text_present(u"最近讨论")
        return valid

    def visit(self, url, text = None):
        if (text is None):
            self.driver.visit(url, u"关于豆瓣")
        else:
            self.driver.visit(url, text)


    def parseUser(self, html):
        soup = BeautifulSoup(html,features="html.parser")
        people_list = soup.find_all("a", href=re.compile("https://www.douban.com/people"))
        people_list = set([pi.attrs["href"] for pi in people_list])
        people_list = set(people_list)
        return people_list

    def findLink(self, text):
        b = self.browser.find_link_by_partial_text(text)
        return len(b) > 0


    def getContactList(self, start = 0):
        if(not self.loginDone):
            self.login()

        start_url = self.contacts_list_url + str(start)
        self.visit(start_url, u"我关注的人")

        
        # get list
        html = self.driver.html
        people_list = self.parseUser(html)

        self.contacts_list = self.contacts_list.union(people_list)
        # check next page
        if(self.findLink(u"后页")):
            self.getContactList(start + self.contacts_page_step)



        
    def blockUser(self, user_url):
        if(not self.isUserValid(user_url)):
            return

        b = self.browser.find_by_xpath("/html/body/div[3]/div[1]/div/div[2]/div[1]/div/div[2]/div[2]/div[2]/a")
        if(len(b) == 0):
            return

        b[0].click()
        time.sleep(0.05)
        bb = self.browser.find_by_id("add-to-blacklist")
        bb[0].click()
        time.sleep(0.051)
        alert = self.browser.get_alert()
        cnt = 0
        while( alert is None and cnt < 10):
            time.sleep(0.01)
            cnt += 1

        if(not alert is None):
            print(alert.text)
            # alert.accept() # click ok
            alert.dismiss() # click cancel


        
    def blockUserList(self, user_list):
        user_list.difference_update(self.contacts_list)
        for u in user_list:
            print("block ", u)

            self.blockUser(u)

        print("block done")


    def getMember(self, url, start = 0 ):
        start_url = url + str(start)

        self.visit(start_url)
        html = self.driver.html
        people_list = self.parseUser(html)
        self.member_list = self.member_list.union(people_list)

        # check next page
        if(self.findLink(u"后页")):
            self.getMember(url, start + self.members_page_step)


    def scanGroup(self, url):
        if(not self.isGroupValid(url)):
            print(url, "is not valid")
            return
        
        self.getMember(self.browser.url + "members?start=")

    def getGroupMembers(self, group_list):
        self.group_list = group_list

        self.members_page_step = 35
        self.member_list = set()

        for g in self.group_list:
            self.scanGroup(g)

    def dump(self):
        with open('member_list.csv', 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for i in self.member_list:
                spamwriter.writerow([i])

        with open('contacts_list.csv', 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for i in self.contacts_list:
                spamwriter.writerow([i])



