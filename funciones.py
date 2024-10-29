import time
import msvcrt
import os
productos = []
producto = str
marca = str
tipo = str
observaciones = str
detalle = str
stock = int
precio = float

def app_search():
    print("")
    print("Que es lo que desea buscar: ")
    print("1. Cliente")
    print("2. Empleado")
    print("3. Producto")
    print("4 Volver al menu principal")
    print("")
    search_opt = input("Elja el Nº de la opcion deseada: ")
    os.system("cls")
    if search_opt <= '4' and search_opt >= '0':
        match search_opt:
            case '1':
                print("cliente")
            case '2':
                print("Empleado")
            case '3':
                print("Producto")
            case '4':
                os.system("cls")
                menu()
    else:
        print("Opcion invalida elija un numero del 0 al 4")
        app_search()

def newuser():
    global user
    global keypass
    user = input("Ingrese un nuevo usuario: ")
    keypass = input("Ingrese una contraseña: ")

def v_user():
    while True:
        usuario = input("Usuario: ")
        if usuario != user:
            print("Usuario Invalido")
            continue
        while True:
            password = input("Contraseña: ")
            if password != keypass:
                print("Contraseña Invalida")
                continue
            break
        break
    print("Usuario Valido!")

def m_user():
    global user
    while True:
        usuario = input("Usuario: ")
        if usuario != user:
            print("Usuario Invalido")
            continue
        user = input("Ingrese un nuevo usuario: ")
        print("Has modificado el usuario con exito")
        print("")
        print("Para regresar toque una tecla")
        msvcrt.getch()
        os.system("cls")
        editdts()
        break
def m_pass():
    global keypass
    while True:
        password = input("Contraseña: ")
        if password != keypass:
            print("Contraseña Invalida")
            continue
        keypass = input("Ingrese una nueva contraseña")
        print("Has modificado la contraseña con exito")
        print("")
        print("Para regresar toque una tecla")
        msvcrt.getch()
        os.system("cls")
        editdts()
        break

def datos():
    global empresa
    global cuit
    global direccion
    global telefono
    global email
    empresa = input("Ingrese el nombre de la empresa: ")
    cuit = input('Ingrese el numero de cuit de la empresa: ')
    direccion = input("Ingrese la direccion de la empresa: ")
    telefono = input("Ingrese el telefono de la empresa: ")
    email = input('Ingrese el e-mail de la empresa: ')
    os.system("cls")

def informacion():
    print("")
    print(f"Empresa: {empresa.upper()}")
    print(f"Cuit:  {cuit}")
    print(f"Direccion: {direccion.title()}")
    print(f"Telefono: {telefono}")
    print(f"E-mail: {email}")
    print("")
#puedo modificar el menu con esdigital() para tener un 'int' en vez de un 'str'
def menu():
    print("")
    print(f"{'':>10} _____________________________")
    print(f"{'':>10}|\t\t       \t\t|")
    print(f"{'':>10}|\t      Menu   \t\t|")
    print(f"{'':>10}|_____________________________|")
    print(f"{'':>10}|   Opcion\t|  Descripcion\t|")
    print(f"{'':>10}|-----------------------------|")
    print(f"{'':>10}|\t1\t| Registrar\t|")
    print(f"{'':>10}|\t2\t| Buscar\t|")
    print(f"{'':>10}|\t3\t| Lista\t\t|")
    print(f"{'':>10}|\t4\t| Actualizar\t|")
    print(f"{'':>10}|\t5\t| Eliminar\t|")
    print(f"{'':>10}|\t6\t| Reportes\t|")
    print(f"{'':>10}|\t7\t| Edit Empresa\t|")
    print(f"{'':>10}|\t9\t| Info Empresa\t|")
    print(f"{'':>10}|\t0\t| Salir\t\t|")
    print(f"{'':>10}|_____________________________|")
    print("")
    opcion = str(input("Eija un N° de Opcion: "))
    os.system("cls")
    if opcion <= '9' and opcion >= '0':
        match opcion:
            case '1':
                print("Registrar")
                additemsinit()
            case '2':
                print("Buscar")
                buscar()
            case '3':
                print("Lista")
                list()
            case '4':
                os.system("cls")
                v_user()
                os.system("cls")
                print("Actualizar")
                edititems()
            case '5': #eliminar
                os.system("cls")
                v_user()
                os.system("cls")
                popitems()
            case '6':
                print("Reporte")
            case '7':
                os.system("cls")
                v_user()
                os.system("cls")
                editdts()
            case '9':
                informacion()
            case '0':
                print("")
                print("Gracias, que tenga un buen dia")
                time.sleep(2)
                exit()
        print("")
        print("Para regresar toque una tecla")
        msvcrt.getch()
        os.system("cls")
        menu()
    else:
        print("Opcion invalida elija un numero del 0 al 9")
        menu()

