
preguntas = [{
    'pregunta':'pregunta1',
    'respuesta':'respuesta1'
},{
    'pregunta':'pregunta2',
    'respuesta':'respuesta2'
}]

preguntas2 = [{
    'pregunta':'pregunta1',
    'respuesta':'respuesta1'
},{
    'pregunta':'pregunta2',
    'respuesta':'respuesta2'
}]

preguntas.extend(preguntas2)

for pregunta in preguntas:
    print('La pregunta {} tiene como respuesta {}'.format(pregunta['pregunta'], pregunta['respuesta']))