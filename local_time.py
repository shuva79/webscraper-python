import time


def local_time():
    current = time.localtime()
    current_time = time.strftime("%H:%M:%S", current)
    return current_time




