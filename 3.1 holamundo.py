print("Hola mundo")
#Esto es texto
print("cierre")
"""
esto es un comentario
de varias lineas en simultaneo;
sirve para escribi mucho
y que quede prolija la cosa
"""
print(2+2)


#VARIABLES
x=5
nombre="Juan y el Lobo"
print(x,nombre)

#SECUECNIAS
lista=[1,2,3,4]     #es mutable
print(lista)

tupla=(1,2,3,4)     #es inmutable
print(tupla)

rango=range(0,13)   #secuencia inmutable DE NÚMEROS
print(rango)

#MAPEO (MAPPING TYPE): pares clave-valor
diccionario={
    "nombre": "Fede",
    "edad": 32
    }

#CONJUNTOS (SET TYPES): no ordenada y mutable de elementos únicos
conjunto={1,2,3,4}

#FROZEN SET: no ordenada e inmutable
conj_inmut=frozenset({1,2,3,4})

#DATOS BOOLENAO (verdadero o falso)
booleano=True
boolenao2=False

#NONE/NULL (nulo)
nulo=None

#Numéricas
x=1
y=3.14
z=4j
print(type(x))
print(type(y))
print(type(z))


#Ejercicios con variables de texto
txt="Seguimos trabajando con Strings"
print(txt[9:19])
print(txt[:8])
print(txt[23:])
print(txt[-7:]) #equivalente al anterior