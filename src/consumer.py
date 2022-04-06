from threading import Lock
import util
import time

consumer_id = 0
def get_consumer_id():
    global consumer_id
    with Lock():
        consumer_id += 1
        return consumer_id

class Consumer:
    def __init__(self, message_queue):
        self.message_queue = message_queue
        self.id = get_consumer_id()
        self.subcribed_topics = {}

    def subscribe(self, topic):
        if not self.subcribed_topics.get(topic.name):
            self.subcribed_topics[topic.name] = topic

    def listen(self):
        util.executor.submit(self.__listen)

    def __listen(self):
        while True:
            for topic in self.subcribed_topics.values():
                if not topic.messages.empty():
                    topic.full.acquire()
                    topic.mutex.acquire()
                    message = topic.remove_message()
                    topic.mutex.release()
                    topic.empty.release()     
                    print('{} received {}'.format(self.id, message))
                    break
            time.sleep(1.5)
