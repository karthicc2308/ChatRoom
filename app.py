from tkinter import *

bg_color = "#FBF9F1"
text_color = "#0F1035"
bubble_color = "#AAD7D9"
header_color = "#E5E1DA"
div_color = "#AAD7D9"
font = "Helvetica 14"
font_b = "Helvetica 13 bold"

class App:
    def __init__(self):
        self.window = Tk()
        self._setup_main_window()
    def run(self):
        self.window.mainloop()
        
    def _setup_main_window(self):
        self.window.title("ChatRoom")
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
        
    def _on_enter_pressed(self,event):
        msg  = self.msg_box.get()
        self._insert_msg(msg,"You")
        
    def _insert_msg(self,msg,sender):
        if not msg:
            return
        self.msg_box.delete(0,END)
        msg1 =  f"{sender}: {msg}\n"
        self.text_widget.configure(cursor="arrow",state = NORMAL)
        self.text_widget.insert(END,msg1)
        self.text_widget.configure(state=DISABLED)

if __name__ == '__main__':
    app = App()
    app.run()