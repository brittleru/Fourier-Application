import scipy
import numpy as np
import matplotlib.pyplot as plt
from operator import add
import tkinter as tk
from tkinter import *
from functools import partial


def fierastrau(f, N, m, n, A, dt, d):
    an = []
    bn = []
    for x in range(0, n):
        if x == 0:
            b = 0
        else:
            b = A / (x * np.pi)
            # b=int(b)
        an.append(0)
        bn.append(b)
        x = x + 1
    return an, bn


def rectificat(f, N, m, n, A, dt, d):
    an = []
    bn = []
    for x in range(0, n):
        if x == 0:
            a = 2 * A / np.pi
        else:
            a = -4 * A / (np.pi * (4 * x ^ 2 - 1))
        an.append(a)
        bn.append(0)
        x = x + 1
    return an, bn


def cosinus(f, N, m, n, A, dt, d):
    an = []
    bn = []
    for x in range(0, n):
        if x == 0:
            a = 0
        elif x == 1:
            a = A
        else:
            a = 0
        an.append(a)
        bn.append(0)
        x = x + 1
    return an, bn


def pulse(f, N, m, n, A, dt, d):
    an = []
    bn = []
    for x in range(0, n):
        if x == 0:
            a = A * d
        else:
            a = ((2 * A) / (x * np.pi)) * np.sin(x * np.pi * d)
            b = 0
        an.append(a)
        bn.append(0)
        x = x + 1
    return an, bn


def square(f, N, m, n, A, dt, d):
    an = []
    bn = []
    for x in range(0, n):
        if x == 0:
            a = 0
        else:
            a = ((2 * A) / (x * np.pi)) * np.sin((x * np.pi) / 2)
            b = 0
        an.append(a)
        bn.append(0)
        x = x + 1
    return an, bn


def triangle(f, N, m, n, A, dt, d):
    an = []
    bn = []
    for x in range(0, n):
        if x == 0:
            a = 0
        else:
            a = (4 * A) / pow((x * np.pi), 2)
            b = 0
        an.append(a)
        bn.append(0)
        x = x + 1
    return an, bn


def seria_fourier(an, bn, f, N, m, n, A, dt, d):
    listaunde = []

    for w in range(0, n):
        unda = []
        for y in range(0, N * m):
            cos = np.cos(2 * np.pi * f * w * dt * y)
            sin = np.sin(2 * np.pi * f * w * dt * y)
            zz = an[w] * cos + bn[w] * sin
            unda.append(zz)  # se inmulteste an si bn cu cosarg/singarg si se aduna
            y = y + 1
        listaunde.append(unda)
        w = w + 1

    list_sum = np.zeros(len(listaunde[0]))  # se aduna lista cu lista, element cu element ==> o lista cu un numar N*m
    # de elemente
    for i in listaunde:
        list_sum += i
    list_sum = list_sum.tolist()

    print("an=", an)
    print("bn=", bn)

    return listaunde, list_sum


'''
def plot(listaunde,list_sum):
    window = Frame(root)
   # plt.figure()
    fig = plt.figure(figsize=(4, 4),dpi=60)
    plt.subplot(611)
    plt.plot(listaunde[0],'g')
    #plt.subplot(612)
    plt.plot(listaunde[1],'b')
    #plt.subplot(613)
    plt.plot(listaunde[2],'r')
    #plt.subplot(614)
    plt.plot(listaunde[3],'m')
    #plt.subplot(615)
    plt.plot(listaunde[4],'k')
    plt.subplot(616)
    plt.plot(list_sum)
   # plt.show()
    plt.bar(2, 2)
    #plt.xticks(x, rotation=90)
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().grid(row=0, column=5, ipadx=40, ipady=20)
    window.place(x=300,y=10)
'''


def plot(listaunde, list_sum, nr_unda):
    plt.figure()
    plt.subplot(611, title='Primele 5 unde')
    plt.plot(listaunde[0], 'lime')
    plt.plot(listaunde[1], 'cyan')
    plt.plot(listaunde[2], 'red')
    plt.plot(listaunde[3], 'violet')
    plt.plot(listaunde[4], 'black')
    plt.subplot(613, title='Suma de unde')
    plt.plot(list_sum)
    plt.subplot(615, title='Unda aleasa')
    plt.plot(listaunde[nr_unda])
    plt.show()


