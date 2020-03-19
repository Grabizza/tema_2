# inspirat de pe net

# importing Tkinter and math
from tkinter import *
import math

# calculator class
class calculator:

    def inlocuire_operator(self):

        "inlocuieste 'x cu *' si ': cu /'"
        self.expresie = self.calculator.get()
        self.text_nou = self.expresie.replace(':', '/')
        self.text_nou = self.text_nou.replace('x', '*')

    def egal(self):
        "cand este apasat butonul egal"
        self.inlocuire_operator()
        try:
            # evalueaza expresia utilizand functia eval
            self.value = eval(self.text_nou)
        except SyntaxError or NameError:
            self.calculator.delete(0, END)
            self.calculator.insert(0, 'Reintroduceti variabila!')
        else:
            self.calculator.delete(0, END)
            self.calculator.insert(0, self.value)

    def stergetot(self):
        "cand este apasat butonul, este stearsa toata casuta input"
        self.calculator.delete(0, END)

    def sterge(self):
        self.text = self.calculator.get()[:-1]
        self.calculator.delete(0, END)
        self.calculator.insert(0, self.text)

    def actiune(self, arg):
        "apasarea unui buton, valoarea acestuia este introdusa la sfarsitul textului din casuta"
        self.calculator.insert(END, arg)

    def __init__(self, master):
        "Metoda de constructie"
        master.title('Calculator')
        master.geometry()
        self.calculator = Entry(master)
        self.calculator.grid(row=0, column=0, columnspan=6, pady=3)
        self.calculator.focus_set()

        # Buton AC
        Button(master, text="AC", width=5, height=7, fg="red",
               bg="white", command=lambda: self.stergetot()).grid(
            row=1, column=5, rowspan=2)

        # Buton C
        Button(master, text="C", width=5, height=7, fg="red",
               bg="white", command=lambda: self.sterge()).grid(
            row=3, column=5, rowspan=2)

        # Buton +
        Button(master, text="+", width=5, height=3, fg="red",
               bg="white", command=lambda: self.actiune('+')).grid(
            row=4, column=3)

        # Buton *
        Button(master, text="x", width=5, height=3, fg="red",
               bg="white", command=lambda: self.actiune('*')).grid(
            row=2, column=3)

        # Buton -
        Button(master, text="-", width=5, height=3, fg="red",
               bg="white", command=lambda: self.actiune('-')).grid(
            row=3, column=3)

        # Buton :
        Button(master, text=":", width=5, height=3, fg="red",
               bg="white", command=lambda: self.actiune('/')).grid(
            row=1, column=3)

        # Buton =
        Button(master, text="=", width=5, height=3, fg="red",
               bg="white", command=lambda: self.egal()).grid(
            row=4, column=2)

        # Buton 7
        Button(master, text="7", width=5, height=3, fg="red",
               bg="white", command=lambda: self.actiune(7)).grid(
            row=1, column=0)

        # Buton 8
        Button(master, text="8", width=5, height=3, fg="red",
               bg="white", command=lambda: self.actiune(8)).grid(
            row=1, column=1)

        # Buton 9
        Button(master, text="9", width=5, height=3, fg="red",
               bg="white", command=lambda: self.actiune(9)).grid(
            row=1, column=2)

        # Buton 4
        Button(master, text="4", width=5, height=3, fg="red",
               bg="white", command=lambda: self.actiune(4)).grid(
            row=2, column=0)

        # Buton 5
        Button(master, text="5", width=5, height=3, fg="red",
               bg="white", command=lambda: self.actiune(5)).grid(
            row=2, column=1)

        # Buton 6
        Button(master, text="6", width=5, height=3, fg="red",
               bg="white", command=lambda: self.actiune(6)).grid(
            row=2, column=2)

        # Buton 1
        Button(master, text="1", width=5, height=3, fg="red",
               bg="white", command=lambda: self.actiune(1)).grid(
            row=3, column=0)

        # Buton 2
        Button(master, text="2", width=5, height=3, fg="red",
               bg="white", command=lambda: self.actiune(2)).grid(
            row=3, column=1)

        # Buton 3
        Button(master, text="3", width=5, height=3, fg="red",
               bg="white", command=lambda: self.actiune(3)).grid(
            row=3, column=2)

        # Buton 0
        Button(master, text="0", width=5, height=3, fg="red",
               bg="white", command=lambda: self.actiune(0)).grid(
            row=4, column=0)

        # Buton .
        Button(master, text=".", width=5, height=3, fg="red",
               bg="white", command=lambda: self.actiune('.')).grid(
            row=4, column=1)

        # Buton .
        Button(master, text=".", width=5, height=3, fg="red",
               bg="white", command=lambda: self.actiune('.')).grid(
            row=4, column=1)

#Driver Code


root = Tk()

obj = calculator(root)  # object instantiated

root.mainloop()