import tkinter as tk
from tkinter import *


root = tk.Tk()

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

powitanie = tk.Label(root, text="Witamy w kalkulatorze BMI! ", font="Raleway")
powitanie.grid(columnspan=3, column=0, row=0)

L1 = Label(root, text="Podaj wage")
L1.grid(column=0, row=1)
wag = Entry(root, width=25)
wag.grid(column=1, row=1)

L2 = Label(root, text="Podaj wzrost w metrach")
L2.grid(column=0, row=2)
wzr = Entry(root, width=25)
wzr.grid(column=1, row=2)


def oblicz_bmi():
    while True:
        try:
            waga = float(wag.get())
            wzrost = float(wzr.get())
            break
        except ValueError:
            print("ERROR: wpisz jeszcze raz")

    BMI = waga / (wzrost ** 2)
    return BMI

def pokaz_bmi():
    BMI = oblicz_bmi()
    wyniki1 = Label(root, text=str("{:.2f}".format(BMI)))
    wyniki1.grid(column=1, row=3)
    BMIstr = str("{:.2f}".format(BMI))
    Outfile = open("wyniki.txt", "a+")
    Outfile.write(BMIstr + ", ")
    Outfile.close()

def dni():
    file = open("wyniki.txt", "r")
    dni = file.read()
    liczba_przecinkow = dni.count(",")
    print("Tyle dni już wyliczasz bmi: " + str(liczba_przecinkow))

def oblicz_srednia():
    with open("wyniki.txt", 'r') as file:
        zawartosc = file.read()
        numerki = zawartosc.split(", ")
        suma = 0
        count = 0
        for numer in numerki:
            try:
                num = float(numer.strip())
                suma += num
                count += 1
            except ValueError:
                pass
    if count > 0:
        srednia = suma / count
        wyniki2 = Label(root, text=str("srednie bmi z " + str(count) + " dni to " + "{:.2f}".format(srednia)))
        wyniki2.grid(column=0, row=3)
        return srednia
    else:
        return None

#GUZIK
guzik = tk.Button(root, text="Oblicz!", command=pokaz_bmi, width=20)
guzik.grid(column=2, row=3)

#GUZIK ŚREDNIA
guziksr = tk.Button(root, text="Policz średnia", command=oblicz_srednia)
guziksr.grid(column=2, row=0)

root.mainloop()