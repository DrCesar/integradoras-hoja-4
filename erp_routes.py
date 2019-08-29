
import pika

def erp_product_callback(ch, method, properties, body):
    pass


def erp_invoice_callback(ch, method, properties, body):
    pass


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

