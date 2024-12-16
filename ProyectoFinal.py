#                                                           Proyecto python 
#                                                  Programación Inicial con Python 
#                                                   Curso: 24216 | Martes | 19h.
#                                                       Alumno Oviedo Matias


import time
import msvcrt
import os
import sqlite3
from colorama import Fore, Back, Style, init 
init(autoreset=True)

conexion = sqlite3.connect('inventario.db') 
cursor = conexion.cursor()

def run(): #Funcion que ejecuta el orden de las funciones en el inicio
    crear_tabla_usuario()
    crear_tabla_informacion()
    crear_tabla_productos()
    cursor.execute("SELECT COUNT(*) FROM user")
    resultado = cursor.fetchone()[0]
    if resultado <= 0:
        newuser()
    cursor.execute("SELECT COUNT(*) FROM info")
    resultado = cursor.fetchone()[0]
    if resultado <= 0:
        datos()
    cursor.execute("SELECT COUNT(*) FROM productos")
    resultado = cursor.fetchone()[0]
    if resultado <= 0:
        demo()
    informacion()
    print(f"{"":>15}{'Bienvenidos a la app'}")
    print(f"{"":>15}{"===================="}")
    menu()

def insertar_Demo(): #funcion que almacena y crea un inventario de ejemplo para la programa
    db_demo = [
    ("YERBA", "Nobleza Gaucha 500 grs", 25, 1199.85, "Almacen"),
    ("GALLETITAS", "Mediatarde x3u 105grs", 46, 749.65, "Almacen"),
    ("CHOCLO", "Marolio Grano AmarilloLata x 300grs", 132, 899.75, "Almacen"),
    ("MAYONESA", "Molto 241Grs", 32, 549.25, "Almacen"),
    ("HARINA", "Cañuela 000 1 Kg.", 283, 519.41, "Almacen"),
    ("JUGO EN POLVO", "clight 20grs", 32, 229.78, "Almacen"),
    ("GASEOSA", "Pepsi Ligth 1,5Lts", 14, 1299.95, "Bebidas"),
    ("VINO", "Toro 750cc", 18, 1399.90, "Bebidas"),
    ("CHOCOLATADA", "Cindor Chocolate 1Lts", 192, 2249.43, "Bebidas"),
    ("CERVEZA", "Corona 710cc", 20, 519.74, "Bebidas"),
    ("JUGO", "Cepita 200cc", 54, 349.39, "Bebidas"),
    ("LAVANDINA", "AYUDIN 1 Lts", 26, 1399.58, "Art. Limpieza"),
    ("JABON PAN", "ESENCIAL 200Grs", 39, 679.85, "Art. Limpieza"),
    ("JABON EN POLVO", "SKIP 10 Kg.", 63, 22499.88, "Art. Limpieza"),
    ("PAPEL HIGENICO", "ESENCIAL x4Uni 50mt", 35, 599.49, "Art. Limpieza"),
    ("ROLLO DE COCINA", "SUSSEX x3Uni 50mt", 34, 1299.87, "Art. Limpieza"),
    ("ESPONJA", "De ACERO ESENCIAL1Uni 30 Gr", 35, 739.68, "Art. Limpieza"),
    ("INSECTICIDA", "RAID Aerosol 380cc", 12, 3729.68, "Art. Limpieza"),
    ("BOLSA DE RESIDUO", "60x100Cm 10Uni", 44, 1399.15, "Art. Limpieza"),
    ("MATECOCIDO", "Marolio x25saq", 21, 599.48, "Almacen"),
    ("TE", "La virginia x25saq", 18, 549.35, "Almacen"),
    ("SAL", "Celusal Fina", 25, 449.82, "Almacen"),
    ("PURE DE TOMATE", "Marolio T/B 520Grs", 186, 549.35, "Almacen"),
    ("FIDEO", "Molto Nid x500Grs", 16, 549.35, "Almacen"),
    ("ARROZ", "Marolio Largo Fino 500grs", 18, 679.35, "Almacen"),
    ("ACEITE", "Marolio Mezcla x900cc", 34, 1252.35, "Almacen")
    ]
    for prod in db_demo: #inicia un bule donde va almacenando a la base de datos cada producto registrado
        cursor.execute("""INSERT INTO productos(nombre, descripcion, cantidad, precio, categoria) VALUES (?,?,?,?,?)""", prod)
    conexion.commit() #guarda los cambios en la base de datos
    print(Fore.GREEN + "Productos DEMO añadidos")

def demo(): #Notificacion y consulta si deseamos una lista de productos en forma de ejemplo en el programa
    print(Back.CYAN+Style.BRIGHT+"                                                                         ")
    print(Back.CYAN+Style.BRIGHT+"                        Bienvenido a mi aplicacion                       ")
    print(Back.CYAN+Style.BRIGHT+"                                                                         ")
    print("")
    print("Desea cargar una lista DEMO de productos o desea ingresar una nueva lista")
    while True: #validacion si es un numero para el menu
        try:
            demo = input('ingrese '+Fore.GREEN+'"Y"'+Fore.WHITE+' para cargar DEMO que es una lista de motocicletas o '+Fore.GREEN+'"N"'+Fore.WHITE+' para ingresar una nueva: '+Fore.GREEN)
            print("")
            if demo.lower() == "y": #de ingresar por este if se dirije a la funcion "insertar_demo" y carga la lista de productos de ejemplificacion
                insertar_Demo()
                print(Fore.GREEN+"Se ha cargado una lista DEMO de productos de motos con exito")
                break
            elif demo.lower() == "n": #de ser igual por este elif continua corriendo por la linea de codigo sin ingresar a "insertar_demo"
                print(Fore.LIGHTCYAN_EX+"Ha elejido colocar sus propios productos a la app para registrarlos")
                print(Fore.LIGHTCYAN_EX+"a continuacion se le pedira los datos para poder registrarlos con mas detalle3s")
                print(Fore.LIGHTCYAN_EX+"le recordamos que mas adelante puede modificar estos mismos datos.")
                print("")
                break
            else: #de no ingresar a ninguna de sus dos opciones anteriores se le notifica q no ingreso correctamente la respuesta a la consulta
                os.system('cls')
                print("¡Error! El digito ingresado es invalido")
        except ValueError:
            print("¡Error!")

def crear_tabla_productos(): #linea de codigo para crear la base de datos "productos" y ejecuta crear la misma
    query = """CREATE TABLE "productos" (
                "id"	INTEGER NOT NULL UNIQUE,
                "nombre"	TEXT NOT NULL,
                "descripcion"	TEXT,
                "cantidad"	INTEGER NOT NULL,
                "precio"	REAL NOT NULL,
                "categoria"	TEXT,
                PRIMARY KEY("id" AUTOINCREMENT)
                )"""
                #Almacena la informacion en la base de datos de los productos de la empresa    
    try: 
        conexion.execute(query)
        print("se creó la db de productos")
    except sqlite3.OperationalError: # de estar creada nos avisa que exite
        print(Fore.RED +"Cargando la base de datos existente...")

