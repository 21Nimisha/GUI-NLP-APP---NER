from tkinter import *
from tkinter import messagebox
from myapi import TextRazorAPI
from mydb import Database

class NLPApp:
    def __init__(self):
        self.root = Tk()
        self.root.title('NLPApp')
        self.root.geometry('350x600')
        self.root.configure(bg='#34495E')
        self.dbo = Database()
        self.textRazor = TextRazorAPI("5a55a65a27ba18397118a35b1ff1c2f1905f92cddc19434571b671d0")

        self.login_gui()

        self.root.mainloop()

    def login_gui(self):
        self.clear()

        heading = Label(self.root, text='NLPApp', bg='#34495E', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        label1 = Label(self.root, text='Enter Email:')
        label1.pack()

        self.email_input_login = Entry(self.root, width=50)
        self.email_input_login.pack(pady=(5,10),ipady=4)

        label2 = Label(self.root, text='Enter Password:')
        label2.pack(pady=(10, 10))

        self.password_input_login = Entry(self.root, width=30, show='*')
        self.password_input_login.pack(pady=(5, 10), ipady=4)

        login_btn = Button(self.root, text='Login', width=20, command=self.perform_login)
        login_btn.pack(pady=(10,10))

        label3 = Label(self.root, text='Not a member?')
        label3.pack(pady=(20, 10))


        redirect_btn = Button(self.root, text='Register Now', command=self.register_gui)
        redirect_btn.pack(pady=(20, 10))

    def register_gui(self):
        self.clear()

        heading = Label(self.root, text='NLPApp', bg='#34495E', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        label0 = Label(self.root, text='Enter Name')
        label0.pack(pady=(10, 10))

        self.name_input = Entry(self.root, width=50)
        self.name_input.pack(pady=(5, 10), ipady=4)

        label1 = Label(self.root, text='Enter Email')
        label1.pack(pady=(10, 10))

        self.email_input_register = Entry(self.root, width=50)
        self.email_input_register.pack(pady=(5, 10), ipady=4)

        label2 = Label(self.root, text='Enter Password')
        label2.pack(pady=(10, 10))

        self.password_input_register = Entry(self.root, width=50, show='*')
        self.password_input_register.pack(pady=(5, 10), ipady=4)

        register_btn = Button(self.root, text='Register', width=30, height=2, command=self.perform_registration)
        register_btn.pack(pady=(10, 10))

        label3 = Label(self.root, text='Already a member?')
        label3.pack(pady=(20, 10))

        redirect_btn = Button(self.root, text='Login Now', command=self.login_gui)
        redirect_btn.pack(pady=(10, 10))

    def clear(self):
        # Clear the existing GUI
        for widget in self.root.winfo_children():
            widget.destroy()

    def perform_registration(self):
        # fetch data from the gui
        name = self.name_input.get()
        email = self.email_input_register.get()
        password = self.password_input_register.get()

        response = self.dbo.add_data(name, email, password)

        if response:
            messagebox.showinfo('Success', 'Registration successful. You can login now')
        else:
            messagebox.showerror('Error', 'Email already exists')

    def perform_login(self):

        email = self.email_input_login.get()
        password = self.password_input_login.get()

        response = self.dbo.search(email, password)

        if response:
            messagebox.showinfo('success', 'Login successful')
            self.home_gui()
        else:
            messagebox.showerror('error', 'Incorrect email/password')
    # app inside login function
    def home_gui(self):
        self.clear()

        heading = Label(self.root, text='NLPApp', bg='#34495E', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        ner_frame = Frame(self.root, bg='#34495E')
        ner_frame.pack(expand=True, pady=(50, 10))

        ner_label = Label(ner_frame, text='Named Entity Recognition', bg='#34495E', fg='white')
        ner_label.pack(pady=(10, 20))
        ner_label.configure(font=('verdana', 20))

        label1 = Label(ner_frame, text='Enter the text', bg='#34495E', fg='white')
        label1.pack(pady=(10, 10))

        self.ner_input = Entry(ner_frame, width=50)
        self.ner_input.pack(pady=(5, 10), ipady=4)

        ner_btn = Button(ner_frame, text='Analyze Entities', command=self.perform_ner_analysis)
        ner_btn.pack(pady=(10, 10))

        self.ner_result = Label(ner_frame, text='', bg='#34495E', fg='white', anchor='center')
        self.ner_result.pack(pady=(10, 10))
        self.ner_result.configure(font=('verdana', 16))

        goback_btn = Button(self.root, text='Go Back', command=self.login_gui)
        goback_btn.pack(pady=(10, 10))

    def ner_gui(self):
        self.clear()

        heading = Label(self.root, text='NLPApp', bg='#34495E', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root, text='Named Entity Recognition', bg='#34495E', fg='white')
        heading2.pack(pady=(10, 20))
        heading2.configure(font=('verdana', 20))

        label1 = Label(self.root, text='Enter the text')
        label1.pack(pady=(10, 10))

        self.ner_input = Entry(self.root, width=50)
        self.ner_input.pack(pady=(5, 10), ipady=4)

        ner_btn = Button(self.root, text='Analyze Entities', command=self.perform_ner_analysis)
        ner_btn.pack(pady=(10, 10))

        self.ner_result = Label(self.root, text='', bg='#34495E', fg='white',
                                wraplength=300)  # Adjust wrap length as needed
        self.ner_result.pack(pady=(10, 10))
        self.ner_result.configure(font=('verdana', 16))

        # Create a frame to hold the "Go Back" button
        button_frame = Frame(self.root, bg='#34495E')
        button_frame.pack(pady=(10, 10))

        # Add the "Go Back" button to the frame
        goback_btn = Button(button_frame, text='Go Back', command=self.home_gui)
        goback_btn.pack(side=LEFT, padx=(0, 5))

        # Adjust the "Analyze Entities" button to be on the right side
        ner_btn.pack(side=RIGHT)

    def perform_ner_analysis(self):
        text = self.ner_input.get()
        entities = self.textRazor.entity_recognition(text)

        result_text = "Named Entities:\n"
        for entity in entities:
            result_text += f"{entity.id}: {entity.confidence_score:.2f}\n"

        self.clear()  # Clear existing widgets

        # Center the result label
        self.ner_result = Label(self.root, text=result_text, bg='#34495E', fg='white', anchor='center')
        self.ner_result.pack(expand=True)  # Expand to fill available space
        self.ner_result.configure(font=('verdana', 16))

        # Create a frame to hold the "Go Back" button
        button_frame = Frame(self.root, bg='#34495E')
        button_frame.pack(pady=(10, 10))

        # Add the "Go Back" button to the frame
        goback_btn = Button(button_frame, text='Go Back', command=self.home_gui)
        goback_btn.pack(side=LEFT, padx=(0, 5))


NLPApp()

