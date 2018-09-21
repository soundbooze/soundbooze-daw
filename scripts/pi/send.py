import os

path = "/tmp/my_program.fifo"
os.mkfifo(path)

fifo = open(path, "w")
fifo.write("Message from the sender!\n")
fifo.close()