def crear_tabla_usuario(): #linea de codigo para crear la base de datos "user" y ejecuta crear la misma
    query = """CREATE TABLE "user" (
                "id" INTEGER NOT NULL UNIQUE,
                "nombre" TEXT NOT NULL UNIQUE,
                "contraseña" TEXT,
                PRIMARY KEY("Id" AUTOINCREMENT)
                )"""
                #Almacena los datos las personas empleadas(Usuario/Contraseña) 
    try:
        conexion.execute(query)
        print("se creó la db de usuarios")
    except sqlite3.OperationalError:
        pass

def crear_tabla_informacion():#linea de codigo para crear la base de datos "info" y ejecuta crear la misma
    query = """CREATE TABLE "info" (
                "id"	INTEGER NOT NULL UNIQUE,
                "empresa"	TEXT NOT NULL DEFAULT 'Comercio',
                "cuit"	TEXT,
                "direccion"	TEXT,
                "telefono"	TEXT,
                "email"	TEXT,
                PRIMARY KEY("id" AUTOINCREMENT)
                )"""
                #Almacena la informacion dentro de la base de datos de la empresa/comercio 
    try:
        conexion.execute(query)
        print("se creó la db de informacion")
    except sqlite3.OperationalError:
        pass

def newuser(): #crea un usuario contraseña
    while True:
        print(Back.GREEN + Fore.RED + "               REGISTRAR NUEVO USUARIO               ")
        user = input("Ingrese un usuario: ") #Variable donde almaceno el nombre del usuario
        query = "SELECT * FROM user WHERE nombre = ?" #almaceno dentro de una variable la linea de codigo de sqlite para hacer la consulta
        cursor.execute(query, (user, )) #Ejecuto la linea de codigo almacenado dentro de query usando la variable "user" q contiene de dato un string
        vn_user = cursor.fetchone() #almaceno en la variable el resultado de la linea anterior de no tener datos guardara un "None"
        if vn_user == None: #De no tener resultados con datos en la base de datos ingresa al if
            keypass = input("Ingrese una contraseña: ")
            query = """INSERT INTO user(nombre, contraseña) VALUES (?,?)""" #almaceno linea de codigo de sqlite para insertar un dato a la base de datos llamada "info"
            cursor.execute(query, (user, keypass)) #ejecuto linea de codigo superior almacenando en la base de datos la variable user y la variable keypass
            conexion.commit() #guardo todos los cambios en la base de datos
            print("Registros añadidos")
            break #fuerzo a salir del bucle una vez terminado el if
        else: #de existir un usuario con el mismo nombre nos notifica q ya existe y repite el bucle
            print(Fore.RED +"El Usuario ya existe") 

def v_user(): #valida el usuario
    print("")
    print(Back.RED + Fore.BLUE + "               VALIDAR USUARIO               ")
    while True:
        usuario = input("Usuario: ") #Variable q almacena el string "Usuario" escrito por el cliente 
        password = input("Contraseña: ")#Variable q almacena el string "Contraseña" escrito por el cliente
        try:
            query = """SELECT nombre, contraseña FROM user WHERE nombre = ?"""  #almaceno dentro de una variable la linea de codigo de sqlite para hacer la consulta
            cursor.execute(query, (usuario, )) #Ejecuto la linea de codigo almacenado dentro de query usando la variable "usuario" q contiene de dato un string
            user = cursor.fetchone() #almaceno la informacion retornada de la funcion anterior
            nombre , contraseña = user #separo la informacion en dos variables
            if usuario == nombre and contraseña == password: #uso las dos variables para comparar lo que escribio es igual a lo que esta almacenado en la base de datos
                print(Fore.GREEN + "Datos Validos")
                break
            else: #si la clave es erronea va a mostras datos invalidos
                print(Fore.RED + "Datos invalidos")
        except TypeError: #si el usuario es invalido va a mostrar datos invalidos
            print("Datos Invalido")

def datos(): #Funcion para ingresar los datos de la empresa en distitas variables y almacenarlo en la base de datos
    empresa = input("Ingrese el nombre de la empresa: ")
    cuit = input('Ingrese el numero de cuit de la empresa: ')
    direccion = input("Ingrese la direccion de la empresa: ")
    telefono = input("Ingrese el telefono de la empresa: ")
    email = input('Ingrese el e-mail de la empresa: ')
    query = """INSERT INTO info(empresa, cuit, direccion, telefono, email) VALUES (?,?,?,?,?)""" #linea de codigo de sqlite para insertar la informacion a la table info de mi bd
    cursor.execute(query, (empresa, cuit, direccion, telefono, email))  #ejecuta linea de codigo anterior con las variables ya almacenadas  
    conexion.commit() #guarda los cambios
    print(Fore.GREEN +"Registros añadidos")
    os.system("cls")

def informacion(): #Muestra la informacion de la empresa
    try:
        query = "SELECT empresa, cuit, direccion, telefono, email FROM info" #almacena linea de codigo de sqlite haciendo una consulta
        cursor.execute(query) #ejecuta linea de codigo superior
        resultados = cursor.fetchone() #almacena la informacion recibida de la ejecucion
        if resultados: #de tener informacion ingresa al if mostrado los datos almacenados en varios prints
            empresa, cuit, direccion, telefono, email = resultados
            print(Fore.BLACK + Back.CYAN + Style.BRIGHT + f"                  Empresa: {empresa}                  ")
            print("")
            print(f" Cuit:  {cuit}")
            print(f" Dirección:  {direccion}")
            print(f" Teléfono:  {telefono}")
            print(f" E-mail:  {email}")
            print("")
        else: #de no tener datos nos notifica que no hay datos
            print("No se encontraron informacion.")
    except Exception: #de no poder conectarse a la base de datos o no este creada nos notifica que no puede obtener esos datos
        print(f"Error al obtener la información")

