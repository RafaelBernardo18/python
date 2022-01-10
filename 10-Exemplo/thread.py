import threading
from time import sleep

global var

var = False

def tarefa1(num, x):
    while x < num:
        print("primeiro")
        x = x + 1
        sleep(1)

def tarefa2():
    y = 0
    while y < 10:
        print("segundo")
        y = y + 1
        sleep(1)

def tarefa3():
    z = 0
    while z < 10:
        if var:
            break
        print("terceiro")
        z = z + 1
        sleep(1)

threading.Thread(target = tarefa1 ,args = (15,3,)).start()
threading.Thread(target = tarefa2).start()
threading.Thread(target = tarefa3).start()

var = True