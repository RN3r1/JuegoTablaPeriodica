import docx

doc = docx.Document('hueles a cacax2.docx')
descripciones=[]

for paragraph in doc.paragraphs:
    try:
        print('********************************************')

        elemento = paragraph.text[:paragraph.text.index('(')-1]
        desc = paragraph.text[paragraph.text.index('-')+2:]

        print(paragraph.text[:paragraph.text.index('(')-1])
        print(paragraph.text[paragraph.text.index('-')+2:])

        descripcion = [{
            'elemento': elemento,
            'desc': desc
        }]

        descripciones.extend(descripcion)

    except ValueError:
        print('sin index')

print(descripciones)