def menu(): #los menus principal 
    while True: #bucle principal que solo se puede salir ingresado el numero 0
        if alerta_productos_bajo_stock() == True: #antes de iniciar la lista de opciones ejecuta para ver la cantidad de unidades de los productos
            lista_menu_alerta() #de tener de resultado verdadero nos dara un menu visible en print rojo con una notificacion de que uno o varios productos hay escases
        else:
            lista_menu_ok() # de tener de resultado false nos dara un menu visible en print verde que nos indica que la cantidad de producto esta bien

        try:
            opcion = int(input("Eija un N° de Opcion: ")) #variable que almacena el numero de la opcion elegida
            os.system("cls") #limpia la pantalla 
            if opcion <= 9 and opcion >= 0: #si la variable esta dentro de los parametros indicados ingresa al menu
                match opcion:   #Menu de opciones ejecutable segun la variable opcion
                    case 1:#Create                   - - - -  >  >  >  opcion que nos dirije a una funcion para crear un nuevo producto  <  <  <  - - - - 
                        print(Back.GREEN + Fore.BLUE + "                Registrar nuevo producto               ")
                        additemsinit()  #Funcion para crear productos y mostrarlo en una lista
                    case 2:#Read                     - - - -  >  >  >  opcion que nos dirije a una funcion para buscar productos y mostrarlo en una lista  <  <  <  - - - -
                        print(Back.GREEN + Fore.BLUE + "               Buscar Producto               ")
                        producto_a_buscar = input(f'Ingrese el nombre del producto: ')
                        buscar_lista(producto_a_buscar) #Funcion para buscar productos y mostrarlo en una lista
                    case 3:#Read                     - - - -  >  >  >  opcion que nos dirije a una funcion para mostrar todos los producto  <  <  <  - - - -
                        print(Back.GREEN + Fore.BLUE + "               Lista de Productos               ")
                        list()
                    case 4: #Update                  - - - -  >  >  >  opcion que nos dirije a una funcion modificar un producto  <  <  <  - - - -
                        os.system("cls")#limpia la pantalla 
                        v_user()                        #valido un usuario y contraseña para continuar
                        os.system("cls")#limpia la pantalla 
                        print(Back.GREEN + Fore.BLUE + "               Actualizar/Modificar Productos                ")
                        print("")
                        editar_producto() #Funcion para editar productos y mostrarlo en una lista
                    case 5: #Delete                   - - - -  >  >  >  opcion que nos dirije a una funcion para buscar y eliminar un producto  <  <  <  - - - -
                        os.system("cls")#limpia la pantalla 
                        v_user()                        #valido un usuario y contraseña para continuar
                        os.system("cls")#limpia la pantalla 
                        print("")
                        print(Back.GREEN + Fore.BLUE + "               Eliminar Producto               )")
                        producto_a_buscar = input(f'Ingrese el nombre del producto que desea ' + Fore.RED + 'ELIMINAR: ')
                        buscar_lista(producto_a_buscar) #Funcion para buscar productos y mostrarlo en una lista
                        print("")
                        eliminarprod() #Funcion para eliminar producto
                    case 6:#                        - - - -  >  >  >  opcion que muestra la informacion de la empresa   <  <  <  - - - - 
                        informacion() #funcion que muestra la informacion de la empresa 
                    case 7:#                        - - - -  >  >  >  opcion que muestra una tabla con los productos con bajo stock   <  <  <  - - - - 
                        buscar_productos_bajo_stock()          
                    case 8:#                        - - - -  >  >  >  opcion que muestra un submenu para editar datos   <  <  <  - - - -
                        os.system("cls")#limpia la pantalla 
                        v_user()                    #valido un usuario y contraseña para continuar
                        os.system("cls")#limpia la pantalla 
                        while True: 
                            print(Back.GREEN + Fore.BLUE + "               Menu Editar Datos               )")
                            print("")
                            print(Fore.BLUE + "------------------------")
                            print(Fore.BLUE + " Que desea Editar:")
                            print(Fore.BLUE + "------------------------")
                            print("")
                            print(Fore.GREEN + "1. Usuario/Contraseña")
                            print(Fore.GREEN + "2. Datos de la empresa")
                            print("")
                            print(Fore.BLUE + "3. Volver al menu principal")
                            print("")
                            
                            try: #si la variable esta dentro de los parametros indicados ingresa al menu
                                opt_edits = int(input("Elija su N° de opcion ")) #variable que almacena el numero de la opcion elegida
                                if opt_edits <= 3 and opt_edits >= 0:  #de ser verdadero ingresa al la funcion que contiene el menu de usuarios
                                    match opt_edits:
                                        case 1:
                                            os.system("cls")
                                            menu_user()
                                        case 2:
                                            os.system("cls")
                                            editdts()#de ser verdadero ingresa al la funcion que contiene el menu de informacion
                                        case 3: #de ser verdadero ingresa al la funcion que contiene el menu principal
                                            os.system("cls")
                                            menu()
                                else: # de no ingresar un numero dentro de los parametros nos indica por una notificacion que ingresemos un numero valido
                                    os.system("cls")
                                    print("")
                                    print(Back.RED+"¡Error! El número ingresado no es valido")
                                    print("")
                            except ValueError :#si la variable no es un numero  nos muestra un print notificando
                                os.system("cls")
                                print(Back.RED+"¡Error! Ingrese un número válido.")
                            
                    case 9: #                        - - - -  >  >  >  opcion que BORRA TODA LA BASE DE DATOS   <  <  <  - - - -
                        os.system("cls")
                        reiniciar() #Funcion que BORRA TODA LA BASE DE DATOs
                        os.system("cls")
                    case 0: #                        - - - -  >  >  >  opcion que sale del menu   <  <  <  - - - -
                        print("")
                        print(f"{'':>10}"+Back.CYAN+f"{'':>44}")
                        print(f"{'':>10}"+Back.CYAN+f"{'':>44}")
                        print(f"{'':>10}"+Back.CYAN+"     "+Back.WHITE+Fore.BLUE+f"{'':>34}"+Back.CYAN+"     ")
                        print(f"{'':>10}"+Back.CYAN+"     "+Back.WHITE+Fore.BLUE+f"{'':>34}"+Back.CYAN+"     ")
                        print(f"{'':>10}"+Back.CYAN+"     "+Back.WHITE+Fore.BLUE+f"{'':>4}Gracias! Que tenga buen dia{'':>3}"+Back.CYAN+"     ")
                        print(f"{'':>10}"+Back.CYAN+"     "+Back.WHITE+Fore.BLUE+f"{'':>34}"+Back.CYAN+"     ")
                        print(f"{'':>10}"+Back.CYAN+"     "+Back.WHITE+Fore.BLUE+f"{'':>34}"+Back.CYAN+"     ")
                        print(f"{'':>10}"+Back.CYAN+f"{'':>44}")
                        print(f"{'':>10}"+Back.CYAN+f"{'':>44}")
                        time.sleep(2) # funcion que pausa la pantalla dos segundo para que puedas obserbar el mensaje anterior
                        exit() # Funcion que sale del programa tambien ubiera funcionado si ubiera puesto un break
                print("")
                print(Fore.BLUE+"Para regresar toque una tecla")
                msvcrt.getch() #funcion que espera que el cliente toque una tecla para poder continuar
                os.system("cls")
            else: # de no poner un numero dentro de los paramentros nos muestra un mensaje y nos vuele a mostrar el menu principal
                print(Fore.RED + "Opcion invalida elija un numero del 0 al 9")
        except ValueError: # de no poner un numero nos indica que pongamos un numero dentro de los paramentros
            print(Fore.RED + "Opcion invalida elija un numero del 0 al 9")

