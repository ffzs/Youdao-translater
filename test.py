#encoding:utf-8

from tkinter import Tk,Button,Entry,Label,Text,END

class Application(object):

    def __init__(self):
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
        self.result.delete(1.0,END)
        self.result.insert(END,content)


    def run(self):
        self.window.mainloop()

if __name__ == '__main__':
    app = Application()
    app.run()
