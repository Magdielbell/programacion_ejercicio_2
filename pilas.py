#variables para los ciclos while
repetición = '1'
salir = 'n'

while repetición == '1':

    # se importó randint y deque

    from _collections import deque
    from random import randint
    historial = deque()
#las opciones a elegir
    opciones = ['piedra', 'papel', 'tijeras']

    respuesta_PC = randint(0,2)
#la opcion random para la PC
    IA = opciones[respuesta_PC]


    print('1) Piedra: ')
    print('2) Papel: ')
    print('3) Tijera: ')
#el usuario elige que opcion poner

    Humano = input('\nElige tu respuesta: ')
#comienzo de decisiones para el juego
    if Humano == IA:
        print('Empate! ')

    if Humano == 'tijeras':

        if IA == 'papel':
            print("RESULTADO: " "Gana Humano!")

    if Humano == 'piedra':
         print("HUMANO: ", Humano)
         print("RESULTADO: " "Gana Humano!")

    if Humano == 'papel':
        print("Humano: ", Humano)
        print("RESULTADO: Gana Humano!")

        if IA == 'piedra':
            print("Computadora: ",IA)

        if IA == 'tijeras':
            print("HUMANO: ", Humano)

    if Humano == 'piedra':

        if IA == 'tijeras':
            print("COMPUTADORA: ", IA)



    if IA == 'papel':
        print("COMPUTADORA", IA)
    print("-----------------------------------------")
    historial.append(Humano)
    historial.append(IA)

    while len(historial) > 0:

        ultima_acction = historial.pop()



#pregunta al usuario que se desea hacer
    print("Desea? ")
    print("1) Jugar otra vez")
    print("2) Ver resultado anterior")
    print("3) Salir")
#su el usuario elige 3 se muestra la opcion y los resultados

    repetición = input("\nQue opcion elige: ")
    print("\nEligió opción: ",repetición)
    if repetición == '3':
        print("\n")
        print("Usted eligió Salir")
        print("Se muestra el resultado obtenido: ")
        print("\n")
        print(f"{historial}")
        print(f"La opcion fué: {ultima_acction}")
        print("Humano: ", Humano)
        print("COMPUTADORA: ", IA)
#si el usuario elige 2 se muestra solo el historial
        print(f":{historial}")
    if repetición == '2':

        print(f"{historial}")
        print(f"La opcion fué: {ultima_acction}")
        print("Humano: ",Humano)
        print("COMPUTADORA: ", IA)
        historial.append('Mostrar resultados: ')

        print(f":{historial}")


