import random
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