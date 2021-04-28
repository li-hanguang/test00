#盒子布局管理器嵌套
import wx  #导入wx模块

#定义有默认值属性的表（自定义窗口类MyFrame）
class MyFrame(wx.Frame): 
    def __init__(self):
        super().__init__(None,title="布局管理器嵌套",size=(300,120))
        panel = wx.Panel(parent=self)
        self.statictext = wx.StaticText(panel, label='请单击按钮')
        #创建按钮对象
        b1 = wx.Button(panel,id=10, label='Button1')
        b2 = wx.Button(panel,id=11, label='Button2')
        #绑定id为参数id~id2的按钮，参数id是开始按钮的id，参数id2是结束按钮的id
        self.Bind(wx.EVT_BUTTON, self.on_click, id=10, id2=20)

        #创建水平方向的盒子布局管理器hbox对象
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        #添加b1到hbox布局管理器
        hbox.Add(b1, proportion=1, flag=wx.EXPAND|wx.ALL, border=10)
        #添加b2到hbox布局管理器
        hbox.Add(b2, proportion=1, flag=wx.EXPAND|wx.ALL, border=10)


        #创建垂直方向的盒子布局管理对象vbox
        vbox = wx.BoxSizer(wx.VERTICAL)
        #添加静态文本到Vbox布局管理器
        vbox.Add(self.statictext, proportion=1,flag=wx.CENTER|wx.FIXED_MINSIZE|wx.TOP, border=10)
        #将水平hbox布局管理器对象添加到垂直vbox布局管理器对象
        vbox.Add(hbox, proportion=1, flag=wx.CENTER)

        #设置面板（panel）采用vbox布局管理器
        panel.SetSizer(vbox) #两个控件都放到面板中，所以需要设置面板布局为盒子布局


    #事件处理程序
    def on_click(self,event):
        event_id = event.GetId()  #获得绑定按钮的id
        print(event_id)
        if event_id == 10:       #根据id判断单击了哪一个按钮
            self.statictext.SetLabelText('Button1单击')
        else:
            self.statictext.SetLabelText('Button2单击')




# 创建应用程序对象
app = wx.App()  #创建一个实例

# 创建窗口对象
frm = MyFrame()
#显示窗口
frm.Show()

#请求实例开始事件（进入主事件循环）
app.MainLoop()