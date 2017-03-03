#-*- coding:utf-8 -*-
import pika
import os
import json

class RabbitEngine(object):
    def __init__(self, config={}, purge=False):
        #Class variables
        self.rabbit_host = config['host'] if 'host' in config.keys() else os.getenv('STREAMER_HOST','localhost')
        self.rabbit_key = config['routing_key'] if 'routing_key' in config.keys() else os.getenv('STREAMER_ROUTING_KEY','')
        self.rabbit_queue = config['queue'] if 'queue' in config.keys() else os.getenv('STREAMER_QUEUE','')
        self.rabbit_exchange = config['exchange'] if 'exchange' in config.keys() else os.getenv('STREAMER_EXCHANGE','')
        self.rabbit_exchange_type = config['exchange_type'] if 'exchange_type' in config.keys() else os.getenv('STREAMER_EXCHANGE_TYPE','')

        # Initialize connection to the Rabbit Server
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.rabbit_host,heartbeat_interval=0))
        self.channel = self.connection.channel()
        # Exchange declaration 
        if self.rabbit_exchange_type == '' and self.rabbit_exchange != '':
            self.channel.exchange_declare(exchange=self.rabbit_exchange, 
                                            type=self.rabbit_exchange_type)  # type = 'direct' | 'fanout' | ' topic'
        # Set up the queue
        self.channel.queue_declare(queue=self.rabbit_queue)
        if purge:
            self.channel.queue_purge(queue=self.rabbit_queue)

    def send(self, key, msg):
        # Pubishing the message to the queue
        self.channel.basic_publish(exchange=self.rabbit_exchange,
                      routing_key=self.rabbit_key,
                      body=json.dumps(msg),# ensure_ascii=False),
                      properties=pika.BasicProperties(content_type='application/json', delivery_mode=2))

    def set_callback(self, callback):
        # Callback function to return body
        self._callback = callback
        return self

    def consume(self, no_ack=False, msg=''):
        # Receiving the message from the queue
        self.channel.basic_consume(self._callback,
                              queue=self.rabbit_queue,
                              no_ack=no_ack)
        # Consumer listener init
        if len(msg) == 0:
            print(' [*] Waiting for messages. To exit press CTRL+C')
        else:
            print(str(msg) + 'To exit press CTRL+C')
        return self.channel.start_consuming()

    def close(self):
        # Close connection with the server
        return self.connection.close()
