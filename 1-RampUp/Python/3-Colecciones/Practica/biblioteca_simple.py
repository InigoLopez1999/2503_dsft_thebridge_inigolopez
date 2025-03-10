import pprint # importamos la librería pprint para que visualizar mejor el conjunto de diccionarios
# en un fichero .py los import siempre al principio

# luego van las funciones

def imprimir (): # esta primera función sin argumentos simplemente imprime la lista completa de libros una vez se la llama
    pprint.pprint (libros)

def buscar (libros):
    libro_buscar = input ("Introduce el título del libro para que lo busque:") # se crea un input para que el usuario introduzca el título del libro que busca
    for libro in libros: # con este for se recorren todos los diccionarios dentro de la lista
        titulo = libro["Titulo"] # se declara la variable titulo que nos servirá para compararla con el input previo y se accede a la clave "Titulo" de cada diccionario
        if libro_buscar == titulo: #en caso de que el título introducido en el input coincida con alguno de los valores de la clave "Titulo"
            # se imprime el diccionario que incluya el mismo título que el introducido
            print("Libro encontrado. Aquí le proporciono la lista completa de los campos del libro que me ha solicitado:")
            print (libro)

def nuevo_libro (libros):
    nuevo_titulo = input ("Introduce el título del  nuevo libro:")
    nuevo_autor = input ("Introduce el autor del  nuevo libro:") # en el caso de querer introducir un nuevo libro se requieren dos inputs con título y autor a incluir
    for libro in libros: # se vuelven a recorrer todos los diccionarios 
        if nuevo_titulo != libro or nuevo_autor != libro: # se comprueba inicialmente que el título y autor introducidos no estén ya incluidos en algún diccionario
            libros.append({"Titulo":nuevo_titulo, # en caso de que el título o el autor no estén en algún diccionario se incluyen ambos inputs en la lista como un diccionario adicional
                           "Autor":nuevo_autor})
            print("Aquí le proporciono la lista completa de todos los libros en nuestro archivo, incluido el libro cuyo título y autor usted nos ha facilitado:")
            pprint.pprint(libros)
            break
           
def eliminar (libros):
    libro_a_eliminar = input ("Introduce el título del libro para que lo elimine:") # en primer lugar se pide al usuario que introduzca el título del libro que desee eliminar
    for libro in libros: # se vuelven a recorrer todos los diccionarios en la lista
        titulo = libro["Titulo"] # así como en la función buscar(libros) se define la variable titulo que corresponde al valor de cada clave "Titulo"
        if libro_a_eliminar == titulo:
            libros.remove(libro) # en caso de que el input y la variable titulo coincidan (que el programa "encuentre" el libro), elimina el diccionario entero que lo contenga
    print("Aquí le proporciono la lista completa de todos los libros en nuestro archivo, a excepción del que me ha solicitado eliminar:")
    pprint.pprint(libros)

def alquilar (libros):
    libro_alquilar = input("Introduce el título del libro que desea alquilar:") # se pide al usuario que indique el título del libro que desee alquilar
    for libro in libros: # se vuelven a recorrer los diccionarios como en las funciones anteriores
        titulo = libro["Titulo"] # se vuelve a definir la variable titulo
        if libro_alquilar == titulo: # en caso de que el input y titulo coincidan
            if libro["Alquilado"] == False: # este primer condicional cambia la condición del libro a True para indicar que ha sido alquilado en caso de que el valor relacionado a la clave "Alquilado" sea False
                libro["Alquilado"] = True
            elif libro["Alquilado"] == True: # si se da el caso que el usuario introduce el título de un libro que ya ha sido alquilado (la clave "Alquilado" ya posee el valor True)
                # el programa indica al usuario que el libro ya ha sido alquilado
                print("Este libro ya ha sido alquilado")
                break # en caso de que el usuario introduzca un título ya alquilado se sale del programa
            print("Aquí le proporciono la lista completa de todos los libros en nuestro archivo, indicando que usted ha alquilado el libro solicitado:")
            pprint.pprint(libros)

def devolver (libros): # esta función es idéntica a la anterior con la excepción que se cambia la condición de "Alquilado" a False para indicar que el libro ha sido devuelto
    libro_devolver = input("Introduce el título del libro que desea devolver:")
    for libro in libros:
        titulo = libro["Titulo"]
        if libro_devolver == titulo:
            if libro["Alquilado"] == True:
                libro["Alquilado"] = False
            elif libro["Alquilado"] == False:
                print("Este libro ya está en nuestros archivos, no es el libro que debe devolver")
                break # al igual que en la anterior función, si el usuario introduce un libro que ya ha sido devuelto, se sale del programa
            print("Aquí le proporciono la lista completa de todos los libros en nuestro archivo, indicando que usted ha devuelto el libro previamente alquilado:")
            pprint.pprint(libros)

