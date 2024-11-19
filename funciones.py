import time
import msvcrt
import os
productos = []
producto = str
detalle1 = str
detalle2 = str
detalle4 = str
detalle3 = str
stock = int
precio = float
detproductos = ['Producto','detalle31','detalle32','detalle33','detalle34']

def run(): #Funcion que ejecuta el orden de las funciones en el inicio
    datos()
    newuser()
    informacion()
    demo()
    print(f"{"":>15}{'Bienvenidos a la app'}")
    print(f"{"":>15}{"===================="}")
    menu()

def test(): #lista DEMO donde agregamos automaticamente datos a la lista de producto como ejemplo
    obj0 = "Moto"
    obj1 = "Marca"
    obj2 = "tipo"
    obj3 = "color"
    obj4 = "Cilindrada"
    detproductos[0] = obj0
    detproductos[1] = obj1
    detproductos[2] = obj2
    detproductos[3] = obj3
    detproductos[4] = obj4
    producto = 'rx150'
    detalle1 = 'zanella'
    detalle2 = 'calle'
    detalle3 = 'roja'
    detalle4 = '150cc'
    stock = 10
    precio = 1200000
    productos.append([producto.upper(),detalle1, detalle2, detalle3, detalle4, stock, precio])
    producto = 'skua150'
    detalle1 = 'motomel'
    detalle2 = 'enduro'
    detalle3 = 'verde'
    detalle4 = '150cc'
    stock = 7
    precio = 1500000
    productos.append([producto.upper(),detalle1, detalle2, detalle3, detalle4, stock, precio])
    producto = 'cg150'
    detalle1 = 'honda'
    detalle2 = 'calle'
    detalle3 = 'negro'
    detalle4 = '150cc'
    stock = 24
    precio = 1800000
    productos.append([producto.upper(),detalle1, detalle2, detalle3, detalle4, stock, precio])
    producto = 'zr150'
    detalle1 = 'zanella'
    detalle2 = 'enduro'
    detalle3 = 'roja'
    detalle4 = '150cc'
    stock = 12
    precio = 1700000
    productos.append([producto.upper(),detalle1, detalle2, detalle3, detalle4, stock, precio])
    producto = 'skua250'
    detalle1 = 'motomel'
    detalle2 = 'enduro'
    detalle3 = 'roja'
    detalle4 = '250cc'
    stock = 7
    precio = 2500000
    productos.append([producto.upper(),detalle1, detalle2, detalle3, detalle4, stock, precio])
    producto = 'rx250'
    detalle1 = 'zanella'
    detalle2 = 'calle'
    detalle3 = 'roja'
    detalle4 = '250cc'
    stock = 12
    precio = 2200000
    productos.append([producto.upper(),detalle1, detalle2, detalle3, detalle4, stock, precio])
    producto = 'fz150'
    detalle1 = 'yamaha'
    detalle2 = 'naked'
    detalle3 = 'azul'
    detalle4 = '250cc'
    stock = 11
    precio = 3200000
    productos.append([producto.upper(),detalle1, detalle2, detalle3, detalle4, stock, precio])
    producto = 'fz25'
    detalle1 = 'yamaha'
    detalle2 = 'naked'
    detalle3 = 'negra'
    detalle4 = '250cc'
    stock = 16
    precio = 1800000
    productos.append([producto.upper(),detalle1, detalle2, detalle3, detalle4, stock, precio])
    producto = 'ns200'
    detalle1 = 'rouser'
    detalle2 = 'naked'
    detalle3 = 'negra'
    detalle4 = '200cc'
    stock = 16
    precio = 1640000
    productos.append([producto.upper(),detalle1, detalle2, detalle3, detalle4, stock, precio])
    producto = 'n250'
    detalle1 = 'rouser'
    detalle2 = 'naked'
    detalle3 = 'negra'
    detalle4 = '250cc'
    stock = 16
    precio = 2540000
    productos.append([producto.upper(),detalle1, detalle2, detalle3, detalle4, stock, precio])
    producto = 'rz25'
    detalle1 = 'zanella'
    detalle2 = 'naked'
    detalle3 = 'roja'
    detalle4 = '250cc'
    stock = 10
    precio = 2500000
    productos.append([producto.upper(),detalle1, detalle2, detalle3, detalle4, stock, precio])
    producto = 'cb1'
    detalle1 = 'honda'
    detalle2 = 'naked'
    detalle3 = 'negro'
    detalle4 = '150cc'
    stock = 24
    precio = 1950000
    productos.append([producto.upper(),detalle1, detalle2, detalle3, detalle4, stock, precio])
    producto = 'cbx'
    detalle1 = 'honda'
    detalle2 = 'naked'
    detalle3 = 'roja'
    detalle4 = '250cc'
    stock = 24
    precio = 2950000
    productos.append([producto.upper(),detalle1, detalle2, detalle3, detalle4, stock, precio])
    producto = 'xr150'
    detalle1 = 'honda'
    detalle2 = 'enduro'
    detalle3 = 'roja'
    detalle4 = '150cc'
    stock = 17
    precio = 1620000
    productos.append([producto.upper(),detalle1, detalle2, detalle3, detalle4, stock, precio])
    producto = 'ybr'
    detalle1 = 'yamaha'
    detalle2 = 'calle'
    detalle3 = 'azul'
    detalle4 = '150cc'
    stock = 12
    precio = 1930000
    productos.append([producto.upper(),detalle1, detalle2, detalle3, detalle4, stock, precio])
    producto = 'xr250'
    detalle1 = 'honda'
    detalle2 = 'enduro'
    detalle3 = 'roja'
    detalle4 = '250cc'
    stock = 17
    precio = 2730000
    productos.append([producto.upper(),detalle1, detalle2, detalle3, detalle4, stock, precio])
    producto = 'zt150'
    detalle1 = 'zanella'
    detalle2 = 'enduro'
    detalle3 = 'azul'
    detalle4 = '250cc'
    stock = 29
    precio = 2250000
    productos.append([producto.upper(),detalle1, detalle2, detalle3, detalle4, stock, precio])
    producto = 'xtz250'
    detalle1 = 'yamaha'
    detalle2 = 'naked'
    detalle3 = 'azul'
    detalle4 = '150cc'
    stock = 19
    precio = 2650000
    productos.append([producto.upper(),detalle1, detalle2, detalle3, detalle4, stock, precio])

