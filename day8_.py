#1
dog = {}    # dog es un diccionario vacio

#2
dog = {"nombre": "Carlos", "color": "Negro", "raza": "pug", "patas": 4, "edad": 4}

#3
student_dictionary = {
    "Nombre": "Deivi",
    "Apellido": "Morales",
    "Genero": "H",
    "Edad": 22,
    "Estado": "soltero",
    "Habilidad": ["Procrastinar", "Dormir", "Comer"],
    "Pais": "Mexico",
    "Ciudad": "Aguascalientes",
    "Direccion": "tu corazon",
}

#4
print(len(student_dictionary))

#5
print(student_dictionary["Habilidad"]) 

#6
student_dictionary["Habilidad"].append("Programar") 

#7
list_keys = list(student_dictionary.keys()) # Convierte las claves del diccionario en una lista

#8
list_values = list(student_dictionary.values())

#9
list_of_tuples = [(k, v) for k, v in student_dictionary.items()] # Convierte el diccionario en una lista de tuplas

#10
student_dictionary.pop("Pais")  # Elimina la clave "Pais" del diccionario

#11
del dog 
