import random

# ------------------ variables de decoración de interfaz -----------------
asteriscos = "*" * 50
lineas = "-" * 50
relanzamiento_msj = "Opps... casi!!! \nSegunda oportunidad!! Oprima enter para relanzar el dado diferente"
failed_msj = "Esta ronda no pudo ser..."
acerto_msj = "Acertaste la apuesta!!!"


puntos_player_1 = 0
puntos_player_2 = 0


# reglas del juego
print("")
print("\n\n", asteriscos, " REGLAS DEL JUEGO: DADOS", asteriscos)
print("\nSe juega con 3 dados y se enfrentan 2 jugadores. El juego se desarrolla en 2 rondas, y en cada ronda ambos jugadores pueden sumar puntos según las reglas de esa ronda:")
print("\n\n", lineas*2, "\nReglas de la PRIMER RONDA ⚀ ⚁ ⚂ ⚃ ⚄ ⚅")
print("El primer jugador lanza los 3 dados.")
print("☛a.) Si los tres dados fueran iguales el jugador suma 6 puntos. Por ejemplo, si el jugador obtiene los siguientes dados, sumará 6 puntos:")
print("☛b.) Si el jugador tuviera dos dados iguales y uno distinto (como en el ejemplo que sigue), entonces el jugador vuelve a tirar, pero únicamente")
print(" el dado distinto (que en el caso del ejemplo es el dado con valor 1). Si al volver a lanzar ese dado logra que los tres dados sean iguales ")
print("(como por ejemplo que se obtenga un 5 en el caso descripto), entonces sumará los 6 puntos en esa ronda.")
print("Si el dado relanzado sigue siendo distinto a los dos que eran iguales, el jugador sumará 3 puntos en esa ronda.")
print("☛c.) Si los tres dados fueran todos distintos, entonces obtiene 0 puntos y no puede volver a tirar ningún dado en esa ronda. Por ejemplo, en este caso:")
print("\n\n", lineas*2, "\nReglas de la SEGUNDA RONDA⚀ ⚁ ⚂ ⚃ ⚄ ⚅")
print("☛a.) El primer jugador vuelve a lanzar los 3 dados, y se considera que apuesta todo el puntaje de la ronda anterior a par/impar")
print("(el programa debe pedir que el jugador elija si apuesta por par o impar).")
print("☛b.) Si la suma de los tres dados en esta segunda jugada es de la paridad elegida, entonces suma el dado de mayor valor a su puntaje de la ronda anterior;")
print("en caso contrario, resta el dado de menor valor a su puntaje anterior.")
print("☛c.) Si efectivamente la suma en la segunda jugada es de la paridad elegida, entonces el programa debe controlar si además los tres dados fueron de la paridad elegida,")
print("y en ese caso, se duplica el puntaje total.")
print("Se repite la jugada para el segundo jugador con las mismas reglas que el primero.")
print("\n\n", lineas*2, "\nFINAL DEL JUEGO")
print("☛Gana el jugador que más puntaje haya obtenido.")

# Pide ingresar los nombres de los jugadores.
print("\n\n\n", asteriscos * 2)
nj1 = input("Ingrese el nombre del jugador 1: ")
nj2 = input("Ingrese el nombre del jugador 2: ")
print("\n", asteriscos * 2)

# --------------------------- RONDA 1 -----------------------------------
# jugador 1

print("\n\n", lineas, " RONDA 1 ", lineas)
print("\nTurno del jugador 1, ", nj1)
input("Presione enter para comenzar la partida")

# asignación de valores random
a = random.randint(1, 6)
b = random.randint(1, 6)
c = random.randint(1, 6)


aB = a == b
bC = b == c
cA = a == c

print("\tDados tirados: ", "\n\t\t", a, "\n\t\t", b, "\n\t\t", c)
if (b == a) and (b == c):      # se compara si los 3 dados son iguales
    puntos_player_1 = +6
else:
    if aB or bC or cA:
        input(relanzamiento_msj)
        if aB:            # relanzamiento, si a y b son iguales, entonces el diferente es c
            aux = random.randint(1, 6)
            print("\tTu dado ", c, " ahora vale ", aux)
            if aux == b:  # compara b con el nuevo valor de c (ya sabemos que a es igual a b)
                puntos_player_1 = +6
            else:
                puntos_player_1 = +3
        elif cA:         # si a y c son iguales, entonces el diferente es b
            # b = random.randint(1, 6)
            aux = random.randint(1, 6)  # Valor de prueba
            print("\tTu dado ", b, " ahora vale ", aux)
            if aux == a:
                puntos_player_1 = +6
            else:
                puntos_player_1 = +3
        else:  # por descarte, el diferente es a
            aux = random.randint(1, 6)  # Valor de prueba
            print("\tTu dado ", a, " ahora vale ", aux)
            if aux == c:
                puntos_player_1 = +6
            else:
                puntos_player_1 = +3
    else:  # ninguno de ellos coincide entre sí
        print(failed_msj)

print("Puntos que has obtenido esta ronda: ", puntos_player_1)

# jugador 2

print("\n\nTurno del jugador 2, ", nj2)
input("Presione enter para comenzar la partida")

# asignación de valores random
a = random.randint(1, 6)
b = random.randint(1, 6)
c = random.randint(1, 6)

aB = a == b  # realiza la validacion una sola vez para no tener que validarlo continuamente
bC = b == c
cA = a == c

print("\tDados tirados: ", "\n\t\t", a, "\n\t\t", b, "\n\t\t", c)
if (b == a) and (b == c):      # se compara si los 3 dados son iguales
    puntos_player_2 = +6
