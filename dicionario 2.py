diccionario={"Andres":{"pc":3.4 , "ge":2.8},
             "cristian":{"cc":2.0 , "al":4.0},
             "gary":{"eb":1.0},
             "stiven":{"ge":1.5 , "pc":2.5 , "pb":3.0},
             "felipe":{"pb":1.8}}
nombre = input("Escriba Nombre ")
if nombre in diccionario:
    materia = input("Esriba la Materia ")
    if materia in diccionario[nombre]:
        calificacion = diccionario[nombre][materia]
        print("su calificacion es de",calificacion)
    else:
        print("No esta la materia ")
else:
    print ("No esta en el registro")