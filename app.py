from tkinter import *
import socket
import app
import threading
from text import *

bg_color = "#FBF9F1"
text_color = "#0F1035"
bubble_color = "#AAD7D9"
header_color = "#E5E1DA"
div_color = "#AAD7D9"
font = "Helvetica 14"
font_b = "Helvetica 13 bold"

class chat:
    

    def __init__(self,title,isserver):
        self.window = Tk()
        self.tit=title
        self.msg= ''
        self.isServer = isserver
        self.host = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        if isserver:
            self.host.bind(("192.168.141.105",9999))
            self.host.listen()
            print("Server is listening")
            self.client ,self.addr = self.host.accept()
            print("Connection established")
        else:
            self.host.connect(("192.168.141.105",9999))
        self._setup_main_window()
        
    # def isServer(b):
    #     self.Server = b        
    
    def run(self):
        t1 = threading.Thread(target=self.rec)
        t1.start()
        self.window.mainloop()
            
        
    
    def get_msg(self):
        return self.msg
        
    def _setup_main_window(self):
        self.window.title("ChatRoom-"+self.tit)
        self.window.resizable(width=False,height=False)
        self.window.configure(width = 500, height = 500, bg = bg_color)

        head_label = Label(self.window, bg = bg_color , fg = text_color , text = "Welcome",font = font_b , pady = 10)
        head_label.place(relwidth = 1)
        
        line = Label(self.window , width = 480, bg = div_color)
        line.place(relwidth=1,rely =0.07,relheight=0.012)
        
        self.text_widget = Text(self.window , width = 20 ,height=2,border = False,bg = header_color,fg= text_color,font = font,padx = 5,pady=5)
        self.text_widget.place(relheight=0.745,relwidth=1,rely=0.08)
        self.text_widget.configure(cursor="arrow",state = DISABLED )
        
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight = 1,relx = 0.974)
        scrollbar.configure(command=self.text_widget.yview)
        
        bottom_label = Label(self.window,bg= bg_color,height=80)
        bottom_label.place(relwidth=1,rely=0.825)
        self.msg_box = Entry(bottom_label , bg = "#FFFFFF",fg = text_color, font = font )
        self.msg_box.place(relwidth = 0.74,relheight = 0.04,rely = 0.008,relx = 0.011)
        self.msg_box.focus()
        self.msg_box.bind("<Return>",self._on_enter_pressed)
        send_but = Button(bottom_label,text = "Send",font=font_b,width = 10, bg = bubble_color, command = lambda:self._on_enter_pressed(None))
        send_but.place(relx=0.77,rely=0.008,relheight=0.04,relwidth =0.12)
        file_but =Button(bottom_label,text = "Attach",font=font_b,width = 10, bg = bubble_color, command = lambda:self._on_enter_pressed_file(None))
        send_but.place(relx=0.57,rely=0.008,relheight=0.04,relwidth =0.12)
         

        
    def rec(self):
        if self.isServer:
            msg = decrypt(self.client.recv(1024).decode("utf-8"))
            self._insert_msg(msg,"Sender")
        else:
            msg = decrypt(self.host.recv(1024).decode("utf-8"))
            self._insert_msg(msg,"Sender")
    def set_msg(self):
         self.msg = self.msg_box.get()
        
    def _on_enter_pressed(self,event):
        self.set_msg()
        if self.isServer:
            self.client.send(encrypt(self.msg.encode("utf-8")))
        else:
            self.host.send(encrypt(self.msg.encode("utf-8")))
        self._insert_msg(self.msg,"You")
    
    def _insert_msg(self,msg,sender):
        if not msg:
            return
        self.msg_box.delete(0,END)
        msg1 =  f"{sender}: {msg}\n"
        self.text_widget.configure(cursor="arrow",state = NORMAL)
        self.text_widget.insert(END,msg1)
        self.text_widget.configure(state=DISABLED)
        

if __name__ == '__main__':
    app = chat("test",True)
    app.run()
    
     
     
     
        