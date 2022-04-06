import util

class Producer:
    def __init__(self, message_queue):
        self.message_queue = message_queue

    def publish_message(self, topic, message):
        util.executor.submit(self.__publish_message, topic, message)
        
    def __publish_message(self, topic, message):
        topic.empty.acquire()
        topic.mutex.acquire()

        topic.add_message(message)
        print('Published Message {} to topic {}'.format(message, topic.name))

        topic.mutex.release()
        topic.full.release()