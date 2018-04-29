import time
import sys

baud = 1200

def delayperchar():
    return (1/baud)*8


def dpc():
    return delayperchar()


def output(text):
    delay = float(dpc())
    for l in text:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")
    sys.stdout.flush()