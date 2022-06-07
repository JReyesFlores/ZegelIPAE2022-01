
try:
    numero = int(input("Introducir un número: "))
    factorial = 1
    for num in range(1, numero + 1):
        factorial *= num
    print(factorial)

except Exception as ex:
    print(f'Error:\n{ex}')
