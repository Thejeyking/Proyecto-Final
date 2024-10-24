import time
import msvcrt
import os

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
            case '2':
                print("Buscar")
                app_search()
            case '3':
                print("Lista")
            case '4':
                print("Actualizar")
            case '5': #eliminar
                os.system("cls")
                v_user()
                os.system("cls")
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