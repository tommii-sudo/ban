# douban black-list automation tool
## dependency:
1.安装 
[splinter](https://splinter.readthedocs.io/en/latest/install.html), pyyaml


运行
```
pip install -r requirements.txt
```
2.下载 firefox driver
[firefox for splinter](https://splinter.readthedocs.io/en/latest/drivers/firefox.html)
，[geckodriver download](https://github.com/mozilla/geckodriver/releases)

spider目录下已有firefox driver-linux-64和firefox driver-windows-64驱动

3.chrome driver
[chrome for splinter](https://splinter.readthedocs.io/en/latest/drivers/chrome.html)
，[chromedriver download](https://sites.google.com/a/chromium.org/chromedriver/downloads)

根据版本选择对应驱动
- If you are using Chrome version 77, please download [ChromeDriver 77.0.3865.10](https://chromedriver.storage.googleapis.com/index.html?path=77.0.3865.10/)
- If you are using Chrome version 76, please download [ChromeDriver 76.0.3809.68](https://chromedriver.storage.googleapis.com/index.html?path=76.0.3809.68/)
- If you are using Chrome version 75, please download [ChromeDriver 75.0.3770.140](https://chromedriver.storage.googleapis.com/index.html?path=75.0.3770.140/)

解压后放到spider目录。

4.将该目录添加到PATH变量中

linux
```
export PATH=$('pwd')/spider:$PATH

```
windows:
```
//todo
```


## usage :
写入需要拉入黑名单的小组网址
在blacklist.yaml， 按照固定格式
```
- url1
- url2
```

运行:
```
python app.py blacklist.yaml

```
