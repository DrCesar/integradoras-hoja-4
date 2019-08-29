
import pika
import Funciones
# import sqlalchemy

import json

from db import session
from resources.product import Product
from resources.invoice import Invoice

test_invoice = {
    'id': 3242
    'date': '2019-08-20',
    'description': 'De Chipilin',
    'name': 'tamalito',
    'price': 5,
    'stock': 34
}

def erp_product_callback(ch, method, properties, body):
    prod = Product(**test_invoice)
    session.add(prod)
    session.commit()




def erp_invoice_callback(ch, method, properties, body):
    pass

# prod = Product(id=1, name='Jabon', description='Jabon de manos', price=233)
# invoice = Invoice(id=1, address='hola', date_created=1566430918, name='Juan Perez', nit='234242-1')

# prod.invoices.append(invoice)


# session.add(prod)
# session.commit()



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


client

