def elMayorEs(num1, num2):
    if compararMayorA(num1, num2):
        return num1
    return num2


def compararMenorA(num1, num2):
    return num1 < num2


def compararMayorA(num1, num2):
    return num1 > num2


def compararIgual(num1, num2):
    return num1 == num2
