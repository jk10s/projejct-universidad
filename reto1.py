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
            opcion=None
            contador=0
            while contador !=3:
                contador=contador+1
                
                print("""sesion Iniciada
                
                    MENU

                1. Adivinanza  
                2. Cerrar sesión.
                
                """)
            
                opcion=int(input("Digita una opcion: "))    
                Num_Aleatorio = random.randint(0, 10)
                bandera= True
                conteo=0
                while opcion==1 and bandera==True:
                    conteo=conteo+1
                    numero=int(input("Cual es el numero secreto (0-10) "))
                    if numero<Num_Aleatorio:
                        print("estas por debajo")
                    elif numero>Num_Aleatorio:
                        print("Te pasaste")
                    elif numero==Num_Aleatorio:
                        print(f"adivinaste el nuemro en {conteo} intentos")
                        bandera=False
                if opcion==2:
                    exit()
            else:
                print("hasta pronto")
                exit()
        
        
        else:
            print(" ERROR capcha incorrecto")
            exit()
    else:
        print("ERROR contraseña incorrecta")
        exit()
else:
    print("ERROR usuario incorrecto")
    exit()
