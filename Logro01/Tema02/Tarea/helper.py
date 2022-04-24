import datetime as modulo_date

# Función que valida la fecha con el formato especificado
def validando_fecha(fecha_string, formato = '%d/%m/%Y'):
    try:
        modulo_date.datetime.strptime(fecha_string, formato)
        return True
    except ValueError:
        return False