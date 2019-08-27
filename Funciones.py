import operator
facturas = []
productos = []
cantidades_facturas = {}
cantidades_produtos = {}
class Factura:
    id = 0
    monto = 0
    productos = []
    materiaPrima = []

    def __init__(self, id, monto, productos, materiaPrima):
        self.id = id
        self.monto = monto
        self.productos = productos
        self.materiaPrima = materiaPrima
        fecha = self.fecha_de_caducidad.split('-')
        self.quantity = fecha[0] * 10000 + fecha[1] * 100 + fecha[2]

class Producto:
    id = 0
    cantidad = 0
    fecha_de_caducidad  = 0

    def __init__(self, id, cantidad, fecha_de_caducidad):
        self.id = id
        self.cantidad = cantidad
        self.fecha_de_caducidad = fecha_de_caducidad

#Obtener Datos de Rabit sobre las ultimas 5000 facturas de la tabla
def actualizarDatos():
    cantidades_facturas = {}
    for factura in facturas:
        for producto in factura.productos:
            if producto in cantidades_facturas:
                cantidades_facturas[producto] = cantidades_facturas[producto] + 1
            else:
                cantidades_facturas[producto] = 1

    #YYYY-MM-DD
    cantidades_produtos = {}
    productos.sort(key=lambda x: x.quantity, reverse=False)
    return


def obtenerProductoMasVendido():
    return max(cantidades_facturas.iteritems(), key=operator.itemgetter(1))[0]


def obtenerProductoMenosVendido():
    return min(cantidades_facturas.iteritems(), key=operator.itemgetter(1))[0]


def obtenerProductoconMasStock():

    return


def obtenerProductoconMenosStock():
    return
