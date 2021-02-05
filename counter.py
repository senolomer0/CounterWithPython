import tkinter as tk
from tkinter import messagebox
import time
from PIL import ImageTk,Image

class Counter():
    def __init__(self):
        super().__init__()
        self.screen = tk.Tk()
        self.init()       
         
    def get_time(self):
        time_format = time.strftime("%H:%M:%S")
        self.time.config(text=time_format)
        self.time.after(1000,self.get_time)

    def hour_up_function(self):
        hour = self.hour_text.get()
        if(int(hour)==23):
            self.minute_text.set("00")
            self.second_text.set("00")
        if int(hour)<24:   
            hour = str(int(hour) + 1)
            if len(hour)==1:
                hour = "0" + hour
            self.hour_text.set(hour)

    def hour_down_function(self):
        hour = self.hour_text.get()
        if int(hour)<=24 and int(hour)>0:
            hour = str(int(hour) - 1)
            if len(hour)==1:
                hour = "0" + hour
            self.hour_text.set(hour)

    def minute_up_function(self):
        hour = self.hour_text.get()
        minute = self.minute_text.get()
        if int(minute)<59 and int(hour)!=24:
            minute = str(int(minute) + 1)
            if len(minute)==1:
                minute = "0" + minute
            self.minute_text.set(minute)

    def minute_down_function(self):
        minute = self.minute_text.get()
        if int(minute)<=59 and int(minute)>0:
            minute = str(int(minute) - 1)
            if len(minute)==1:
                minute = "0" + minute
            self.minute_text.set(minute)

    def second_up_function(self):
        hour = self.hour_text.get()
        second = self.second_text.get()
        if int(second)<59 and int(hour)!=24:
            second = str(int(second) + 1)
            if len(second)==1:
                second = "0" + second
            self.second_text.set(second)

    def second_down_function(self):
        second = self.second_text.get()
        if int(second)<=59 and int(second)>0:
            second = str(int(second) - 1)
            if len(second)==1:
                second = "0" + second
            self.second_text.set(second)

    def button(self):
        self.ss +=1
        self.start()

    def start(self):
        if(self.ss%2==1):
            self.button_text.set("Stop")

        elif(self.ss%2==0):
            self.button_text.set("Start")

        second = self.second_text.get()
        hour = self.hour_text.get()
        minute = self.minute_text.get()

        if(int(second) != 0):
            second = int(second) - 1
            if len(str(second)) == 1:
                second = "0" + str(second)
            self.second_text.set(second)
        
        elif(int(minute)>0 and int(second)==0):
            minute = int(minute) - 1
            if len(str(minute)) == 1:
                minute = "0" + str(minute)
            self.minute_text.set(minute)
            self.second_text.set("59")
        
        elif(int(hour)>0 and int(minute)==0 and int(second)==0):
            hour = int(hour) - 1
            if len(str(hour)) == 1:
                hour = "0" + str(hour)
            self.hour_text.set(hour)
            self.second_text.set("59")
            self.minute_text.set("59")
       
        if(self.hour_text.get() == "00" and self.minute_text.get() =="00" and self.second_text.get() == "00"):
            messagebox.showinfo(title="Counter", message="Time Over")
            self.button_text.set("Start")
            self.ss +=1
            
        elif(self.button_text.get() == "Stop" or self.ss==1):
            self.second.after(1000,self.start)
    
    def cancel(self):
        self.button_text.set("Start")
        #self.ss +=1
        self.hour_text.set("00")
        self.minute_text.set("00")
        self.second_text.set("00")

    def init(self):
        self.screen.tk.call('wm', 'iconphoto', self.screen._w, tk.PhotoImage(file='photos/icon.png'))
        self.screen.title("Counter")
        self.screen.geometry("500x250+500+250")
        self.screen.resizable(False,False)
        self.screen.config(bg="white")

        load = Image.open("photos/background.jpg")
        background = ImageTk.PhotoImage(load)
        img = tk.Label(self.screen, image=background)
        img.place(x=-2, y=-10)

        load2 = Image.open("photos/up.png")
        up = ImageTk.PhotoImage(load2)

        load3 = Image.open("photos/down.png")
        down = ImageTk.PhotoImage(load3)
        
        self.time = tk.Label(text="",bg="dark slate gray",fg="white",font="Arial 15")
        self.time.pack(anchor="ne")
        self.get_time()

        self.hour_text = tk.StringVar()
        self.minute_text = tk.StringVar()
        self.second_text = tk.StringVar()

        self.hour_up = tk.Button(bg="dark slate gray",fg="white",font="Arial 16",image=up,borderwidth=0,activebackground="dark slate gray",command = self.hour_up_function)
        self.hour_up.place(x=100,y=50,width = 72,height=25)
        self.hour = tk.Label(bg="dark slate gray",fg="white",font="Arial 44",textvariable=self.hour_text)
        self.hour_text.set("00")
        self.hour.place(x=100,y=80)
        self.hour_label = tk.Label(text="Hours",bg="dark slate gray",fg="white",font="Arial 10")
        self.hour_label.place(x=100,y=155,width = 72)
        self.hour_down = tk.Button(bg="dark slate gray",fg="white",font="Arial 16",image=down,borderwidth=0,activebackground="dark slate gray",command = self.hour_down_function)
        self.hour_down.place(x=100,y=183,width = 72,height=25)

        self.point = tk.Label(text=":",bg="dark slate gray",fg="white",font="Arial 24")
        self.point.place(x=184,y=95)

        self.minute_up = tk.Button(bg="dark slate gray",fg="white",font="Arial 16",image=up,borderwidth=0,activebackground="dark slate gray",command = self.minute_up_function)
        self.minute_up.place(x=210,y=50,width = 72,height=25)
        self.minute = tk.Label(bg="dark slate gray",fg="white",font="Arial 44",textvariable=self.minute_text)
        self.minute.place(x=210,y=80)
        self.minute_text.set("00")
        self.minute_label = tk.Label(text="Minutes",bg="dark slate gray",fg="white",font="Arial 10")
        self.minute_label.place(x=210,y=155,width = 72)
        self.minute_down = tk.Button(bg="dark slate gray",fg="white",font="Arial 16",image=down,borderwidth=0,activebackground="dark slate gray",command = self.minute_down_function)
        self.minute_down.place(x=210,y=183,width = 72,height=25)

        self.point1 = tk.Label(text=":",bg="dark slate gray",fg="white",font="Arial 24")
        self.point1.place(x=294,y=95)

        self.second_up = tk.Button(bg="dark slate gray",fg="white",font="Arial 16",image=up,borderwidth=0,activebackground="dark slate gray",command = self.second_up_function)
        self.second_up.place(x=320,y=50,width = 72,height=25)
        self.second = tk.Label(bg="dark slate gray",fg="white",font="Arial 44",textvariable=self.second_text)
        self.second.place(x=320,y=80)
        self.second_text.set("00")
        self.second_label = tk.Label(text="Seconds",bg="dark slate gray",fg="white",font="Arial 10")
        self.second_label.place(x=320,y=155,width = 72)
        self.second_down = tk.Button(bg="dark slate gray",fg="white",font="Arial 16",image=down,borderwidth=0,activebackground="dark slate gray",command = self.second_down_function)
        self.second_down.place(x=320,y=183,width = 72,height=25)

        self.ss = 0
        self.button_text = tk.StringVar()
        self.button_text.set("Start")
        self.start_stop = tk.Button(text="Start",bg="dark slate gray",fg="white",textvariable =self.button_text,font="Arial 10",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command=self.button)
        self.start_stop.place(x=423,y=190,width = 72,height=25)

        self.cancel_button = tk.Button(text="Cancel",bg="dark slate gray",fg="white",font="Arial 10",borderwidth=0,activebackground="dark slate gray",activeforeground="white",command = self.cancel)
        self.cancel_button.place(x=423,y=220,width = 72,height=25)
        
        self.screen.mainloop()
        
screen = Counter()
