from os import system
from Imprimir_Listas import repetir
import pickle
man = []
other = []
try:
    f = open("Archivo.txt", '+r')
    print(f.readline(), end='')
    print(f.readline(), end='')
    f.seek(0)
    print(f.readline(), end='')
    system("pause")
    system("cls")
    for line in f:
        try:
            (actor, frase)= line.split(':', 1)
            frase=frase.strip()
            print(actor,' said: ', end='')
            print(frase)
            if actor=='Man':
                man.append(frase)
            elif actor=='Other Man':
                other.append(frase)
        except ValueError:
            pass
    f.close()
except IOError as hola:
    system("pause")
    system("cls")
    print (str(hola))
    print ("Archivo no encontrado")
try:
    with open("Man.txt", '+w') as f, open("Other.txt", '+w') as f1:
        repetir(man, True, f, -1)
        repetir(other, True, f1, -1)
except IOError as error:
    #system("pause")
    #system("cls")
    #print ("Error: ", str(error))
    system("pause")
    system("cls")
    print ("Error con los archivos")

try:
    with open('mydata.pickle','+wb') as mysavedata:
        pickle.dump([1,2,'three'], mysavedata)
    with open("mydata.pickle", "rb") as mystoredata:
        a_list=pickle.load(mystoredata)
    print (a_list)
except IOError as err:
    print (str(err))
except pickle.PickleError as perr:
    print (str(perr))
system("pause")
