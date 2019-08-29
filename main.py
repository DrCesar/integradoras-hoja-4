
import pika
import Funciones
# import sqlalchemy

import json

from db import session
from resources.product import Product
from resources.invoice import Invoice



# Callback para cuando se reciben mensajes que infieren productos.
def erp_product_callback(ch, method, properties, body):
    body = json.loads(body)
    print(body, method.routing_key)

    # Segun que tipo de mensaje se reciba se decide que hacer con cada uno 
    if method.routing_key == 'new_product_queue':
        prod = Product(**body)
        session.add(prod)
        session.commit()

    elif method.routing_key == 'updated_product_queue' or method.routing_key == 'update_stock_queue':
        id = body.pop('id', None)
        session.query(Product).filter(Product.id == id).update(**body)
        session.commit()
    elif method.routing_key == 'delete_product_queue':
        session.query(Product).filter(Product.id == body['id']).delete()
        session.commit()

    products = Product.get_all(session)
    for product in products:
        print(product)

    # TODO 
    # recomedations = gen_recomentations()

    # sales = gen_sales()

    #client_channel.basic_publish(exchange='',routing_key='recomendation',body=json.dumps(recomendations))
    #client_channel.basic_publish(exchange='',routing_key='sales',body=json.dumps(sales))






def erp_invoice_callback(ch, method, properties, body):
    body = json.loads(body)
    print(body, method.routing_key)

    if method.routing_key == 'new_receipt_queue':
        products = body.pop('products', None)
        invo = Invoice(**body)
        for prod in products:
            product = Product.get_by_id(session, prod['id'])
            invo.products.append(product)

        session.add(invo)


    invoices = Invoice.get_all(session)
    for invoice in invoices:
        print(invoice)

    # TODO 
    # recomedations = gen_recomentations()

    # sales = gen_sales()

    #client_channel.basic_publish(exchange='',routing_key='recomendation',body=json.dumps(recomendations))
    #client_channel.basic_publish(exchange='',routing_key='sales',body=json.dumps(sales))





erp_connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
erp_channel = erp_connection.channel()

erp_channel.queue_declare(queue='new_product_queue')
erp_channel.basic_consume(queue='new_product_queue', auto_ack=True, on_message_callback=erp_product_callback)

erp_channel.queue_declare(queue='updated_product_queue')
erp_channel.basic_consume(queue='updated_product_queue', auto_ack=True, on_message_callback=erp_product_callback)

erp_channel.queue_declare(queue='delete_product_queue')
erp_channel.basic_consume(queue='delete_product_queue', auto_ack=True, on_message_callback=erp_product_callback)

erp_channel.queue_declare(queue='update_stock_queue')
erp_channel.basic_consume(queue='update_stock_queue', auto_ack=True, on_message_callback=erp_product_callback)

erp_channel.queue_declare(queue='new_receipt_queue')
erp_channel.basic_consume(queue='new_receipt_queue', auto_ack=True, on_message_callback=erp_invoice_callback)

erp_channel.queue_declare(queue='out_of_stock_queue')
erp_channel.basic_consume(queue='out_of_stock_queue', auto_ack=True, on_message_callback=erp_invoice_callback)

erp_channel.queue_declare(queue='deleted_receipt_queue')
erp_channel.basic_consume(queue='deleted_receipt_queue', auto_ack=True, on_message_callback=erp_invoice_callback)

erp_channel.start_consuming()


client_connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
client_channel = client_connection.channel()

client_channel.queue_declare(queue='new_product_queue')