def editdts():
    global empresa
    global cuit
    global direccion
    global telefono
    global email
    
    print("")
    print("Que datos desea modificar:")
    print("1. Empresa")
    print("2. Cuit")
    print("3. Direccion")
    print("4. Telefono")
    print("5. Email")
    print("6. Modificar Usuario")
    print("7. Modificar Contraseña")
    print("8. Volver al menu principal")
    print("")
    opcions = str(input("Escriba el numero da la opcion: "))
    os.system("cls")
    if opcions <= '8' and opcions >= '0':
        match opcions:
            case '1':
                print("")
                empresa = input("Escriba el nuevo nombre de la empresa: ")
                print(f"El nuevo nombre de la empresa es: {empresa}")
                print("")
                print("Para regresar toque una tecla")
                msvcrt.getch()
                os.system("cls")
                editdts()
            case '2':
                print("")
                cuit = input("Escriba el nuevo cuit de la empresa: ")
                print(f"El nuevo cuit de la empresa es: {cuit}")
                print("")
                print("Para regresar toque una tecla")
                msvcrt.getch()
                os.system("cls")
                editdts()
            case '3':
                print("")
                direccion = input("Escriba la nueva direccion de la empresa: ")
                print(f"La nueva direccion de la empresa es: {direccion}")
                print("")
                print("Para regresar toque una tecla")
                msvcrt.getch()
                os.system("cls")
                editdts()
            case '4':
                print("")
                telefono = input("Escriba el nuevo numero de telefono de la empresa: ")
                print(f"El nuevo telefono de la empresa es: {telefono}")
                print("")
                print("Para regresar toque una tecla")
                msvcrt.getch()
                os.system("cls")
                editdts()
            case '5':
                print("")
                email = input("Escriba el nuevo E-mail de la empresa: ")
                print(f"El nuevo E-mail de la empresa es: {email}")
                print("")
                print("Para regresar toque una tecla")
                msvcrt.getch()
                os.system("cls")
                editdts()
            case '6':
                m_user()
            case '7':
                m_pass()
            case '8':
                os.system("cls")
                menu()
    else:
        print("Opcion invalida elija un numero del 1 al 6")
        editdts()   

#DE ACA PARA ABAJO ES DEL CODIGO 1.0

def additemsinit(): #Agrega un nuevo producto a la lista
    producto = input('Ingrese el nombre del producto: ')
    marca = input('Ingrese el nombre del marca: ')
    tipo = input('Ingrese el nombre del tipo: ')
    cilindrada = input('Ingrese el nombre del cilindrada: ')
    detalle = input('Ingrese el nombre del color: ')
    while True:
        try:
            stock = int(input(f'Ingrese el stock de {producto}: '))
            break
        except ValueError:
            print("¡Error! Ingrese un número válido.")
    while True:
        try:
            precio = float(input(f'Ingrese el precio x unidad de {producto}: '))
            break 
        except ValueError:
            print("¡Error! Ingrese un número válido.")
    productos.append([producto,marca, tipo, detalle, cilindrada, stock, precio])
    print(productos)
    while True:
        print('Ingrese enter para agregar un producto o esc para salir')
        salir = msvcrt.getch()
        if salir == b'\x1b':
            print('Su inventario a sido guardado con exito')
            break
        elif salir == b'\r':
            additemsinit()
        else:
            print('opcion invalida toque enter para ingresar un nuevo producto o esc para salir')
            continue
        break

def modificar(): #Ingresando el ID de la lista modifica el producto dentro de la misma
    while True:
        try:
            identi = int(input("Ingrese el numero de ID del producto "))
            print("")
            if identi <= len(productos):
                break
            else:
                print("¡ID inexistente! ingrese un ID Valido")
                print("")
        except ValueError:
            print("¡Error! Ingrese un numero valido.")
    m_producto = input("Ingrese su nuevo nombre de producto: ")
    m_marca = input("Ingrese la nueva marca de producto: ")
    m_tipo  = input("Ingrese su nuevo tipo: ")
    m_detalle = input("Ingrese su nuevo detalle: ")
    m_observaciones = input("Ingrese la cilindrada: ")
    m_stock = input("Ingrese el nuevo stock: ")
    m_precio = input("Ingrese el nuevo precio: ")
    productos[identi] = [m_producto,m_marca,m_tipo,m_detalle,m_observaciones,m_stock,m_precio]

