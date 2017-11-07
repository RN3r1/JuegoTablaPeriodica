import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.font import Font
from random import randint

import wiringpi

# 7, 15, 23, 31
secuencia = [0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 32, 33, 34, 35, 36, 37, 7, 15, 23, 31]

secuenciaElementos = [21, 24, 34, 30, 32, 12, 17, 6, 25, 10, 14, 5, 31, 8, 0, 18, 22, 35, 11, 33, 19, 37, 28, 26, 16, 2, 1, 7, 27, 4, 20, 36, 29, 15, 13, 9, 23, 3]
preguntas = [{'pregunta': '¿Elemento semejante a la plata?', 'respuesta': 'Aluminio'}, {'pregunta': '¿Elemento cuyo número atómico es 51?', 'respuesta': 'Antimonio'}, {'pregunta': '¿Elemento muy venenoso utilizado en la medicina?', 'respuesta': 'Arsénico'}, {'pregunta': '¿Elemento que se obtiene bombardeando bismuto con partículas alfa?', 'respuesta': 'Ástato'}, {'pregunta': '¿Elemento usado para fabricar pólvora e insecticidas?', 'respuesta': 'Azufre'}, {'pregunta': '¿Elemento que se usa en la fabricación de pinturas?', 'respuesta': 'Bario'}, {'pregunta': '¿Elemento usado principalmente en la industria atómica?', 'respuesta': 'Berilio'}, {'pregunta': '¿Elemento que es un metal de color blanco agrisado con tinte rojizo, duro y quebradizo y fácilmente fusible?', 'respuesta': 'Bismuto'}, {'pregunta': '¿Elemento que se usa en la industria metalúrgica y en los reactores nucleares?', 'respuesta': 'Boro'}, {'pregunta': '¿Elemento que irrita las membranas mucosas y ataca todos los metales?', 'respuesta': 'Bromo'}, {'pregunta': '¿Elemento que es muy blando, de color blanco brillante?', 'respuesta': 'Calcio'}, {'pregunta': '¿Elemento que abunda en la naturaleza como principal componente de sustancias orgánicas?', 'respuesta': 'Carbono'}, {'pregunta': '¿Elemento que se inflama en contacto con el aire?', 'respuesta': 'Cesio'}, {'pregunta': '¿Elemento que se utiliza como desinfectante y decolorante?', 'respuesta': 'Cloro'}, {'pregunta': '¿Elemento que es fácilmente deformable; descompone el agua, se oxida al aire rápidamente?', 'respuesta': 'Estroncio'}, {'pregunta': '¿Elemento que es el más electronegativo y reactivo de todos los elementos?', 'respuesta': 'Flúor'}, {'pregunta': '¿Elemento que se encuentra en la naturaleza combinado en fosfatos inorgánicos y en organismos vivos pero nunca en estado nativo?', 'respuesta': 'Fósforo'}, {'pregunta': '¿Elemento que es un metal líquido que neutraliza los ácidos?', 'respuesta': 'Francio'}, {'pregunta': '¿Elemento que se extrae principalmente del mineral bauxita, en el que se encuentra en muy pequeña proporción?', 'respuesta': 'Galio'}, {'pregunta': '¿Elemento que tiene propiedades como semiconductor?', 'respuesta': 'Germanio'}, {'pregunta': '¿Elemento que se utiliza para proceso de fotocopiado Xerográfico?', 'respuesta': 'Selenio'}, {'pregunta': '¿Elemento que en condiciones normales de presión y temperatura, es un gas incoloro, inodoro y altamente inflamable?', 'respuesta': 'Hidrógeno'}, {'pregunta': '¿Elemento muy escaso en la naturaleza?', 'respuesta': 'Indio'}, {'pregunta': '¿Elemento que es el menos electronegativo y reactivo?', 'respuesta': 'Yodo'}, {'pregunta': '¿Elemento que se usa en la producción de fármacos antidepresivos?', 'respuesta': 'Litio'}, {'pregunta': '¿Elemento que se utiliza en las aleaciones ligeras, en baterías?', 'respuesta': 'Magnesio'}, {'pregunta': '¿Elemento que constituye del orden del 78% del aire atmosférico?', 'respuesta': 'Nitrógeno'}, {'pregunta': '¿Elemento indispensable para la vida del ser humano?', 'respuesta': 'Oxígeno'}, {'pregunta': '¿Elemento que se usa principalmente para fabricar balas para las armas de fuego?', 'respuesta': 'Plomo'}, {'pregunta': '¿Elemento que se utiliza como fuente de neutrones  y fue descubierto por Marie Curie?', 'respuesta': 'Polonio'}, {'pregunta': '¿Elemento que es un nutriente esencial para los seres vivos?', 'respuesta': 'Potasio'}, {'pregunta': '¿Elemento que es extremadamente radiactivo, un millón de veces más que el uranio?', 'respuesta': 'Radio'}, {'pregunta': '¿Elemento que se utiliza como catalizador y en la fabricación de vidrios especiales?', 'respuesta': 'Rubidio'}, {'pregunta': '¿Elemento muy abundante en la corteza terrestre, y forma parte de la arena y las rocas?', 'respuesta': 'Silicio'}, {'pregunta': '¿Elemento que sirve como condimento o descongelante?', 'respuesta': 'Sodio'},{'pregunta': '¿Elemento parecido al plomo?', 'respuesta': 'Talio'}, {'pregunta': '¿Elemento que se obtiene del cobre y se utiliza en aleaciones?', 'respuesta': 'Teluro'}, {'pregunta': '¿Elemento químico que se funde a baja temperatura y se aplica para el recubrimiento de envases de acero?', 'respuesta': 'Estaño'}]
descripciones= [{'elemento': 'Aluminio', 'desc': 'Elemento químico de símbolo Al y número atómico 13; es un metal ligero y dúctil, de color y brillo semejantes a los de la plata, inoxidable y buen conductor eléctrico y térmico una batería de cocina hecha de aluminio. '}, {'elemento': 'Antimonio', 'desc': 'Elemento químico de símbolo Sb y número atómico 51; es un semimetal de color blanco azulado, brillante y quebradizo, por lo que se suele utilizar formando aleaciones (por ejemplo, aleado con plomo y estaño sirve para fabricar los caracteres de imprenta) '}, {'elemento': 'Arsénico', 'desc': 'Elemento químico de símbolo As y número atómico 33; es un semimetal sólido, de color gris metálico, muy venenoso y se usa en medicina, en proporciones adecuadas, para tratar diversas enfermedades. '}, {'elemento': 'Ástato', 'desc': 'Elemento químico de símbolo At y número atómico 85; es un semimetal radiactivo, sólido, que se obtiene bombardeando bismuto con partículas alfa.'}, {'elemento': 'Azufre', 'desc': 'Elemento químico amarillo usado para fabricar pólvora e insecticidas El símbolo químico del azufre es S y su número atómico es 16. '}, {'elemento': 'Bario', 'desc': 'Elemento químico de símbolo Ba y número atómico 56; es de color blanco plateado, blando, pesado, dúctil y difícil de fundir, que se oxida rápidamente en contacto con el aire y el agua; se usa en la fabricación de pinturas. '}, {'elemento': 'Berilio', 'desc': 'Elemento químico de símbolo Be y número atómico 4; es un metal, de color grisáceo, elástico y resistente, usado principalmente en la industria atómica. '}, {'elemento': 'Bismuto', 'desc': 'Elemento químico de símbolo Bi y número atómico 83; es un metal de color blanco agrisado con tinte rojizo, duro y quebradizo y fácilmente fusible; se emplea en la fabricación de medicamentos. '}, {'elemento': 'Boro', 'desc': 'Elemento químico de símbolo B y número atómico 5; es de color pardo oscuro, duro como el diamante, frágil y mal conductor de la electricidad, aunque puede hacerse conductor; en la naturaleza solamente se encuentra combinado con otros elementos; se usa en la industria metalúrgica y en los reactores nucleares. '}, {'elemento': 'Bromo', 'desc': 'Elemento químico de símbolo Br y número atómico 35; es un líquido a temperatura normal, de color rojo pardusco, volátil, de olor fuerte y repugnante, que irrita las membranas mucosas y ataca todos los metales.'}, {'elemento': 'Calcio', 'desc': 'Elemento químico de símbolo Ca y número atómico 20; es muy blando, de color blanco brillante; se oxida con el aire y el agua y, combinado con el oxígeno, forma la cal. '}, {'elemento': 'Carbono', 'desc': 'Elemento químico de símbolo C y número atómico 6; es un no metal sólido, sin olor ni sabor y abunda en la naturaleza como principal componente de sustancias orgánicas'}, {'elemento': 'Cesio', 'desc': 'Elemento químico de símbolo Cs y número atómico 55; es un metal alcalino de color blanco plateado; se inflama en contacto con el aire y se utiliza para fabricar células fotoeléctricas. '}, {'elemento': 'Cloro', 'desc': 'Elemento químico de símbolo Cl y número atómico 17; es un gas tóxico de color amarillo verdoso que se utiliza como desinfectante y decolorante el cloro pertenece al grupo de los halógenos. '}, {'elemento': 'Estroncio', 'desc': 'Elemento químico de símbolo Sr y número atómico 38; es un metal de color amarillo, poco brillante, fácilmente deformable; descompone el agua, se oxida al aire rápidamente y arde con llama muy brillante. '}, {'elemento': 'Flúor', 'desc': 'El flúor es el elemento químico de número atómico 9, su símbolo es F. Es un gas a temperatura ambiente, de color amarillo pálido, formado por moléculas diatómicas. Es el más electronegativo y reactivo de todos los elementos. En forma pura es altamente peligroso, causando graves quemaduras químicas en contacto con la piel. '}, {'elemento': 'Fósforo', 'desc': 'El fósforo es un elemento químico de número atómico 15 y símbolo P. Es un no metal multivalente perteneciente al grupo del nitrógeno (Grupo 15 (VA): nitrogenoideos) que se encuentra en la naturaleza combinado en fosfatos inorgánicos y en organismos vivos pero nunca en estado nativo. Es muy reactivo y se oxida espontáneamente en contacto con el oxígeno atmosférico emitiendo luz. '}, {'elemento': 'Francio', 'desc': 'Elemento químico de símbolo Fr y número atómico 87; es un metal líquido que neutraliza los ácidos y que es muy radiactivo el isótopo más estable del francio tiene una vida media de 21 mn. '}, {'elemento': 'Galio', 'desc': 'Elemento químico de símbolo Ga y número atómico 31, de color blanco brillante o gris azulado, duro y maleable, que se usa en odontología el galio se extrae principalmente del mineral bauxita, en el que se encuentra en muy pequeña proporción (0,01%) '}, {'elemento': 'Germanio', 'desc': 'Elemento químico de símbolo Ge y número atómico 32; es sólido de color blanco grisáceo, duro, muy resistente a los ácidos y a las bases, que se utiliza en la fabricación de transistores y otros dispositivos electrónicos por sus propiedades como semiconductor. '}, {'elemento': 'Selenio', 'desc': 'Propiedades semejantes a las del Teluro. Uno de sus usos usos son el proceso de fotocopiado Xerográico y decoloración de vidrios.'}, {'elemento': 'Hidrógeno', 'desc': 'El hidrógeno es un elemento químico representado por el símbolo H y con un número atómico de 1. En condiciones normales de presión y temperatura, es un gas diatómico (H2) incoloro, inodoro, insípido, no metálico y altamente inflamable. '}, {'elemento': 'Indio', 'desc': 'Elemento químico de símbolo In y número atómico 49; es un metal blanco y brillante, blando y muy escaso en la naturaleza, que se utiliza en algunos compuestos semiconductores. '}, {'elemento': 'Yodo', 'desc': 'El yodo es un elemento químico de número atómico 53, su símbolo es I, es un oligoelemento y se emplea principalmente en medicina, fotografía y como colorante. Químicamente, el yodo es el halógeno menos reactivo y electronegativo.'}, {'elemento': 'Litio', 'desc': 'Elemento químico de símbolo Li y número atómico 3; es un metal brillante, blanco plateado, blando y ligero, del grupo de los alcalinos; se usa en la producción de fármacos antidepresivos y, en combinación con otros metales, en la fabricación de cerámicas y vidrios especiales, etc. '}, {'elemento': 'Magnesio', 'desc': 'Elemento químico de símbolo Mg y número atómico 12; es un metal, de color plateado, maleable y ligero, que arde con una llama blanca brillante; se utiliza en las aleaciones ligeras, en baterías y para obtener aceites especiales que se utilizan en luminotecnia y fotografía y es un elemento esencial para los seres vivos. '}, {'elemento': 'Nitrógeno', 'desc': 'El nitrógeno es un elemento químico, de número atómico 7, símbolo N y que en condiciones normales forma un gas diatómico (nitrógeno diatómico o molecular) que constituye del orden del 78% del aire atmosférico. '}, {'elemento': 'Oxígeno', 'desc': 'El oxígeno es un elemento químico de número atómico 8 y símbolo O. En su forma molecular más frecuente, O2, es un gas a temperatura ambiente. Representa aproximadamente el 20,9% en volumen de la composición de la atmósfera terrestre.  '}, {'elemento': 'Plomo', 'desc': 'Elemento químico de símbolo Pb y número atómico 82; es un metal denso, blando y de color gris azulado, muy maleable, dúctil y poco conductor del calor y la electricidad, que se oxida fácilmente en contacto con el aire; se usa principalmente para fabricar tubos, pinturas y balas para las armas de fuego. '}, {'elemento': 'Polonio', 'desc': 'Elemento químico de símbolo Po y número atómico 84 que pertenece al grupo de los anfígenos; es un metal raro muy tóxico y muy radiactivo que se utiliza como fuente de neutrones y partículas alfa; procede de la desintegración del radio el polonio fue descubierto por Marie Curie. '}, {'elemento': 'Potasio', 'desc': 'Elemento químico de símbolo K y número atómico 19; es un metal alcalino, muy reactivo, de color plateado, blando y ligero; se oxida fácilmente y produce llama en contacto con el agua, ya que se inflama espontáneamente desprendiendo hidrógeno; tiene infinidad de aplicaciones (medicina, fotografía, metalurgia, etc) y es un nutriente esencial para los seres vivos los componentes del potasio se usan como abono. '}, {'elemento': 'Radio', 'desc': 'El radio es un elemento químico de la tabla periódica. Su símbolo es Ra y su número atómico es 88. '}, {'elemento': 'Rubidio', 'desc': 'Elemento químico de símbolo Rb y número atómico 37; es un metal parecido al potasio, pero más blando y pesado; se utiliza en semiconductores, como catalizador y en la fabricación de vidrios especiales. '}, {'elemento': 'Silicio', 'desc': 'Elemento químico de símbolo Si y número atómico 14, en su forma cristalina, es gris y con brillo metálico, y en su variante amorfa es de color amarillento, muy abundante en la corteza terrestre, y forma parte de la arena y las rocas; se utiliza en la industria del acero como componente de aleaciones, en la fabricación de células solares, rectificadores, transistores y circuitos integrados, así como en vidrios, material refractario, cementos, etc. '}, {'elemento': 'Sodio', 'desc': 'Elemento químico de símbolo Na y número atómico 11; es de color plateado, blando y maleable, buen reductor y muy abundante en la naturaleza; forma sales con otros elementos, es muy reactivo y se descompone con el agua y se oxida con el aire; se utiliza en la conservación de alimentos, como descongelante, como condimento (forma parte de la sal común), etc; es esencial para los seres vivos. '}, {'elemento': 'Talio', 'desc': 'Elemento químico de símbolo Tl y número atómico 81; es un metal blando, pesado, brillante, dúctil y maleable, de color azulado y parecido al plomo, y tanto él como sus compuestos son muy venenosos; se empleaba sobre todo en la fabricación de insecticidas (actualmente este uso está prohibido) y sus aplicaciones hoy en día son escasas construcción de ciertos vidrios, aleaciones experimentales y electrónica. '}, {'elemento': 'Teluro', 'desc': 'Elemento químico de símbolo Te y número atómico 52, que pertenece al grupo de los anfígenos; es quebradizo y cristalino, y de color plateado cuando se encuentra en estado sólido; se obtiene del cobre y se utiliza en aleaciones, en la fabricación de semiconductores, en vidrio y en cerámica.'}, {'elemento': 'Estaño', 'desc': 'Se funde a baja temperatura tiene gran fluidez, es suave, felxible y resistente a la corrosión.'}]