def lista_menu_ok(): #funcion que muestra la lista de opciones del menu principal con marco verde
    print("")
    print(f"{'':>10}"+Back.GREEN+f"{'':>38}")
    print(f"{'':>10}"+Back.GREEN+"  "+Back.BLUE+f"{'':>34}"+Back.GREEN+"  ")
    print(f"{'':>10}"+Back.GREEN+"  "+Back.BLUE+f"{'':>15}Menu{'':>15}"+Back.GREEN+"  ")
    print(f"{'':>10}"+Back.GREEN+"  "+Back.BLUE+f"{'':>34}"+Back.GREEN+"  ")
    print(f"{'':>10}"+Back.GREEN+"  "+Back.CYAN +f"     Opcion      Descripcion      "+Back.GREEN+"  ")
    print(f"{'':>10}"+Back.GREEN+"  "+Back.CYAN +f"----------------------------------"+Back.GREEN+"  ")
    print(f"{'':>10}"+Back.GREEN+"  "+Back.WHITE + f"{'':>34}"+Back.GREEN+"  ")
    print(f"{'':>10}"+Back.GREEN+"  "+Back.WHITE + f"       1        Registrar         "+Back.GREEN+"  ")
    print(f"{'':>10}"+Back.GREEN+"  "+Back.WHITE + f"{'':>7}2        Buscar            "+Back.GREEN+"  ")
    print(f"{'':>10}"+Back.GREEN+"  "+Back.WHITE + f"{'':>7}3        Lista             "+Back.GREEN+"  ")
    print(f"{'':>10}"+Back.GREEN+"  "+Back.WHITE + f"{'':>7}4        Actualizar        "+Back.GREEN+"  ")
    print(f"{'':>10}"+Back.GREEN+"  "+Back.WHITE + f"{'':>7}5        Eliminar          "+Back.GREEN+"  ")
    print(f"{'':>10}"+Back.GREEN+"  "+Back.WHITE + f"{'':>7}6        Info Empresa      "+Back.GREEN+"  ")
    print(f"{'':>10}"+Back.GREEN+"  "+Back.WHITE + f"{'':>7}7        Bajo Stock        "+Back.GREEN+"  ")
    print(f"{'':>10}"+Back.GREEN+"  "+Back.WHITE + f"{'':>7}8        Editar datos      "+Back.GREEN+"  ")
    print(f"{'':>10}"+Back.GREEN+"  "+Back.WHITE + f"{'':>7}9        REINICIAR APP     "+Back.GREEN+"  ")
    print(f"{'':>10}"+Back.GREEN+"  "+Back.WHITE + f"{'':>7}0        Salir             "+Back.GREEN+"  ")
    print(f"{'':>10}"+Back.GREEN+"  "+Back.WHITE + f"{'':>34}"+Back.GREEN+"  ")
    print(f"{'':>10}"+Back.GREEN+f"{'':>38}")
    print("")

def lista_menu_alerta():#funcion que muestra la lista de opciones del menu principal con marco rojo
    print("")
    print(f"{'':>10}"+Back.RED+f"{'':>38}")
    print(f"{'':>10}"+Back.RED+"  "+Back.BLUE+f"{'':>34}"+Back.RED+"  ")
    print(f"{'':>10}"+Back.RED+"  "+Back.BLUE+f"{'':>15}Menu{'':>15}"+Back.RED+"  ")
    print(f"{'':>10}"+Back.RED+"  "+Back.BLUE+f"{'':>34}"+Back.RED+"  ")
    print(f"{'':>10}"+Back.RED+"  "+Back.CYAN +f"     Opcion      Descripcion      "+Back.RED+"  ")
    print(f"{'':>10}"+Back.RED+"  "+Back.CYAN +f"----------------------------------"+Back.RED+"  ")
    print(f"{'':>10}"+Back.RED+"  "+Back.WHITE + f"{'':>34}"+Back.RED+"  ")
    print(f"{'':>10}"+Back.RED+"  "+Back.WHITE + f"       1        Registrar         "+Back.RED+"  ")
    print(f"{'':>10}"+Back.RED+"  "+Back.WHITE + f"{'':>7}2        Buscar            "+Back.RED+"  ")
    print(f"{'':>10}"+Back.RED+"  "+Back.WHITE + f"{'':>7}3        Lista             "+Back.RED+"  ")
    print(f"{'':>10}"+Back.RED+"  "+Back.WHITE + f"{'':>7}4        Actualizar        "+Back.RED+"  ")
    print(f"{'':>10}"+Back.RED+"  "+Back.WHITE + f"{'':>7}5        Eliminar          "+Back.RED+"  ")
    print(f"{'':>10}"+Back.RED+"  "+Back.WHITE + f"{'':>7}6        Info Empresa      "+Back.RED+"  ")
    print(f"{'':>10}"+Back.RED+"  "+Back.WHITE + f"{'':>7}7        Bajo Stock        "+Back.RED+"  ")
    print(f"{'':>10}"+Back.RED+"  "+Back.WHITE + f"{'':>7}8        Editar datos      "+Back.RED+"  ")
    print(f"{'':>10}"+Back.RED+"  "+Back.WHITE + f"{'':>7}9        REINICIAR APP     "+Back.RED+"  ")
    print(f"{'':>10}"+Back.RED+"  "+Back.WHITE + f"{'':>7}0        Salir             "+Back.RED+"  ")
    print(f"{'':>10}"+Back.RED+"  "+Back.WHITE + f"{'':>34}"+Back.RED+"  ")
    print(f"{'':>10}"+Back.RED+f"{'':>38}")
    print("")

