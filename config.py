import os

rabbit_host = os.getenv('STREAMER_HOST','localhost')
rabbit_key = os.getenv('STREAMER_ROUTING_KEY', 'tasks')
rabbit_queue = os.getenv('STREAMER_QUEUE', 'tasks')
rabbit_exchange = os.getenv('STREAMER_EXCHANGE', '')
rabbit_exchange_type = os.getenv('STREAMER_EXCHANGE_TYPE', '')
