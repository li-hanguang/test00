#布局管理
#盒子布局管理器
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

        #创建垂直方向的盒子布局管理对象vbox
        vbox = wx.BoxSizer(wx.VERTICAL)
        #添加静态文本到Vbox布局管理器\两个控件proportion都为1，所以两个控件各占二分之一，flag|控件水平居中|刚好包裹控件|设置顶部有边框，设置顶部边框宽度为30
        vbox.Add(self.statictext, proportion=1,flag=wx.ALIGN_CENTER_HORIZONTAL|wx.FIXED_MINSIZE|wx.TOP, border=30)
        #添加按钮b到vbox布局管理器 \flag|填满有效空间|设置底边有边框，底部边框宽度为10
        vbox.Add(b, proportion=1, flag=wx.EXPAND|wx.BOTTOM, border=10)
        #设置面板（panel）采用vbox布局管理器
        panel.SetSizer(vbox) #两个控件都放到面板中，所以需要设置面板布局为盒子布局


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