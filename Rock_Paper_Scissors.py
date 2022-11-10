import random

options = ('piedra', 'papel', 'tijera')
usuario_win = 0
computadora_win = 0

rounds = 1
while True:

    print("*" * 9)
    print(f"*ROUND {rounds}*")
    print("*" * 9)

    print("\ncomputadora win:", computadora_win)
    print("usuario win:", usuario_win)


    usuario = input("\npiedra, papel o tijera ").lower()
    computadora = random.choice(options)

    rounds +=1

    if not usuario in options:
        print("por favor escoge entre: piedra, papel o tijera, de lo contrario no podras jugar")
        continue

    print(f"el usuario escogio: {usuario}")
    print(f"la computadora escogio: {computadora}")

    if usuario == computadora:
        print(f"empate con {usuario}")
    elif (usuario == "piedra" and computadora == "tijera") or (usuario == "tijera" and computadora == "papel") or (usuario == "papel" and computadora == "piedra"):
        print(f"usuario gana con {usuario}")
        usuario_win +=1
    elif (usuario == "tijera" and computadora == "piedra") or (usuario == "papel" and computadora == "tijera") or (usuario == "piedra" and computadora == "papel"):
        print(f"computadora gana con {computadora}")
        computadora_win += 1

    if computadora_win == 2:
        print("el rotundo ganador es la Computadora")
        break
    elif usuario_win == 2:
        print("el rotundo ganador es el Usuario")
        break