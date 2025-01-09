from random import randint

intentos = 0
numero_secreto = randint(1,100)
nombre = input("dime tu nombre: ")

print(f"bueno  {nombre}, he pensado un numero entre 1 y 100\mTienes 8 intentos")

while intentos < 8:
    estimado = int(input("cual es el numero?: "))
    intentos += 1


    if estimado < numero_secreto:
        print("mi numero es mas alto")

    if estimado > numero_secreto:
        print("mi numero es mas bajo")

    if estimado == numero_secreto:
        print(f"felicitaciones {nombre}! has adivinado en {intentos} intentos")
        break


if estimado != numero_secreto:
    print(f"lo siento, se han agotado los intentos. el numero secreto era {numero_secreto}")