def demo(): #Notificacion y consulta si deseamos la lista demo
    print("Bienvenido a mi aplicacion")
    print("Desea cargar una lista DEMO de productos o desea ingresar una nueva lista")
    while True: #validacion si es un numero para el menu
        try:
            demo = input('ingrese "Y" para cargar DEMO que es una lista de motocicletas o "N" para ingresar una nueva: ')
            print("")
            if demo.lower() == "y":
                test()
                print("Se ha cargado una lista DEMO de productos de motos con exito")
                break
            elif demo.lower() == "n":
                print("Ha elejido colocar sus propios productos a la app para registrarlos")
                print("a continuacion se le pedira los datos para poder registrarlos con mas detalle3s")
                print("le recordamos que mas adelante puede modificar estos mismos datos.")
                print("")
                detprod()
                break
            else:
                os.system('cls')
                print("¡Error! El digito ingresado es invalido")
        except ValueError:
            print("¡Error!")

def detprod():#Consula el nombre de las listas segun el elemento que deseamos agregar en la app
    obj0 = input("Ingrese el nombre del Elemento a registrar (Producto, libro, grupo musical, modelo etc): ")
    obj1 = input(f"Ingrese primera (1/4) informacion del {obj0} Ej marca, autor, artista, fabricante etc: ")
    obj2 = input(f"Ingrese segunda (2/4) informacion del {obj0} Ej tipo, genero etc: ")
    obj3 = input(f"Ingrese tercera (3/4) informacion del {obj0} Ej año, color, editorial, etc: ")
    obj4 = input(f"Ingrese cuarta (4/4) informacion del {obj0} Ej observaciones, vencimientos, otros: ")
    detproductos[0] = obj0
    detproductos[1] = obj1
    detproductos[2] = obj2
    detproductos[3] = obj3
    detproductos[4] = obj4

