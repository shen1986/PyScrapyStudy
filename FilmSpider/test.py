import re

testStr = '\r\n\r\n\r\n\r\n发布时间：2020-02-02  \r\n \r\n \r\n\r\n'

re_match = re.match(".*(\d+[-]\d+[-]\d+).*", testStr)

if re_match:
    print(re_match.group(1))

print("aa")