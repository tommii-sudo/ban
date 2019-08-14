
from spider.douban_spider import *

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(description='Process some integers.')
    # parser.add_argument('group', metavar='group', type=str, nargs='+')
    parser.add_argument('group', metavar='group', type=str)

    args = parser.parse_args()
    print(args.group)
    stream = open(args.group, 'r')
    group_list = yaml.load(stream,Loader=Loader)

    douban = DoubanDriver()

    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(douban.getGroupMembers(group_list))
    douban.getGroupMembers(group_list)
    print(len(douban.member_list))
    douban.createBrowser()

    douban.login()


    # test part of list
    douban.member_list = set(list(douban.member_list)[:3])
    douban.blockUserList(douban.member_list)



    



