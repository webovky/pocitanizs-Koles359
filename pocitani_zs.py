# -*- coding: utf-8 -*-

from os.path import basename, splitext
import tkinter as tk
from tkinter import Scale, Canvas, Entry, HORIZONTAL, StringVar, Label, Frame, messagebox, IntVar, Button
import random


class Pocitani(Frame):

    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("Počítání 1. stupeň ZŠ")
        self.master.maxsize(1500, 3000)
        self.master.resizable(True, True)
        self.master.rowconfigure(0, weight=500)
        self.master.rowconfigure(1, weight=500)
        self.master.rowconfigure(2, weight=500)
        self.master.rowconfigure(3, weight=500)
        self.master.rowconfigure(4, weight=500)
        self.master.rowconfigure(5, weight=500)
        self.master.columnconfigure(0, weight=1500)
        self.master.columnconfigure(1, weight=1500)
        self.master.columnconfigure(2, weight=1500)
        self.rozmisteni()
        self.zadani()
        
       

    def rozmisteni(self):
        self.nadpis = Label(text="Vítej v procvičování počítání")
        self.nadpis.grid(row=0, column=1)

        self.varCisloa = StringVar()
        self.cislo1 = Entry(textvariable=self.varCisloa, width=15, bd=10, justify="center", state="readonly")
        self.cislo1.grid(row=1, column=0)

        self.varOperant = StringVar()
        self.operant = Label(textvariable=self.varOperant, justify="center", font=("Helvetica", 18))
        self.operant.grid(row=1, column=1)

        self.varCislob = StringVar()
        self.cislo2 = Entry(textvariable=self.varCislob, width=15, bd=10, justify="center", state="readonly")
        self.cislo2.grid(row=1, column=2)

        self.napis = Label(text="Výsledek:")
        self.napis.grid(row=2, column=1)

        self.varClean = StringVar()
        self.rovna_se = Entry(textvariable=self.varClean, width=15, bd=10, justify="center")
        self.rovna_se.grid(row=3, column=1)

        self.tlacitko = Button(width=15, bd=10, justify="center", text="ověřit", command=self.overeni)
        self.tlacitko.grid(row=4, column=1)

        self.napis_spatne = Label(text="Špatně:")
        self.napis_spatne.grid(row=3, column=0)
        self.varSpatne = IntVar()
        self.pocitadlo1 = Entry(textvariable=self.varSpatne, width=7, bd=10, justify="center")
        self.pocitadlo1.grid(row=4, column=0)

        self.napis_spravne = Label(text="Správně:")
        self.napis_spravne.grid(row=3, column=2)
        self.varSpravne = IntVar()
        self.pocitadlo2 = Entry(textvariable=self.varSpravne, width=7, bd=10, justify="center")
        self.pocitadlo2.grid(row=4, column=2)

        self.tlacitko2 = Button(width=15, bd=10, justify="center", text="další příklad", command=self.zadani)
        self.tlacitko2.grid(row=5, column=0, columnspan=3, sticky="WE")



    def zadani(self):
        global cislo_a
        global cislo_b
        global operant
        cislo_a = 0
        cislo_b = 0
        self.rovna_se.configure(background="white")
       
        operant = random.choice("+-*/")
        self.varOperant.set(operant)

        if operant == "+":
            cislo_a = random.randint(0, 101)
            cislo_b = random.randint(0, 100 - cislo_a)
            self.varCisloa.set(cislo_a)
            self.varCislob.set(cislo_b)
            
        elif operant == "-":
            cislo_a = random.randint(0, 101)
            cislo_b = random.randint(0, cislo_a)
            self.varCisloa.set(cislo_a)
            self.varCislob.set(cislo_b)
            
        elif operant == "*":
            cislo_b = random.randint(2, 10)
            self.varCislob.set(cislo_b)

            if cislo_b == 2:
                cislo_a = random.randint(0, 50)
                self.varCisloa.set(cislo_a)
                
            if cislo_b == 3:
                cislo_a = random.randint(0, 33)
                self.varCisloa.set(cislo_a)
               

            if cislo_b == 4:
                cislo_a = random.randint(0, 25)
                self.varCisloa.set(cislo_a)
               
            if cislo_b == 5:
                cislo_a = random.randint(0, 20)
                self.varCisloa.set(cislo_a)
               
            if cislo_b == 6:
                cislo_a = random.randint(0, 16)
                self.varCisloa.set(cislo_a)
               
            if cislo_b == 7:
                cislo_a = random.randint(0, 14)
                self.varCisloa.set(cislo_a)
                

            if cislo_b == 8:
                cislo_a = random.randint(0, 12)
                self.varCisloa.set(cislo_a)
                
            if cislo_b == 9:
                cislo_a = random.randint(0, 11)
                self.varCisloa.set(cislo_a)
               
            if cislo_b == 10:
                cislo_a = random.randint(0, 10)
                self.varCisloa.set(cislo_a)
               
        elif operant == "/":
            cislo_a = random.randint(2, 100)
            cislo_b = random.randint(2, 10)

            while (cislo_a % cislo_b) != 0:
                cislo_a = random.randint(2, 100)
                cislo_b = random.randint(2, 10)

            self.varCisloa.set(cislo_a)
            self.varCislob.set(cislo_b)
        else:
            pass

    def overeni(self):
        vysledek = int(self.rovna_se.get())
        spravne = int(self.pocitadlo2.get())
        spatne = int(self.pocitadlo1.get())
        clean = ""
        
        if vysledek is not int():
            messagebox.showerror("Chyba", "zadejte výsledné číslo")
        else:
            if operant == "+":
                if vysledek == (cislo_a + cislo_b):
                    self.rovna_se.configure(background="#00FF00")
                    spravne += 1
                    self.varSpravne.set(spravne)
                else:
                    self.rovna_se.configure(background="red")
                    spatne += 1
                    self.varSpatne.set(spatne)

            elif operant == "-":
                if vysledek == (cislo_a - cislo_b):
                    self.rovna_se.configure(background="#00FF00")
                    spravne += 1
                    self.varSpravne.set(spravne)
                else:
                    self.rovna_se.configure(background="red")
                    spatne += 1
                    self.varSpatne.set(spatne)


            elif operant == "*":
                if vysledek == (cislo_a * cislo_b):
                    self.rovna_se.configure(background="#00FF00")
                    spravne += 1
                    self.varSpravne.set(spravne)
                else:
                    self.rovna_se.configure(background="red")
                    spatne += 1
                    self.varSpatne.set(spatne)


            else:
                if vysledek == (cislo_a / cislo_b):
                    self.rovna_se.configure(background="#00FF00")
                    spravne += 1
                    self.varSpravne.set(spravne)
                else:
                    self.rovna_se.configure(background="red")
                    spatne += 1 
                    self.varSpatne.set(spatne)

            self.varClean.set(clean)
        
       

root = tk.Tk()
app = Pocitani(root)
root.mainloop()
