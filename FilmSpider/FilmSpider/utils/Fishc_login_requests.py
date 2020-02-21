# 鱼C论坛的登录

# username: shen1986
# password: 4456d776d1c73dddaa25d88b317ace7b
# quickforward: yes
# handlekey: ls

# https://fishc.com.cn/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes&inajax=1

import requests
try:
    import cookielib
except:
    import http.cookiejar as cookielib

import re

session = requests.session()
session.cookies = cookielib.LWPCookieJar(filename="cookies.txt")
try:
    session.cookies.load(ignore_discard=True)
except:
    print ("cookie未能加载")

agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36"
header = {
    "HOST": "fishc.com.cn",
    "Referer": "https://fishc.com.cn/",
    "User-Agent": agent
}

def is_login():
    #通过个人中心页面返回状态码来判断是否为登录状态
    inbox_url = "https://fishc.com.cn/thread-51842-1-1.html"
    response = session.get(inbox_url, headers=header, allow_redirects=False)
    if response.status_code != 200:
        return False
    else:
        return True

# 鱼Clogin
def fish_c_login(account, password):
    print("鱼C-login")
    post_url = "https://fishc.com.cn/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes&inajax=1"
    post_data = {
        "username": account,
        "password": password,
        "quickforward": "yes",
        "handlekey": "ls"
    }
    response_text = session.post(post_url, data=post_data, headers=header)
    session.cookies.save()

if __name__ == "__main__":
    fish_c_login("shen1986", "4456d776d1c73dddaa25d88b317ace7b")

    print(is_login())