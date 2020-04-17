import _json

base_de_datos = []
registros = input('Veces que quieres repetir: ')

for n in range(registros):
    modo = {}

    print('Automovil', 'Precio: Q30.00')
    print('Motocicleta', 'Precio: Q15.00')
    print('Camión', 'Precio Q50.00')

    vehiculo = input('Que tipo de vehiculo es: ')
    precio = input('ingrese precio')
    print('Estandar')
    print('Miembro')
    tipo_cliente = input('ingrese clase de cliente')
    finde = input('Es fin de semana ?')

    if tipo_cliente == 'miembro':
        precio_desc = (precio(precio * 0.10))

        #--------------------------------
    if finde == 'no':
        precio_finde = precio - precio_desc
        print('Tipo de cliente')
        print(tipo_cliente)
        print('Total: ', '', precio)
        print(precio_desc)
        if finde == 'si':
            print('Tipo de cliente')
            print(tipo_cliente)
            print('Total: ', '', precio)
            print(precio_desc)


    else:
        print(tipo_cliente)
        print(precio - 10)


print(base_de_datos)

with open('base_de_datos.json', 'w') as archivo:
    _json.dump(base_de_datos, archivo)
    print('Archivo exportado')


