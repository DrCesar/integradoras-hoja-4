
import pika
import Funciones

import json


def erp_receiver_callback(ch, method, properties, body):
    factura = json.loads(body)

    recomendacion = Funciones.actualizar(factura)

    local_channel.basic_publish(exchange='', routing_key='ClientesYVentas', body=json.dumps(recomendacion))



erp_connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
erp_channel = erp_connection.channel()

erp_channel.queue_declare(queue='ERP')
erp_channel.basic_consume(queue='ERP', auto_ack=True, on_message_callback=erp_receiver_callback)



local_connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
local_channel = local_connection.channel()
local_channel.queue_declare('ClientesYVentas')

