from concurrent.futures import ThreadPoolExecutor

def init():
    global executor
    executor = ThreadPoolExecutor(max_workers=10)