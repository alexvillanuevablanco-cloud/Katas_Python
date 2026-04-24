"""
Proyecto de Katas en Python
Autor: Alejandro Villanueva
Descripcion: Resolucion de ejercicios usando funciones, programacion funcional y OOP
"""

#############################################
## Funcion para mostrar el titulo de cada kata.

def titulo_kata(numero_kata):
    print(f"\n========== KATA {numero_kata} ==========")

#############################################
## Importo la funcion reduce para usarla en las Katas que lo requieren.
from functools import reduce
import math

#############################################
## KATA 01: Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario 
# con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.

def frecuencia_letras(texto):
    frecuencias = {}
    for letra in texto.lower():
        if letra != ' ':
            if letra in frecuencias:
                frecuencias[letra] += 1
            else:
                frecuencias[letra] = 1
    return frecuencias

## Prueba de la función con una cadena de texto
titulo_kata(1)
resultado_kata1 = frecuencia_letras("Esta es mi primera kata en Python")
print("Frecuencia de letras:", resultado_kata1)

##############################################
## KATA 02: Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map().

def doblar_lista(numeros):
    return list(map(lambda x: x * 2, numeros))

# Multiplica por 2 cada elemento de la lista.
titulo_kata(2)
resultado_kata2 = doblar_lista([1, 2, 3, 4, 5])
print("Lista doblada:", resultado_kata2)

##############################################
## KATA 03: Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. 
# La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.

def buscar_palabras(lista_palabras, palabra_objetivo):
    resultado = []
    for palabra in lista_palabras:
        if palabra_objetivo.lower() in palabra.lower():
            resultado.append(palabra)
    return resultado

# Prueba de la función con una lista de palabras y una palabra objetivo
titulo_kata(3)
resultado_kata3 = buscar_palabras(["manzana", "banana", "naranja", "pera", "Manzana Verde"], "manzana")
print("Palabras que contienen 'manzana':", resultado_kata3)

##############################################
## KATA 04: Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map().

def diferencia_listas(lista1, lista2):
    return list(map(lambda x, y: x - y, lista1, lista2))

# Esta solucion resta por posicion: primer elemento de lista1 con primer elemento de lista2, segundo elemento de lista1 con segundo elemento de lista2, etc.
titulo_kata(4)
resultado_kata4 = diferencia_listas([1, 2, 3, 4, 5], [2, 4, 6, 8, 10])
print("Diferencia entre listas:", resultado_kata4)

##############################################
## KATA 05: Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por
## defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual
## que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver
## una tupla que contenga la media y el estado.

def calcular_nota(lista_notas, nota_aprobado=5):
    media = sum(lista_notas) / len(lista_notas)
    if media >= nota_aprobado:
        estado = "Aprobado"
    else:
        estado = "Suspenso"
    return (media, estado)

# Prueba de la función con una lista de números y un valor opcional
titulo_kata(5)
resultado1_kata5 = calcular_nota([6, 7, 8, 9, 10])
resultado2_kata5 = calcular_nota([3, 4, 5, 6, 1])
print("Media y estado Alumno 1:", resultado1_kata5)
print("Media y estado Alumno 2:", resultado2_kata5)

###############################################
## KATA 06: Escribe una función que calcule el factorial de un número de manera recursiva. - CORREGIDO -

# Corregido para manajar el caso de números negativos, que no tienen factorial definido, y para manejar el caso de 0 y 1, cuyo factorial es 1.
def factorial(n):
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos.")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
# Prueba de la función con diferentes números
titulo_kata(6)

try:
    resultado1_kata6_5 = factorial(5)
    print("Factorial de 5:", resultado1_kata6_5)

    resultado2_kata6_5 = factorial(-1)
    print("Factorial de -1:", resultado2_kata6_5)

except ValueError as e:
    print("Error:", e)

###############################################
## KATA 07: Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map().

def tuplas_a_strings(lista_tuplas):
    return list(map(lambda tupla: ' '.join(map(str, tupla)), lista_tuplas))

# Prueba de la función con una lista de tuplas
titulo_kata(7)
resultado_kata7 = tuplas_a_strings([(1, 'manzana'), (2, 'banana'), (3, 'naranja')])
print("Lista de strings:", resultado_kata7)

