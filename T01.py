# coding=utf-8
import wx  #导入wx模块

#定义有默认值属性的表（自定义窗口类MyFrame）
class MyFrame(wx.Frame): 
    def __init__(self):
        super().__init__(None,title="第一个wxPython程序！",size=(400,300),pos=(100,100))
        #你的代码
        #参数 parent传递的是self，即设置面板所在地父容器为当前窗口对象
        panel = wx.Panel(parent=self)
        #创建静态文本（StaticText）对象，将静态文本对象放到panel面板中，
        #所以parent参数传递的是panel，参数label是在静态文本对象上显示的文字，参数pos用于设置静态文本对象的位置
        statictext = wx.StaticText(panel, label='Hello World!', pos=(10,10))



# 创建应用程序对象
app = wx.App()  #创建一个实例

# 创建窗口对象
frm = MyFrame()
#显示窗口
frm.Show()

#请求实例开始事件（进入主事件循环）
app.MainLoop()