import time
import random

def random_delay(min_delay=0.5, max_delay=2.0):
    delay = random.uniform(min_delay, max_delay)
    time.sleep(delay)
