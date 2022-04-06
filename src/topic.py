from threading import Semaphore
from queue import Queue

CAPACITY_PER_TOPIC = 2
class Topic:
    def __init__(self, name):
        self.name = name
        self.messages = Queue()
        self.mutex = Semaphore()
        self.empty = Semaphore(CAPACITY_PER_TOPIC)
        self.full = Semaphore(0)

    def remove_message(self):
        return self.messages.get()

    def add_message(self, message):
        self.messages.put(message)
