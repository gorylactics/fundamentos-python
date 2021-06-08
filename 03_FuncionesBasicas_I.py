#1
def a():
    return 5
print(a())
#imprime 5

#2
def a():
    return 5
print(a()+a())
#imprime 10

#3
def a():
    return 5
    return 10
print(a())
#retorna 5

#4
def a():
    return 5
    print(10)
print(a())
#retorna 5

#5
def a():
    print(5)
x = a()
print(x)
#imprime 5

#6
def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3))
#retorna print(3) y print(5) pero no puede generar la suma porque no retorna ningun valor solo imprime

#7
def a(b,c):
    return str(b)+str(c)
print(a(2,5))
#retorna 25 ya que es un string y no suma

#8
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())
#retorna 100 por la impresion de b y 10 ya que b es mayor que 10 y solo se retorna una cosa en esta funcion

#9
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))
#imprime 7
#imprime 14
#imprime 21

#10
def a(b,c):
    return b+c
    return 10
print(a(3,5))
#retorna 8

#11
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)
#imprime 500
#imprime 500
#imprime 300
#imprime 500

#12
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)
#imprime 500
#imprime 500
#imprime 300
#no se retorna 300 ya que no hay variable para almacenar el valor
#imprime 500

#13
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)
#imprime 500
#imprime 500
#imprime 300
#retorna 300

#14
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()

#imprime 1
#imprime 3
#imprime 2

#15
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)
#imprime 1
#imprime 3
#retorna 5
#retorna 10