from tkinter import *


class NLPApp:
    def __init__(self):
        # we load GUI first
        self.root = Tk()
        self.root.title('NLPApp')
        self.root.geometry('350x600')
        self.root.configure(bg='#93879c')

        self.login_gui()

        self.root.mainloop()

    def login_gui(self):
        heading = Label(self.root, text='NLPApp', bg='#93879c', fg='white')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana', 24, 'bold'))


nlp = NLPApp()
