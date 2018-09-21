import os
import sys

path = "/tmp/bark.fifo"
fifo = open(path, "r")
for line in fifo:
    print "Received: " + line,
fifo.close()
