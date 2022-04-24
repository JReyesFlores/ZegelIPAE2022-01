from helper import *
from datetime import date

# print(dir(date))
# ...year

try:
    formato_fecha = '%d/%m/%Y'
    fecha_nacimiento = input('Ingrese su fecha de cumpleaños (día/mes/año): ')
    if validando_fecha(fecha_nacimiento, formato_fecha): 
        str_fecha_nac = fecha_nacimiento.split('/')
        fecha_nacimiento = date(int(str_fecha_nac[2]),int(str_fecha_nac[1]),int(str_fecha_nac[1]))
        fecha_actual = date.today()
        edad_calculada = fecha_actual.year - fecha_nacimiento.year
        print(f'Su edad actual es: {edad_calculada}')
    else:
        print(f'Formato incorrecto de fecha ==> {fecha_nacimiento}')


except KeyboardInterrupt:
    print('\nSe ha interrumpido la consola...')     

except Exception:
    print('Error en la aplicación')
