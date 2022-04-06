import time
from topic import Topic
from producer import Producer
from consumer import Consumer
from message_queue import MessageQueue
from util import init

init()
messageQueue = MessageQueue()
topic1 = Topic('topic1')
topic2 = Topic('topic2')
messageQueue.add_topic(topic1)
messageQueue.add_topic(topic2)
producer1 = Producer(messageQueue)
producer2 = Producer(messageQueue)

consumer1 = Consumer(messageQueue)
consumer2 = Consumer(messageQueue)
consumer3 = Consumer(messageQueue)
consumer4 = Consumer(messageQueue)
consumer5 = Consumer(messageQueue)

consumer1.subscribe(topic1)
consumer2.subscribe(topic1)
consumer3.subscribe(topic1)
consumer4.subscribe(topic1)
consumer5.subscribe(topic1)


consumer1.subscribe(topic2)
consumer3.subscribe(topic2)
consumer4.subscribe(topic2)

producer1.publish_message(topic1, 'Message 1')
producer1.publish_message(topic1, 'Message 2')
producer2.publish_message(topic1, 'Message 3')
producer1.publish_message(topic2, 'Message 4')
producer2.publish_message(topic2, 'Message 5')

consumer1.listen()
consumer2.listen()
consumer3.listen()
consumer4.listen()
consumer5.listen()
