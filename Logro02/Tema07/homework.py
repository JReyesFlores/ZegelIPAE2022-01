class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.monto = 0

    def depositar(self, monto):
        self.monto = self.monto + monto

    def extraer(self, monto):
        self.monto = self.monto - monto

    def retornar_monto(self):
        return self.monto

    def imprimir(self):
        print(self.nombre, "tiene depositado la suma de: ", self.monto)


class Banco:
    clientes = []
    def __init__(self, cant_clientes):
        try:
            print('='*50)
            registro = 1
            while registro <= cant_clientes:
                self.clientes.append(
                    Cliente(input(f'Ingrese el nombre del cliente #{registro}: ')))
                registro += 1
            #self.cliente1 = Cliente("Juan")
            #self.cliente2 = Cliente("Ana")
            #self.cliente3 = Cliente("Diego")
        except:
            print('Error en la aplicación')

    def operar(self):
        try:
            print('='*50)
            operacion = 0
            while operacion != 3:
                operacion = int(
                    input('Ingrese la operación por realizar\n1) Depósito\n2) Extraer\n3) Salir\nOperacion #:'))
                if operacion == 3:
                    break
                
                numero_cliente = int(input('Ingrese el número de cliente: '))
                if numero_cliente > 0 and numero_cliente < len(self.clientes):
                    numero_cliente -= 1
                    monto = float(
                        input(f'Ingrese el monto a {("extraer","depositar")[operacion == 1]}: '))
                    if operacion == 1:
                        self.clientes[numero_cliente].depositar(monto)
                    else:
                        self.clientes[numero_cliente].extraer(monto)
                else:
                    print('Número de cliente no válido.')
                    break

            # self.cliente1.depositar(100)
            # self.cliente2.depositar(150)
            # self.cliente3.depositar(200)
            # self.cliente3.extraer(150)
        except:
            print('Error en la aplicación')

    def depositos_totales(self):
        try:
            print('='*50)
            total = 0
            for cliente in self.clientes:
                cliente.imprimir()
                total += cliente.monto

            print(f'El total de dinero del banco es: {total}')
            # total = self.cliente1.retornar_monto() + self.cliente2.retornar_monto() + \
            #    self.cliente3.retornar_monto()
            #print("El total de dinero del banco es: ", total)
            # self.cliente1.imprimir()
            # self.cliente2.imprimir()
            # self.cliente3.imprimir()
        except:
            print('Error en la aplicación')


# bloque principal
banco1 = Banco(3)
banco1.operar()
banco1.depositos_totales()
