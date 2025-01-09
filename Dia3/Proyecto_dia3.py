# 1. Ingreso de datos
texto_usuario = input("Ingresa un texto cualquiera: ").lower()
letras = []

for i in range(3):
    letra = input(f"Ingresa la letra {i + 1}: ").lower()
    letras.append(letra)

print("\n🔎 Análisis del texto:\n")

# 1. ¿Cuántas veces aparece cada letra?
print("1. Frecuencia de letras:")
for letra in letras:
    cantidad = texto_usuario.count(letra)
    print(f"   - La letra '{letra}' aparece {cantidad} veces")

# 2. ¿Cuántas palabras hay?
palabras = texto_usuario.split()
print(f"\n2. El texto tiene {len(palabras)} palabras.")

# 3. Primera y última letra
primera = texto_usuario[0]
ultima = texto_usuario[-1]
print(f"\n3. La primera letra del texto es: '{primera}'")
print(f"   La última letra del texto es: '{ultima}'")

# 4. Texto con palabras invertidas
palabras_invertidas = ' '.join(palabras[::-1])
print(f"\n4. Texto con el orden de palabras invertido:\n   {palabras_invertidas}")

# 5. ¿Contiene la palabra "Python"?
contiene_python = "python" in texto_usuario
print(f"\n5. ¿El texto contiene la palabra 'Python'? {contiene_python}")
