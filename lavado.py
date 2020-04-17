#veces a repetir
registros = int(input("Cuantos registros desea hacer ? "))

#menu de opciones
menu = """
MENÚ
-----------Opciones-------------
Motocicleta Q 15.00
Automovil   Q 30.00
Camion      Q 50.00
"""
# agregar los precios
print(menu)
for n in range(registros):
#se selecciona al tipo de vehiculo
    vehiculo = str(input('Que tipo de vehiculo es: '))
#condicional de opciones
#---------------------------------------------------------------------
#para vehiculos
    if vehiculo == vehiculo:
        print(" ",vehiculo , " ")
        precio = float(input('Ingrese precio: '))
        cliente = str(input('Que tipo de cliente es: '))
        print(cliente)
#---------------------------------------------------------------------

#pregunta si el cliente es miembro
        if cliente == 'miembro':
            precio_desc = precio + precio * 0.10
#---------------------------------------------------------------------
# fin de semana
        finde = str(input('Es fin de semana? '))
    if finde == "no":
        precio_finde = precio + precio * 0.10
        #descuento = precio + precio_desc

        #desc_miembro = descuento + precio_finde
        print("Tipo de cliente: ", cliente) # separar esto
        print("Total: ", precio)
        print("Total gastado: ", precio_finde)
    else:
        print("El cliente es: ", cliente)
        print("Cantidad gastada: ", precio)
       # print("TOTAL: ", desc_miembro)
"" 

"" 
if finde == "si":
    precio_descontado = precio 
    print("Tipo de cliente: ", cliente) # separar esto
    print("Total: ", precio)

"" 

""
#---------------------------------------------------------------------
#---------------------------------------------------------------------    