###############################################
## KATA 08: Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico
## o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje
## indicando si la división fue exitosa o no.

def dividir_numeros():
    try:
        num1 = float(input("Ingrese el dividendo: "))
        num2 = float(input("Ingrese el divisor: "))
        resultado = num1 / num2
        print(f"La división de {num1} entre {num2} es: {resultado}")
    except ValueError:
        print("Error: Por favor, ingrese un valor numérico válido.")
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
    finally:
        print("Operación de división finalizada.")

# Llamada a la función para probarla
titulo_kata(8)
dividir_numeros() 

################################################
## KATA 08 - SEGUNDA FORMA CON DOS FUNCIONES: UNA PARA DIVIDIR Y OTRA PARA EJECUTAR LA DIVISION Y MANEJAR LAS EXCEPCIONES. - CORREGIDO -

def dividir(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError("Error: No se puede dividir por cero.")
    return num1 / num2

def ejecutar_division():
    try:
        num1 = float(input("Ingrese el dividendo: "))
        num2 = float(input("Ingrese el divisor: "))
        resultado = dividir(num1, num2)
        print(f"La división de {num1} entre {num2} es: {resultado}")
    except ValueError:
        print("Error: Por favor, ingrese un valor numérico válido.")
    except ZeroDivisionError as e:
        print(e)
    finally:
        print("Operación de división finalizada.")

# Llamada a la función para probarla
titulo_kata(8)
ejecutar_division()


################################################
## KATA 09: Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista
## excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es 
## ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]. Usa la función filter(). - CORREGIDO -

# Corregido para manejar el caso de mayúsculas y minúsculas, y para asegurar que la comparación se haga de manera insensible a las mayúsculas.
# Version nueva para no recalcular la lista en cada iteracion.

titulo_kata(9)
def filtrar_mascotas(lista_mascotas):
    mascotas_prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    prohibidas = set(mascota.lower() for mascota in mascotas_prohibidas)

    return list(filter(lambda mascota: mascota.lower() not in prohibidas, lista_mascotas))

# Prueba de la función con una lista de nombres de mascotas
resultado_kata9 = filtrar_mascotas(["Perro", "Gato", "Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso", "Conejo"])
print("Mascotas permitidas:", resultado_kata9)

################################################
## KATA 10: Escribe una función que reciba una lista de números y calcule su promedio. 
# Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.

class ListaVaciaError(Exception):
    pass

def calcular_promedio(lista_numeros):
    if len(lista_numeros) == 0:
        raise ListaVaciaError("Error: La lista de números está vacía. No se puede calcular el promedio.")
    return sum(lista_numeros) / len(lista_numeros)

def ejecutar_promedio(lista_numeros):
    try:
        promedio = calcular_promedio(lista_numeros)
        print(f"El promedio de la lista es: {promedio}")
    except ListaVaciaError as error:
        print(error)

titulo_kata(10)
# Prueba de la función con una lista de números y una lista vacía
ejecutar_promedio([10, 20, 30, 40, 50])

## Prueba de la función con una lista vacía
ejecutar_promedio([])

#################################################
## KATA 11: Escribe un programa que pida al usuario que introduzca su edad. 
# Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), 
# maneja las excepciones adecuadamente.

def pedir_edad():
    try:
        edad = int(input("Por favor, ingrese su edad: "))
        if edad < 0 or edad > 120:
            raise ValueError("Error: La edad debe estar entre 0 y 120.")
        print(f"Su edad es: {edad}")
    except ValueError as error:
        print(error)

# Llamada a la función para probarla
titulo_kata(11)
pedir_edad()

###############################################
## KATA 12: Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map().

def longitud_palabras(frase):
    return list(map(len, frase.split()))

# Prueba de la función con una frase
titulo_kata(12)
print(f"Longitudes de cada palabra: {longitud_palabras('Hola Profe, esta es mi kata 12 en Python')}")

###############################################
## KATA 13: Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en
## mayúsculas y minúsculas. Las letras no pueden estar repetidas. Usa la función map().

def letras_mayus_minus(caracteres):
    letras_unicas = set(caracteres)
    return list(map(lambda letra: (letra.upper(), letra.lower()), letras_unicas))

# Prueba de la función con un conjunto de caracteres
titulo_kata(13)
print(f"Lista de tuplas con letras en mayúsculas y minúsculas: {letras_mayus_minus('Voy a aprobar este proyeto de Python')}")

###############################################
## KATA 14: Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. 
# Usa la función filter()

def palabras_con_letra(lista_palabras, letra):
    return list(filter(lambda palabra: palabra.lower().startswith(letra.lower()), lista_palabras))

# Prueba de la función con una lista de palabras y una letra específica
titulo_kata(14)
print(f"Palabras que comienzan con 'p': {palabras_con_letra(['Perro', 'Gato', 'Pájaro', 'Pez', 'Conejo'], 'p')}")

################################################
## KATA 15: Crea una función lambda que sume 3 a cada número de una lista dada.

suma_tres = lambda lista: list(map(lambda x: x + 3, lista))

# Prueba de la función lambda con una lista de números
titulo_kata(15) 
print(f"Lista con 3 sumado a cada número: {suma_tres([1, 2, 3, 4, 5])}")

###############################################
## KATA 16: Escribe una función que tome una cadena de texto y un número entero n como parámetros y 
# devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter().

def palabras_mas_largas(frase, n):
    palabras = frase.split()
    return list(filter(lambda palabra: len(palabra) > n, palabras))

# Prueba de la función con una cadena de texto y un número entero
titulo_kata(16)
print(f"Palabras más largas que 5 caracteres: {palabras_mas_largas('Esta es una frase de prueba para la kata 16 en Python', 5)}")

################################################
## KATA 17: Crea una función que tome una lista de dígitos y devuelva el número correspondiente. 
# Por ejemplo, [5,7,2] corresponde al número quinientos setenta y dos (572). Usa la función reduce(). - CORREGIDO -

# Profesor/a, el enunciado de la KATA 17 pedía usar la funcion reduce() y no un join.

def digitos_a_numero(lista_digitos):
    # La función reduce toma una función y una secuencia, y aplica la función acumulativamente a los elementos de la secuencia, reduciéndola a un solo valor. 
    # En este caso, la función lambda toma el acumulador (el número construido hasta ahora) y el dígito actual, y los combina para formar el nuevo número.
    return reduce(lambda acumulador, digito: acumulador * 10 + digito, lista_digitos)

# OPCION MAS SENCILLA CON JOIN
# def digitos_a_numero_join(lista_digitos):
    return int(''.join(map(str, lista_digitos)))

# Prueba de la función con una lista de dígitos
titulo_kata(17) 
print(f"Número generado: {digitos_a_numero([5, 7, 2])}")


################################################
## KATA 18: Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes
## (nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación 
## mayor o igual a 90. Usa la función filter().

def estudiantes_aprobados(estudiantes):
    return list(filter(lambda estudiante: estudiante['calificación'] >= 90, estudiantes))

# Prueba de la función con una lista de diccionarios de estudiantes
titulo_kata(18)
estudiantes = [
    {'nombre': 'Alejandro', 'edad': 20, 'calificación': 95},
    {'nombre': 'Manuel', 'edad': 22, 'calificación': 85},
    {'nombre': 'Nerea', 'edad': 21, 'calificación': 92}
]
print(f"Estudiantes aprobados: {estudiantes_aprobados(estudiantes)}")

################################################
## KATA 19: Crea una función lambda que filtre los números impares de una lista dada.

numeros_impares = lambda lista: list(filter(lambda x: x % 2 != 0, lista))

# Prueba de la función lambda con una lista de números
titulo_kata(19)
print(f"Números impares: {numeros_impares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])}")

################################################
## KATA 20: Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función filter(). - CORREGIDO -
# Corregido para excluir los valores booleanos, que en Python son considerados subclases de int, pero no deberían ser incluidos como enteros en este caso.

def filtrar_enteros(lista):
    return list(filter(lambda elemento: isinstance(elemento, int) and not isinstance(elemento, bool), lista))

# Prueba de la función con una lista de elementos mixtos
titulo_kata(20)
print(f"Lista filtrada con solo enteros: {filtrar_enteros([1, 'hola', 3, 'python', 7, 2.5, True])}")

################################################
## KATA 21: Crea una función que calcule el cubo de un número dado mediante una función lambda.

cubo = lambda x: x ** 3

# Prueba de la función lambda con un número
titulo_kata(21)
print(f"El cubo de 5 es: {cubo(5)}")

################################################
## KATA 22. Dada una lista numérica, obtén el producto total de los valores de dicha lista. Usa la función reduce(). - CORREGIDO -
# Elimino el import de reduce para evitar redundancia.

def producto_total(lista_numeros):
    return reduce(lambda acc, x: acc * x, lista_numeros)

# Prueba de la función con una lista de números
titulo_kata(22)
print(f"Producto total de la lista: {producto_total([1, 2, 3, 4, 5])}")

################################################
## KATA 23. Concatena una lista de palabras. Usa la función reduce().- CORREGIDO -
# Volvemos a lo mismo. El enunciado pide usar la funcion reduce() y no un join.

def concatenar_palabras(lista_palabras):
    return reduce(lambda acc, palabra: acc + ' ' + palabra, lista_palabras)

# OPCION MAS SENCILLA CON JOIN

# def concatenar_palabras_join(lista_palabras):
    return ' '.join(lista_palabras)

# Prueba de la función con una lista de palabras
titulo_kata(23)
print(f"Palabras concatenadas: {concatenar_palabras(['Estoy', 'aprendiendo', 'Python', 'con', 'Katas'])}")

################################################
## KATA 24. Calcula la diferencia total en los valores de una lista. Usa la función reduce(). - CORREGIDO -
# Una vez mas, el enunciado pide usar la funcion reduce().


# La operación realiza la resta acumulada de izquierda a derecha:
# [10, 5, 3, 2] -> ((10 - 5) - 3) - 2
def diferencia_total(lista_numeros):
    return reduce(lambda acc, x: acc - x, lista_numeros)

# Prueba de la función con una lista de números
titulo_kata(24)
print(f"Diferencia total de la lista: {diferencia_total([10, 5, 3, 2])}")   

#################################################
## KATA 25. Crea una función que cuente el número de caracteres en una cadena de texto dada.

def contar_caracteres(cadena):
    return len(cadena)  

# Prueba de la función con una cadena de texto
titulo_kata(25)
print(f"Número de caracteres en la cadena: {contar_caracteres('Hola, esta es una cadena de texto para contar caracteres.')}")

#################################################
## KATA 26. Crea una función lambda que calcule el resto de la división entre dos números dados.

resto_division = lambda x, y: x % y

# Prueba de la función lambda con dos números
titulo_kata(26)
print(f"Resto de la división entre 10 y 3: {resto_division(10, 3)}")

#################################################
## KATA 27. Crea una función que calcule el promedio de una lista de números. - CORREGIDO -
# Corregido para manejar el caso de una lista vacía, que no tiene un promedio definido, y para lanzar una excepción personalizada en ese caso.

def calcular_promedio2(lista_numeros):
    if len(lista_numeros) == 0:
        raise ValueError("La lista está vacía. No se puede calcular el promedio.")
    return sum(lista_numeros) / len(lista_numeros)

# Prueba de la función con una lista de números
titulo_kata(27) 

try:
    print(f"Promedio de la lista: {calcular_promedio2([10, 20, 30, 40, 50])}")
    print(f"Promedio de la lista vacía: {calcular_promedio2([])}")
except ValueError as error:
    print(error)

#################################################
## KATA 28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

def primer_duplicado(lista):
    vistos = set()

    for elemento in lista:
        if elemento in vistos:
            return elemento
        vistos.add(elemento)
    return None  # Devuelve None si no hay duplicados

# Prueba de la función con una lista de elementos
titulo_kata(28)
print(f"Primer elemento duplicado: {primer_duplicado([1, 2, 3, 4, 5, 2, 6])}")

##################################################
## KATA 29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el
## carácter '#', excepto los últimos cuatro.

def enmascarar_variable(variable):
    variable_str = str(variable)
    if len(variable_str) <= 4:
        return variable_str
    return '#' * (len(variable_str) - 4) + variable_str[-4:]

# Prueba de la función con diferentes variables
titulo_kata(29)
print(f"Variable enmascarada: {enmascarar_variable(1234567890)}")
print(f"Variable enmascarada: {enmascarar_variable('HolaProfesor')}")

##################################################
## KATA 30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras
## pero en diferente orden.

def son_anagramas(palabra1, palabra2):
    return sorted(palabra1.replace(" ", "").lower()) == sorted(palabra2.replace(" ", "").lower())

# Prueba de la función con diferentes pares de palabras
titulo_kata(30)
print(f"¿'roma' y 'amor' son anagramas? {son_anagramas('roma', 'amor')}")
print(f"¿'hola' y 'profe' son anagramas? {son_anagramas('hola', 'profe')}")

###################################################
## KATA 31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en
## esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se
## lanza una excepción.

def buscar_nombre():

    try:
        nombres = input("Ingrese una lista de nombres separados por comas: ").split(',')
        nombres = [nombre.strip() for nombre in nombres]  # Eliminar espacios en blanco alrededor de los nombres.

        nombre_buscar = input("Ingrese el nombre que desea buscar: ").strip()  # Eliminar espacios en blanco alrededor del nombre a buscar.

        if nombre_buscar in nombres:
            print(f"El nombre '{nombre_buscar}' fue encontrado en la lista.")
        else:
            raise ValueError(f"El nombre '{nombre_buscar}' no fue encontrado en la lista.")
    except ValueError as error:
        print(error)

# Llamada a la función para probarla
titulo_kata(31)
buscar_nombre()

###################################################
## KATA 32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y
## devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona
## no trabaja aquí.


def buscar_empleado(nombre_completo, lista_empleados):
    for empleado in lista_empleados:
        if empleado["nombre"].lower() == nombre_completo.lower():
            return empleado["puesto"]
    return "La persona no trabaja aquí."

# Prueba de la función con un nombre completo y una lista de empleados
titulo_kata(32)
empleados = [
    {"nombre": "Alejandro Villanueva", "puesto": "Data Analyst"},
    {"nombre": "Manuel García", "puesto": "Software Engineer"},
    {"nombre": "Nerea López", "puesto": "Project Manager"}
]   
print(f"El puesto de 'Alejandro Villanueva' es: {buscar_empleado('Alejandro Villanueva', empleados)}")
print(f"El puesto de 'Juan Pérez' es: {buscar_empleado('Juan Pérez', empleados)}")
print(f"El puesto de 'Nerea López' es: {buscar_empleado('Nerea López', empleados)}")

####################################################
## KATA 33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.

sumar_listas = lambda lista1, lista2: list(map(lambda x, y: x + y, lista1, lista2))

# Prueba de la función lambda con dos listas de números
titulo_kata(33) 
print(f"Suma de elementos correspondientes: {sumar_listas([1, 2, 3], [4, 5, 6])}")

####################################################
## KATA 34. Crea la clase Arbol, define un árbol genérico con un tronco y ramas como atributos. 
# Los métodos disponibles son: crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol.
# El objetivo es implementar estos métodos para manipular la estructura del árbol. - CORREGIDO -

# Corregido para llamar a los metodos de forma correcta.

class Arbol:
    def __init__(self):
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        self.tronco += 1

    def nueva_rama(self):
        self.ramas.append(1)

    def crecer_ramas(self):
        self.ramas = list(map(lambda x: x + 1, self.ramas))

    def quitar_rama(self, posicion):
        if 0 <= posicion < len(self.ramas):
            self.ramas.pop(posicion)
        else:
            print("Posición de rama no válida.")

    def info_arbol(self):
        return {
            "Tronco": self.tronco,
            "Ramas": self.ramas,
            "Longitud_ramas": len(self.ramas)
        }
    
# Prueba de la clase Arbol y sus métodos
titulo_kata(34)
mi_arbol = Arbol()
mi_arbol.crecer_tronco()
mi_arbol.nueva_rama()
mi_arbol.crecer_ramas()
mi_arbol.nueva_rama()
mi_arbol.nueva_rama()
mi_arbol.quitar_rama(1)
print(f"Información del árbol: {mi_arbol.info_arbol()}")

#####################################################
## KATA 35. No se ha dado informacion para esta KATA, por lo que se omite.
titulo_kata(35)
print("No se ha dado información para esta KATA, por lo que se omite.")

######################################################
## KATA 36. Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente. 
# Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y agregar dinero al saldo. - CORREGIDO -

# Corregido para validar que la cantidad sea positiva y reutilizando metodos para evitar duplicación de código.

class UsuarioBanco:
    def __init__(self, nombre, saldo=0, cuenta_corriente=False):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad):
        if cantidad <= 0:
            raise ValueError(f"[{self.nombre}] La cantidad a retirar debe ser positiva.")
        
        if cantidad > self.saldo:
            raise ValueError(f"[{self.nombre}] Fondos insuficientes para retirar {cantidad}.")
        else:
            self.saldo -= cantidad
            print(f"[{self.nombre}] Has retirado {cantidad}. Saldo actual: {self.saldo}")
    
    def agregar_dinero(self, cantidad):
        if cantidad <= 0:
            raise ValueError(f"[{self.nombre}] La cantidad a agregar debe ser positiva.")
        else:
            self.saldo += cantidad
            print(f"[{self.nombre}] Has agregado {cantidad}. Saldo actual: {self.saldo}")

    def transferir_dinero(self, destinatario, cantidad):
        if cantidad <= 0:
            raise ValueError(f"[{self.nombre}] La cantidad a transferir debe ser positiva.")
        
        if cantidad > self.saldo:
            raise ValueError(f"[{self.nombre}] Fondos insuficientes para transferir {cantidad} a {destinatario.nombre}.")
        else:
            self.retirar_dinero(cantidad)
            destinatario.agregar_dinero(cantidad)
            print(f"[{self.nombre}] Has transferido {cantidad} a {destinatario.nombre}. Saldo actual: {self.saldo}")

