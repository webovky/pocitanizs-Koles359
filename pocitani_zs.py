# -*- coding: utf-8 -*-

from os.path import basename, splitext
import tkinter as tk
from tkinter import Scale, Canvas, Entry, HORIZONTAL, StringVar, Label, Frame, messagebox, IntVar, Button

class Mishmash(Frame):

    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("Pocitadlo")
        self.master.maxsize(1500, 3000)
        self.master.resizable(True, True)
        self.master.rowconfigure(0, weight=500)
        self.master.rowconfigure(1, weight=500)
        self.master.rowconfigure(2, weight=500)
        self.master.rowconfigure(3, weight=500)
        self.master.rowconfigure(4, weight=500)
        self.master.columnconfigure(0, weight=1500)
        self.master.columnconfigure(1, weight=1500)
        self.master.columnconfigure(2, weight=1500)
        self.rozmisteni()


    def rozmisteni(self):
        self.nadpis = Label(text="Vítej v procvičování počítání")
        self.nadpis.grid(row=0, column=1)

        self.cislo1 = Entry(width=15, bd=10, justify="center")
        self.cislo1.grid(row=1, column=0)

        self.operant = Label(text="")
        self.operant.grid(row=1, column=1)

        self.cislo2 = Entry(width=15, bd=10, justify="center")
        self.cislo2.grid(row=1, column=2)

        self.napis = Label(text="Výsledek:")
        self.napis.grid(row=2, column=1)

        self.vysledek = Entry(width=15, bd=10, justify="center")
        self.vysledek.grid(row=3, column=1)











root = tk.Tk()
app = Mishmash(root)
root.mainloop()

