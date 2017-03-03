import sys
from rabbit_engine import RabbitEngine
from config import *


producer = RabbitEngine({'host':'localhost', 
						'queue':'tasks', 
						'routing_key':'tasks'},
						purge=True)

message = ' '.join(sys.argv[1:]) or "Hello World!"

for i in range(0,10000):
    producer.send('tasks',{'message':str(message+" "+str(i))})

producer.close()