def edititems(): #funcion busca el ID y lo envia a la funcion modificar
    tecla = "0"
    while tecla != b'\x1b':
        producto_a_buscar = input('Ingrese el nombre del producto: ')
        for i, (bproducto,bmarca, btipo, bdetalle, bobservaciones, bstock, bprecio) in enumerate(productos):
            if bproducto == producto_a_buscar.lower():
                print("")
                print(f"Su ID es: {i}")
                print(f"Producto {bproducto}\t\tMarca: {bmarca}\t\tTipo: {btipo}\t\tDetalle: {bdetalle}\t\tCilindrada: {bobservaciones}\t\tStock: {bstock}\t\tPrecio: ${bprecio}")
                print("")
                print('Toque "ENTER" identificar el producto a modificar o cualquiero otra tecla para salir')
                tecla = msvcrt.getch()
                if tecla == b'\r':
                    modificar()
                return i
            else:
                i = -1
        if i == -1:
            print("")
            print(f"El producto {producto_a_buscar} no se encontró.")
            print("")
            print('Toque cualquier tecla para volver a buscar')
            print('Toque \"ESC\" para volver al menu de busqueda')
            tecla = msvcrt.getch()

def eliminarprod(): #Funcion ingresando el ID elimina el producto de la lista
    while True:
        try:
            identi = int(input("Ingrese el numero de ID del producto "))
            print("")
            if identi <= len(productos):
                break
            else:
                print("¡ID inexistente! ingrese un ID Valido")
                print("")
        except ValueError:
            print("¡Error! Ingrese un numero valido.")
    print("")
    print(f"El Producto: {productos[identi]} ha sido eliminado de la lista")
    print("")
    productos.pop(identi)

def popitems(): #funcion busca el ID y lo envia a la funcion eliminarprod
    tecla = "0"
    while tecla != b'\x1b':
        producto_a_buscar = input('Ingrese el nombre del producto: ')
        for i, (bproducto,bmarca, btipo, bdetalle, bobservaciones, bstock, bprecio) in enumerate(productos):
            if bproducto == producto_a_buscar.lower():
                print("")
                print(f"Su ID es: {i}")
                print(f"Producto {bproducto}\t\tMarca: {bmarca}\t\tTipo: {btipo}\t\tDetalle: {bdetalle}\t\tCilindrada: {bobservaciones}\t\tStock: {bstock}\t\tPrecio: ${bprecio}")
                print("")
                print('Toque "ENTER" identificar el producto a eliminar o cualquiero otra tecla para salir')
                tecla = msvcrt.getch()
                if tecla == b'\r':
                    eliminarprod()
                return i
            else:
                i = -1
        if i == -1:
            print("")
            print(f"El producto {producto_a_buscar} no se encontró.")
            print("")
            print('Toque cualquier tecla para volver a buscar')
            print('Toque \"ESC\" para volver al menu de busqueda')
            tecla = msvcrt.getch()

def list(): #Imprime todos los producto de la lista
    for i, producto in enumerate(productos):
        print(f'ID: {i}\t Producto: {producto[0]}   \t\tMarca: {producto[1]}\t\tTipo: {producto[2]}\t\tCilindrada: {producto[4]}\t\tColor: {producto[3]}\t\tStock: {producto[5]}\t\tPrecio: ${producto[6]}')
        print("")
    
    print("Para regresar toque una tecla")
    msvcrt.getch()
    os.system("cls")
    menu()

