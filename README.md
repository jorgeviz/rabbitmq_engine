# Data Streamer class with JSON serializer

Library to set producers and consumers to stream data.
Currently uses pika library to create a simple consumers and producer with json serialization and stream data using RABBIT as broker.

## Environmental Variables

```
	export STREAMER_HOST='localhost'
	export STREAMER_ROUTING_KEY='tasks'
	export STREAMER_QUEUE='tasks'
	export STREAMER_EXCHANGE=''
	export STREAMER_EXCHANGE_TYPE='fanout'
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
	producer = RabbitEngine({'host':'localhost', 
							'queue':'tasks', 
							'routing_key':'tasks'},
							purge=True)

	# Publishes with designated or predefined params
	producer.send('tasks',{'message': 'Hello world!', 'date':str(dt.utcnow())})

	# Close socket connection
	producer.close()
```


### TO DO

* Add `multi_q` argument to method `send()` to allow multiple queues publishes within one instance
* Add Kafka compatibility
* Add Streamer selector
