estatura = input("Cual es tu estatura? -->")
peso = input("Cual es tu peso?     -->")          
                                          
#cast
e = float(estatura)
p = float(peso)
                                          
                                                      
imc = p/(e**2)                     
print(f"Tu IMC es: ------------>{imc}")