# Funciones para cadenas
c1 = "a"
c2 = "@"

# Identificamos el código ASCII del caracter que se envia
print(ord(c1))
print(ord(c2))
print("-"*50)

# Genera el valor ASCII 
print(chr(97))
print(chr(64))
print("-"*50)

# Identificamos 
alpha = "abdefg"
print(alpha[1:3])
print(alpha[3:])
print(alpha[:3])
print(alpha[3:-2])
print(alpha[-3:4])
print(alpha[::2])
print(alpha[1::2])
print("-"*50)

# Capturando el valor mínimo y máximo
t = 'Los caballeros que dicen "Ni!"'
print('[' + min(t) + ']')
t = [0, 1, -2]
print(min(t))
print("-"*50)

t = 'Los caballeros que dicen "Ni!"'
print('[' + max(t) + ']')
t = [0, 1, 2]
print(max(t))
print("-"*50)

Palabra_texto = input("Ingrese texto: ")
Palabra_buscar = input("Ingrese palabra a buscar: ")
inicio = Palabra_texto.find(Palabra_buscar)
print(f'Palabra localizada en la posición: {inicio}')