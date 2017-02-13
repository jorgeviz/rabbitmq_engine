import sys
from rabbit_engine import RabbitEngine
from config import *


producer = RabbitEngine({'rabbit_host':'localhost', 
						'rabbit_queue':'tasks', 
						'rabbit_key':'tasks'},
						purge=True)

message = ' '.join(sys.argv[1:]) or "Hello World!"

for i in range(0,10000):
    producer.publish({'message':str(message+" "+str(i))})

producer.close()