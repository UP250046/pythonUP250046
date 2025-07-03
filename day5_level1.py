# 1
lista = list()

#2
games = ['MH', 'Minecraft', 'VivaPinata', 'Terraria', 'Cs2']

# 3
print(len(games))

# 4
primero = games[0]
segundo = games[2]
tercero = games[4]
print(primero, "<---Este es el primero", segundo , "<---Este es el de en medio", tercero, "<---Este es el ultimo")

# 5
mixed_data_types = ["Deivi", "22", "1.64", "Soltero", "Palma Canaria, tu casa",]

# 6
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# 7
print(it_companies)

# 8
print(len(it_companies))

# 9
primero = it_companies[0]
segundo = it_companies[3]
tercero = it_companies[6]
print(primero)
print(segundo)
print(tercero)

# 10
print(it_companies)
it_companies[0] = "Instagram"
print(it_companies)

#11
it_companies.append('Cisco')
print(it_companies)

# 12
it_companies.insert(4, "Huawei")
print (it_companies)

#13
it_companies[4] = it_companies[4].upper()
print (it_companies)

# 14
it_companiesNumeral = '#'.join(it_companies)
print(it_companiesNumeral)

# 15
print('IBM' in it_companies)    ##Verifica si IBM está en la lista

# 16
it_companies.sort()     ##Ordena alfabéticamente
print(it_companies)

# 17
it_companies.reverse()  ##Invierte el orden
print(it_companies)

# 18
it_companies = it_companies[3:] ##Elimina los tres primeros elementos
print(it_companies)

it_companies = it_companies[:len(it_companies) - 3]
print(it_companies)  ##Elimina los tres últimos elementos

# 20
it_companies = it_companies[0:len(it_companies) // 2] + it_companies[len(it_companies) // 2 + 1:]
print(it_companies)  ##Elimina el elemento del medio

# 21
it_companies.pop(0)  ##Elimina el primer elemento
print(it_companies)

# 22
it_companies.pop(len(it_companies) - 1)  ##Elimina el último elemento
print(it_companies)

# 23
it_companies.pop(len(it_companies) - 1)

# 24
it_companies.clear()

# 25
del it_companies

# 26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
front_end.append(back_end)

# 27
full_stack = front_end
indx = full_stack.index('Redux')
full_stack = full_stack[:indx] + ['Python', 'SQL'] + full_stack[indx:]