# y una vez definidas las funciones se mete el resto del código

libros = [
    {"Titulo": "Python Data Science Handbook", "Autor": "Jake VanderPlas", "Alquilado": False},
    {"Titulo": "Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow", "Autor": "Aurélien Géron", "Alquilado": True},
    {"Titulo": "Pattern Recognition and Machine Learning", "Autor": "Christopher M. Bishop", "Alquilado": False},
    {"Titulo": "Deep Learning", "Autor": "Ian Goodfellow, Yoshua Bengio, Aaron Courville", "Alquilado": True},
    {"Titulo": "The Elements of Statistical Learning", "Autor": "Trevor Hastie, Robert Tibshirani, Jerome Friedman", "Alquilado": False},
    {"Titulo": "Data Science for Business", "Autor": "Foster Provost, Tom Fawcett", "Alquilado": False},
    {"Titulo": "Bayesian Data Analysis", "Autor": "Andrew Gelman et al.", "Alquilado": True},
    {"Titulo": "Introduction to the Theory of Computation", "Autor": "Michael Sipser", "Alquilado": False},
    {"Titulo": "Artificial Intelligence: A Modern Approach", "Autor": "Stuart Russell, Peter Norvig", "Alquilado": True},
    {"Titulo": "Computer Vision: Algorithms and Applications", "Autor": "Richard Szeliski", "Alquilado": False},
    {"Titulo": "Data Science from Scratch", "Autor": "Joel Grus", "Alquilado": True},
    {"Titulo": "The Art of Statistics", "Autor": "David Spiegelhalter", "Alquilado": False},
    {"Titulo": "Python Machine Learning", "Autor": "Sebastian Raschka, Vahid Mirjalili", "Alquilado": True},
    {"Titulo": "An Introduction to Statistical Learning", "Autor": "Gareth James, Daniela Witten, Trevor Hastie, Robert Tibshirani", "Alquilado": False},
    {"Titulo": "Fundamentals of Data Engineering", "Autor": "Joe Reis, Matt Housley", "Alquilado": False},
    {"Titulo": "Storytelling with Data", "Autor": "Cole Nussbaumer Knaflic", "Alquilado": True},
    {"Titulo": "Building Machine Learning Powered Applications", "Autor": "Emmanuel Ameisen", "Alquilado": False},
    {"Titulo": "Practical Statistics for Data Scientists", "Autor": "Peter Bruce, Andrew Bruce", "Alquilado": True},
    {"Titulo": "SQL for Data Scientists", "Autor": "Renee M. P. Teate", "Alquilado": False},
    {"Titulo": "Data Engineering on Azure", "Autor": "Vlad Riscutia", "Alquilado": True}
]

while True: # se introduce un while True para que se repita el bucle hasta que se pida salir del mismo
    accion = input ("Bienvenido a la biblioteca, qué desea hacer?").lower() # este primer input pide al usuario que indique la acción que desee realizar
    # se aplica lower() para asegurarnos que a pesar de que el usuario incluya mayúsculas se ejecute el siguiente "if"
    if accion in ["visualizar","alquilar","devolver","eliminar","añadir","buscar"]: # en caso de que el input esté entre los siguientes strings de la lista:
        if accion == "visualizar": # en función de lo que se desee realizar, el programa llama su respectiva función previamente definida
            print("Aquí le proporciono la lista completa de todos los libros en nuestro archivo:")
            imprimir()
        elif accion == "buscar":
            buscar(libros)
        elif accion == "eliminar":
            eliminar(libros)
        elif accion == "alquilar":
            alquilar(libros)
        elif accion == "devolver":
            devolver(libros)
        elif accion == "añadir":
            nuevo_libro(libros)
        break # se sale del bucle para indicar los resultados del programa
    else: # si el usuario introduce una entrada que no esté registrada en la lista de strings superior, vuelve al principio del while y pide al usuario que introduzca
        # la correpondiente acción hasta que se indique una entrada admitida
        print("Palabra errónea, vuelva a intentarlo")
        continue # vuelve al principio del while
        