# Prueba de la clase UsuarioBanco y sus métodos
titulo_kata(36)

#Print saldo inicial de cada usuario.
usuario1 = UsuarioBanco("Alicia", 100, True)
usuario2 = UsuarioBanco("Bob", 50, True)
print(f"Saldo inicial de {usuario1.nombre}: {usuario1.saldo}")
print(f"Saldo inicial de {usuario2.nombre}: {usuario2.saldo}")

# Realiza operaciones de retiro, transferencia y agregar dinero.
usuario2.agregar_dinero(20)
try:
    usuario2.transferir_dinero(usuario1, 80)
except ValueError as e:
    print(e)
usuario1.retirar_dinero(50)
print(f"Saldo de {usuario1.nombre}: {usuario1.saldo}")
print(f"Saldo de {usuario2.nombre}: {usuario2.saldo}")

#########################################################
## KATA 37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: 
# contar_palabras, reemplazar_palabras, eliminar_palabra. 
# Estas opciones son otras funciones que tenemos que definir primero y llamar dentro de la función procesar_texto.

def contar_palabras(texto):
    palabras = texto.split()
    resultado = {}

    for palabra in palabras:
        palabra = palabra.lower()
        resultado[palabra] = resultado.get(palabra, 0) + 1
    return resultado

def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    return texto.replace(palabra_original, palabra_nueva)

