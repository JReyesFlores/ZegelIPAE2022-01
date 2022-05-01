from typing import Any


def mayor_valor(*numbers: int) -> Any:
    if len(numbers) == 0:
        return None
    mayor = 0
    for num in numbers:
        if num > mayor:
            mayor = num
    return mayor


def menor_valor(*numbers: int) -> Any:
    if len(numbers) == 0:
        return None

    menor = numbers[0]
    for num in numbers:
        if num < menor:
            menor = num
    return menor
