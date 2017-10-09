from os import system
athnames=["james", "julie", "mikey", "sarah"]
ath={}
def cambio(line):
    arreglo=''
    for char in range(0, len(line)):
        if linea[char]==':' or line[char]=='-':
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
for arch in athnames:
    try:
        with open((arch+".txt"), "+r") as f:
            linea=f.readline()
            linea=cambio(linea)
            ath[arch]=linea.strip().split(',')
            ath[arch]=[float(num) for num in ath[arch]]
    except IOError as ioerr:
        print (str(ioerr))
system("pause")
for name in athnames:
    ath[name]=sorted(repetidos(ath[name]), reverse = True)
    print ('Nombre: ', name, '\tTiempos: ', ath[name])
for name in athnames:
    print ('Los 3 mejores tiempos de: ', name, 'son: ', end='')
    y=0
    while y<3:
        if y<2:
            print (str(ath[name][y]), end=', ')
            y+=1
        else:
            print (str(ath[name][y]))
            y+=1