def eliminar_palabra(texto, palabra_a_eliminar):
    palabras = texto.split()
    palabras = list(filter(lambda palabra: palabra.lower() != palabra_a_eliminar.lower(), palabras))        
    return " ".join(palabras)

def procesar_texto(texto, opcion, *args):
    if opcion == "contar_palabras":
        return contar_palabras(texto)
    elif opcion == "reemplazar_palabras":
        if len(args) != 2:
            return "Error: Se requieren dos argumentos para reemplazar palabras."
        return reemplazar_palabras(texto, args[0], args[1])
    elif opcion == "eliminar_palabra":
        if len(args) != 1:
            return "Error: Se requiere un argumento para eliminar una palabra."
        return eliminar_palabra(texto, args[0])
    else:
        return "Opción no válida."
    
# Prueba de la función procesar_texto con diferentes opciones
titulo_kata(37) 
texto_prueba = "Hola , esta es una prueba de la función procesar_texto. Hola a todos."
print(f"Contar palabras: {procesar_texto(texto_prueba, 'contar_palabras')}")
print(f"Reemplazar palabras: {procesar_texto(texto_prueba, 'reemplazar_palabras', 'Hola', 'Adiós')}")
print(f"Eliminar palabra: {procesar_texto(texto_prueba, 'eliminar_palabra', 'prueba')}")