def newuser(): #crea un usuario contraseña
    global user
    global keypass
    user = input("Ingrese un nuevo usuario: ")
    keypass = input("Ingrese una contraseña: ")

def v_user(): #valida el usuario
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

def datos(): #Funcion para ingresar los datos de la empresa
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

def informacion(): #Muestra los datos de la empresa
    print("")
    print(f"Empresa: {empresa.upper()}")
    print(f"Cuit:  {cuit}")
    print(f"Direccion: {direccion.title()}")
    print(f"Telefono: {telefono}")
    print(f"E-mail: {email}")
    print("")

def menu(): #Menu Principal
    while True:
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
        print(f"{'':>10}|\t6\t| Reiniciar App\t|")
        print(f"{'':>10}|\t7\t| Edit Registro\t|")
        print(f"{'':>10}|\t8\t| Edit Empresa\t|")
        print(f"{'':>10}|\t9\t| Info Empresa\t|")
        print(f"{'':>10}|\t0\t| Salir\t\t|")
        print(f"{'':>10}|_____________________________|")
        print("")
        opcion = str(input("Eija un N° de Opcion: "))
        os.system("cls")
        if opcion <= '9' and opcion >= '0':
            match opcion:
                case '1':#Create
                    print("Registrar")
                    additemsinit()
                case '2':#Read
                    print("Buscar")
                    buscar()
                case '3':#Read
                    print("Lista")
                    list()
                case '4': #Update
                    os.system("cls")
                    v_user()
                    os.system("cls")
                    print("Actualizar")
                    print("")
                    tecla = "0"
                    while tecla != b'\x1b':
                        producto_a_buscar = input(f'Ingrese {detproductos[0]} que desee modificar: ')
                        for i, (bproducto,bdetalle1, bdetalle2, bdetalle4, bdetalle3, bstock, bprecio) in enumerate(productos):
                            if bproducto == producto_a_buscar.upper():
                                print("")
                                print(f"Su ID es: {i}")
                                print(f"{detproductos[0]} {bproducto}\t\t{detproductos[1]}: {bdetalle1}\t\t{detproductos[2]}: {bdetalle2}\t\t{detproductos[3]}: {bdetalle4}\t\t{detproductos[4]}: {bdetalle3}\t\tStock: {bstock}\t\tPrecio: ${bprecio}")
                                print("")
                                print(f"El ID a modificar es el {i}")
                                print('Toque "ENTER" para ingresar el ID a modificar o cualquiero otra tecla para salir')
                                tecla = msvcrt.getch()
                                if tecla == b'\r':
                                    modificar()
                                return i
                            else:
                                i = -1
                        if i == -1:
                            print("")
                            print(f"{detproductos[0]}: {producto_a_buscar} no se encontró.")
                            print("")
                            print('Toque cualquier tecla para volver a buscar')
                            print('Toque \"ESC\" para volver al menu de busqueda')
                            tecla = msvcrt.getch()
                case '5': #Delete
                    os.system("cls")
                    v_user()
                    os.system("cls")
                    tecla = "0"
                    while tecla != b'\x1b':
                        producto_a_buscar = input(f'Ingrese {detproductos[0]}: ')
                        for i, (bproducto,bdetalle1, bdetalle2, bdetalle4, bdetalle3, bstock, bprecio) in enumerate(productos):
                            if bproducto == producto_a_buscar.upper():
                                print("")
                                print(f"Su ID es: {i}")
                                print(f"{detproductos[0]} {bproducto}\t\t{detproductos[1]}: {bdetalle1}\t\t{detproductos[2]}: {bdetalle2}\t\t{detproductos[3]}: {bdetalle4}\t\t{detproductos[4]}: {bdetalle3}\t\tStock: {bstock}\t\tPrecio: ${bprecio}")
                                print("")
                                print('Toque "ENTER" para ingresar el ID eliminar o cualquiero otra tecla para salir')
                                tecla = msvcrt.getch()
                                if tecla == b'\r':
                                    eliminarprod()
                                return i
                            else:
                                i = -1
                        if i == -1:
                            print("")
                            print(f"{detproductos[0]}: {producto_a_buscar} no se encontró.")
                            print("")
                            print('Toque cualquier tecla para volver a buscar')
                            print('Toque \"ESC\" para volver al menu de busqueda')
                            tecla = msvcrt.getch()
                case '6':#DELETE GENERAL
                    os.system("cls")
                    v_user()
                    os.system("cls")
                    while True:
                        print('Ingrese "ENTER" para Confirmar o "ESC" para salir')
                        salir = msvcrt.getch()
                        if salir == b'\x1b':
                            print('Operacion cancelada')
                            break
                        elif salir == b'\r':
                            productos.clear()
                            run()
                        else:
                            print('opcion invalida toque "ENTER" para CONFIRMAR o "ESC" para salir')
                            continue
                        break
                case '7':
                    os.system("cls")
                    v_user()
                    os.system("cls")
                    print("")
                    detprod()
                case '8':
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
        else:
            print("Opcion invalida elija un numero del 0 al 9")

