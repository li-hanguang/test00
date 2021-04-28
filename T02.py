import wx  #导入wx模块

#定义有默认值属性的表（自定义窗口类MyFrame）
class MyFrame(wx.Frame): 
    def __init__(self):
        super().__init__(None,title="事件处理",size=(300,180))
        panel = wx.Panel(parent=self)
        self.statictext = wx.StaticText(panel, label='请单击OK按钮', pos=(110,20))

        #创建按钮对象
        b = wx.Button(panel, label='OK', pos=(100,50))
        #绑定事件，wx.EVT_BUTTON是事件类型，即按钮单击事件；self.on_click是事件处理程序；b是实践源，即按钮对象
        self.Bind(wx.EVT_BUTTON, self.on_click, b)

    #事件处理程序
    def on_click(self,event):
        self.statictext.SetLabelText('Hello World!')    



# 创建应用程序对象
app = wx.App()  #创建一个实例

# 创建窗口对象
frm = MyFrame()
#显示窗口
frm.Show()

#请求实例开始事件（进入主事件循环）
app.MainLoop()