def buscar(): #Busca dentro de la lista el producto especifico
    print("")
    print("Desea buscar por: ")
    print("")
    print("1. Nombre del producto.")
    print("2. Marca del producto.")
    print("3. Tipo de producto.")
    print("4. Detalle del producto")
    print("5. Cilindrada")
    print("6. Salir al Menu")
    print("")
    while True: #validacion si es un numero para el menu
        try:
            bopc = int(input("ingrese el numero de la opcion: "))
            print("")
            if bopc <= 6 and bopc >= 1:
                break
            else:
                print("¡Opcion invalida! ingrese un numero del 1 al 6")
                print("")
        except ValueError:
            print("¡Error! Ingrese un numero valido.")
    match bopc: #Menu  de opciones
        case 1: #busca por producto
            tecla = "0"
            while tecla != b'\x1b':
                producto_a_buscar = input('Ingrese el nombre del producto: ')
                for i, (bproducto,bmarca, btipo, bdetalle, bobservaciones, bstock, bprecio) in enumerate(productos):
                    if bproducto == producto_a_buscar.lower():
                        print("")
                        print(f"Producto {bproducto}\t\tMarca: {bmarca}\t\tTipo: {btipo}\t\tDetalle: {bdetalle}\t\tCilindrada: {bobservaciones}\t\tStock: {bstock}\t\tPrecio: ${bprecio}")
                        return i
                    else:
                        i = -1
                if i == -1:
                    print("")
                    print(f"El producto {producto_a_buscar} no se encontró.")
                    print("")
                    print('Toque cualquier tecla para volver a buscar')
                    print('Toque \"ESC\" para volver al menu de busqueda')
                    tecla = msvcrt.getch()
            buscar()
        case 2: #busca por marca
            tecla = "0"
            y = 0
            while tecla != b'\x1b':
                producto_a_buscar = input('Ingrese la marca: ')
                for i, (bproducto, bmarca, btipo, bdetalle, bobservaciones, bstock, bprecio) in enumerate(productos):
                    if bmarca == producto_a_buscar.lower():
                        print("")
                        print(f"Producto {bproducto}\t\tMarca: {bmarca}\t\tTipo: {btipo}\t\tDetalle: {bdetalle}\t\tCilindrada: {bobservaciones}\t\tStock: {bstock}\t\tPrecio: ${bprecio}")
                        y = 1
                    else:
                        i = -1
                if y == 0 and i == -1:
                    print("")
                    print(f"La marca {producto_a_buscar} no se encontró.")
                    print("")
                    print('Toque cualquier tecla para volver a buscar ')
                    print('Toque \"ESC\" para volver al menu principal')
                    tecla = msvcrt.getch()
                else:
                    break
                buscar()                
        case 3: #busca por tipo
            tecla = "0"
            y = 0
            while tecla != b'\x1b':
                producto_a_buscar = input('Ingrese el tipo: ')
                for i, (bproducto,bmarca, btipo, bdetalle, bobservaciones, bstock, bprecio) in enumerate(productos):
                    if btipo == producto_a_buscar.lower():
                        print("")
                        print(f"Producto {bproducto}\t\tMarca: {bmarca}\t\tTipo: {btipo}\t\tDetalle: {bdetalle}\t\tCilindrada: {bobservaciones}\t\tStock: {bstock}\t\tPrecio: ${bprecio}")
                        y = 1
                    else:
                        i = -1
                if y == 0 and i == -1:
                    print("")
                    print(f"La marca {producto_a_buscar} no se encontró.")
                    print("")
                    print('Toque cualquier tecla para volver a buscar ')
                    print('Toque \"ESC\" para volver al menu principal')
                    tecla = msvcrt.getch()
                else:
                    break
        case 4: #busca por detalle
            tecla = "0"
            y = 0
            while tecla != b'\x1b':
                producto_a_buscar = input('Ingrese el detalle: ')
                for i, (bproducto,bmarca, btipo, bdetalle, bobservaciones, bstock, bprecio) in enumerate(productos):
                    if bdetalle == producto_a_buscar.lower():
                        print("")
                        print(f"Producto {bproducto}\t\tMarca: {bmarca}\t\tTipo: {btipo}\t\tDetalle: {bdetalle}\t\tCilindrada: {bobservaciones}\t\tStock: {bstock}\t\tPrecio: ${bprecio}")
                        y = 1
                    else:
                        i = -1
                if y == 0 and i == -1:
                    print("")
                    print(f"El detalle: {producto_a_buscar} no se encontró.")
                    print("")
                    print('Toque cualquier tecla para volver a buscar ')
                    print('Toque \"ESC\" para volver al menu principal')
                    tecla = msvcrt.getch()
                else:
                    break
        case 5: #busca por obserbaciones
            tecla = "0"
            y = 0
            while tecla != b'\x1b':
                producto_a_buscar = input('Ingrese el cilindrada: ')
                for i, (bproducto,bmarca, btipo, bdetalle, bobservaciones, bstock, bprecio) in enumerate(productos):
                    if bobservaciones == producto_a_buscar.lower():
                        print("")
                        print(f"Producto {bproducto}\t\tMarca: {bmarca}\t\tTipo: {btipo}\t\tDetalle: {bdetalle}\t\tCilindrada: {bobservaciones}\t\tStock: {bstock}\t\tPrecio: ${bprecio}")
                        y = 1
                    else:
                        i = -1
                if y == 0 and i == -1:
                    print("")
                    print(f"La Cilindrada: {producto_a_buscar} no se encontró.")
                    print("")
                    print('Toque cualquier tecla para volver a buscar ')
                    print('Toque \"ESC\" para volver al menu principal')
                    tecla = msvcrt.getch()
                else:
                    break
        case 6: #ejecuta la funcion menu para volver atras
            menu()