print('Preguntas -> {}'.format(len(preguntas)))
print('Descripciones -> {}'.format(len(descripciones)))

gameMode = False
menu = True

puntaje = 0
selectedPin = 0
randomIndex = 0

wiringpi.wiringPiSetup()
#
wiringpi.pinMode(0, 1)
wiringpi.pinMode(1, 1)
wiringpi.pinMode(2, 1)
wiringpi.pinMode(3, 1)
wiringpi.pinMode(4, 1)
wiringpi.pinMode(5, 1)
wiringpi.pinMode(6, 1)

root = Tk()
root.resizable(width=False, height=False)
root.geometry('800x480')
root.title('Juego de Tabla Periódica')

content = ttk.Frame(root)

def enableLeds():
    wiringpi.digitalWrite(6, 1)  # enable!
    print('LEDS ENABLED')

def disableLeds():
    wiringpi.digitalWrite(6, 0)  # disable!
    print('LEDS DISABLED')

def binDigitalWrite(num):
    num = bin(num)[2:].zfill(6)
    wiringpi.digitalWrite(0, int(num[5]))
    wiringpi.digitalWrite(1, int(num[4]))
    wiringpi.digitalWrite(2, int(num[3]))
    wiringpi.digitalWrite(3, int(num[2]))
    wiringpi.digitalWrite(4, int(num[1]))
    wiringpi.digitalWrite(5, int(num[0]))

