import os 
from collections import deque
contador = 1
lista = []
cola = deque()
lista.insert(0,"cancelar") 
opciones = 1
while opciones == 1 or opciones == 2 :
    print('desea?')
    print('1) agregar un elemento a la cola de imprecion')
    print('2)imprimir')
    print('3)salir')
    opciones=int(input())
    #agregar elemento
    if opciones == 1:
        print('se detectaron estos archivos dentro de la carpeta:')
        for carp in os.listdir('carpeta'):
            ruta = os.path.join('carpeta',carp)
            archivos_pri = f'{contador}  {carp}'
            print('   ',archivos_pri)
            
            lista.append(archivos_pri)
            contador = contador + 1 
        print('    0  cancelar')
        elemento = int(input('que archivo desea agregar a la cola:''\n'))
        if elemento >0:
            print('usted a seleccionado:')
            print(lista[elemento])
            cola.append(lista[elemento])
    #imprimir    
    elif opciones == 2:
        while len(cola) > 0:
            siguiente_elemento = cola.popleft()
            print(f'siguiente_elemento:' )
            print(siguiente_elemento)
            print(cola)
            print('++++++++++++++++++++++++++++++++++++++++++')
    #salir    
    elif opciones == 3:
        print('eligio salir')
    else:
        print('opcion no encontrada')   
