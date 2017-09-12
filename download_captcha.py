# -*- coding: utf-8 -*-

import urllib
import json
import base64
import time

def downloadCtripCaptcha():
    url = 'https://accounts.ctrip.com/member/ajax/AjaxChkBWGAndVerifyCode.ashx?username=18701439558&st=sgo'
    data = json.loads(urllib.urlopen(url).read())
    imgData = base64.b64decode(data['Image'])
    fn = 'captcha/' + str(time.time()) + '.jpg'
    fw = open(fn, 'wb')
    fw.write(imgData)
    fw.close()
    return fn

for i in range(100):
    print(i, downloadCtripCaptcha())
    time.sleep(1)
