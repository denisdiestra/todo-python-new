lista = ['a','b','c','d']

for letra in lista:
    print("Letra: "+letra)

lista = ['pablo','laura', 'fede', 'luis', 'julia']

for nombre in lista:
    if nombre.startswith('l'):
        print(nombre)
    else:
        print('nombre que o comienza con l')

numeros = [1,2,3,4,5]

mi_valor = 0

for numero in numeros:
    mi_valor = mi_valor + numero
print(mi_valor)


palabra = 'python'

for letra in palabra:
    print(letra)
