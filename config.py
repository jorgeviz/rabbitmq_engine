import os

rabbit_host = os.getenv('RABBITMQ_HOST','localhost')
rabbit_key = os.getenv('RABBIT_ROUTING_KEY', 'tasks')
rabbit_queue = os.getenv('RABBIT_QUEUE', 'tasks')
rabbit_exchange = os.getenv('RABBIT_EXCHANGE', '')
rabbit_exchange_type = os.getenv('RABBIT_EXCHANGE_TYPE', '')
