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

import requests

response = requests.get("https://www.dytt8.net/")

print(response.text)