def menu_user():#funcion que muestra y ejecuta la lista de opciones del menu usuarios y poder modificar los datos del mismo
    print("")
    print(Back.GREEN + Fore.BLUE + "               CONFIGURACION DE USUARIOS               ")
    print("")
    print(Fore.CYAN+"-------------------")
    print(Fore.CYAN+" OPCIONES:")
    print(Fore.CYAN+"-------------------")
    print("")
    print(Fore.CYAN+"1."+Fore.GREEN+" Agregar nuevo Usuario")
    print(Fore.CYAN+"2."+Fore.YELLOW+" Modificar nombre de Usuario")
    print(Fore.CYAN+"3."+Fore.YELLOW+ " Modificar contraseña del Usuario")
    print(Fore.CYAN+"4."+Fore.RED+" Eliminar Usuario")
    print("")
    print(Fore.BLUE+"5. Volver al menu principal ")
    print("")
    opcions = str(input("Escriba el numero da la opcion: "+Fore.CYAN))  #variable que almacena el numero de la opcion elegida
    os.system("cls")
    if opcions <= '5' and opcions >= '0': #si la variable esta dentro de los parametros indicados ingresa al menu
        match opcions:
            case '1':                      #   - - - -  >  >  >    Opcion AGREGAR NUEVO USUARIO   <  <  <  - - - - 
                newuser() #Ejecuta la funcion para crear un nuevo usuario
                print("Para regresar toque una tecla")
                msvcrt.getch() #Ejecuta funcion q pausa la ejecucion hasta que el cliente toque una tecla
                os.system("cls")
                menu_user() #ejecuta la funcion menu de usuario para regresar atras
            case '2':                      #   - - - -  >  >  >    Opcion Modificar NOMBRE DE USUARIO   <  <  <  - - - - 
                print("")
                print(Fore.CYAN + Back.GREEN+ "               Modificar NOMBRE DE USUARIO               ")
                while True:
                        print("")
                        usuario = input("Usuario: ") #pide al usuario que ingrese su usuario modificar 
                        password = input("Contraseña: ") #pide al usuario que ingrese su contraseña para validar que es el mismo y no otro usuario
                        print("")
                        try:
                            query = """SELECT * FROM user WHERE nombre = ?"""  #almaceno dentro de una variable la linea de codigo de sqlite para hacer la consulta
                            cursor.execute(query, (usuario, )) #Ejecuto la linea de codigo almacenado dentro de query usando la variable "usuario" q contiene de dato un string
                            user = cursor.fetchone() #almacena en la variable el resultado de la linea anterior
                            id, nombre , contraseña = user #separo la informacion en dos variables
                            if password == contraseña and usuario == nombre: #uso las dos variables para comparar lo que escribio es igual a lo que esta almacenado en la base de datos
                                print(Fore.GREEN + "Datos Validos")
                                try:
                                    print("")
                                    m_user = input("Ingrese su nuevo nombre de usuario: " + Fore.GREEN) #Almaceno dentro de la variable el nuevo nombre de usuario
                                    query = """UPDATE user SET nombre = ? WHERE id = ?""" #linea de codigo de sqlite para actualizar la informacion a la table user de mi bd
                                    cursor.execute(query, (m_user, id)) #ejecuta la linia anterior actualizando el usuario con la variable "m_user"
                                    conexion.commit() #Guarda todos los cambios en la base de datos
                                    print(Fore.GREEN + "Se ha modificado exitosamente el nombre de usuario")
                                    print("")
                                    break
                                except sqlite3.IntegrityError: #si arroja error en la base de datos pide q lo intente de nuevo
                                    print(Fore.RED + "Ingrese un usuario")
                            else:
                                print(Fore.RED + "Datos Invalidos") #de equivocarse con el USUARIO/CONTRASEÑA pide que los vuelva a intentar
                        except TypeError:
                            print(Fore.RED + "Datos Invalidos")  #de equivocarse con el USUARIO/CONTRASEÑA pide que los vuelva a intentar
                print("Para regresar toque una tecla")
                msvcrt.getch()#Ejecuta funcion q pausa la ejecucion hasta que el cliente toque una tecla
                os.system("cls")
                menu_user() #ejecuta la funcion menu de usuario para regresar atras
            case '3':                      #   - - - -  >  >  >    Opcion Modificar CONTRASEÑA DE USUARIO   <  <  <  - - - - 
                print("")
                print(Fore.CYAN + Back.GREEN+ "               Modificar CONTRASEÑA               ")
                while True:
                        usuario = input("Usuario: ")#pide al usuario que ingrese su usuario 
                        password = input("Contraseña: ") #pide al usuario que ingrese su contraseña para validar que es el mismo y no otro usuario
                        try:
                            query = """SELECT * FROM user WHERE nombre = ?""" #almaceno dentro de una variable la linea de codigo de sqlite para hacer la consulta
                            cursor.execute(query, (usuario, ))#Ejecuto la linea de codigo almacenado dentro de query usando la variable "usuario" q contiene de dato un string
                            user = cursor.fetchone()#almacena en la variable el resultado de la linea anterior
                            id, nombre , contraseña = user#separo la informacion en dos variables
                            while True:
                                if password == contraseña and usuario == nombre:#uso las dos variables para comparar lo que escribio es igual a lo que esta almacenado en la base de datos
                                    print(Fore.GREEN + "Datos Validos")
                                    try:
                                        print("")
                                        m_user = input("Ingrese su nueva contraseña: " + Fore.GREEN) #Almaceno dentro de la variable la nueva contraseña
                                        query = """UPDATE user SET contraseña = ? WHERE id = ?"""#linea de codigo de sqlite para actualizar la informacion a la table user de mi bd
                                        cursor.execute(query, (m_user, id))#ejecuta la linia anterior actualizando el usuario con la variable "m_user"
                                        conexion.commit()#Guarda todos los cambios en la base de datos
                                        print(Fore.GREEN + "Se ha modificado exitosamente su contraseña")
                                        print("")
                                        break
                                    except sqlite3.IntegrityError: #si arroja error en la base de datos pide q lo intente de nuevo
                                        print(Fore.RED + "Ingrese una contraseña")
                                else: #de equivocarse con el USUARIO/CONTRASEÑA pide que los vuelva a intentar
                                    print(Back.RED+"Datos Invalidos")
                                break
                            break
                        except TypeError: #de equivocarse con el USUARIO/CONTRASEÑA pide que los vuelva a intentar
                            print(Back.RED+"Datos Invalido")
                print("Para regresar toque una tecla")
                msvcrt.getch()#Ejecuta funcion q pausa la ejecucion hasta que el cliente toque una tecla
                os.system("cls")
                menu_user() #ejecuta la funcion menu de usuario para regresar atras
            case '4':                      #   - - - -  >  >  >    Opcion ELIMINAR USUARIO   <  <  <  - - - - 
                print("")
                print(Back.RED + "               ELIMINAR USUARIO               ")
                usuario = input("Ingrese el usuario a eliminar: ") #pide al usuario que ingrese el usuario a eliminar
                query = "SELECT * FROM user WHERE nombre = ?" #almaceno dentro de una variable la linea de codigo de sqlite para hacer la consulta
                cursor.execute(query, (usuario,))#ejecuta la linia anterior seleccionando el usuario con la variable "usuario"
                usuario_eliminado = cursor.fetchone() #almacena en la variable el resultado de la linea anterior
                v_user()    # Ejecuta una validacion de usuario
                if usuario_eliminado != None:
                    query = "DELETE FROM productos WHERE id = ?" #almaceno dentro de una variable la linea de codigo de sqlite para borrar el usuario
                    cursor.execute(query, (usuario,)) #ejecuta la linia anterior borrando el usuario con la variable "usuario"
                    print(Fore.RED + "El Usuario ha eliminado correctamente.")
                else: #de no encontrar coincidencias con el nombre de usuario notifica que no encontro el mismo
                    print(Back.RED+"No se encontró ningún usuario con ese nombre")
                print("")
                print("Toque una tecla para regresar al menu")
                msvcrt.getch()#Ejecuta funcion q pausa la ejecucion hasta que el cliente toque una tecla
                os.system("cls")
                menu_user() #ejecuta la funcion menu de usuario para regresar atras
            case '5':                       #   - - - -  >  >  >    Opcion VOLVER AL MENU PRINCIPAL   <  <  <  - - - - 
                os.system("cls")
                menu() #Ejecuta la funcion y retorna al menu principal
    else:
        print(Back.RED+"Opcion invalida elija un numero del 1 al 5")
        menu_user()    #ejecuta la funcion menu de usuario para regresar atras