def enableLabel():
    label.grid(column=0, row=0, columnspan=6, sticky=(N, S, E, W))
    desc.grid_remove()
    game.grid_remove()

def upCallback():
    if (selectedPin > 0 and menu == False):
        global selectedPin
        selectedPin -= 1
        binDigitalWrite(secuencia[selectedPin])
        if gameMode == False:
            setLabelText()
        print('left')

def downCallback():
    if selectedPin < 37 and menu == False:
        global selectedPin
        selectedPin+=1
        binDigitalWrite(secuencia[selectedPin])
        if gameMode == False:
            setLabelText()
        print('right')

def rightCallback():
    if selectedPin < 33 and menu == False:
        global selectedPin
        selectedPin+=5
        binDigitalWrite(secuencia[selectedPin])
        if gameMode == False:
            setLabelText()
        print('right')

def leftCallback():
    if(selectedPin > 4  and menu == False):
        global selectedPin
        selectedPin-=5
        binDigitalWrite(secuencia[selectedPin])
        if gameMode == False:
            setLabelText()
        print('left')

def okCallback():
    global randomIndex
    global puntaje
    if menu == False and gameMode == True:
        if preguntas[randomIndex]['respuesta'] == descripciones[secuenciaElementos[selectedPin]]['elemento']:
            puntaje += 1
            randomIndex = randint(0, 37)
            labelVar.set('{}\n\nPuntaje = {}'.format(preguntas[randomIndex]['pregunta'], puntaje))
            print('OK')
        else:
            labelVar.set('FALLASTE!\n\nPuntaje Final: {}'.format(puntaje))

