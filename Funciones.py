import operator
import random as r
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

    def actualizar(self, json):
        return generar_oferta()


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
    actualizarDatos()
    return productos.keys()[-1]


def obtenerProductoconMenosStock():
    actualizarDatos()
    return productos.keys()[0]


def generar_oferta():
    productoMasVendido = obtenerProductoMasVendido()
    productoMenosVendido = obtenerProductoMenosVendido()
    productoMasStock = obtenerProductoconMasStock()
    productoMenosStock = obtenerProductoconMenosStock()

    rng = r.randint(0,3)
    if rng == 1:
        return {"id": productoMasVendido, "oferta": "Llevate un " + productoMenosVendido + " A mitad de precio en la "
                                                                    "compra de un " + productoMasVendido }
    elif rng == 2:
        return {"id": productoMenosVendido, "oferta": "En la compra de un " + productoMenosVendido + " llevate el tercero gratis."}
    elif rng == 3:
        return {"id": productoMasStock, "recomendacion": "Crear una oferta con menus relacionados con "                                                                            "este producto"}
    else:
        return {"id": productoMenosStock, "recoomendacion": "Comprar mas " + productoMenosStock}
