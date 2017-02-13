#-*- coding:utf-8 -*-
from rabbit_engine import RabbitEngine

def callback(ch, method, properties, body):
	print('properties')
	print(properties)
	print('body')
	print(body)

consumer = RabbitEngine(purge=True)
consumer.set_callback(callback)
consumer.consume(no_ack=True)
