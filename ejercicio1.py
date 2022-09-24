from os import name
import threading
import time

sillas = threading.semaphore(4)
barberolisto = threading.semaphore(1)
clientelisto = threading.semaphore(1)
corteterminado = threading.semaphore(1)

Sillasdisponibles = 4
Totalclientes = 0

def corteFinalizado():
    print('\ncorte terminado')
    corteterminado.release()

def cortarcabello():
    print('cortando el cabello...')
    time.sleep(3)
    corteFinalizado()

def funcionbarbero():
    global totalclientes 
    while totalclientes == 0:
        print('No hay clientes.El barbero duerme tranquilamente...')
        while totalclientes > 0:
            clientelisto.acquire()
            global sillasDisponibles 
            print('\nEl barbero recibe solicitud del cliente y lo atiente')
            sillas.disponibles += 1
            sillas.release()
            print('sillas disponibles: ', sillasDisponibles)
            print('total de clientes (sumando al que esta siendo atendido): ', totalclientes)
            cortarcabello()
            totalclientes -= 1


def funcioncliente(index):
    print('\nllega cliente: ', index)
    global sillasdisponibles 
    if(sillasdisponibles>0):
        sillas.acquire()
        sillasdisponibles -= 1
        global totalclientes
        totalclientes += 1
        print('EL cliente se sienta en una silla')
        print('El cliente indica que esta listo para recibir el corte')
        print('sillas disponibles: ', sillasdisponibles)
        print('total de clientes (sumando al que esta siendo atendido): ', totalclientes)
        clientelisto.release()
        corteterminado.acquire()
        barberolisto.acquireI()

    else:
        print('\nEl cliente se va de la tienda al ver que no hay asiento disponible')

def main():
    while True:
        print("cuando el programa finalice, por favor indique si le gustaria repetirlo, (s/n")
        barbero = threading.thread(target=funcionbarbero)
        num = int(input("indique el numero de clientes que llegaran a la tienda: "))

        barbero.start()
        listacliente = list()
        for index in range(num):
            c = threading.thread(targe=funcioncliente, args=(index+1,))
            listacliente.append(c)
            time.sleep(1)
            c.start()
        time.sleep(3*num)
        value = input('¿deseas repetir el programa? s/n.\n')
        if(value == "n" or value == "N"):
            break

if name == 'main':
    main() 
