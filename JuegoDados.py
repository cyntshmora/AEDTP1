import random
# dados de prueba
a = 4
b = 5
c = 6

puntos_player_1 = 0
puntos_player_2 = 0

# RONDA 1

# jugador 1

aB = a == b
bC = b == c
cA = a == c

print("RONDA 1")
print("Jugador 1")

if (aB and bC):      # se compara si los 3 dados son iguales
    puntos_player_1 = +6
    print("suma 6")
else:
    if (aB):            # relanzamiento
        print("El dado c es diferente")
        c = random.randint(1, 6)
        if (b == c):
            puntos_player_1 = +6
        else:
            puntos_player_1 = +3
    else:
        if (cA or bC):         # relanzamiento
            print("El dado a o el b es diferente")
            #b = random.randint(1, 6)
            aux = 3 #Valor de prueba
            if (aux == c):
                puntos_player_1 = +6
            else:
                puntos_player_1 = +3

print("Puntos: ", puntos_player_1)

#jugador 2

# dados de prueba
a = 5
b = 4
c = 4

aB = a == b
bC = b == c
cA = a == c

print("Jugador 2")

if (aB and bC):      # se compara si los 3 dados son iguales
    puntos_player_2 = +6
    print("suma 6")
else:
    if (aB):            # relanzamiento
        print("El dado c es diferente")
        #c = random.randint(1, 6)
        if (b == c):
            puntos_player_2 = +6
        else:
            puntos_player_2 = +3
    else:
        if (cA or bC):         # relanzamiento
            print("El dado a o el b es diferente")
            #b = random.randint(1, 6)
            aux = 4 #Valor de prueba
            if (aux == c):
                puntos_player_2 = +6
            else:
                puntos_player_2 = +3

print("Puntos: ", puntos_player_2)

#RONDA 2

#jugador 1
print("\nRONDA 2")
print("Jugador 1")

# dados de prueba
a = 2
b = 4
c = 4

eleccion = int(input("Ingrese 1 si apuesta por par o 0 si apuesta por impar"))

mayor = 0

acerto = False

duplica = False

if ((a + b + c) % 2 == 0):
    if (eleccion == 1):
        acerto = True
        duplica = (a % 2 == 0) and (b % 2 == 0) and (c % 2 == 0)
else:
    if (eleccion == 0):
        acerto = True
        duplica = (a % 2 != 0) and (b % 2 != 0) and (c % 2 != 0)

if (acerto):
    if (a > b and a > c):
        mayor = a
    else:
        if (b > c):
            mayor = b
        else:
            mayor = c

    puntos_player_1 = +mayor
    if (duplica):
        puntos_player_1 = puntos_player_1 * 2
        print("Duplica!!!")
print("puntos totales: ", puntos_player_1)

#jugador 2

print("Jugador 2")

# dados de prueba
a = 2
b = 1
c = 1

eleccion = int(input("Ingrese 1 si apuesta por par o 0 si apuesta por impar"))

mayor = 0

acerto = False

duplica = False

if ((a+b+c) % 2 == 0):
    if(eleccion == 1):
        acerto = True
        duplica = (a % 2 == 0) and (b % 2 == 0) and (c % 2 == 0)
else:
    if (eleccion == 0):
        acerto = True
        duplica = (a % 2 != 0) and (b % 2 != 0) and (c % 2 != 0)

if (acerto):
    if (a > b and a > c):
        mayor = a
    else:
        if (b > c):
            mayor = b
        else:
            mayor = c

    puntos_player_2 = +mayor
    if (duplica):
        puntos_player_2 = puntos_player_2 * 2
        print("Duplica!!!")
print("puntos totales: ", puntos_player_2)
