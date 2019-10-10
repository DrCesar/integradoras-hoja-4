import pytest
import Funciones
import json


dummy_product1 = {"id": 0,
                  "name": "Galleta",
                  "description": "a cookie",
                  "price": 50,
                  "date": "2020-01-01",
                  }
dummy_product2 = {"id": 1,
                  "name": "Galleta",
                  "description": "a cookie",
                  "price": 50,
                  "date": "2020-01-01",
                  }
dummy_product3 = {"id": 2,
                  "name": "Tortix",
                  "description": "un riscito",
                  "price": 20,
                  "date": "2020-01-01",
                  }
dummy_product4 = {"id": 3,
                  "name": "FiestaSnax",
                  "description": "otro riscito",
                  "price": 10,
                  "date": "2020-01-01",
                  }
dummy_product5 = {"id": 2,
                  "name": "Tortix",
                  "description": "un riscito",
                  "price": 20,
                  "date": "2020-01-01",
                  }
dummy_invoice = {"id": 0,
                 "address": "ciudad",
                 "date_created": "2020-01-01",
                 "name": "Rodolfo Perez",
                 "nit": 12345678-9,
                 "products": [dummy_product1,  dummy_product2, dummy_product3]}
dummy_product6 = {"id": 4,
                  "name": "elotito",
                  "description": "otro riscito",
                  "price": 5,
                  "date": "2020-01-01",
                  }
dummy_product7 = {"id": 4,
                  "name": "elotito",
                  "description": "otro riscito",
                  "price": 5,
                  "date": "2020-01-01",
                  }
dummy_product8 = {"id": 4,
                  "name": "elotito",
                  "description": "otro riscito",
                  "price": 5,
                  "date": "2020-01-01",
                  }




def test_mayoresymenoresventas():
    Funciones.agregarProducto(dummy_product1)
    Funciones.agregarProducto(dummy_product2)
    Funciones.agregarProducto(dummy_product3)
    Funciones.agregarProducto(dummy_product4)
    Funciones.agregarProducto(dummy_product5)
    Funciones.agregarProducto(dummy_product6)
    Funciones.agregarProducto(dummy_product7)
    Funciones.agregarProducto(dummy_product8)
    Funciones.agregarFactura(dummy_invoice)
    Funciones.actualizarDatos()
    resultado1 = Funciones.obtenerProductoMasVendido()
    resultado2 = Funciones.obtenerProductoMenosVendido()
    assert resultado1 == "Galleta"
    assert resultado2 == "Tortix"
    return


def test_recommendations():
    print("=========================================================")
    Funciones.ordenarProductos()
    resultado1 = Funciones.obtenerProductoconMasStock()
    resultado2 = Funciones.obtenerProductoconMenosStock()
    assert resultado1.nombre == 'Galleta' and resultado1.stock == 4
    assert resultado2.nombre == 'FiestaSnax' and resultado2.stock == 1


def test_exploratory_1():
    keylist = []
    for property, value in vars(Funciones.productos[0]).items():
        keylist.append(property)
    assert keylist == ['id', 'nombre', 'descripcion', 'cantidad', 'fecha', 'stock', 'quantity']
