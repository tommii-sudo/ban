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
[geckodriver download](https://github.com/mozilla/geckodriver/releases)

spider目录下已有linux-64和windows-64驱动
将该目录添加到PATH变量中

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










