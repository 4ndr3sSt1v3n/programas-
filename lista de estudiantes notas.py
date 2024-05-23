dic_est={"Andres":3.4,
         "cristian":2.0,
         "gary" :1.0,
         "steven":1.5,
         "Felipe":1.8,}

dic_notas={"Andres":[3.4,"pc"],
         "cristian":[2.0,"cc"],
         "gary" :[1.0,"eb"],
         "steven":[1.5,"ge"],
         "Felipe":[1.8,"pb"]}
nombre = input("estudiante ")
print("el estudiante",nombre, "saco", dic_notas[nombre][0], "en", dic_notas[nombre][1])