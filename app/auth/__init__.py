from tkinter import Frame, Button

class RegisterUI(Frame):
    def __init__(self, parent, container):
        # making a register widget
        Frame.__init__(self, parent, bg="#202124")

        self.geometry = "400x600"

        self.btn = Button(self, text = "show Login page", command = lambda:container.show_page(LoginUI))
        self.btn.pack()


class LoginUI(Frame):
    def __init__(self, parent, container):
        # making a register widget
        Frame.__init__(self, parent, bg="red")

        self.geometry = "400x400"

        self.btn = Button(self, text = "show register page", command = lambda:container.show_page(RegisterUI))
        self.btn.pack()