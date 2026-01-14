import os

while True:

    print("---------------------------")
    print(" ")
    print('-----*Suma de numeros*-----')
    
    print('\n..escribe salir para cerrar el programa \n')


    try:
        numero1 = input("Dame un numero:").strip()
        numero2 = input("Dame un numero mas:").strip()
        
        if numero1 == "salir" or numero2 == "salir":
            break
        #cast
        n1 = float(numero1)
        n2 = float(numero2)
        suma = n1+n2
        print(f"La suma de tus numeros es:{suma}")
        input("\nPresiona Enter para continuar...")   
        os.system("cls" if os.name == "nt" else "clear")
    except ValueError:
        print("Error: para que el programa funcione, ingresa solo numeros")
    except Exception as e:
        print(f"Error inesperado: {e}")
