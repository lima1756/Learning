"""Este codigo imprime cada item dentro una lista, imprimiendo a su vez, cada item de listas que se encuentren anidadas"""
import sys
def repetir(x, opc=False, outfile=sys.stdout, ind=-1):
    #x es la lista que se lee, si x es una lista pasa al for el cual manda a llamar a la funcion
    #opc permite indentar los resultados si es true, en caso de no especificarlo no se indenta
	#outfile se refiere en donde se mostrara los datos de la lista, en caso de no poner ningun archivo se imprimen en la ventana de consola por defecto
    #ind establece el nivel que se indentara algo, (iniciando desde el primer nivel).
    if isinstance(x,list):
        for elemento in x:
            repetir(elemento, opc, outfile, ind+1)
    #En caso de que no sea una lista el elemento, se imprime
    else:
        if opc:
            for tab in range(ind):
                print ("\t", end='', file=outfile)
        print (str(x), file=outfile)