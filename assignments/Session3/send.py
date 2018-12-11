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
while(1):
    channel.basic_publish(exchange='',
                      routing_key='presentation',
                      body='Julien',
                      properties=pika.BasicProperties(delivery_mode = 2))
                        
    print(" [x] Sent 'Julien'")
    time.sleep(2) 



