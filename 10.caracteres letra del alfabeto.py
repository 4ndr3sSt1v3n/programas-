# 10 Escriba un programa para verificar si un caracter es una letra del alfabeto o no.
caracter = input("digite un caracter ")
print (caracter)
codigo = ord(caracter)
print (codigo)
if  codigo>=65 and codigo <=90:
    print("Es una letra Mayuscula ") 
if codigo>=97 and codigo <=127:
    print("Es una letra minuscula ")
    
    
    
#65/90 