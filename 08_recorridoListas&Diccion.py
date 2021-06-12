listaSimple = [3,6,34,6,8,3,78,9]
for x in listaSimple: #Toma el valor y no el indice
    print(x) #Imprime los valores uno a uno de la lista
    print(listaSimple) #Imprime la lista completa la cantidad de veces del largo de la lista 

listaSimpleB = [3,6,34,6,8,3,78,9]
for x in range(len(listaSimpleB)): #Toma el indice del largo de la lista
    print(x) #Imprime el numero de indice
    print(listaSimpleB) #Imprime la lista completa la cantidad de veces del largo de la lista 

######################################################################################################################

listaBidimensional  = [[22,33,23],[45,232,667]]
for x in listaBidimensional:
    print(x) #Imprime un elemento por iteracion, cada lista es un elemento []
    print(listaBidimensional)  #Imprime la lista completa la cantidad de veces del len de la lista 
    listaBidimensional[0][0] = 'hola' #Modifica el contenido indicando el elemento y la posicion dentro de este
    
    if listaBidimensional[0][1] == 33:
        listaBidimensional[0][1] = 'chao' #Si o si debe ir indicado la lista interna y la posicion a modificar
print(listaBidimensional)

for y in range(len(listaBidimensional)):
    print(y)#muestra los indices
    print(listaBidimensional[y])#Muestra el contenido en el indice
    print(listaBidimensional[y][1]) #Muestra los elementos en la posicion indicada de cada uno de las listas internas
    listaBidimensional[-1][-1] = 'abc' #Asi se modifica el elemnto indicado por sus indices
print(listaBidimensional)
######################################################################################################################

listaMixtaNivel1 = [{'Nombre': 'adrian'}]
print(listaMixtaNivel1) #Muestra la lista con todo su contenido
print(listaMixtaNivel1[0]) #Muestra el diccionario en el indice seleccionado, no soporta string como parametro ej: ['apellido']

listaMixtaNivel1[0]['Nombre'] = 'rodrigo' #Accedo al indice de la key y modifico el value
print(listaMixtaNivel1)

for x in listaMixtaNivel1:
    if  x['Nombre'] == 'adrian': #Asi se modifica el value de una key por el value y no por el indice
        x['Nombre'] =  'rodrigo'
        x['segundoNombre'] = 'alberto'
print(x) #Asi se imprime el Diccionario
print(listaMixtaNivel1) #Asi se imprime la lista con su contenido

######################################################################################################################

listaMixtaNivel2 = [{'nombre': 'adrian' , 'apellido' : 'miranda'},{'nombre' : 'rodrigo' , 'apellido' : 'riquelme'}]

#modificar la segunda key segun el indice del diccionario
for x in range(len(listaMixtaNivel2)):
    if  listaMixtaNivel2[x]['apellido'] == 'riquelme':
        listaMixtaNivel2[x-1]['apellido'] = 'perez'
print(listaMixtaNivel2)

#modificar la segunda key del value encontrado segun comparativa en el diccionario
for x in listaMixtaNivel2:
    if  x['apellido'] == 'miranda':
        x['apellido'] = 'validivia'
        print(x)

######################################################################################################################

listaMixtaNivel3 = [{'nombre': 'adrian' , 'apellido' : 'miranda' , 'datos' : [{'rut' : 12345 , 'idUser' : 0.1}]},
                    {'nombre' : 'rodrigo' , 'apellido' : 'riquelme', 'datos' : [{'rut' : 456 , 'idUser' : 0.2}]}
                    ]
# listaMixtaNivel3[0]['datos'][0]['rut'] = 567890
# print(listaMixtaNivel3)
for dato in range(len(listaMixtaNivel3)):
    print(listaMixtaNivel3[dato])
print(listaMixtaNivel3)

for dato2 in listaMixtaNivel3:
    if dato2['datos'][0]['rut'] == 456:
        dato2['datos'][0]['rut'] = 'abc'
print(listaMixtaNivel3)