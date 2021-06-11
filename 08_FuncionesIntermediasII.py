# Cambia el valor 10 en x a 15. Una vez que haya terminado, x ahora debería ser [[5,2,3], [15,8,9]].
x = [ [5,2,3], [10,8,9] ]
for i in x:
    x[1][0] = 15
    print(i)
print(x)

# Cambia el apellido del primer alumno de 'Jordan' a 'Bryant'
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
for student in students:
    if student['last_name'] == 'Jordan':
        student['last_name'] = 'Bryant'
print(students)


# En el directorio sports_directory, cambia 'Messi' a 'Andres'
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0] = 'andres'
for sport in sports_directory:
    for variable in range(len(sports_directory[sport])):
        if sports_directory[sport][variable] == 'Messi':
            sports_directory[sport][variable] = 'Andres'
print(sports_directory)

    


# Camba el valor 20 en z a 30
z = [ {'x': 10, 'y': 20} ]
for r  in z:
    if r['y'] == 20:
        r['y'] = 30
print(z)


