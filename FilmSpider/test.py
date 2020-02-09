# import re
#
# testStr = '<br>◎IMDb评分 8.2/10 from 107423 users <br>'
#
# re_match = re.match('.*IMDb评分 ?(\d+[.]\d+).*', testStr)
#
# if re_match:
#     print(re_match.group(1))
#
# pass

# import requests
#
# response = requests.get("https://www.dytt8.net/")
#
# print(response.text)

# from fake_useragent import UserAgent
# ua = UserAgent(verify_ssl=False)

# print(ua.random)

from selenium.webdriver import Chrome
import  time

browser = Chrome(executable_path='/Users/shen112/downloads/common/selenium-chromedriver/chromedriver')

browser.get('https://www.zhihu.com/')

time.sleep(3)

browser.find_element_by_css_selector(".SignFlow-tabs .SignFlow-tab:nth-child(2)").click()
time.sleep(3)

browser.find_element_by_css_selector("input[name=username]").send_keys("15601980930")
time.sleep(3)

browser.find_element_by_css_selector("input[name=password]").send_keys("shen5801A")

time.sleep(3)

browser.find_element_by_css_selector(".SignFlow-submitButton").click()

print(browser.page_source)

browser.quit()