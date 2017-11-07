import docx

doc = docx.Document('hueles a caca.docx')
preguntas=[]

for paragraph in doc.paragraphs:
    try:
        print('********************************************')
        # print('index -> {}'.format(paragraph.text.index('¿')))
        # print('frase -> {}'.format(paragraph.text))
        text = paragraph.text[paragraph.text.index('¿'):paragraph.text.index('?')+1]
        answer = paragraph.text[paragraph.text.index('(')+1:paragraph.text.index(')')]

        print(paragraph.text[paragraph.text.index('¿'):paragraph.text.index('?')+1])
        print(paragraph.text[paragraph.text.index('(')+1:paragraph.text.index(')')])

        pregunta = [{
            'pregunta': text,
            'respuesta': answer
        }]

        preguntas.extend(pregunta)

    except ValueError:
        print('sin index')

print(preguntas)[{'pregunta': '¿Elemento semejante a la plata?', 'respuesta': 'Aluminio'}, {'pregunta': '¿Elemento cuyo número atómico es 51?', 'respuesta': 'Antimonio'}, {'pregunta': '¿Elemento muy venenoso utilizado en la medicina?', 'respuesta': 'Arsénico'}, {'pregunta': '¿Elemento que se obtiene bombardeando bismuto con partículas alfa?', 'respuesta': 'Ástato'}, {'pregunta': '¿Elemento usado para fabricar pólvora e insecticidas?', 'respuesta': 'Azufre'}, {'pregunta': '¿Elemento que se usa en la fabricación de pinturas?', 'respuesta': 'Bario'}, {'pregunta': '¿Elemento usado principalmente en la industria atómica?', 'respuesta': 'Berilio'}, {'pregunta': '¿Elemento que es un metal de color blanco agrisado con tinte rojizo, duro y quebradizo y fácilmente fusible?', 'respuesta': 'Bismuto'}, {'pregunta': '¿Elemento que se usa en la industria metalúrgica y en los reactores nucleares?', 'respuesta': 'Boro'}, {'pregunta': '¿Elemento que irrita las membranas mucosas y ataca todos los metales?', 'respuesta': 'Bromo'}, {'pregunta': '¿Elemento que es muy blando, de color blanco brillante?', 'respuesta': 'Calcio'}, {'pregunta': '¿Elemento que abunda en la naturaleza como principal componente de sustancias orgánicas?', 'respuesta': 'Carbono'}, {'pregunta': '¿Elemento que se inflama en contacto con el aire?', 'respuesta': 'Cesio'}, {'pregunta': '¿Elemento que se utiliza como desinfectante y decolorante?', 'respuesta': 'Cloro'}, {'pregunta': '¿Elemento que es fácilmente deformable; descompone el agua, se oxida al aire rápidamente?', 'respuesta': 'Estroncio'}, {'pregunta': '¿Elemento que es el más electronegativo y reactivo de todos los elementos?', 'respuesta': 'Flúor'}, {'pregunta': '¿Elemento que se encuentra en la naturaleza combinado en fosfatos inorgánicos y en organismos vivos pero nunca en estado nativo?', 'respuesta': 'Fósforo'}, {'pregunta': '¿Elemento que es un metal líquido que neutraliza los ácidos?', 'respuesta': 'Francio'}, {'pregunta': '¿Elemento que se extrae principalmente del mineral bauxita, en el que se encuentra en muy pequeña proporción?', 'respuesta': 'Galio'}, {'pregunta': '¿Elemento que tiene propiedades como semiconductor?', 'respuesta': 'Germanio'}, {'pregunta': '¿Elemento más ligero que el aire?', 'respuesta': 'Helio'}, {'pregunta': '¿Elemento que en condiciones normales de presión y temperatura, es un gas incoloro, inodoro y altamente inflamable?', 'respuesta': 'Hidrógeno'}, {'pregunta': '¿Elemento muy escaso en la naturaleza?', 'respuesta': 'Indio'}, {'pregunta': '¿Elemento que es el menos electronegativo y reactivo?', 'respuesta': 'Yodo'}, {'pregunta': '¿Elemento que se usa en la producción de fármacos antidepresivos?', 'respuesta': 'Litio'}, {'pregunta': '¿Elemento que se utiliza en las aleaciones ligeras, en baterías?', 'respuesta': 'Magnesio'}, {'pregunta': '¿Elemento que constituye del orden del 78% del aire atmosférico?', 'respuesta': 'Nitrógeno'}, {'pregunta': '¿Elemento indispensable para la vida del ser humano?', 'respuesta': 'Oxígeno'}, {'pregunta': '¿Elemento que se usa principalmente para fabricar balas para las armas de fuego?', 'respuesta': 'Plomo'}, {'pregunta': '¿Elemento que se utiliza como fuente de neutrones  y fue descubierto por Marie Curie?', 'respuesta': 'Polonio'}, {'pregunta': '¿Elemento que es un nutriente esencial para los seres vivos?', 'respuesta': 'Potasio'}, {'pregunta': '¿Elemento que es extremadamente radiactivo, un millón de veces más que el uranio?', 'respuesta': 'Radio'}, {'pregunta': '¿Elemento que se utiliza como catalizador y en la fabricación de vidrios especiales?', 'respuesta': 'Rubidio'}, {'pregunta': '¿Elemento muy abundante en la corteza terrestre, y forma parte de la arena y las rocas?', 'respuesta': 'Silicio'}, {'pregunta': '¿Elemento parecido al plomo?', 'respuesta': 'Talio'}, {'pregunta': '¿Elemento que se obtiene del cobre y se utiliza en aleaciones?', 'respuesta': 'Teluro'}]
