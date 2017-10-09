from os import system, listdir
import sys
ath={}
def cambio(line):
    arreglo=''
    for char in range(0, len(line)):
        if line[char]==':' or line[char]=='-':
            arreglo=arreglo+'.'
        else:
            arreglo=arreglo+line[char]
    return arreglo
def repetidos(lista):
    cambio=[]
    for elemento in lista:
        if elemento not in cambio:
            cambio.append(elemento)
    return cambio
def obtdat(arch):
    try:
        linea = f.readline()
        linea = cambio(linea)
        athl = linea.strip().split(',')
        (name, lstnm) = athl[0].split(' ')   
        ath[name] = [athl.pop(0), athl.pop(0), [float(num) for num in athl]]
    except IOError as ioerr:
        print (str(ioerr))
    except:
        system("pause")

#with open("sarah2.txt", "+r") as f:
#    obtdat(f)
x=True
while x==True:
    try:
        for item in listdir('.'):
            print (item)
        file = str(input("Inserte el nombre del archivo de texto que desea agregar a su diccionarios (sin extension): "))
        try:
            with open((file+".txt"), "+r") as f:
                obtdat(f)
        except IOError as ioerr:
            print (str(ioerr))
        else:
            y=True
            while y==True:
                try:
                    opc = int(input("Desea agregar otro archivo al diccionario\n1)Si\n2)No\n"))
                    if opc==1:
                        x=True
                        y=False
                    elif opc==2:
                        x=False
                        y=False
                    else:
                        print ("Seleccione una opcion correcta")
                except:
                    print ("Seleccione una opcion correcta")
    except NameError as namerr:
        print (str(namerr))
        print ("Inserte un archivo valido")
        system("pause")
for name in ath.keys():
    ath[name][2]=sorted(repetidos(ath[name][2]), reverse = True)
    print ('Nombre: ', name, '\tTiempos: ', ath[name][2])
for name in ath.keys():
    print ('Los 3 mejores tiempos de: ', name, 'son: ', end='')
    y=0
    while y<3:
        if y<2:
            print (str(ath[name][2][y]), end=', ')
            y+=1
        else:
            print (str(ath[name][2][y]))
            y+=1