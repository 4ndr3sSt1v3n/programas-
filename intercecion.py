lista1 = [15,9,10,56,78,4,6,21]
lista2 = [3,5,9,4,25,21,10,13]
interseccion = [elemento for elemento in lista1 if elemento in lista2]
print(interseccion)


lista4 =[elemento for elemento in range (1,10)]
print(lista4)
lista3=[]
for elemento in lista1:
    if elemento in lista2:
        lista3 += [elemento]
        print(lista3)