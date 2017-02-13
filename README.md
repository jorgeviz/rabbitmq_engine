# RabbitMQ class with JSON serializer

Uses pika library to create a simple consumers and producer with json serialization

## Environmental Variables

```
	export RABBIT_HOST='localhost'
	export RABBIT_ROUTING_KEY='tasks'
	export RABBIT_QUEUE='tasks'
	export RABBIT_EXCHANGE=''
	export RABBIT_EXCHANGE_TYPE='fanout'
```

## Simple Consumer usage

```python 
	from rabbit_engine import RabbitEngine

	def callback(ch, method, properties, body):
		#do whatever you want with the message received
		print(body)

	# Create consumer instance with values taken from the env vars
	consumer = RabbitEngine()
	# Specify the name of your callback function
	consumer.set_callback(callback)
	# Start consuming with or without acknowledgement
	consumer.consume(no_ack=True)
```

## Simple producer usage

```python
	from rabbit_engine import RabbitEngine
	from datetime import datetime as dt

	# Instantiate producer or consumer with a dict as well, purge param clears the queue before publishing
	producer = RabbitEngine({'rabbit_host':'localhost', 
							'rabbit_queue':'tasks', 
							'rabbit_key':'tasks'},
							purge=True)

	# Publishes with designated or predefined params
	producer.publish({'message': 'Hello world!', 'date':str(dt.utcnow())})

	# Close socket connection
	producer.close()
```