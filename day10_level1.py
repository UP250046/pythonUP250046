# Level 1
# 1
for i in range(0, 11):
    print(i)

print("---------------------------")

# 2
for i in range(10, -1, -1): # cuenta hacia atras
    print(i)

k = 10
while k >= 0:
    print(k)
    k -= 1

print("---------------------------")

# 3
hash_string = '#'
for i in range(1, 8):
    print(hash_string * i)

#4
for i in range(1, 9):   # Primero es el numero de filas desde 1 a 8
    for j in range(1, 9):
        print("#", end=' ')
    print()

# 5
for i in range(0, 11):
    print(i, "x", i, "=", i * i)

print("---------------------------")
# 6
for lang in ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']:
    print(lang) #imprime el nombre del lenguaje

# 7
for i in range(0, 101): # imprime los numeros del 0 al 100, pero solo los pares
    if i % 2 == 0: # % es el operador modulo, que da el residuo de la division
        print(i)

print("---------------------------")
# 8
for i in range(0, 101): # ahora solo los impares
    if i % 2 != 0:
        print(i)