##########################################################
## KATA 38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.

def momento_del_dia(hora):
    if 6 <= hora < 12:
        return "Es de día."
    elif 12 <= hora < 20:
        return "Es por la tarde."
    else:
        return "Es de noche."
    
# Prueba de la función con una hora proporcionada por el usuario.
titulo_kata(38)
hora_usuario = int(input("Ingrese la hora (0-23): "))
print(momento_del_dia(hora_usuario))

###########################################################
## KATA 39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica.
# Las reglas de calificación son:
# 0 - 69 insuficiente
# 70 - 79 bien
# 80 - 89 muy bien
# 90 - 100 excelente

def calificacion_texto(calificacion):
    if 0 <= calificacion < 70:
        return "Insuficiente"
    elif 70 <= calificacion < 80:
        return "Bien"
    elif 80 <= calificacion < 90:
        return "Muy bien"
    elif 90 <= calificacion <= 100:
        return "Excelente"
    else:
        return "Calificación no válida."
    
# Prueba de la función con diferentes calificaciones numéricas
titulo_kata(39)
calificaciones = [65, 75, 85, 95, 105]
for calificacion in calificaciones:
    print(f"Calificación {calificacion}: {calificacion_texto(calificacion)}")

###########################################################
## KATA 40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo" , "circulo" o "triangulo") 
# y datos (una tupla con los datos necesarios para calcular el área de la figura). - CORREGIDO -

