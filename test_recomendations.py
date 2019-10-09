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
dummy_invoice = {"id": 0,
                 "address": "ciudad",
                 "date_created": "2020-01-01",
                 "name": "Rodolfo Perez",
                 "nit": 12345678-9,
                 "products": [dummy_product1,  dummy_product2, dummy_product3]}



def test_mayoresymenoresventas():
    Funciones.agregarFactura(dummy_invoice)
    Funciones.actualizarDatos()
    resultado1 = Funciones.obtenerProductoMasVendido()
    resultado2 = Funciones.obtenerProductoMenosVendido()
    assert resultado1 == "Galleta"
    assert resultado2 == "Tortix"
    return


def test_recommendations():
    for i in Funciones.productos:
        print(i)
    print("=========================================================")
    Funciones.agregarProducto(dummy_product1)
    Funciones.agregarProducto(dummy_product2)
    Funciones.agregarProducto(dummy_product3)
    Funciones.actualizarDatos()
    resultado1 = Funciones.obtenerProductoconMasStock()
    print(resultado1)

