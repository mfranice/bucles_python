# Bucles [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Realice un programa que pida por consola dos números que representen
el principio y fin de una secuencia numérica.
Realizar un bucle "for" que recorra esa secuencia armada con "range"
y cuente cuantos números ingresados hay, y la sumatoria de todos los números
Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
sino que va hasta el anterior.
'''

print('Comenzamos a ponernos serios!')
# Empezar aquí la resolución del ejercicio

# inicio = ....
inicio_aux = int(input('Ingrese el primer número de la secuencia\n'))

# fin = ....
fin_aux = int(input('Ingrese el número final de la secuencia\n'))

if inicio_aux > fin_aux:
    inicio = fin_aux
    fin = inicio_aux
else:
    inicio = inicio_aux
    fin = fin_aux

# cantidad_numeros ....
cantidad_de_numeros = 0

# sumatoria ....
sumatoria = 0

# bucle.....
for i in range (inicio, fin + 1):
    cantidad_de_numeros += 1
    sumatoria += i

# Al terminar el bucle calcular el promedio como:
# promedio = sumatoria / cantidad_numeros
promedio = sumatoria / cantidad_de_numeros

# Imprimir resultado en pantalla

print('El resultado de la suma de todos los números que intervienen en la secuencia es:', sumatoria)
print('La cantidad total de número que intervienen e la secuencia es:', cantidad_de_numeros)
print('El promedio de los números que intervienen en la secuencia es:', promedio)