def reiniciar(): #funcion que borra la base de datos y todas sus tablas, vuelve a ejecutar desde el inicio
    v_user()
    print("")
    print('     '+Back.RED + "                                                              ")
    print('     '+Back.RED + "                     REINICIAR APLICACION                     ")
    print('     '+Back.RED + "                                                              ")
    print("")
    print('\t'"¿USTED ESTA SEGURO QUE DESEA REINICIAR LA APLICACION?")
    print("  ¡ATENCION!    Reiniciar la aplicacion es una operecion irreversible,")
    print("  todos los datos se perderan de forma permanente y no se podran recuperar")
    print("")
    print("Escriba "+Fore.GREEN+" YES "+Fore.WHITE+" en MAYUSCULAS para continuar")
    print("Escriba "+Fore.RED+" NO "+Fore.WHITE+" en MAYUSCULAS para CANCELAR")
    print("")
    while True:
        reinicio = input("ESCRIBA la opcion deseada "+Fore.GREEN+"YES/"+Fore.RED+"NO: "+Fore.WHITE) #Variable que almacena la confirmacion o cancelacion de la ejecucion
        if reinicio == "YES": #si es verdadero ingresa al if
            query = """DROP TABLE IF EXISTS user""" #Borra la base de datos de usuarios
            cursor.execute(query) #ejecuta la linea anterior
            query = """DROP TABLE IF EXISTS productos"""#Borra la base de datos de productos
            cursor.execute(query) #ejecuta la linea anterior
            query = """DROP TABLE IF EXISTS info"""#Borra la base de datos de informacion
            cursor.execute(query) #ejecuta la linea anterior
            conexion.commit() #Guarda los cambios realizados
            print(Fore.BLUE+"La aplicacion se reinicio con exito")
            print(Fore.GREEN+"Para iniciar la aplicacion toque una tecla")
            msvcrt.getch()
            os.system("cls")
            run() #Ejecuta la funcion y iniciar desde el principio del programa


        elif reinicio == "NO": #de ser verdadero la variable con el "NO" ejecuta la funcion menu y regresa al menu principal
            menu()
        else: #de no escribir una respuesta valida se le notifica que no escribio correctamente su respuesta
            print("")
            print("No escribio una opcion valida")
            print("")

def editdts(): #Funcion que abre el menu de opciones para editar los datos de la empresa/comercio
    print("")
    print(Back.CYAN+"        Menu de edicion de datos de la empresa        ")
    print("")
    print(Fore.CYAN + "------------------------------")
    print(Fore.CYAN + "Que datos desea modificar:")
    print(Fore.CYAN + "------------------------------")
    print("")
    print(Fore.LIGHTYELLOW_EX + "1. Empresa")
    print(Fore.LIGHTYELLOW_EX + "2. Cuit")
    print(Fore.LIGHTYELLOW_EX + "3. Direccion")
    print(Fore.LIGHTYELLOW_EX + "4. Telefono")
    print(Fore.LIGHTYELLOW_EX + "5. Email")
    print("")
    print(Fore.BLUE + "6. Volver al menu principal")
    print("")
    opcions = str(input("Escriba el numero da la opcion: "+Fore.GREEN))
    os.system("cls")
    if opcions <= '6' and opcions >= '0':
        match opcions:
            case '1':                      #   - - - -  >  >  >    Opcion MODIFICAR NOMBRE DEL COMERCIO   <  <  <  - - - - 
                print("")
                empresa = input("Escriba el nuevo nombre de la empresa: ")
                query = """ 
                        UPDATE info 
                        SET empresa = ?
                        WHERE id = 1
                        """   #linea de codigo de sqlite para actualizar la informacion a la table info de mi bd
                cursor.execute(query, (empresa, )) #ejecuta la linia anterior actualizando los datos con la variable almacenada anterior mente
                conexion.commit() #Guarda los cambios realizados en la base de datos
                print("El nuevo nombre de la empresa es: "+ Fore.GREEN + empresa)
                print("")
                print("Para regresar toque una tecla")
                msvcrt.getch()
                os.system("cls")
                editdts() #Ejecuta la funcion y vuelve al menu de editar datos de la empresa/comercio
            case '2':                      #   - - - -  >  >  >    Opcion MODIFICAR CUIT DEL COMERCIO   <  <  <  - - - - 
                print("")
                cuit = input("Escriba el nuevo cuit: ")
                query = """
                        UPDATE info 
                        SET cuit = ?
                        WHERE id = 1
                        """             #linea de codigo de sqlite para actualizar la informacion a la table info de mi bd
                cursor.execute(query, (cuit, ))     #ejecuta la linia anterior actualizando los datos con la variable almacenada anterior mente
                conexion.commit()#Guarda los cambios realizados en la base de datos
                print("El nuevo cuit es: "+ Fore.GREEN + cuit)
                print("")
                print("Para regresar toque una tecla")
                msvcrt.getch()
                os.system("cls")
                editdts()#Ejecuta la funcion y vuelve al menu de editar datos de la empresa/comercio
            case '3':                       #   - - - -  >  >  >    Opcion MODIFICAR DIRECCION DEL COMERCIO   <  <  <  - - - - 
                print("")
                direccion = input("Escriba la nueva direccion: ")
                query = """
                        UPDATE info 
                        SET direccion = ?
                        WHERE id = 1
                        """ #linea de codigo de sqlite para actualizar la informacion a la table info de mi bd
                cursor.execute(query, (direccion, ))    #ejecuta la linia anterior actualizando los datos con la variable almacenada anterior mente
                conexion.commit()#Guarda los cambios realizados en la base de datos
                print("La nueva direccion es: "+ Fore.GREEN + direccion)
                print("")
                print("Para regresar toque una tecla")
                msvcrt.getch()
                os.system("cls")
                editdts()#Ejecuta la funcion y vuelve al menu de editar datos de la empresa/comercio
            case '4':                      #   - - - -  >  >  >    Opcion MODIFICAR TELEFONO DEL COMERCIO   <  <  <  - - - - 
                print("")
                telefono = input("Escriba el nuevo telefono: ")
                query = """
                        UPDATE info 
                        SET telefono = ?
                        WHERE id = 1
                        """     #linea de codigo de sqlite para actualizar la informacion a la table info de mi bd
                cursor.execute(query, (telefono, ))    #ejecuta la linia anterior actualizando los datos con la variable almacenada anterior mente
                conexion.commit()#Guarda los cambios realizados en la base de datos
                print("El nuevo telefono es: "+ Fore.GREEN + telefono)
                print("")
                print("Para regresar toque una tecla")
                msvcrt.getch()
                os.system("cls")
                editdts()#Ejecuta la funcion y vuelve al menu de editar datos de la empresa/comercio
            case '5':                      #   - - - -  >  >  >    Opcion MODIFICAR Email DEL COMERCIO   <  <  <  - - - - 
                print("")
                email = input("Escriba el nuevo email: ")
                query = """
                        UPDATE info 
                        SET email = ?
                        WHERE id = 1        
                        """     #linea de codigo de sqlite para actualizar la informacion a la table info de mi bd
                cursor.execute(query, (email, ))    #ejecuta la linia anterior actualizando los datos con la variable almacenada anterior mente
                conexion.commit()#Guarda los cambios realizados en la base de datos
                print("El nuevo email es: "+ Fore.GREEN + email)
                print("")
                print("Para regresar toque una tecla")
                msvcrt.getch()
                os.system("cls")
                editdts()#Ejecuta la funcion y vuelve al menu de editar datos de la empresa/comercio
            case '6': #   - - - -  >  >  >    Opcion VOLVER AL MENU PRINCIPAL   <  <  <  - - - - 
                os.system("cls")
                menu() #Ejecuta la funcion y retorna al menu principal
    else:
        print(Back.RED+"Opcion invalida elija un numero del 1 al 6")
        editdts()   #Ejecuta la funcion y vuelve al menu de editar datos de la empresa/comercio

