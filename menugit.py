import os
import time

usario = []
while True:
    os.system('cls')
    print("hola bienvenido ")
    print("menu")
    print("""1. inicio de sesion 
             2. registrar usario
             3. eliminar usario 
             4. salir""")
    opc = int(input("que opcion tomara"))
    if opc ==1 :
        print("inicio sesion")
        x =input("nomre de usario")
    elif opc == 2:
        nombre = input("que nombre de usario usaras")
        clae = input("crea una contreseña ")
        usario = {
            "nombre",nombre,
            "contra",clae}
    elif opc == 3:
        pass
    else:
        print("saliste")
        time.sleep(3)
        break