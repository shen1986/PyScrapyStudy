# PyScrapyStudy
scrapy 爬虫学习

## pip安装慢的时候可以用豆瓣的镜像来安装
https://pypi.douban.com/simple/

- 使用方法：
```
sudo pip install -i https://pypi.douban.com/simple/ saltTesting
```

## Mac下搭建python虚拟环境
https://www.jianshu.com/p/7cc87bddb7e1

升级pip
pip3 install --upgrade pip

安装virtualenv
pip install virtualenv

安装 virtualenvwrapper， Virtaulenvwrapper是virtualenv的扩展包，可以更方便地新增，删除，复制，切换虚拟环境。
pip install virtualenvwrapper

创建存放虚拟环境的文件夹
mkdir ~/.virtualenvs

进入存放虚拟环境的文件夹
cd ~/.virtualenvs

查找python3和virtualenvwrapper.sh的路径
which python3

which virtualenvwrapper.sh

! 我的python3路径为：

/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

! 我的virtualenvwrapper.sh路径为：

/Library/Frameworks/Python.framework/Versions/3.7/bin/virtualenvwrapper.sh

打开环境变量设置
open ~/.bash_profile

打开文本编辑器后，在最下面添加
export WORKON_HOME='~/.virtualenvs'

export VIRTUALENVWRAPPER_PYTHON='/Library/Frameworks/Python.framework/Versions/3.7/bin/python3'

(此为你的python3路径)

source /Library/Frameworks/Python.framework/Versions/3.7/bin/virtualenvwrapper.sh

保存后在终端输入
source ~/.bash_profile

虚拟环境搭建成功，接下来可以创建虚拟环境，进入.virtualenvs在终端输入

mkvirtualenv -p python3 xxx

在终端输入 workon 虚拟环境名称 即可进入
输入deactivate即可退出虚拟环境
输入rmvirtualenv xxx删除虚拟环境
输入workon已存在的虚拟环境

## 解决Mac上安装mysqlclient的错误
- PATH="$PATH":/usr/local/mysql/bin/
- mysql_config
- 之后pip install mysqlclient

## 要用 pip 安装指定版本的 Python 包，只需通过 == 操作符 指定
pip install robotframework==2.8.7