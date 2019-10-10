import operator
import pprint
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
        self.stock = 1
        self.quantity = self.fecha[0] * 10000 + self.fecha[1] * 100 + self.fecha[2]

    def __str__(self):
        return "{ id: " + str(self.id) + ",\nnombre: " + str(self.nombre) + ",\ndescripcion: " + str(self.descripcion) + \
               ",cantidad :" + str(self.cantidad) + ",\nfecha: " + str(self.fecha) + ",\nstock: " + str(self.stock) + "\n"



#Obtener Datos de Rabit sobre las ultimas 5000 facturas de la tabla

def agregarFactura(factura):
    nuevaFactura = Factura(factura)
    facturas.append(nuevaFactura)

    for i in factura['products']:
        agregarProducto(i)

def agregarProducto(producto):
    for elemento in productos:
        if elemento.nombre == producto['name']:
            elemento.stock = elemento.stock + 1
            return
    nuevoProducto = Producto(producto)
    productos.append(nuevoProducto)

def actualizarDatos():
    for factura in facturas:
        for producto in factura.products:
            if producto['name'] in cantidades_facturas:
                cantidades_facturas[producto['name']] = cantidades_facturas[producto['name']] + 1
            else:
                cantidades_facturas[producto['name']] = 1

    #YYYY-MM-DD
    cantidades_produtos = {}

    cantidades_produtos = productos.sort(key=lambda x: x.stock, reverse=False)
    print(cantidades_produtos)
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

    return str(cantidades_produtos[0])


def obtenerProductoconMenosStock():
    actualizarDatos()
    return str(cantidades_produtos[-1])


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
    if productoMasStock > 200:
        recomendaciones.append({"id": str(productoMasStock), "recomendacion": "Crear una oferta con menus relacionados con "
                                                                         "este producto"})
    if productoMenosStock < 50:
        recomendaciones.append({"id": str(productoMenosStock), "recomendacion": "Comprar mas " + str(productoMenosStock)})

    return recomendaciones

