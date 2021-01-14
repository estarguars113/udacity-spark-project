import asyncio

from confluent_kafka import Consumer

BROKER_URL = 'PLAINTEXT://localhost:9092'
TOPIC_NAME = 'police-service-calls'


async def consume(topic_name):
    consumer = Consumer({
        'bootstrap.servers': BROKER_URL,
        'group.id': '0',
    })
    
    consumer.subscribe([topic_name])
    
    while True:
        all_messages = consumer.consume()
        for message in all_messages:
            if message is None:
                print('Message not found')
            elif message.error() is not None:
                print(f'Error: {message.error()}')
            else:
                print(f'{message.value()}')
                
                
def start_consumer():
    try:
        asyncio.run(consume(TOPIC_NAME))
    except KeyboardInterrupt as _e:
        print("Shutting down")


if __name__ == '__main__':
    start_consumer()