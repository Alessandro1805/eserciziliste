#modo preferito (pythonico)
lista=[110,12,45,23,66]
minimo=lista[0]
massimo=lista[0]
for elemento in lista[1:]:
    if minimo>elemento:
        minimo=elemento
    else:
        pass
    if massimo<elemento:
        massimo=elemento
print(minimo)
print(massimo)