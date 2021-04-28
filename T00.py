import wx  #导入wx模块


#初始化应用程序（创建应用程序对象）
app=wx.App() 
#创建一个窗体*(创建窗口对象)
#  None表示没有所在的父窗口
# size：窗口的大小； pos:窗口的位置
frame=wx.Frame(None,title="第一个wxPython程序！",size=(400,300),pos=(100,100))

#显示窗体（显示窗口）
#窗口默认隐藏，需要调用show()方法才能显示
frame.Show()

#请求实例开始事件（进入主事件循环）
#让应用程序进入主事件循环中
app.MainLoop()