def editdts(): #Menu para editar datos de la empresa
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

def additemsinit(): #Agrega un nuevo producto a la lista
    producto = input(f'Ingrese {detproductos[0]}: ')
    detalle1 = input(f'Ingrese {detproductos[1]}: ')
    detalle2 = input(f'Ingrese {detproductos[2]}: ')
    detalle4 = input(f'Ingrese {detproductos[3]}: ')
    detalle3 = input(f'Ingrese {detproductos[4]}: ')
    while True: #consulta y valida el Stock si es un INT
        try:
            stock = int(input(f'Ingrese el stock de {producto}: '))
            break
        except ValueError:
            print("¡Error! Ingrese un número válido.")
    while True: #consulta y valida el Valor si es un float
        try:
            precio = float(input(f'Ingrese el precio x unidad de {producto}: '))
            break 
        except ValueError:
            print("¡Error! Ingrese un número válido.")
    productos.append([producto.upper(),detalle1.lower(), detalle2.lower(), detalle3.lower(), detalle4.lower(), stock, precio])
    print("")
    print(f"Se ha guardado ID:{len(productos)-1} {detproductos[0]}: {producto} \t {detproductos[1]}: {detalle1} \t {detproductos[2]}: {detalle2} \t {detproductos[3]}: {detalle4} \t {detproductos[4]}: {detalle3} \t Stock: {stock} \t Precio: ${precio}" )
    print("")
    while True: #Consulta y valida si deseamos agregar otro objeto o si deseamos ya iniciar el menu
        print(f'Ingrese "ENTER" para agregar un {productos[0]} o "ESC" para salir')
        salir = msvcrt.getch()
        if salir == b'\x1b':
            print('Su inventario a sido guardado con exito')
            break
        elif salir == b'\r':
            additemsinit()
        else:
            print(f'Opcion invalida toque "ENTER" para ingresar un {productos[0]} o "ESC" para salir')
            continue
        break

def modificar(): #Ingresando el ID de la lista modifica el producto dentro de la misma
    while True: #Consulta y valida si es un INT el ID del objeto que deseamos modificar
        try:
            identi = int(input(f"Ingrese el numero de ID del {detproductos[0]} "))
            print("")
            if identi <= len(productos):
                break
            else:
                print("¡ID inexistente! ingrese un ID Valido")
                print("")
        except ValueError:
            print("¡Error! Ingrese un numero valido.")
    m_producto = input(f"Ingrese {detproductos[0]}: ")
    m_detalle1 = input(f"Ingrese {detproductos[1]}: ")
    m_detalle2  = input(f"Ingrese {detproductos[2]}: ")
    m_detalle3 = input(f"Ingrese {detproductos[3]}: ")
    m_detalle4 = input(f"Ingrese {detproductos[4]}: ")
    while True: #consulta y valida el Stock si es un INT
        try:
            m_stock = int(input(f'Ingrese el stock de {detproductos[0]}: '))
            break
        except ValueError:
            print("¡Error! Ingrese un número válido.")
    while True: #consulta y valida el Valor si es un float
        try:
            m_precio = float(input(f'Ingrese el precio x unidad de {detproductos[0]}: '))
            break 
        except ValueError:
            print("¡Error! Ingrese un número válido.")
    productos[identi] = [m_producto,m_detalle1,m_detalle2,m_detalle3,m_detalle4,m_stock,m_precio]
    print(f"{detproductos[0]}: {m_producto} \t {detproductos[1]}: {m_detalle1} \t {detproductos[2]}: {m_detalle2} \t {detproductos[3]}: {m_detalle3} \t {detproductos[4]}: {m_detalle4} \t Stock: {m_stock} \t Precio: {m_precio}")
    print("")
    print("Toque una tecla para regresar al menu")
    msvcrt.getch()
    os.system("cls")
    menu()

