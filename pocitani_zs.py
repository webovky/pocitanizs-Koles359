# -*- coding: utf-8 -*-

from os.path import basename, splitext
import tkinter as tk
from tkinter import Scale, Canvas, Entry, HORIZONTAL, StringVar, Label, Frame, messagebox, IntVar, Button
import random


class Pocitani(Frame):

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
        self.prvni_cislo()

    def rozmisteni(self):
        self.nadpis = Label(text="Vítej v procvičování počítání")
        self.nadpis.grid(row=0, column=1)

        self.varCisloa = StringVar()
        self.cislo1 = Entry(textvariable=self.varCisloa, width=15, bd=10, justify="center")
        self.cislo1.grid(row=1, column=0)

        self.varOperant = StringVar()
        self.operant = Label(textvariable=self.varOperant, justify="center", font=("Helvetica", 18))
        self.operant.grid(row=1, column=1)

        self.varCislob = StringVar()
        self.cislo2 = Entry(textvariable=self.varCislob, width=15, bd=10, justify="center")
        self.cislo2.grid(row=1, column=2)

        self.napis = Label(text="Výsledek:")
        self.napis.grid(row=2, column=1)

        self.vysledek = Entry(width=15, bd=10, justify="center")
        self.vysledek.grid(row=3, column=1)

        self.tlacitko = Button(width=15, bd=10, justify="center", text="ověřit", command=self.prvni_cislo)
        self.tlacitko.grid(row=4, column=1)

    def prvni_cislo(self):
        cislo_a = 0
        cislo_b = 0
        vstup = 0

        operant = random.choice("+-*/")
        print(operant)
        self.varOperant.set(operant)

        if operant == "+":
            cislo_a = random.randint(0, 101)
            cislo_b = random.randint(0, 100 - cislo_a)
            self.varCisloa.set(cislo_a)
            self.varCislob.set(cislo_b)
            vstup = int(input())
            if vstup == (cislo_a + cislo_b):
                print("správně")
            else:
                print("špatně, správný výsledek je ", cislo_a + cislo_b)

        elif operant == "-":
            cislo_a = random.randint(0, 101)
            cislo_b = random.randint(0, cislo_a)
            self.varCisloa.set(cislo_a)
            self.varCislob.set(cislo_b)
            vstup = int(input())
            if vstup == (cislo_a - cislo_b):
                print("správně")
            else:
                print("špatně, správný výsledek je ", cislo_a - cislo_b)

        elif operant == "*":
            cislo_b = random.randint(2, 11)
            self.varCislob.set(cislo_b)

            if cislo_b == 2:
                cislo_a = random.randint(0, 51)
                self.varCisloa.set(cislo_a)
                vstup = int(input())
                if vstup == (cislo_a * cislo_b):
                    print("správně")
                else:
                    print("špatně, správný výsledek je ", cislo_a * cislo_b)

            if cislo_b == 3:
                cislo_a = random.randint(0, 34)
                self.varCisloa.set(cislo_a)
                vstup = int(input())
                if vstup == (cislo_a * cislo_b):
                    print("správně")
                else:
                    print("špatně, správný výsledek je ", cislo_a * cislo_b)

            if cislo_b == 4:
                cislo_a = random.randint(0, 26)
                self.varCisloa.set(cislo_a)
                vstup = int(input())
                if vstup == (cislo_a * cislo_b):
                    print("správně")
                else:
                    print("špatně, správný výsledek je ", cislo_a * cislo_b)

            if cislo_b == 5:
                cislo_a = random.randint(0, 21)
                self.varCisloa.set(cislo_a)
                vstup = int(input())
                if vstup == (cislo_a * cislo_b):
                    print("správně")
                else:
                    print("špatně, správný výsledek je ", cislo_a * cislo_b)

            if cislo_b == 6:
                cislo_a = random.randint(0, 17)
                self.varCisloa.set(cislo_a)
                vstup = int(input())
                if vstup == (cislo_a * cislo_b):
                    print("správně")
                else:
                    print("špatně, správný výsledek je ", cislo_a * cislo_b)

            if cislo_b == 7:
                cislo_a = random.randint(0, 15)
                self.varCisloa.set(cislo_a)
                vstup = int(input())
                if vstup == (cislo_a * cislo_b):
                    print("správně")
                else:
                    print("špatně, správný výsledek je ", cislo_a * cislo_b)

            if cislo_b == 8:
                cislo_a = random.randint(0, 13)
                self.varCisloa.set(cislo_a)
                vstup = int(input())
                if vstup == (cislo_a * cislo_b):
                    print("správně")
                else:
                    print("špatně, správný výsledek je ", cislo_a * cislo_b)

            if cislo_b == 9:
                cislo_a = random.randint(0, 12)
                self.varCisloa.set(cislo_a)
                vstup = int(input())
                if vstup == (cislo_a * cislo_b):
                    print("správně")
                else:
                    print("špatně, správný výsledek je ", cislo_a * cislo_b)

            if cislo_b == 10:
                cislo_a = random.randint(0, 11)
                self.varCisloa.set(cislo_a)
                vstup = int(input())
                if vstup == (cislo_a * cislo_b):
                    print("správně")
                else:
                    print("špatně, správný výsledek je ", cislo_a * cislo_b)

        elif operant == "/":
            cislo_a = random.randint(2, 101)
            cislo_b = random.randint(2, 11)
            self.varCisloa.set(cislo_a)
            self.varCislob.set(cislo_b)
            if cislo_a % cislo_b == 0:
                vstup = int(input())
                if vstup == (cislo_a / cislo_b):
                    print("správně")
                else:
                    print("špatně, správný výsledek je ", cislo_a / cislo_b)
            else:
                pass

        else:
            pass


root = tk.Tk()
app = Pocitani(root)
root.mainloop()
