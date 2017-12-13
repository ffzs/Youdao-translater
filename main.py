#encoding: utf_8

import urllib.request
import urllib.parse
import time
import random
import hashlib
from tkinter import Tk,Button,Entry,Label,Text,END
import json

class YouDao_translater(object):
    def __init__(self):
        pass

    def crawl(self,content):
        headers = {
            'Referer':'http://fanyi.youdao.com/',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
        }
        timestamp = int(time.time()*1000) + random.randint(0,10)
        u = "fanyideskweb"
        d = content
        f = str(timestamp)
        c = "rY0D^0'nM0}g5Mm1z%1G4"

        sign = hashlib.md5((u+d+f+c).encode('utf_8')).hexdigest()

        data = {
            'i':content,
            'from':'AUTO',
            'to':'AUTO',
            'smartresult':'dict',
            'client':'fanyideskweb',
            'salt':timestamp,
            'sign':sign,
            'doctype':'json',
            'version':'2.1',
            'keyfrom':'fanyi.web',
            'action':'FY_BY_CLICKBUTTION',
            'typoResult':'false'
        }
        data = urllib.parse.urlencode(data).encode('utf-8')
        requset = urllib.request.Request(url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom=",method='POST',data=data,headers=headers)
        response = urllib.request.urlopen(requset)
        result_dict = response.read().decode('utf-8')
        result_dict = json.loads(result_dict)
        result =  result_dict["translateResult"][0][0]['tgt']
        return result

class Application(object):

    def __init__(self):
        self.helper = YouDao_translater()
        self.window = Tk()
        self.window.title(u'泛泛词典')
        self.window.geometry('275x350+300+100')

        self.entry = Entry(self.window)
        self.entry.place(x=10,y=10,width=200, height=25)

        self.submit_btn = Button(self.window,text ='查询',command=self.submit)
        self.submit_btn.place(x=215,y=10,width =50, height=25)

        self.title_label = Label(self.window,text="翻译结果：")
        self.title_label.place(x=10,y=50)

        self.result = Text(self.window,background="#ccc")
        self.result.place(x=10,y=75,width=255,height=265)

    def submit(self):
        content = self.entry.get()
        result = self.helper.crawl(content)
        self.result.delete(1.0,END)
        self.result.insert(END,result)

    def run(self):
        self.window.mainloop()

if __name__ == '__main__':
    app = Application()
    app.run()

