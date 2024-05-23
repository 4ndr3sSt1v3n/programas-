lista_Nombre = ["Andres","Cristiam","Gary","Stiven","Felipe"]
lista_Calificacion = [3.4, 2.0, 1.0, 1.5, 1.8]
lista_Asignaturas = ["PC","CC","EB","GEO","PB"]
#1 Que tipo de dato es Lista_Calificaciones 
print(type(lista_Calificacion))
#2 Cuantos elementos tiene Lista_Nombres
Elementos = len(lista_Nombre)
print("la lista tiene ", Elementos ,"Elementos")
#3 Compruebe que la lista tienen la misma cantidad de estudiantes
if set(lista_Nombre) == set(lista_Calificacion) == set(lista_Asignaturas):
    print ("las listas tienen diferentes elementos. ")
else:
    print("Todas las lista tienen los mismo elementos.")
#4 Imprima lista_Nombre al reves
lista_Nombre.reverse()
print(lista_Nombre)
#5 Dado un estudiante, indique la posicion de la lista en que esta
elementos = (input("ingrese el nombre del estudiante "))
if elementos in lista_Nombre:
    posicion = lista_Nombre.range(elementos)
    print("El Nombre ", elementos, "se encuentra en la posicion", posicion)
else:
    print("El Nombre", elementos, "no esta en la lista")


                  

