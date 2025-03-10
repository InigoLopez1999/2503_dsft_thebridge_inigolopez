import math
#Ejercicio 1
def dia_semana(numero):
    dicc_dias = {"1":"Lunes","2":"Martes","3":"Miércoles","4":"Jueves","5":"Viernes","6":"Sábado","7":"Domingo"}
    if numero in dicc_dias.keys():
        print(f"El número {numero} corresponde al {dicc_dias[numero]}")
#Ejercicio 2
def piramide_invertida(longitud_lista):
    lista_nueva =[]
    while longitud_lista > 0:
        lista_nueva.append(longitud_lista)
        longitud_lista = longitud_lista - 1
    while lista_nueva != []:
        for num in lista_nueva:
            print (num, end=" ")
        print()
        del(lista_nueva[0])
#Ejercicio 3
def comparador (num_1,num_2):
    if num_1 > num_2:
        print(f"{num_1} es mayor que {num_2}")
    elif num_1 == num_2:
        print(f"{num_1} y {num_2} son idénticos")
    elif num_2 > num_1:
        print(f"{num_2} es mayor que {num_1}")
#Ejercicio 4
def cuenta_letras (texto,letra):
    num_letras = 0
    for i in texto:
        if letra == i:
            num_letras = num_letras + 1
    print(f"La letra {letra} está {num_letras} vez / veces en su palabra")
#Ejercicio 5
def dicc_letras (palabra):
    num_letras = 0
    dicc = {}
    for letra in palabra:
        num_letras = num_letras + 1
    dicc[palabra] = num_letras
    return dicc
#Ejercicio 6
def lista_modificable (*args, accion = "add",elemento = None):
    lista_nueva = [*args]
    if accion == "add":
        lista_nueva.append(elemento)
        return lista_nueva
    elif accion == "remove":
        if elemento not in lista_nueva:
            print("Error! Ese elemento no está en la lista. No puedo eliminarlo")
        elif elemento in lista_nueva:
            for num in lista_nueva:
                while elemento in lista_nueva:
                    lista_nueva.remove(elemento)
            return lista_nueva
#Ejercicio 7
def union_palabras(*args):
    return " ".join(args)

union_palabras("En","un","lugar","de","la","Mancha")
#Ejercicio 8
def fibonacci (numero):
    lista_fibo = [1,1]
    for num in lista_fibo:
        while lista_fibo[-1] < 10000000:
            lista_fibo.append(lista_fibo[-1] + lista_fibo[-2])
    fibo_final = lista_fibo[numero-2] + lista_fibo[numero-3]
    return fibo_final
#Ejercicio 9
def area_cuadrado(lado):
    area = lado * lado
    return area

def area_triángulo(base,altura):
    area = (base * altura)/2
    return area

def area_circulo(radio):
    area = math.pi * (radio**2)
    return area

primer_calculo = (2*area_circulo(10))+ area_triángulo(3,7)

print(f"El resultado del primer cálculo de áreas es {primer_calculo.__round__(1)} cm cuadrados")

segundo_calculo = area_cuadrado(10) + (2*area_circulo(6)) + area_circulo(4) + (5*area_triángulo(2,4))

print(f"El resultado del segundo cálculo de áreas es {segundo_calculo.__round__(1)} cm cuadrados")