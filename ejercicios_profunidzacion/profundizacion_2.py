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
Tome el ejercicio de clase:
<condicionales_python /  ejercicios_profundizacion / profundizacion_3.py>,
copielo a este ejercicio y modifíquelo, ahora se deberá ejecutar
indefinidamente hasta que como operador se ingrese la palabra "FIN",
en ese momento debe terminar el programa

Se debe debe imprimir un cartel de error si el operador ingresado no es
alguno de lo soportados o no es la palabra "FIN".
'''

print("Mi Calculadora (^_^)")
# Empezar aquí la resolución del ejercicio

while True:     #Bucle infinito

    temperatura_1 = 'No ingresada'
    temperatura_2 = 'No ingresada'
    temperatura_3 = 'No ingresada'
    terminar = False

    print('Si desea finalizar el programa ingrese la palabra FIN')

# -----------INGRESO DE LA PRIMERA TEMPERATURA----------------
#Se solicitan los ingresos por teclado, en todos los casos el ingreso puede ser un string o un float
#Se solicita el ingreso de un valor de temperatura hasta que se ingrese un dato válido
   
    while (temperatura_1 == 'No ingresada'):
    
        ingreso_teclado_1 = input('Ingrese la primera temperatura en grados centígrados:\n')
        
        if ingreso_teclado_1 == 'FIN':
            terminar = True
            break   
#Si el valor ingresado es FIN, se fuerza a terminar el bucle de ingreso de variable y el bucle infito del programa
#si el valor ingresado no es FIN, se prueba almacenarlo en otra variable como un float
        else:           
            try:
                temperatura_1 = float(ingreso_teclado_1)
#En caso de no poder almacenar el valor como un float indica que se ingresó un comando no admitido
            except:     
                print('Error, el ingreso por teclado no es válido, por favor ingrese una temperatura válida')
                temperatura_1 = 'No ingresada'

    if terminar == True:
        break

# -----------INGRESO DE LA SEGUNDA TEMPERATURA----------------
    
    while (temperatura_2 == 'No ingresada'):

        ingreso_teclado_2 = input('Ingrese la segunda temperatura en grados centígrados:\n')

        if ingreso_teclado_2 == 'FIN':
            terminar = True
            break
        else:
            try:
                temperatura_2 = float(ingreso_teclado_2)
            except:
                print('Error, el ingreso por teclado no es válido, por favor ingrese una temperatura válida') 
                temperatura_2 = 'No ingresada'

    if terminar == True:
        break

# -----------INGRESO DEL LA TERCERA TEMPERATURA----------------
    
    while (temperatura_3 == 'No ingresada'):

        ingreso_teclado_3 = input('Ingrese la tercera temperatura en grados centígrados:\n')

        if ingreso_teclado_3 == 'FIN':
            terminar = True
            break
        else:
            try:
                temperatura_3 = float(ingreso_teclado_3)
            except:
                print('Error, el ingreso por teclado no es válido, por favor ingrese una temperatura válida') 
                temperatura_3 = 'No ingresada'

    if terminar == True:
        break

#Búsqueda de temperatura máxima:
    if temperatura_1 > temperatura_2 and temperatura_1 > temperatura_3:
        print('La máxima temperatura ingresada es la temperatura 1:', temperatura_1)
    elif temperatura_2 > temperatura_1 and temperatura_2 > temperatura_3:
        print('La máxima temperatura ingresada es la temperatura 2:', temperatura_2)
    else:
        print('La máxima temperatura ingresada es la temperatura 3:', temperatura_3)

#Búsqueda de temperatura mínima:
    if temperatura_1 < temperatura_2 and temperatura_1 < temperatura_3:
        print('La mínima temperatura ingresada es la temperatura 1:', temperatura_1) 
    elif temperatura_2 < temperatura_1 and temperatura_2 < temperatura_3:
        print('La mínima temperatura ingresada es la temperatura 1:', temperatura_2)
    else:
        print('La mínima temperatura ingresada es la temperatura 1:', temperatura_3)

#Cálculo del promedio de temperatura:
    temp_promedio = (temperatura_1 + temperatura_2 + temperatura_3) / 3
    print('El promedio de las temperaturas ingresadas es:', temp_promedio)
