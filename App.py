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

        self.clear()

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

        self.password_input = Entry(self.root, width=30, show='*')
        self.password_input.pack(pady=(5, 10))

        login_button = Button(self.root, text='login', width=20, height=1)
        login_button.pack(pady=(10, 10))

        label3 = Label(self.root, text='Not a Member?', bg='#93879c', fg='white')
        label3.pack(pady=(20, 10))
        label3.configure(font=('verdana', 14, 'bold'))

        redirect_button = Button(self.root, text='Register Now', width=16, height=1, command=self.register_gui)
        redirect_button.pack(pady=(10, 10))

    def register_gui(self):
        # Clear the existing GUI
        self.clear()

        heading = Label(self.root, text='Welcome to NLPApp', bg='#93879c', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        label0 = Label(self.root, text='Enter Name: ', bg='#93879c', fg='white')
        label0.pack(pady=(10, 10))
        label0.configure(font=('verdana', 17, 'bold'))

        self.name_input = Entry(self.root, width=30)
        self.name_input.pack(pady=(5, 10))

        label1 = Label(self.root, text='Enter Email: ', bg='#93879c', fg='white')
        label1.pack(pady=(10, 10))
        label1.configure(font=('verdana', 17, 'bold'))

        self.email_input = Entry(self.root, width=30)
        self.email_input.pack(pady=(5, 10))

        label2 = Label(self.root, text='Enter Password: ', bg='#93879c', fg='white')
        label2.pack(pady=(10, 10))
        label2.configure(font=('verdana', 17, 'bold'))

        self.password_input = Entry(self.root, width=30, show='*')
        self.password_input.pack(pady=(5, 10))

        login_button = Button(self.root, text='Register', width=20, height=1)
        login_button.pack(pady=(20, 10))

        label3 = Label(self.root, text='Already a Member?', bg='#93879c', fg='white')
        label3.pack(pady=(20, 5))
        label3.configure(font=('verdana', 14, 'bold'))

        redirect_button = Button(self.root, text='Login Now', width=16, height=1, command=self.login_gui)
        redirect_button.pack(pady=(10, 10))

    def clear(self):
        for i in self.root.pack_slaves():
            print(i.destroy())



nlp = NLPApp()
