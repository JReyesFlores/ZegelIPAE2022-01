from typing import Any


def suma(*numbers: float) -> Any:
    if len(numbers) == 0:
        return None

    suma_total = 0
    for num in numbers:
        suma_total += num
    return suma_total


def resta(num1: float, num2: float) -> float:
    return num1 - num2


def multiplicar(num1: float, num2: float) -> float:
    return num1 * num2


def dividir(num1: float, num2: float) -> float:
    return num1 / num2
