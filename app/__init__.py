from tkinter import Tk, Canvas
from app.auth import RegisterUI, LoginUI

class UI(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        container = Canvas(self, bg="#202124", highlightthickness="0")
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.pages = {} # dictionary of pages in the app
        for page in (RegisterUI, LoginUI):
            frame = page(container, self)

            # putting the object of Pages in the self.pages dictionary
            self.pages[page] = frame

            # pack the page created now
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_page(RegisterUI)
        print(self.pages)
    
    def show_page(self, page):
        frame = self.pages[page]

        self.geometry(frame.geometry)

        frame.tkraise()