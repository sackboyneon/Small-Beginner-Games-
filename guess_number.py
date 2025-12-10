import random

mayor = 10 
menor = 1


player = input("Quieres jugar a adivinar el numero? ")
seguir_jugando = "si"

while seguir_jugando== "si": 
    if player == "no":
        print("Adios!")
    player = input("Dame un numero: ")
    decisiones_compu = random.randint(menor, mayor)
    if decisiones_compu == player:
        print("Felicidades, adivinaste el numero!")
    elif decisiones_compu != player:
        print("Perdiste el numero real era ", decisiones_compu)

