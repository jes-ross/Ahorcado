'''
Jesús Rosales Santana
18-03-2023
Juego del ahorcado con python.
'''
import random #Con esta librería elegiremos una palabra aleatoria. 
import string #Con esta librería se recopilarán las letras. 


lista_palabras = ["Aguacate", "Coche", "Caballo", "Almeja", "Percutor", "Moto", "Fotosintesis"]
ahorcado = {#Dibujo del ahorcado. 
    6: """
        +---+
        |   |
            |
            |
            |
            |
    =========
    """,
    5: """
        +---+
        |   |
        O   |
            |
            |
            |
    =========
    """,
    4: """
        +---+
        |   |
        O   |
        |   |
            |
            |
    =========
    """,
    3: """
        +---+
        |   |
        O   |
       /|   |
            |
            |
    =========
    """,
    2: """
        +---+
        |   |
        O   |
       /|\  |
            |
            |
    =========
    """,
    1: """
        +---+
        |   |
        O   |
       /|\  |
       /    |
            |
    =========
    """,
    0: """
        +---+
        |   |
        O   |
       /|\  |
       / \  |
            |
    =========
    """
}


def obtenerPalabra(palabra):#Función para la obtención de la palabra. 
    palabra = random.choice(palabra)
    return palabra.upper()#Que nos devuelva el resultado en mayuscula. 




def juegoAhorcado():#Función principal del juego.
    print("=========================")
    print("Bienvenido al juego del ahorcado")
    print("=========================")
    palabra = obtenerPalabra(lista_palabras)#Se declara la variable de la palabra. 
    letras_por_adivinar = set(palabra)#Conjunto de letras por adivinar. 
    abc = set(string.ascii_uppercase)#Conjunto de letras del abecedario en mayuscula. 
    letras_adivinadas = set()#En este caso se deja vacio pues este debe ser rellenado posteriormente. 

    vidas = 6 #Número de vidas del usuario. 
    while len(letras_por_adivinar) > 0 and vidas > 0:#Ciclo del juego, hasta que termine o pierda el jugador. 
        print(f"Te quedan {vidas} vidas y has usado estas letras: {' '.join(letras_adivinadas)}")#Imprime el número de vidas y las letras usadas. 

        palabra_lista = [letra if letra in letras_adivinadas else '_' for letra in palabra]#Por cada letra de la palabra esta será suplantada por una barra baja. 
        print(ahorcado[vidas])#Se imprime el ahorcado por pantalla. 
        print(f"Palabras usadas:{' '.join(palabra_lista)}")

        respuesta_usuario = input("Dime una letra: ").upper()#Recoge la respuesta del usuario. 
        if respuesta_usuario in abc - letras_adivinadas:#Condicionales del juego. 
            letras_adivinadas.add(respuesta_usuario)#Añade las respuestas del usuario
            if respuesta_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(respuesta_usuario)#Quita letras de la lista por adivinar. 
                print(" ")
            else:
                vidas -= 1
                print(f"\nTu letra, {respuesta_usuario} no está en la palabra")
        elif respuesta_usuario in letras_adivinadas:
            print("Ya escogiste esa letra")
        else:
            print("Esa letra no es válida")
    if vidas == 0:#Si pierde diremos la respuesta con un mensaje. 
        print("Has perdido, la palabra era {}".format(palabra))
    else:
        print("Has ganado")





if __name__ == "__main__":#Función main.
    juegoAhorcado()