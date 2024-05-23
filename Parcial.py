lista_Nombre = ["Andres","Cristiam","Gary","Stiven","Felipe"]
lista_Calificacion = [3.4, 2.0, 1.0, 1.5, 1.8]
lista_Asignaturas = ["PC","CC","EB","GEO","PB"]

def buscar(persona,lista):
    for i, nombre in enumerate (lista):
        if nombre==persona:
            return i
    return -1
est = (input("ingrese el nombre del estudiante "))
pos=buscar(est,lista_Nombre)
nota = lista_Calificacion [pos]
print(est,"saco ", nota)

    
