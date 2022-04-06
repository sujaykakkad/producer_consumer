
class MessageQueue:
    def __init__(self):
        self.topics = {}

    def add_topic(self, topic):
        if not self.topics.get(topic.name):
            self.topics[topic.name] = topic