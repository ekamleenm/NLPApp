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
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        label1 = Label(self.root, text='Enter Email: ', bg='#93879c', fg='white')
        label1.pack(pady=(10, 10))
        label1.configure(font=('verdana', 17, 'bold'))

        self.email_input = Entry(self.root, width=30)
        self.email_input.pack(pady=(5, 10))

        label2 = Label(self.root, text='Enter Password: ', bg='#93879c', fg='white')
        label2.pack(pady=(10, 10))
        label2.configure(font=('verdana', 17, 'bold'))

        self.password_input = Entry(self.root, width=30)
        self.password_input.pack(pady=(5, 10))

        login_button = Button(self.root, text='login', width=20, height=1)
        login_button.pack(pady=(10, 10))

        label3 = Label(self.root, text='Not a Member?', bg='#93879c', fg='white')
        label3.pack(pady=(20, 10))
        label3.configure(font=('verdana', 14, 'bold'))

        redirect_button = Button(self.root, text='Register Now', width=16, height=1)
        redirect_button.pack(pady=(10, 10))


nlp = NLPApp()