def eliminarprod(): #Funcion ingresando el ID elimina el producto de la lista
    while True: #Consulta y valida si es un INT el ID del objeto que deseamos Eliminar
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
    print(f"{detproductos[0]}: {productos[identi]} ha sido eliminado de la lista")
    print("")
    productos.pop(identi)
    print("Toque una tecla para regresar al menu")
    msvcrt.getch()
    os.system("cls")
    menu()

def list(): #Imprime todos los producto de la lista
    for i, producto in enumerate(productos):
        print(f'ID: {i}\t {detproductos[0]}: {producto[0]}   \t\t{detproductos[1]}: {producto[1]}\t\t{detproductos[2]}: {producto[2]}\t\t{detproductos[3]}: {producto[3]}\t\t{detproductos[4]}: {producto[4]}\t\tStock: {producto[5]}\t\tPrecio: ${producto[6]}')
        print("")
    
    print("Para regresar toque una tecla")
    msvcrt.getch()
    os.system("cls")
    menu()

def buscar(): #Busca dentro de la lista el producto especifico
    print("")
    print("Desea buscar por: ")
    print("")
    print(f"1. {detproductos[0]}.")
    print(f"2. {detproductos[1]}.")
    print(f"3. {detproductos[2]}.")
    print(f"4. {detproductos[3]}.")
    print(f"5. {detproductos[4]}.")
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
                producto_a_buscar = input(f'Ingrese el nombre del {detproductos[0]}: ')
                for i, (bproducto,bdetalle1, bdetalle2, bdetalle4, bdetalle3, bstock, bprecio) in enumerate(productos):
                    if bproducto == producto_a_buscar.upper():
                        print("")
                        print(f"{detproductos[0]} {bproducto}\t\t{detproductos[1]}: {bdetalle1}\t\t{detproductos[2]}: {bdetalle2}\t\t{detproductos[3]}: {bdetalle4}\t\t{detproductos[4]}: {bdetalle3}\t\tStock: {bstock}\t\tPrecio: ${bprecio}")
                        return i
                    else:
                        i = -1
                try:
                    if i == -1:
                        print("")
                        print(f"El {detproductos[0]} {producto_a_buscar} no se encontró.")
                        print("")
                        print('Toque cualquier tecla para volver a buscar')
                        print('Toque \"ESC\" para volver al menu de busqueda')
                        tecla = msvcrt.getch()
                    else:
                        break
                except UnboundLocalError:
                    print("No hay datos en la base de datos")
                    break
        case 2: #busca por detalle1
            tecla = "0"
            y = 0
            while tecla != b'\x1b':
                producto_a_buscar = input(f'Ingrese la {detproductos[1]}: ')
                for i, (bproducto, bdetalle1, bdetalle2, bdetalle4, bdetalle3, bstock, bprecio) in enumerate(productos):
                    if bdetalle1 == producto_a_buscar.lower():
                        print("")
                        print(f"{detproductos[0]} {bproducto}\t\t{detproductos[1]}: {bdetalle1}\t\t{detproductos[2]}: {bdetalle2}\t\t{detproductos[3]}: {bdetalle4}\t\t{detproductos[4]}: {bdetalle3}\t\tStock: {bstock}\t\tPrecio: ${bprecio}")
                        y = 1
                    else:
                        i = -1
                try:
                    if y == 0 and i == -1:
                        print("")
                        print(f"{detproductos[1]} {producto_a_buscar} no se encontró.")
                        print("")
                        print('Toque cualquier tecla para volver a buscar ')
                        print('Toque \"ESC\" para volver al menu principal')
                        tecla = msvcrt.getch()
                    else:
                        break
                except UnboundLocalError:
                    print("No hay datos en la base de datos")   
                    break             
        case 3: #busca por detalle2
            tecla = "0"
            y = 0
            while tecla != b'\x1b':
                producto_a_buscar = input(f'Ingrese {detproductos[2]}: ')
                for i, (bproducto,bdetalle1, bdetalle2, bdetalle4, bdetalle3, bstock, bprecio) in enumerate(productos):
                    if bdetalle2 == producto_a_buscar.lower():
                        print("")
                        print(f"{detproductos[0]} {bproducto}\t\t{detproductos[1]}: {bdetalle1}\t\t{detproductos[2]}: {bdetalle2}\t\t{detproductos[3]}: {bdetalle4}\t\t{detproductos[4]}: {bdetalle3}\t\tStock: {bstock}\t\tPrecio: ${bprecio}")
                        y = 1
                    else:
                        i = -1
                try:
                    if y == 0 and i == -1:
                        print("")
                        print(f"{detproductos[2]} {producto_a_buscar} no se encontró.")
                        print("")
                        print('Toque cualquier tecla para volver a buscar ')
                        print('Toque \"ESC\" para volver al menu principal')
                        tecla = msvcrt.getch()
                    else:
                        break
                except UnboundLocalError:
                    print("No hay datos en la base de datos") 
                    break   
        case 4: #busca por detalle3
            tecla = "0"
            y = 0
            while tecla != b'\x1b':
                producto_a_buscar = input(f'Ingrese el {detproductos[3]}: ')
                for i, (bproducto,bdetalle1, bdetalle2, bdetalle4, bdetalle3, bstock, bprecio) in enumerate(productos):
                    if bdetalle4 == producto_a_buscar.lower():
                        print("")
                        print(f"{detproductos[0]} {bproducto}\t\t{detproductos[1]}: {bdetalle1}\t\t{detproductos[2]}: {bdetalle2}\t\t{detproductos[3]}: {bdetalle4}\t\t{detproductos[4]}: {bdetalle3}\t\tStock: {bstock}\t\tPrecio: ${bprecio}")
                        y = 1
                    else:
                        i = -1
                try:
                    if y == 0 and i == -1:
                        print("")
                        print(f"{detproductos[3]} {producto_a_buscar} no se encontró.")
                        print("")
                        print('Toque cualquier tecla para volver a buscar ')
                        print('Toque \"ESC\" para volver al menu principal')
                        tecla = msvcrt.getch()
                    else:
                        break
                except UnboundLocalError:
                    print("No hay datos en la base de datos") 
                    break   
        case 5: #busca por obserbaciones
            tecla = "0"
            y = 0
            while tecla != b'\x1b':
                producto_a_buscar = input(f'Ingrese el {detproductos[4]}: ')
                for i, (bproducto,bdetalle1, bdetalle2, bdetalle4, bdetalle3, bstock, bprecio) in enumerate(productos):
                    if bdetalle3 == producto_a_buscar.lower():
                        print("")
                        print(f"{detproductos[0]} {bproducto}\t\t{detproductos[1]}: {bdetalle1}\t\t{detproductos[2]}: {bdetalle2}\t\t{detproductos[3]}: {bdetalle4}\t\t{detproductos[4]}: {bdetalle3}\t\tStock: {bstock}\t\tPrecio: ${bprecio}")
                        y = 1
                    else:
                        i = -1
                try:
                    if y == 0 and i == -1:
                        print("")
                        print(f"{detproductos[4]} {producto_a_buscar} no se encontró.")
                        print("")
                        print('Toque cualquier tecla para volver a buscar ')
                        print('Toque \"ESC\" para volver al menu principal')
                        tecla = msvcrt.getch()
                    else:
                        break
                except UnboundLocalError:
                    print("No hay datos en la base de datos") 
                    break   
        case 6: #ejecuta la funcion menu para volver atras
            menu()

run()