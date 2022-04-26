def contar_letras(frase):
    txt = 0
    for l in frase:
        if l != '':
            txt += 1
    return print(txt)

# contar_letras('Hola')