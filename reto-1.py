# ejercicio realizado por john nelson celada uchima cc 94365188 grupo 60
import random

print("Bienvenido al sistema de ubicación para zonas públicas WIFI")
usuario=input("Nombre de usuario: ")

if usuario=='60':
    print("usuario validado correcctamente")
    contraseña=input("Contraseña: ")
    if contraseña=='06':
        print("contraseña correcta")
        capcha=int(input("la suma 6 + 0 = "))
        if capcha==6:
            print("""sesion Iniciada
                
                    MENU

                1. Adivinanza  
                2. Cerrar sesión.
                
                """)
            input()

        
        else:
            print(" ERROR capcha incorrecto")
            exit()
    else:
        print("ERROR contraseña incorrecta")
        exit()
else:
    print("ERROR usuario incorrecto")
    exit()
