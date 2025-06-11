## 1 - 4
miEdad = 22
miAltura = 1.64
complejo = (3 - 4j)

base = input ("Dame la base (es 20): \n")
altura = input ("Dame la altura (es 10): \n")
baseint = int(base)
alturaint = int(altura) 
area = (0.5*(baseint*alturaint))
print (area)

## 5
a_lado = int(input("Dame el lado A (es 5):\n"))     ## Aca me di cuenta que puedo castear y usar input a la vez :))
b_lado = int(input("Dame el lado B (es 4):\n"))
c_lado = int(input("Dame el lado A (es 3):\n"))
print ("El perimetro es: ",a_lado + b_lado + c_lado)

## 6
ancho = int(input("Dame el ancho: \n"))
largo = int(input("Dame el largo: \n"))
print ("El area del rectangulo es: ",ancho*largo)
print ("El perimetro del rectangulo es: ",2*(ancho+largo))

## 7
radio = int(input("Dame el radio del circulo: \n"))
pi = 3.14
area = pi*(radio*radio)
print ("El area del triangulo es: ",area)
circunferencia = 2*(pi*radio)
print ("Circunferencia del circulo: ",circunferencia)

## 8
print ("X interseccion: ", 1)
print ("Y interseccion: ", -2)
print ("pendiente: ", 2)

## 9 
x1, x2, y1, y2 = 2, 6, 2, 10
print ('Distancia: ')
print ('{0:.2f}'.format(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5))
print ('Pendiente:')
print ((y2 - y1) / (x2 - x1))

## 10
print(2 if 2 < (y2 - y1) / (x2 - x1) else (y2 - y1) / (x2 - x1))

# 11
for x in range(0, 10):
    print(x ** 2 + 6 * x + 9)
print(3, -3, "is where y is 0")

# 12
print(not len('python') == len('dragon'))

# 13
print('on' in 'python' and 'on' in 'dragon')

# 14
print('jargon' in "I hope this course is not full of jargon")

# 15
print('on' not in 'python' and 'on' in 'dragon')

# 16
print(str(float(len('python'))))

# 18
number = int(input('Enter number:'))
print("Even" if number % 2 == 0 else "Odd")

# 19
print(type('10') == type(10))

# 20
print(int('9.8') == 10)

# 21
hours = int(input('Enter hours:'))
rph = int(input('Enter rate per hour:'))
print("Weekly Earning:", hours * rph)

# 22
years = int(input('Enter years:'))
print(years * 365 * 24 * 60 * 60 * 60)

# 23
for i in range(1, 6):
    print(i, i ** 0, i ** 1, i ** 2, i ** 3)