else:
    if aB or bC or cA:
        input(relanzamiento_msj)
        if aB:            # relanzamiento, si a y b son iguales, entonces el diferente es c
            # aux = random.randint(1, 6)
            aux = random.randint(1, 6)
            print("\tTu dado ", c, " ahora vale ", aux)
            if aux == b:  # compara b con el nuevo valor de c (ya sabemos que a es igual a b)
                puntos_player_2 = +6
            else:
                puntos_player_2 = +3
        elif cA:         # si a y c son iguales, entonces el diferente es b
            aux = random.randint(1, 6)  # Valor de prueba
            print("\tTu dado ", b, " ahora vale ", aux)
            if aux == a:
                puntos_player_2 = +6
            else:
                puntos_player_2 = +3
        else:  # por descarte, el diferente es a
            aux = random.randint(1, 6)  # Valor de prueba
            print("\tTu dado ", a, " ahora vale ", aux)
            if aux == c:
                puntos_player_2 = +6
            else:
                puntos_player_2 = +3
    else:  # ninguno de ellos coincide entre sí
        print(failed_msj)

print("Puntos que has obtenido esta ronda: ", puntos_player_2)


# ---------------------------------------------- RONDA 2 -------------------------------------------------


print("\n\n\n", lineas, " RONDA 2 ", lineas)
print("\nReglas de la SEGUNDA RONDA ⚀ ⚁ ⚂ ⚃ ⚄ ⚅")
print("☛a.) El primer jugador vuelve a lanzar los 3 dados, y se considera que apuesta todo el puntaje de la ronda anterior a par/impar")
print("☛b.) Si la suma de los tres dados en esta segunda jugada es de la paridad elegida, entonces suma el dado de mayor valor a su puntaje de la ronda anterior;")
print("en caso contrario, resta el dado de menor valor a su puntaje anterior.")
print("☛c.) Si efectivamente la suma en la segunda jugada es de la paridad elegida, entonces el programa debe controlar si además los tres dados fueron de la paridad elegida,")
print("y en ese caso, se duplica el puntaje total.")
print("Se repite la jugada para el segundo jugador con las mismas reglas que el primero.")
print("")


# jugador 1


print("\nTurno del jugador 1, ", nj1)

# asignación de valores random
a = random.randint(1, 6)
b = random.randint(1, 6)
c = random.randint(1, 6)

eleccion = int(input("Ingrese 1 si apuesta por par (en caso contrario presione cualquier otra tecla) "))

mayor = 0
menor = 0
acerto = False
duplica = False
suma = a + b + c

print("\tDados tirados: ", "\n\t\t", a, "\n\t\t", b, "\n\t\t", c)
print("La suma de tus dados es de: ", suma)

if suma % 2 == 0:
    if eleccion == 1:
        acerto = True
        duplica = (a % 2 == 0) and (b % 2 == 0) and (c % 2 == 0)
else:
    if eleccion != 1:
        acerto = True
        duplica = (a % 2 != 0) and (b % 2 != 0) and (c % 2 != 0)

if acerto:
    print(acerto_msj)
    if a > b and a > c:
        mayor = a
    else:
        if b > c:
            mayor = b

        else:
            mayor = c

    puntos_player_1 += mayor
    if duplica:
        puntos_player_1 = puntos_player_1 * 2
        print("Todos tus dados tirados fueron pares.. Duplica!!!")
else:
    if a < b and a < c:
        menor = a
    else:
        if b > c:
            menor = b
        else:
            menor = c

    puntos_player_1 -= menor
print("PUNTOS TOTALES: ", puntos_player_1)

# jugador 2


print("\nTurno del jugador 2, ", nj2)

# asignación de valores random
a = random.randint(1, 6)
b = random.randint(1, 6)
c = random.randint(1, 6)

eleccion = int(input("Ingrese 1 si apuesta por par (en caso contrario presione cualquier otra tecla) "))
mayor = 0
menor = 0
acerto = False
duplica = False
suma = a + b + c

print("\tDados tirados: ", "\n\t\t", a, "\n\t\t", b, "\n\t\t", c)
print("La suma de tus dados es de: ", suma)

if suma % 2 == 0:
    if eleccion == 1:
        acerto = True
        duplica = (a % 2 == 0) and (b % 2 == 0) and (c % 2 == 0)
else:
    if eleccion != 1:
        acerto = True
        duplica = (a % 2 != 0) and (b % 2 != 0) and (c % 2 != 0)

if acerto:
    print(acerto_msj)
    if a > b and a > c:
        mayor = a
    else:
        if b > c:
            mayor = b
        else:
            mayor = c

    puntos_player_2 += mayor
    if duplica:
        puntos_player_2 *= 2
        print("Todos tus dados tirados fueron pares.. Duplica!!!")
else:
    if a < b and a < c:
        menor = a
    else:
        if b > c:
            menor = b
        else:
            menor = c

    puntos_player_1 -= menor
print("PUNTOS TOTALES: ", puntos_player_2)


# ganador de la partida

print("\n\n\n", asteriscos, " FIN DE LA PARTIDA ", asteriscos)
input("\nOprima cualquier tecla para conocer el resultado de la partida ")
print("\n\n", lineas*2)

if puntos_player_1 == puntos_player_2:
    print("\t\t\t\t  Opps... EMPATE !!!")
else:
    if puntos_player_1 < puntos_player_2:
        print("\t\t\t\t", nj2, ", GANASTE!!! 🏆")
    else:
        print("\t\t\t\t", nj1, ", GANASTE!!! 🏆")
print("\n", lineas*2)
