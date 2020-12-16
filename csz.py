#!/usr/bin/env python
# coding: utf-8

# In[17]:


import tkinter
import tkinter.messagebox
import math
import random

root = tkinter.Tk()
root.title('猜数字')
root.geometry('800x800')
num1=random.randint(1,100)


def cai_shu_zi():
    guess=num.get()
    guess=int(guess)

    if guess =='' :
        tkinter.messagebox.showerror("输入不能为空")
    if guess > num1:
        tkinter.messagebox.showinfo("太大了","你猜的太大了")
    if guess < num1:
        tkinter.messagebox.showinfo("太小了","你猜的太小了")
    if guess == num1:
        tkinter.messagebox.showinfo("恭喜你你猜对了")

label = tkinter.Label(root,text='Wellcome to our game!',font=(16))
label.place(x=10,y=40,height=30,width=250)

labelNum = tkinter.Label(root,text='请输入你猜的数字')
labelNum.place(x=10,y=120,height=30,width=150)

num = tkinter.StringVar(root)
entryNum = tkinter.Entry(root,width=150,textvariable=num)
entryNum.place(x=150,y=120,height=30,width=80)

button = tkinter.Button(root,text='确定',command=cai_shu_zi)
button.place(x=50,y=150,height=30,width=80)  
root.mainloop()


# In[ ]:




