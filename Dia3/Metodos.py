texto = "este es el texto de prueba"
resultado = texto.upper()
print(resultado)

resultado = texto[2].upper()
print(resultado)

resultado = texto.lower()
print(resultado)

resultado = texto.split()
print(resultado)

resultado = texto.split("t")
print(resultado)

a = "aprender"
b = "python"
c = "es genial"
e = " ".join([a, b, c])
print(e)

resultado = texto.find("este")
print(resultado)

resultado = texto.replace("prueba", "pruebas")
print(resultado)

lista_palabras = ["La","legibilidad","cuenta."]
resultado = " ".join(lista_palabras)
print(resultado)

frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."
resultado = frase.replace("prueba", "pruebas")
resultado = frase.replace("mala", "buena")

print(resultado)
