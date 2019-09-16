from tkinter import *
import time
import math
import pygame

root = Tk()
root.geometry("460x665")
root.resizable(False, False)
root.title("Computer Use Time")
root.iconbitmap('icon.ico')
def passss():
    pass
root.bind("<Alt-F4>", passss)
def Start():
    Start_Win = Toplevel(root)
    Start_Win.iconbitmap('icon.ico')
    Start_Win.geometry("300x300")
    Start_Win.iconbitmap('icon.ico')
    Start_Win.overrideredirect(True)
    def passss():
        pass
    root.protocol("WM_DELETE_WINDOW", passss)
    Start_Win.bind("<Alt-F4>", passss)
    U_Hr_Val = Hour.get()
    U_Min_Val = Minute.get()
    U_Sec_Val = Second.get()
    U_Total_Sec = U_Hr_Val * 3600 + U_Min_Val * 60 + U_Sec_Val
    B_Hr_Val = B_Hour.get()
    B_Min_Val = B_Minute.get()
    B_Total_Sec = B_Hr_Val * 3600 + B_Min_Val * 60
    B_Total_ms = B_Total_Sec * 1000
    def countDown():
        Countdown.config(bg = "black")
        Countdown.config(fg = 'white')
        Countdown.config(height = 3, font = "微軟正黑體 20")
        for k in range(U_Total_Sec, 0, -1):
            kk = math.floor(k / 3600)
            kkk = k % 3600
            kkkk = math.floor(kkk / 60)
            kkkkk = kkk % 60
            Countdown["text"] = kk, ":", kkkk, ":",  kkkkk
            Start_Win.update()
            time.sleep(1)
        Start_Win.overrideredirect(False)
        Start_Win.attributes("-topmost", True)
        Start_Win.attributes("-fullscreen", True)
        Countdown.config(bg = 'black')
        Countdown.config(fg = 'white')
        Countdown["text"] = "It's time to take a break!"
        Start_Win.overrideredirect(True)
        pygame.mixer.init()
        pygame.mixer.music.load("End_Sound.mp3")
        pygame.mixer.music.play()
    
    Start_Win.title("Countdown")
    Countdown = Label(Start_Win)
    Countdown.pack(fill = BOTH, expand = 1)
    countDown()
    Start_Win.after(B_Total_ms, Start_Win.destroy)

Space_1 = Label(root, text = " ", font = "微軟正黑體 10")
Space_1.pack()

Use_Time_text = Label(root, text = "Use Time", font = "微軟正黑體 15")
Use_Time_text.pack()

Hour = Scale(orient = HORIZONTAL, width = 15, length = 150)
Hour.config(from_ = 0, to = 5)
Hour.config(showvalue = 1, tickinterval = 1, resolution = 1)
Hour.config(label = "                Hour(s)", font = "微軟正黑體 10")
Hour.set(0)
Hour.pack()

Minute = Scale(orient = HORIZONTAL, width = 15, length = 300)
Minute.config(from_ = 0, to = 60)
Minute.config(showvalue = 1, tickinterval = 5, resolution = 1)
Minute.config(label = "                                       Minute(s)", font = "微軟正黑體 10")
Minute.set(0)
Minute.pack()

Second = Scale(orient = HORIZONTAL, width = 15, length = 300)
Second.config(from_ = 0, to = 60)
Second.config(showvalue = 1, tickinterval = 5, resolution = 1)
Second.config(label = "                                       Second(s)", font = "微軟正黑體 10")
Second.set(0)
Second.pack()

Space_2 = Label(root, text = " ", font = "微軟正黑體 10")
Space_2.pack()

Break_Time_text = Label(root, text = "Break Time", font = "微軟正黑體 15")
Break_Time_text.pack()

B_Hour = Scale(orient = HORIZONTAL, width = 15, length = 150)
B_Hour.config(from_ = 0, to = 5)
B_Hour.config(showvalue = 1, tickinterval = 1, resolution = 1)
B_Hour.config(label = "                Hour(s)", font = "微軟正黑體 10")
B_Hour.set(0)
B_Hour.pack()

B_Minute = Scale(orient = HORIZONTAL, width = 15, length = 300)
B_Minute.config(from_ = 10, to = 60)
B_Minute.config(showvalue = 1, tickinterval = 5, resolution = 1)
B_Minute.config(label = "                                       Minute(s)", font = "微軟正黑體 10")
B_Minute.set(0)
B_Minute.pack()

Space_3 = Label(root, text = " ", font = "微軟正黑體 10")
Space_3.pack()

Space_4 = Label(root, text = " ", font = "微軟正黑體 10")
Space_4.pack()

Start_but = Button(root, text = "Start", font = "微軟正黑體 10", command = Start)
Start_but.pack()

root.mainloop()