# Corregido para usar excepciones en vez de strings para manejar los errores.

def calcular_area(figura, datos):
    if figura == "rectangulo":
        if len(datos) != 2:
            raise ValueError("Error: Se requieren dos datos (base y altura) para calcular el área del rectángulo.")
        base, altura = datos
        return base * altura
    elif figura == "circulo":
        if len(datos) != 1:
            raise ValueError("Error: Se requiere un dato (radio) para calcular el área del círculo.")
        radio = datos[0]
        return math.pi * radio ** 2
    elif figura == "triangulo":
        if len(datos) != 2:
            raise ValueError("Error: Se requieren dos datos (base y altura) para calcular el área del triángulo.")
        base, altura = datos
        return (base * altura) / 2
    else:
        raise ValueError("Error: Figura no válida.")
    
# Prueba de la función con diferentes figuras y datos
titulo_kata(40)

try:
    print(f"Área del rectángulo (base = 5, altura = 3): {calcular_area('rectangulo', (5, 3))}")
    print(f"Área del círculo (radio = 4): {calcular_area('circulo', (4,))}")
    print(f"Área del triángulo (base = 6, altura = 4): {calcular_area('triangulo', (6, 4))}")
    print(f"Área del rombo (diagonal mayor = 5, diagonal menor = 3): {calcular_area('rombo', (5, 3))}")
except ValueError as e:
    print(e)

###########################################################
## KATA 41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el
# monto final de una compra en una tienda en línea, después de aplicar un descuento. - CORREGIDO -

# Nueva version corregida para manejar casos de precios negativos, descuentos negativos y descuentos mayores que el precio, que no son válidos.

def calcular_precio(precio, descuento = 0):
    if precio < 0:
        raise ValueError("El precio no puede ser negativo.")
    
    if descuento < 0:
        raise ValueError("El descuento no puede ser negativo.")
    
    if descuento > precio:
        raise ValueError("El descuento no puede ser mayor que el precio.")
    
    return precio - descuento

def calcular_precio_final():
    try:
        precio = float(input("Ingrese el precio del producto: "))
        tiene_descuento = input("¿Tiene descuento? (si/no): ").strip().lower()

        if tiene_descuento == "si":
            descuento = float(input("Ingrese el valor del descuento: "))
        else:
            descuento = 0

        precio_final = calcular_precio(precio, descuento)
        print(f"El precio final de compra es: {precio_final}")

    except ValueError as e:
        print(f"Error: {e}")