import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.font import Font
import wiringpi

wiringpi.wiringPiSetup()

wiringpi.pinMode(0, 1)
wiringpi.pinMode(1, 1)
wiringpi.pinMode(2, 1)

root = Tk()
root.resizable(width=False, height=False)
root.geometry('800x480')
root.title('Juego de Tabla Periódica')

gameMode = False
menu = True

selectedPin = 0

content = ttk.Frame(root)

def binDigitalWrite(num):
    num = bin(num)[2:].zfill(6)
    wiringpi.digitalWrite(0, int(num[5]))
    wiringpi.digitalWrite(1, int(num[4]))
    wiringpi.digitalWrite(2, int(num[3]))

def enableLabel():
    label.grid(column=0, row=0, columnspan=6, sticky=(N, S, E, W))
    desc.grid_remove()
    game.grid_remove()

def upCallback():
    print('up')

def downCallback():
    print('down')

def rightCallback():
    global selectedPin
    selectedPin+=1
    binDigitalWrite(selectedPin)
    print('right')

def leftCallback():
    global selectedPin
    selectedPin-=1
    binDigitalWrite(selectedPin)
    print('left')

def okCallback():
    print('OK')

def exitCallback():
    desc.grid(column=3, row=0, columnspan=3, sticky=(N, S, E, W))
    game.grid(column=0, row=0, columnspan=3, sticky=(N, S, E, W))
    label.grid_remove()
    menu = True
    gameMode = False
    print('Salir')

def gameCallback():
    enableLabel()
    menu = False
    gameMode = True
    print('Jugar')

def descCallback():
    gameMode = False
    menu = False
    enableLabel()
    print('Descripcion')


labelVar = tkinter.StringVar()
labelVar.set('TEXTO')

helv36 = Font(family='Helvetica', size=15, weight='bold')
labelFont = Font(family='Helvetica', size=15)

up = tkinter.Button(content, text = '^', command = upCallback, font=helv36)
down = tkinter.Button(content, text = '↓', command = downCallback, font=helv36)
right = tkinter.Button(content, text = '>', command = rightCallback, font=helv36)
left = tkinter.Button(content, text = '<', command = leftCallback, font=helv36)
ok = tkinter.Button(content, text = 'OK', command = okCallback, font=helv36)
salir = tkinter.Button(content, text = 'Salir', command = exitCallback, font=helv36)
desc = tkinter.Button(content, text = 'Descripción', command = descCallback, font=helv36)
game = tkinter.Button(content, text = 'Jugar', command = gameCallback, font=helv36)


label = tkinter.Label(content, textvariable=labelVar, relief=tkinter.RAISED, font=labelFont, wraplength=480, anchor='center')

content.grid(column=0, row=0, sticky=(N, S, E, W))

label.grid(column=0, row=0, columnspan=6, sticky=(N, S, E, W))
label.grid_remove()

desc.grid(column=3, row=0, columnspan=3, sticky=(N, S, E, W))
game.grid(column=0, row=0, columnspan=3, sticky=(N, S, E, W))
left.grid(column=0, row=1, rowspan=2, sticky=(N, S, E, W))
right.grid(column=2, row=1, rowspan=2, sticky=(N, S, E, W))
up.grid(column=1, row=1, sticky=(N, S, E, W))
down.grid(column=1, row=2, sticky=(N, S, E, W))
ok.grid(column=3, row=1, rowspan=2, sticky=(N, S, E, W))
salir.grid(column=5, row=1, rowspan=2, sticky=(N, S, E, W))


root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

content.columnconfigure(0, weight=2)
content.columnconfigure(1, weight=2)
content.columnconfigure(2, weight=2)
content.columnconfigure(3, weight=1)
content.columnconfigure(4, weight=1)
content.columnconfigure(5, weight=1)

content.rowconfigure(0, weight=70)
content.rowconfigure(1, weight=15)
content.rowconfigure(2, weight=15)

root.mainloop()

