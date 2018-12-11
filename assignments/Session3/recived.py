# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 14:45:33 2018

@author: bellangf
"""
import os
import pika
import time

amqp_url ="amqp://sasycihj:n14MVIoGwO09KBsq9ZhDhW0zUPMJYVw-@flamingo.rmq.cloudamqp.com/sasycihj"
url = os.environ.get("CLOUDAMQP",amqp_url)

url = os.environ.get('CLOUDAMQP_URL', amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 5

connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue='presentation', durable=True)
channel.basic_qos(prefetch_count=1)

def callback(ch, method, properties, body):

    print(" [x] Received %r" % body)
    print("message read, deleting message")
    ch.basic_ack(delivery_tag = method.delivery_tag)
    
channel.basic_consume(callback,queue='presentation',no_ack=False)



print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()