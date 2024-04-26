from tkinter import *
from mydb import Database
from tkinter import messagebox
from functions import Functions


class NLPApp:
    def __init__(self):
        # create object of database class
        self.dbo = Database()
        # Object of Function class
        self.func = Functions()
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

        login_button = Button(self.root, text='login', width=20, height=1, command=self.perform_login)
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

        login_button = Button(self.root, text='Register', width=20, height=1, command=self.perform_regist)
        login_button.pack(pady=(20, 10))

        label3 = Label(self.root, text='Already a Member?', bg='#93879c', fg='white')
        label3.pack(pady=(20, 5))
        label3.configure(font=('verdana', 14, 'bold'))

        redirect_button = Button(self.root, text='Login Now', width=16, height=1, command=self.login_gui)
        redirect_button.pack(pady=(10, 10))

    def perform_regist(self):
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()
        response = self.dbo.add_data(name, email, password)
        if response:
            messagebox.showinfo('success', 'Registration successful !')
        else:
            messagebox.showerror('Error', 'Email already exists')

    def perform_login(self):
        email = self.email_input.get()
        password = self.password_input.get()
        response = self.dbo.search(email, password)
        if response:
            messagebox.showinfo('success', 'login successful')
            self.home_gui()
        else:
            messagebox.showerror('error', 'login failed')

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def home_gui(self):
        self.clear()
        sentiment_button = Button(self.root, text='Sentiment Analysis', width=20, height=4, command=self.sentiment_gui)
        sentiment_button.pack(pady=(20, 10))

        NER_button = Button(self.root, text='NER', width=20, height=4, command=self.NER_gui)
        NER_button.pack(pady=(20, 10))

        emotion_button = Button(self.root, text='Emotion Prediction', width=20, height=4, command=self.emotion_gui)
        emotion_button.pack(pady=(20, 10))

        logout_button = Button(self.root, text='LOGOUT', width=10, height=2, command=self.login_gui)
        logout_button.pack(pady=(20, 10))

    def sentiment_gui(self):
        self.clear()
        heading = Label(self.root, text='Sentiment Analysis', bg='#93879c', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        label0 = Label(self.root, text='Enter text ', bg='#93879c', fg='white')
        label0.pack(pady=(10, 10))
        label0.configure(font=('verdana', 17, 'bold'))

    def NER_gui(self):
        self.clear()
        heading = Label(self.root, text='NER', bg='#93879c', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        label0 = Label(self.root, text='Enter text ', bg='#93879c', fg='white')
        label0.pack(pady=(10, 10))
        label0.configure(font=('verdana', 17, 'bold'))

    def emotion_gui(self):
        self.clear()
        heading = Label(self.root, text='Emotion Prediction', bg='#93879c', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        label0 = Label(self.root, text='Enter text ', bg='#93879c', fg='white')
        label0.pack(pady=(10, 10))
        label0.configure(font=('verdana', 17, 'bold'))


nlp = NLPApp()
