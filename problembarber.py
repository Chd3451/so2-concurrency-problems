from threading import Thread, Semaphore
import time
import random

NUMERO_DE_SILLAS_DISPONIBLES = 3

clientes = Semaphore(0)
sillas = Semaphore(1)
clientes_esperando = 0

def atender_cliente():
    print("El barbero atiende a un cliente")
    time.sleep(random.randint(1, 5))

def esperar():
    print("El cliente se sienta a esperar")
    time.sleep(random.randint(1, 5))

def irse():
    print("El cliente se fue, las sillas de espera estan llenas")

def barbero():
    while True:
        
        clientes.acquire()

        
        atender_cliente()

       
        sillas.release()

def cliente():
    global clientes_esperando

    
    if sillas.acquire(False):
        
        clientes_esperando += 1
        clientes.release()
        esperar()
        sillas.release()
        clientes_esperando -= 1
    else:
        
        irse()

def main():
    Thread(target=barbero).start()

    while True:
        time.sleep(random.randint(1, 3))
        Thread(target=cliente).start()

if __name__ == '__main__':
    main()
