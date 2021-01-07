# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 19:50:04 2019

@author: lenovo
"""
# pyinstaller -i logo.ico window.py --noconsole
# 创建GUI窗口打开图像 并显示在窗口中

from PIL import Image, ImageTk # 图像处理函数库
import tkinter as tk           # GUI界面函数库


def resize( w_box, h_box, pil_image): #窗口宽、高、图片
     w, h = pil_image.size #获取图像的原始大小   
     f1 = 1.0*w_box/w 
     f2 = 1.0*h_box/h    
     factor = min([f1, f2])   
     width = int(w*factor)    
     height = int(h*factor)    
     return pil_image.resize((width, height), Image.ANTIALIAS) 

class Main(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        #INTEGER
        self.string = tk.StringVar()
        
        #BUTTONS
        
        Label=tk.Label(self,text='请输入epoch(位于0到4950之间且为50的整数倍):')
        Label.pack()
        #ENTRY
        self.entry0 = tk.Entry(self, textvariable=self.string, width=8)
        self.entry0.pack()
        
        # 创建显示图像按钮
        self.btn_Show = tk.Button(self,text='更新图像',width=10, height=1,command=lambda:self.Show_Img())
        self.btn_Show.pack()    # 按钮位置
        

    def Show_Img(self):
        self.Img = Image.open('.\\output\\epoch'+self.string.get()+'.jpg')
        self.Img = resize(512,512, self.Img)
        self.img_png = ImageTk.PhotoImage(self.Img)
        self.label_Img = tk.Label(self, image=self.img_png)
        self.label_Img.place(x=50,y=75)

window=Main()
window.title('GAN生成动漫人物')
window.geometry('600x600')
# 运行整体窗口
window.mainloop()

