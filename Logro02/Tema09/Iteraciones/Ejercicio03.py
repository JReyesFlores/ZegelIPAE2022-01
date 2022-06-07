# Declara generador
def gen_basico():
    yield "uno"
    yield "dos"
    yield "tres"


for valor in gen_basico():
    print(valor)  # uno, dos, tres
# Crea objeto generador y muestra tipo de objeto
generador = gen_basico()
print(generador)  # generator object gen_basico at 0x7f75ffad55e8
print(type(generador))  # class 'generator'
# Convierte a lista el objeto generador y muestra elementos
lista = list(generador)
print(lista)  # ['uno', 'dos', 'tres']
print(type(lista))  # class 'list'
