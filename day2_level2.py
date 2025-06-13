##  Nivel 2

## 1
print (type(FirstName))
print (type(LastName))
print (type(FullName))
print (type(Country))
print (type(City))
print (type(Age))
print (type(Year))
print (type(Married))
print (type(is_true))
print (type(is_light_on))
print (type([Yo_Soy, Edad, Sitio, Encadenado]))

## 2
print (len(FirstName))

## 3
print ('la comparacion = ', len(FirstName)>len(LastName))

## 4 - 11
numeroUno = 5
numeroDos = 4
variablesSumadas = numeroUno + numeroDos
diferencia = numeroUno - numeroDos
producto = numeroUno * numeroDos
division = numeroUno / numeroDos
modulo = (numeroUno%numeroDos)
exponente = (numeroUno)^numeroDos
pisoDivision = numeroUno//numeroDos

## 12 El radio del circulo es treinta metros
pi = 3.1416
radio = 30
area_of_circle = (pi*((radio)**2))

circum_of_circle = ((2*radio)*pi)

RadioUsuario = input ("Dame el radio: \n")      ## AGUAS!!! Se maneja como cadena!!!
Radio_convertido = float(RadioUsuario)
AreaAuspiciadaPorUsuario = (pi*((Radio_convertido)**2))
print ("Area = \n" ,AreaAuspiciadaPorUsuario)

## 13
tuNombre = input ("Dame tu nombre: \n")
tuApellido = input ("Dame tu apellido: \n")
tuPais = input ("Dame tu Pais: \n")
tuEdad = input ("Deme su edad: \n")
print ("Tu nombre es: ",tuNombre)
print ("Tu apellido es: ",tuApellido)
print ("Tu pais es: ",tuPais)
print ("Tu edad es: ",tuEdad)
