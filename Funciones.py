import operator
import random as r
facturas = []
productos = []
cantidades_facturas = {}
cantidades_produtos = {}


class Factura:
    id = 0
    direccion = ""
    fecha = ""
    nombre = ""
    nit = ""
    monto = 0
    productos = []

    def __init__(self, invoice):
        self.id = invoice['id']
        self.direccion = invoice['address']
        self.fecha = invoice['date_created']
        self.nombre = invoice['name']
        self.nit = invoice['nit']
        self.products = invoice['products']


class Producto:
    id = 0
    nombre = ""
    descripcion = ""
    cantidad = 0
    fecha= 0

    def __init__(self, producto):
        self.id = producto['id']
        self.nombre = producto['name']
        self.descripcion = producto['description']
        self.cantidad = producto['price']
        self.fecha = producto['date']
        self.quantity = self.fecha[0] * 10000 + self.fecha[1] * 100 + self.fecha[2]


#Obtener Datos de Rabit sobre las ultimas 5000 facturas de la tabla

def agregarFactura(factura):
    nuevaFactura = Factura(factura)
    facturas.append(nuevaFactura)

    for i in factura['products']:
        agregarProducto(i)

def agregarProducto(producto):
    nuevoProducto = Producto(producto)
    productos.append(nuevoProducto)

def actualizarDatos():
    contador = len(cantidades_facturas)
    for factura in facturas:
        for producto in factura.products:
            if producto['name'] in cantidades_facturas:
                cantidades_facturas[producto['name']] = cantidades_facturas[producto['name']] + 1
            else:
                cantidades_facturas[producto['name']] = 1

    #YYYY-MM-DD
    cantidades_produtos = {}
    productos.sort(key=lambda x: x.quantity, reverse=False)
    return


def obtenerProductoMasVendido():
    elproductomasvendido = ""
    frecuencia = 0
    for product in  cantidades_facturas.items():
        if product[1] > frecuencia:
            frecuencia = product[1]
            elproductomasvendido = product[0]
    return elproductomasvendido
    # return max(cantidades_facturas.items(), key=operator.itemgetter(1))[0]


def obtenerProductoMenosVendido():
    elproductomenosveniddo = ""
    frecuencia = 100
    for product in  cantidades_facturas.items():
        if product[1] < frecuencia:
            frecuencia = product[1]
            elproductomenosveniddo = product[0]
    return elproductomenosveniddo

def obtenerProductoconMasStock():
    actualizarDatos()
    return productos.keys()[-1]


def obtenerProductoconMenosStock():
    actualizarDatos()
    return productos.keys()[0]


def generar_oferta():
    productoMasVendido = obtenerProductoMasVendido()
    productoMenosVendido = obtenerProductoMenosVendido()

    rng = r.randint(0,3)
    if rng == 1:
        return {"id": productoMasVendido, "oferta": "Llevate un " + productoMenosVendido + " A mitad de precio en la "
                                                                            "compra de un " + productoMasVendido}
    elif rng == 2:
        return {"id": productoMenosVendido,
                "oferta": "En la compra de un " + productoMenosVendido + " llevate el tercero gratis."}
    elif rng == 3:
        return {"id": productoMasVendido, "oferta": "En la compra de un " + productoMasVendido +  " "
                                "llena una encuesta con vale para un " + productoMenosVendido+ " gratis"}
    else:
        return {"id": productoMenosVendido, "oferta": "2x1 en " + productoMenosVendido}

def generar_recomnedacion():
    productoMasStock = obtenerProductoconMasStock()
    productoMenosStock = obtenerProductoconMenosStock()
    recomendaciones = []
    if productos[productoMasStock] > 200:
        recomendaciones.append({"id": productoMasStock, "recomendacion": "Crear una oferta con menus relacionados con "
                                                                         "este producto"})
    if productos[productoMenosStock] < 50:
        recomendaciones.append({"id": productoMenosStock, "recomendacion": "Comprar mas " + productoMenosStock})

    return recomendaciones