def aplicatie(semnal, f, N, m, n, A, dt, d, nr_unda):
    if semnal == "Fierastrau":
        fs = fierastrau(f, N, m, n, A, dt, d)
        fourier = seria_fourier(fs[0], fs[1], f, N, m, n, A, dt, d)
        plot(fourier[0], fourier[1], nr_unda)
    elif semnal == "Rectificat":
        fs = rectificat(f, N, m, n, A, dt, d)
        fourier = seria_fourier(fs[0], fs[1], f, N, m, n, A, dt, d)
        plot(fourier[0], fourier[1], nr_unda)
    elif semnal == "Cosinus":
        fs = cosinus(f, N, m, n, A, dt, d)
        fourier = seria_fourier(fs[0], fs[1], f, N, m, n, A, dt, d)
        plot(fourier[0], fourier[1], nr_unda)
    elif semnal == "Puls":
        fs = pulse(f, N, m, n, A, dt, d)
        fourier = seria_fourier(fs[0], fs[1], f, N, m, n, A, dt, d)
        plot(fourier[0], fourier[1], nr_unda)
    elif semnal == "Patrat":
        fs = square(f, N, m, n, A, dt, d)
        fourier = seria_fourier(fs[0], fs[1], f, N, m, n, A, dt, d)
        plot(fourier[0], fourier[1], nr_unda)
    elif semnal == "Triunghi":
        fs = triangle(f, N, m, n, A, dt, d)
        fourier = seria_fourier(fs[0], fs[1], f, N, m, n, A, dt, d)
        plot(fourier[0], fourier[1], nr_unda)


def update():
    semnal = var_tip_semnal.get()
    frecventa = int(input_frecventa.get())
    nr_sample = int(input_nr_sample.get())
    nr_unde = int(input_nr_unde.get())
    nr_perioade = int(input_nr_perioade.get())
    amplitudine = int(input_amplitudine.get())
    nr_unda = int(input_afiseaza_unda.get())
    T = 1 / frecventa
    dt = T / nr_sample
    k = 0.02
    d = k / T
    aplicatie(semnal, frecventa, nr_sample, nr_perioade, nr_unde, amplitudine, dt, d, nr_unda)
    # aplicatie(frecventa,nr_sample,nr_perioade,nr_unde,amplitudine)
    return 0


root = tk.Tk()
root.title("Serie Fourier")
root.geometry("250x300")
# root.resizable(0,0)
input_frecventa = StringVar(root)
input_amplitudine = StringVar(root)
input_nr_sample = StringVar(root)
input_nr_unde = StringVar(root)
input_nr_perioade = StringVar(root)
input_afiseaza_unda = StringVar(root)
tip_semnal = ["Fierastrau", "Rectificat", "Cosinus", "Puls", "Patrat", "Triunghi"]
var_tip_semnal = StringVar(root)
var_tip_semnal.set(tip_semnal[0])

frecventa_lb = tk.Label(root, text="Frecventa").grid(row=0, column=0, pady=5)
frecventa_En = tk.Entry(root, textvariable=input_frecventa).grid(row=0, column=1)

nr_sample_lb = tk.Label(root, text="Nr sample/s").grid(row=1, column=0, pady=5)
nr_sample_En = tk.Entry(root, textvariable=input_nr_sample).grid(row=1, column=1)

nr_unde_lb = tk.Label(root, text="Nr unde").grid(row=2, column=0, pady=5)
nr_unde_En = tk.Entry(root, textvariable=input_nr_unde).grid(row=2, column=1)

nr_perioade_lb = tk.Label(root, text="Nr perioade").grid(row=3, column=0, pady=5)
nr_perioade_En = tk.Entry(root, textvariable=input_nr_perioade).grid(row=3, column=1)

amplitudine_lb = tk.Label(root, text="Amplitudine").grid(row=4, column=0, pady=5)
amplitudine_En = tk.Entry(root, textvariable=input_amplitudine).grid(row=4, column=1)

afiseaza_unda_lb = tk.Label(root, text="Afiseaza unda").grid(row=5, column=0, pady=5)
afiseaza_unda_En = tk.Entry(root, textvariable=input_afiseaza_unda).grid(row=5, column=1)

tip_semnal_lb = tk.Label(root, text="Tip Semnal").grid(row=6, column=0, pady=5)
optiune_semnal = OptionMenu(root, var_tip_semnal, *tip_semnal)
optiune_semnal.grid(row=6, column=1, sticky="ew")

call_update = partial(update)
button_update = tk.Button(root, text="Refresh", command=call_update).grid(row=9, column=0)
root.mainloop()
# info = tk.Label(root,text="Aceata aplicatie a fost realizata\n de catre Mocanu Sebastian si\n Draghici Andrei \n in
# cadrul laboratorului \n Sisteme de achiziþie \n ºi interfeþe-instrumentaþie \n virtualã  sub indrumarea \n domnului
# profesor Coanda Philip ").grid(row=10,column=1,sticky=W)


# root.mainloop()

