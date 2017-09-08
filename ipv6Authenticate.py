#coding=gbk
import urllib
import httplib

data = {'DDDDD':'student_id', 'upass':'password', '0MKKey':'登　录', 'v6ip':'', 'sava_me':'0'}
data_urlencode = urllib.urlencode(data)
requestURL = "http://ip6.upc6.edu.cn/0.htm"
headerData = {"Host":"ip6.upc6.edu.cn"}
# ip6.upc6.edu.cn/[2001:da8:7007::3]
conn = httplib.HTTPConnection("ip6.upc6.edu.cn",80)
conn.request(method = "POST", url = requestURL, body=data_urlencode, headers=headerData)
response = conn.getresponse()
res = response.read()
#print res
if res.find('登录成功窗') != -1:
    print "登录成功"
elif res.find('信息返回窗') != -1:
    print "登录失败"
else:
    print 'error'