def additemsinit(): #Agrega un nuevo producto a la lista
    print("")
    while True: #consulta y valida el Stock si es un INT
        try:
            producto = str(input('Ingrese el producto: '))
            if len(producto) >= 2:
                break
            else:
                print(Back.RED+"El nombre del producto debe ser de almenos 2 letras")
        except ValueError:
            print(Back.RED+"¡Error! Ingrese un texto válido.")
    detalle = input('Ingrese el detalle: ')
    categoria = input('Ingrese categoria: ')
    while True: #consulta y valida el Stock si es un INT
        try:
            stock = int(input(f'Ingrese el stock de {producto}: '))
            break
        except ValueError:
            print(Back.RED+"¡Error! Ingrese un número válido.")
    while True: #consulta y valida el Valor si es un float
        try:
            precio = float(input(f'Ingrese el precio x unidad de {producto}: '))
            break 
        except ValueError:
            print(Back.RED+"¡Error! Ingrese un número válido.")
    productos = ([producto.upper(),detalle.lower(), stock, precio, categoria.lower()]) #almaceno las variables dentro de un diccionario
    print("")
    cursor.execute("""INSERT INTO productos(nombre, descripcion, cantidad, precio, categoria ) VALUES (?,?,?,?,?)""",productos) #ejecuta la linia anterior agregando los datos con el diccionario almacenada anterior mente
    conexion.commit() #Guarda todos los cambios en la base de datos
    print(Back.BLUE+Style.BRIGHT+"{:<20} {:<30} {:<10} {:<10} {:<15}".format("Producto", "Descripción", "Cantidad", "Precio", "Categoría"))
    print(Back.CYAN+"{:<20} {:<30} {:<10} {:<10} {:<15}".format(producto, detalle, stock, precio, categoria))
    print("")
    while True: #Consulta y valida si deseamos agregar otro objeto o si deseamos ya iniciar el menu
        print( Fore.WHITE + 'Ingrese ' + Fore.GREEN + '"ENTER" ' + Fore.WHITE + ' para agregar un nuevo producto o' + Fore.RED + ' "ESC"' + Fore.WHITE + ' para salir')
        salir = msvcrt.getch()
        if salir == b'\x1b':
            print(Fore.GREEN + 'Su producto a sido guardado con exito')
            break
        elif salir == b'\r':
            additemsinit()
        else:
            print(Fore.RED + 'Opcion invalida toque "ENTER" para ingresar un nuevo producto o "ESC" para salir')
            continue
        break

def editar_producto(): #Funcion para poder actualizar los datos del producto
    while True:
        try:
            identi = input("Ingrese el nombre del producto: ")
            identi = identi.upper()
            query = "SELECT * FROM productos WHERE nombre = ?"
            cursor.execute(query, (identi,))
            productos = cursor.fetchall()
            if productos:
                print("")
                print(Fore.WHITE+Back.BLUE+"{:<5} {:<25} {:<30} {:<10} {:<10} {:<15}".format("ID", "Producto", "Descripción", "Cantidad", "Precio", "Categoría"))
                print(Fore.WHITE+Back.BLUE+"{:<5} {:<25} {:<30} {:<10} {:<10} {:<15}".format("--", "--------", "-----------", "--------", "------", "---------"))
                for producto in productos:
                    id, nombre, descripcion, cantidad, precio, categoria = producto
                    print(Fore.WHITE+Back.LIGHTCYAN_EX+"{:<5} {:<25} {:<30} {:<10} {:<10} {:<15}".format(id, nombre, descripcion, cantidad, precio, categoria))
                while True:
                    try:
                        print("")
                        identi = int(input("Ingrese el número de ID del producto: "))
                        print("")
                        query = "SELECT * FROM productos WHERE id = ?"
                        cursor.execute(query, (identi,))
                        producto = cursor.fetchone()
                        if producto:
                            id, m_producto, m_detalle, m_stock, m_precio, m_categoria = producto
                            print(Fore.BLACK+Back.WHITE+"{:<5} {:<25} {:<20} {:<10} {:<10} {:<15}".format("ID", "Producto", "Descripción", "Cantidad", "Precio", "Categoría"))
                            print(Fore.BLACK+Back.WHITE+"{:<5} {:<25} {:<20} {:<10} {:<10} {:<15}".format("--", "--------", "-----------", "--------", "------", "---------"))
                            print(Fore.WHITE+Back.RED+"{:<5} {:<25} {:<20} {:<10} {:<10} {:<15}".format(id, m_producto, m_detalle, m_stock, m_precio, m_categoria))
                            while True:
                                print("")
                                print("Que desea modificar en el producto:")
                                print("1. Nombre del producto")
                                print("2. Descripcion")
                                print("3. Cantidad")
                                print("4. Precio")
                                print("5. Categoria")
                                print("")
                                print("6. Volver al menu principal")
                                print("")
                                try:
                                    edit_prod = int(input("Elija el n° de la opcion deseada:"+Fore.BLUE))
                                    print("")
                                    if edit_prod <= 6 and edit_prod >= 1:
                                        match edit_prod:
                                            case 1 :
                                                m_producto = input("Ingrese el nuevo nombre del producto: "+Fore.BLUE)
                                            case 2 :
                                                m_detalle = input("Ingrese el nuevo detalle: "+Fore.BLUE)
                                            case 3 :
                                                while True: #consulta y valida el Valor si es un int
                                                    try:
                                                        m_stock = int(input("Ingrese el nuevo stock: "+Fore.BLUE))
                                                        break 
                                                    except ValueError:
                                                        print(Fore.RED+"¡Error! Ingrese un número válido."+Fore.BLUE)
                                            case 4 :
                                                while True: #consulta y valida el Valor si es un float
                                                    try:
                                                        m_precio = float(input("Ingrese el nuevo precio: "+Fore.BLUE))
                                                        break 
                                                    except ValueError:
                                                        print(Fore.RED+"¡Error! Ingrese un número válido.")
                                            case 5 :
                                                m_categoria = input("Ingrese la nueva categoría: "+Fore.BLUE)
                                            case 6 :
                                                menu()
                                        break
                                    else:
                                        print(Fore.RED+ "Ingrese un numero de opcion Valida")
                                except ValueError:
                                    print(Fore.RED+"Ingrese un numero de opcion Valida")
                            query = """
                            UPDATE productos
                            SET nombre = ?, descripcion = ?, cantidad = ?, precio = ?, categoria = ?
                            WHERE id = ?
                            """
                            cursor.execute(query, (m_producto.upper(), m_detalle.lower(), m_stock, m_precio, m_categoria.lower(), id))
                            conexion.commit()  # Confirma los cambios en la base de datos
                            print(Fore.BLACK+Back.WHITE+"{:<5} {:<25} {:<20} {:<10} {:<10} {:<15}".format("ID", "Producto", "Descripción", "Cantidad", "Precio", "Categoría"))
                            print(Fore.BLACK+Back.WHITE+"{:<5} {:<25} {:<20} {:<10} {:<10} {:<15}".format("--", "--------", "-----------", "--------", "------", "---------"))
                            print(Fore.WHITE+Back.GREEN+"{:<5} {:<25} {:<20} {:<10} {:<10} {:<15}".format(id, m_producto.upper(), m_detalle.lower(), m_stock, m_precio, m_categoria.lower()))
                            print("")
                            print(Fore.GREEN+"Producto actualizado correctamente.")
                            print("")
                            print("")
                            print(Fore.BLUE+"Para regresar toque una tecla")
                            msvcrt.getch()
                            os.system("cls")
                            menu()
                        else:
                            print(Fore.RED+"¡ID inexistente! Ingrese un ID válido.")
                    except ValueError:
                        print(Fore.RED+"¡Error! ID Invalido")
            else:
                print(Fore.RED+"No se encontraron productos.")
        except ValueError:
            print(Fore.RED+"¡Error! El Producto no exite")

