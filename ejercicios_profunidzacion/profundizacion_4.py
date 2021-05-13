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
Tome el ejercicio:
<condicionales_python / ejercicios_profundizacion /ejercicio_5.py>,
copielo a este ejercicio y modifíquelo para cumplir el
siguiente requerimiento

En este ejercicio se lo provee de una lista de temperatuas,
esa lista de temperatuas corresponde a los valores de temperaturas
tomados durante una temporada del año en Buenos Aires.
Ustede deberá analizar dicha lista para deducir
en que temporada del año se realizó el muestreo de temperatura.
La variable con la lista de temperaturas se llama "temp_dataloger"
definida al comienzo del archivo

Debe recorrer la lista "temp_dataloger" y obtener los siguientes
resultados

1 - Obtener la máxima temperatura
2 - Obtener la mínima temperatura
3 - Obtener el promedio de las temperatuas

Los resultados se deberán almacenar en las siguientes variables
que ya hemos preparado para usted.

NOTA: No se debe ordenar la lista de temperaturas, se debe obtener
el máximo y el mínimo utilizando los mismos métodos vistos
durante la clase (ejemplos_clase)
'''

print("Mi primer pasito en data analytics")
# Empezar aquí la resolución del ejercicio

temperatura_max = None      # Aquí debe ir almacenando la temp máxima
temperatura_min = None      # Aquí debe ir almacenando la temp mínima
temperatura_sumatoria = 0   # Aquí debe ir almacenando la suma de todas las temp
temperatura_promedio = 0    # Al finalizar el loop deberá aquí alamcenar el promedio
temperatura_len = 0         # Aquí debe almacenar cuantas temperatuas hay en la lista

# Colocar el bucle aqui......
temp_dataloger = [17, 18, 16, 17]

for temperatura in temp_dataloger:
    temperatura_sumatoria += temperatura
    temperatura_len += 1
    if (temperatura_max is None) or (temperatura_max < temperatura):
        temperatura_max = temperatura
    if (temperatura_min is None) or (temperatura_min > temperatura):
        temperatura_min = temperatura

print('La temperatura máxima es:', temperatura_max) 
print('La temperatura mínima es:', temperatura_min)

# Al finalizar el bucle compare si el valor que usted calculó para
# temperatura_max y temperatura_min coincide con el que podría calcular
# usando la función "max" y la función "min" de python
# función "max" --> https://www.w3schools.com/python/ref_func_max.asp
# función "min" --> https://www.w3schools.com/python/ref_func_min.asp

print("Máxima temperatura con función predefinida: ", max(temp_dataloger))
print("Mínima temperatura con función predefinida: ", min(temp_dataloger))

# Al finalizar el bucle debe calcular el promedio como:
# temperatura_promedio = temperatura_sumatoria / cantidad_temperaturas

temperatura_promedio = temperatura_sumatoria / temperatura_len
print('El promedio de las muestras de temperatura es:', temperatura_promedio)

# Corroboren los resultados de temperatura_sumatoria
# usando la función "sum"
# función "sum" --> https://www.w3schools.com/python/ref_func_sum.asp

print('Sumatoria de temperaturas con bucle:', temperatura_sumatoria)
print('Temperatura sumatoria calculada con función predefinida', sum(temp_dataloger))

'''
Una vez que tengamos nuestros valores correctamente calculados debemos
determinar en que epoca del año nos encontramos en Buenos Aires utilizando
la estadística de años anteriores. Basados en el siguiente link realizamos
las siguientes aproximaciones:

verano -->      min = 19, max = 28
otoño -->       min = 11, max = 20
invierno -->    min = 8, max = 14
primavera -->   min = 10, max = 24

Referencia:
https://es.weatherspark.com/y/28981/Clima-promedio-en-Buenos-Aires-Argentina-durante-todo-el-a%C3%B1o
'''

# En base a los rangos de temperatura de cada estación,
# ¿En qué época del año nos encontramos?
# Imprima el resultado en pantalla
# Debe utilizar temperatura_max y temperatura_min para definirlo

if (temperatura_max >= 20) and (temperatura_min >= 19):
    print('La época del año en que se tomaron las mediciones de temperatura es verano')
elif (10 <= temperatura_max <= 24) and ( 10 <= temperatura_min <= 24):
    print('La época del año en que se tomaron las mediciones de temperatura es primavera')
elif (11 <= temperatura_max <= 20) and ( 11 <= temperatura_min <= 20):
    print('La época del año en que se tomaron las mediciones de temperatura es otoño')
elif (temperatura_max <= 14) and (temperatura_min <= 11):
    print('La época del año en que se tomaron las mediciones de temperatura es invierno')
else:
    print('No se puede definir en que época del año fueron tomadas las temperaturas')
