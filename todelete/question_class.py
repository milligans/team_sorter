from tkinter import *

class Question_class(Frame):
    # GUI SET UP

    def __init__(self, master):
        #initialising the question_class class
        Frame.__init__(self, master)
        self.grid()



    def create_prog_select(self, title, choice_array):
        # Create widgets to select a degree programme from a list
        lblProg = Label(self, text=title, font=('MS', 8, 'bold'))
        lblProg.grid(row=0, column=0, columnspan=2, sticky=NE)
        self.listProg = Listbox(self, height=3)
        scroll = Scrollbar(self, command=self.listProg.yview)
        self.listProg.configure(yscrollcommand=scroll.set)
        self.listProg.grid(row=0, column=2, columnspan=2, sticky=NE)
        scroll.grid(row=0, column=4, sticky=W)

        for item in choice_array:
            self.listProg.insert(END, item)
        self.listProg.selection_set(END)

