#!/usr/bin/env python
import pika

cred = pika.credentials.PlainCredentials("qpfuamli","8hXI_DfL2MZTCAvsewLlaeta_A-tG7Ha")
connection = pika.BlockingConnection(pika.ConnectionParameters(host="chimpanzee.rmq.cloudamqp.com",virtual_host="qpfuamli",credentials=cred))
channel = connection.channel()

#channel.queue_declare(queue='teste1')

channel.basic_publish(exchange='fm.fanout', routing_key='', body='Hello World 1!')
channel.basic_publish(exchange='fm.fanout', routing_key='', body='Hello World 2!')
channel.basic_publish(exchange='fm.fanout', routing_key='', body='Hello World 3!')
print(" [x] Sent 'Hello World!'")
connection.close()