def eliminarprod(): #Funcion para poder eliminar un producto
    while True:
        try:
            identi = int(input("Ingrese el número de ID del producto: "))
            print("")
            query = "SELECT * FROM productos WHERE id = ?"
            cursor.execute(query, (identi,))
            producto_eliminado = cursor.fetchone()
            if producto_eliminado != None:
                id, m_producto, m_detalle, m_stock, m_precio, m_categoria = producto_eliminado
                print(Fore.WHITE+Back.RED+"{:<5} {:<25} {:<20} {:<10} {:<10} {:<15}".format("ID", "Producto", "Descripción", "Cantidad", "Precio", "Categoría"))
                print(Fore.WHITE+Back.RED+"{:<5} {:<25} {:<20} {:<10} {:<10} {:<15}".format("--", "--------", "-----------", "--------", "------", "---------"))
                print(Fore.WHITE+Back.LIGHTRED_EX+"{:<5} {:<25} {:<20} {:<10} {:<10} {:<15}".format(id, m_producto, m_detalle, m_stock, m_precio, m_categoria))
                query = "DELETE FROM productos WHERE id = ?"
                cursor.execute(query, (identi,))
                conexion.commit()
                print("")
                print(Fore.GREEN + "Producto eliminado correctamente.")
                print("")
                break
            else:
                print("")
                print(Fore.RED + "No se encontró ningún producto con ese ID.")
                print("")
                print('Toque cualquier tecla para volver a buscar')
                print('Toque \"ESC\" para volver al menu de busqueda')
                tecla = msvcrt.getch()
                if tecla != b'\x1b':
                    eliminarprod()
                else:
                    break
        except ValueError:
            print(Fore.RED + "¡Error!  Ingrese un numero valido")

def list(): #Imprime todos los producto de la lista
    query = "SELECT id, nombre, descripcion, cantidad, precio, categoria FROM productos"
    cursor.execute(query)
    resultados = cursor.fetchall()

    if resultados:
        print(Back.GREEN + f"{'':<38}Lista de productos{'':>39}")
        print(Back.LIGHTGREEN_EX+"{:<5} {:<20} {:<30} {:<10} {:<10} {:<15}".format("ID", "Producto", "Descripción", "Cantidad", "Precio", "Categoría"))
        for producto in resultados:
            id, nombre, descripcion, cantidad, precio, categoria = producto
            print(Back.CYAN+"{:<5} {:<20} {:<30} {:<10} {:<10} {:<15}".format(id, nombre, descripcion, cantidad, precio, categoria))
    else:
        print(Fore.RED+"No se encontraron productos.")


def buscar_lista(objeto_buscado): #Funcion para buscar uno o varios producto con el mismo valor y mostrarlos en una lista
    while True:
        try:
            objeto_buscado = objeto_buscado.upper()
            query = "SELECT * FROM productos WHERE nombre = ?"
            cursor.execute(query, (objeto_buscado,))
            productos = cursor.fetchall()
            if productos:
                print("")
                print(Fore.WHITE+Back.BLUE+"{:<5} {:<25} {:<30} {:<10} {:<10} {:<15}".format("ID", "Producto", "Descripción", "Cantidad", "Precio", "Categoría"))
                print(Fore.WHITE+Back.BLUE+"{:<5} {:<25} {:<30} {:<10} {:<10} {:<15}".format("--", "--------", "-----------", "--------", "------", "---------"))
                for producto in productos:
                    id, nombre, descripcion, cantidad, precio, categoria = producto
                    print(Fore.WHITE+Back.LIGHTCYAN_EX+"{:<5} {:<25} {:<30} {:<10} {:<10} {:<15}".format(id, nombre, descripcion, cantidad, precio, categoria))
                break
            else:
                print("")
                print(Fore.RED + f"No se encontro el producto {objeto_buscado} ")
                print("")
                print('Toque cualquier tecla para volver a buscar')
                print('Toque \"ESC\" para volver al menu de busqueda')
                tecla = msvcrt.getch()
                if tecla != b'\x1b':
                    print("")
                    objeto_buscado = input(f'Ingrese el nombre del producto: ')
                    print("")
                else:
                    break
            
        except ValueError:
            print(Fore.RED + f"No se encontro el producto {objeto_buscado} ")

def alerta_productos_bajo_stock(): #funcion que muestra si hay una cantidad menor a 10 productos
        
        query = """SELECT nombre, descripcion, cantidad FROM productos WHERE cantidad < 10"""
        cursor.execute(query)
        resultados = cursor.fetchall()
        if resultados:
            print("")
            print("     "+Fore.WHITE+Back.RED +"          ¡ ¡  ¡  A T E N C I O N  !  !  !          ")
            print("")
            print(Fore.LIGHTRED_EX + Style.BRIGHT +"        DE ESTOS PRODUCTOS TENES MENOS DE  10  UNIDADES")
            print(Back.LIGHTRED_EX + "{:<20} {:<30} {:<10}".format("Producto", "Descripción", "Cantidad"))
            for resultado in resultados:
                nombre, descripcion, cantidad = resultado
                print(Fore.RED + "{:<20} {:<30} {:<10}".format (nombre, descripcion,cantidad))
            return True
        else:
            return False

def buscar_productos_bajo_stock():#funcion que muestra si hay una cantidad menor a 20 productos y los muestra en una lista
    query = """SELECT id, nombre, descripcion, cantidad, precio, categoria FROM productos WHERE cantidad < 20"""
    cursor.execute(query)
    resultados = cursor.fetchall()

    if resultados:
        print(Back.LIGHTMAGENTA_EX + "{:<5} {:<20} {:<30} {:<10} {:<10} {:<15}".format("ID", "Producto", "Descripción", "Cantidad", "precio", "categoria"))
        for producto in resultados:
            id, nombre, descripcion, cantidad, precio, categoria = producto
            print("{:<5} {:<20} {:<30} {:<10} {:<10} {:<15}".format (id, nombre, descripcion,cantidad, precio, categoria))
    else:
        print(Fore.GREEN+"No se encontraron productos con Bajo stock.")


run() #EJECUTA LA FUNCION E INICIA EL PROGRAMA