#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 06:57:43 2020

@author: ken
"""

import tkinter as tk

def closeWindow():
    tk.messagebox.showinfo(title="警告",message = "不許關閉，好好回答")
    return

#點選喜歡觸發的方法
def Love():
    #Toplevel獨立的頂級視窗，和父級標題一樣
    love = tk.Toplevel(window)
    love.geometry("900x60+300+360")
    love.title("來自Ken的Message")
    label = tk.Label(love,text="Happy Birthday!!在這特別的日子裡，我沒特別準備什麼，禮物就是在生日這天你向Ken說的任何事，他都會說『Yes』哦~~",font =("微軟雅黑",15))
    label.pack()
    # label1 = Label(love,text="加個微信唄",font =("微軟雅黑",20))
    # label1.pack()
    # entry = Entry(love,font = ("微軟雅黑",15))
    # entry.pack()
    btn = tk.Button(love,text = "確定",width = 10 , height = 1,command = close_all)
    btn.pack()
    love.protocol("WM_DELETE_WINDOW",closelove)

def closelove():
    return

#關閉所有的視窗   注意，如果父級視窗關了，下面的所有視窗均會關閉
def close_all():
    #destory 銷燬
    window.destroy()
#關閉不喜歡框的X時
def closenolove():
    #messagebox.showinfo("再考慮一下","再考慮一下唄")
    #return
    disLove()

#點選不喜歡觸發的事件
def disLove():
    no_love = tk.Toplevel(window)
    no_love.geometry("420x60+300+360")
    no_love.title("oh~~No~~")
    label =  tk.Label(no_love,text = "別這樣，再考慮一下，或許會有意想不到的驚喜哦~~",font = ("微軟雅黑",15))
    label.pack()
    btn = tk.Button(no_love,text = "好的",width = 10 , height = 1,command = no_love.destroy)
    btn.pack()
    no_love.protocol("WM_DELETE_WINDOW",closenolove)



# 建立視窗
window =tk.Tk() #類的例項化，建立視窗,window僅僅是個變數

# 視窗標題
window.title("Ken的告白")

# 視窗的大小   運用小寫的x來連線
window.geometry("255x410")

#視窗位置（距離螢幕左上角）      運用+來連線
window.geometry("+500+260")  # geometry意為幾何
#上述可以寫成window.geometry("380x200+500+245")，其中+是用來連線的

#使用者關閉視窗觸發的事件
window.protocol("WM_DELETE_WINDOW",closeWindow)

# 標籤控制元件，一般第一個引數均是父級視窗         ，這裡傳參為window           fg設定顏色
label = tk.Label(window, text = "Hey,Anita姐姐", font = ("微軟雅黑",12), fg="black")

# 定位  grid（網格式） pack（包的方式） place(用的最少的一種，根據位置)
label.grid(row=0,column =0)      #預設值為 0  0

label_1 = tk.Label(window,text = "你好漂亮，可以和我交往嗎？",font = ("微軟雅黑",12))
label_1.grid(row=1,column = 1,sticky = tk.E) #sticky為對齊方式  N上S下W左E右

#  顯示圖片
photo = tk.PhotoImage(file=r"/Users/ken/Desktop/截圖.png")
imageLable = tk.Label(window,image = photo)
#column 元件所跨越的列數
imageLable.grid(row=2,column=0,columnspan =2)  #跨列操作

#按鈕控制元件           點選觸發command事件
btn = tk.Button(window,text="可以",command  = Love)
btn.grid(row = 3,column = 0,sticky = tk.W)

btn1 =tk.Button(window,text="不可以",command = disLove)
btn1 .grid(row = 3,column = 1,sticky = tk.E)
#顯示視窗 訊息迴圈
window .mainloop()