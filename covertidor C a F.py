def convertir_grados(Celsius):
   """
   Programa para convertir grados celsius a fahrenheit
   """
   Fahrenheit = 9/5*Celsius+ 32
   return Fahrenheit
#__________________________________________________________________________________
#global
#_________________________________________________________________________________

C=float(input("Escriba temperatura en Celsius "))
print(C,"grados celsius equivalen a",convertir_grados(C),"Grados Fahrenheit")