def exitCallback():
    global menu
    global gameMode
    global selectedPin
    global puntaje
    desc.grid(column=3, row=0, columnspan=3, sticky=(N, S, E, W))
    game.grid(column=0, row=0, columnspan=3, sticky=(N, S, E, W))
    label.grid_remove()
    disableLeds()
    menu = True
    gameMode = False
    selectedPin = 0
    binDigitalWrite(0)
    puntaje = 0
    print('Salir gameMode={} & menu={}'.format(gameMode, menu))

def gameCallback():
    global menu
    global gameMode
    global selectedPin
    global randomIndex
    enableLabel()
    enableLeds()
    menu = False
    gameMode = True
    randomIndex = randint(0, 37)
    labelVar.set('{}\n\nPuntaje = {}'.format(preguntas[randomIndex]['pregunta'], puntaje))
    print('Jugar gameMode={} & menu={}'.format(gameMode, menu))

def descCallback():
    global menu
    global gameMode
    global selectedPin
    gameMode = False
    menu = False
    enableLeds()
    enableLabel()
    setLabelText()
    print('Descripcion gameMode={} & menu={}'.format(gameMode, menu))

def setLabelText():
    if gameMode == False:
        labelVar.set('{} - {}'.format(descripciones[secuenciaElementos[selectedPin]]['elemento'], descripciones[secuenciaElementos[selectedPin]]['desc']))

labelVar = tkinter.StringVar()

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

