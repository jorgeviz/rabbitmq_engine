#-*- coding:utf-8 -*-
from rabbit_engine import RabbitEngine
import json
from pprint import pprint

def callback(ch, method, properties, body):
	body_json = json.loads(body.decode('utf-8'))
	pprint(body_json)

consumer = RabbitEngine(purge=True)
consumer.set_callback(callback)
consumer.consume(no_ack=True)
