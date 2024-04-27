from tkinter import *
from mydb import Database
from tkinter import messagebox
from myapi import My_API


class NLPApp:
    def __init__(self):
        # create object of database class
        self.dbo = Database()
        # myapi class object
        self.api_obj = My_API()
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
        heading = Label(self.root, text='NLPApp', bg='#93879c', fg='white')
        heading.pack(pady=(10, 20))
        heading.configure(font=('verdana', 24, 'bold'))
        heading = Label(self.root, text='Sentiment Analysis', bg='#93879c', fg='white')
        heading.pack(pady=(10, 20))
        heading.configure(font=('verdana', 24, 'bold'))

        label0 = Label(self.root, text='Enter Text ', bg='#93879c', fg='white')
        label0.pack(pady=(10, 10))
        label0.configure(font=('verdana', 17, 'bold'))

        self.sentiment_text = Entry(self.root, width=30)
        self.sentiment_text.pack(pady=(5, 10))

        senti_button = Button(self.root, text='Analyze', width=10, height=2,
                              command=self.do_senti_analysis)
        senti_button.pack(pady=(20, 10))
        self.sentiment_result = Label(self.root, text='', bg='#93879c')
        self.sentiment_result.pack(pady=(30, 30))
        self.sentiment_result.configure(font=('verdana', 14))

        goBack_button = Button(self.root, text='Go Back', width=5, height=1, command=self.home_gui)
        goBack_button.pack(pady=(20, 10))

    def NER_gui(self):
        self.clear()
        heading = Label(self.root, text='NLPApp', bg='#93879c', fg='white')
        heading.pack(pady=(10, 20))
        heading.configure(font=('verdana', 24, 'bold'))
        heading = Label(self.root, text='NER', bg='#93879c', fg='white')
        heading.pack(pady=(10, 20))
        heading.configure(font=('verdana', 24, 'bold'))

        self.NER_text = Entry(self.root, width=30)
        self.NER_text.pack(pady=(5, 10))

        self.NER_searchkey = Entry(self.root, width=30)
        self.NER_searchkey.pack(pady=(5, 10))

        NER_button = Button(self.root, text='DO NER', width=10, height=2,
                            command=self.do_NER)
        NER_button.pack(pady=(20, 10))
        self.NER_result = Label(self.root, text='', bg='#93879c')
        self.NER_result.pack(pady=(30, 30))
        self.NER_result.configure(font=('verdana', 14))

        goBack_button = Button(self.root, text='Go Back', width=5, height=1, command=self.home_gui)
        goBack_button.pack(pady=(20, 10))

    def emotion_gui(self):
        self.clear()
        heading = Label(self.root, text='NLPApp', bg='#93879c', fg='white')
        heading.pack(pady=(10, 20))
        heading.configure(font=('verdana', 24, 'bold'))
        heading = Label(self.root, text='Emotion Prediction', bg='#93879c', fg='white')
        heading.pack(pady=(10, 20))
        heading.configure(font=('verdana', 24, 'bold'))

        label0 = Label(self.root, text='Enter text ', bg='#93879c', fg='white')
        label0.pack(pady=(10, 10))
        label0.configure(font=('verdana', 17, 'bold'))

    def do_senti_analysis(self):
        response = self.api_obj.sentiment_anlys(self.sentiment_text.get())
        sentiment_analysis_results = []
        for label_info in response['scored_labels']:
            label = label_info['label']
            score = label_info['score']
            sentiment_analysis_results.append(f"{label}: {score:.6f}")

        # Joining all results into a single string to display or use further
        results_string = "\n".join(sentiment_analysis_results)
        print(results_string)
        self.sentiment_result['text'] = results_string

    def do_NER(self):
        response = self.api_obj.ner(self.NER_text.get(), self.NER_searchkey.get())
        print(response)
        self.NER_result['text'] = response

    def do_emotion(self):
        pass


nlp = NLPApp()
