#1

# A  Cambia el valor 10 en x a 15. Una vez que haya terminado, x ahora debería ser [[5,2,3], [15,8,9]].
x = [ [5,2,3], [10,8,9] ]
def cambioValor(lista):
    for i in lista:
        lista[1][0] = 15
    return lista
llamado = cambioValor(x)
print(llamado)

# B Cambia el apellido del primer alumno de 'Jordan' a 'Bryant'
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
def alumno(students):
    for student in students:
        if student['last_name'] == 'Jordan':
            student['last_name'] = 'Bryant'
    return students
alumnado = alumno(students)
print(alumnado)


# C En el directorio sports_directory, cambia 'Messi' a 'Andres'

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

def deportes(deporte):
    deporte['soccer'][0] = 'andres'
    for sport in deporte:
        for variable in range(len(deporte[sport])):
            if deporte[sport][variable] == 'Messi':
                deporte[sport][variable] = 'Andres'
    return deporte

elDeporte = deportes(sports_directory)
print(elDeporte)


# D Camba el valor 20 en z a 30

z = [ {'x': 10, 'y': 20} ]
def cambio(dato):
    for r  in dato:
        if r['y'] == 20:
            r['y'] = 30
    return dato
cambiazo = cambio(z)
print(cambiazo)


# 2 Itera a través de una lista de diccionarios
# Crea una función iterateDictionary(some_list)que, dada una lista de diccionarios, la función recorra cada diccionario de la lista e imprime cada clave y el valor asociado. Por ejemplo, dada la siguiente lista:
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(students):
    estructura = []
    for student in students:
        #print(student['first_name'] , student['last_name'])
        firstName = student['first_name']
        lastName = student['last_name']
        estructura.append(f'first_name - {firstName} - last_name - {lastName}')
        print(f'first_name - {firstName} - last_name - {lastName}')
    return estructura

recorridoAlumnos = iterateDictionary(students)
print(recorridoAlumnos)

# 3
# Crea una función iterateDictionary2(key_name, some_list)que, dada una lista de diccionarios y un nombre de clave, la función imprima el valor almacenado en esa clave para cada diccionario. Por ejemplo, iterateDictionary2 ('first_name', students)

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(students):
    for student in students:
        print(student['first_name'])   
        print(student['last_name'])
print(iterateDictionary(students))

# 4 Crea una función printInfo(some_dict)que, dado un diccionario cuyos valores son todas listas, imprima el nombre de cada clave junto con el tamaño de su lista, y luego imprima los valores asociados dentro de la lista de cada clave. Por ejemplo:

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank' , 'santiago'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dojo):
    contador = 0
    contador2 = 0
    for x in range(len(dojo['locations'])):
        contador = contador+1
    locaciones = dojo['locations']
    ubicacion = f'La cantidad de locaciones son: {contador}, las cuales son las siguientes: \n{locaciones}'
    print(ubicacion)

    for y in dojo['instructors']:
        contador2 = contador2+1
    instructors = dojo['instructors']
    instructores = f'Los instructores son: {contador} y sus nombres son: \n{instructors}'
    print(instructores)

    return
    #return ubicacion ,instructores
    #al crear este retorno , genera una tupla
print(printInfo(dojo))