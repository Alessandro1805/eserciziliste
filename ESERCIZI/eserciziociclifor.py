lista1 = ["a","b","c","d"] 
lista2 = [1,2,3,4] 
# for su lista1 C-style
for i in range(0,len(lista1)):
    print(lista1[i])
# for su lista1 Python-style
for i in lista2:
    print(i)
# for su lista1 con enumerate 
for i,lettera in enumerate(lista1):
    print(i)
    print(lettera)
# # for su lista1 e lista2 Python-style (zip) 
for lettera,numero in zip(lista1,lista2):
    print(lettera)
    print(numero)
# # for su lista1 e lista2 C-style (range...) 
for i in range(0,len(lista2)):
    print(lista1[i])
    print(lista2[i])
diz = {"a":"1","b":"1"} 
# # for su diz usando items() 
for lettera,numero in items(diz):
    print(lettera)
    print(numero)
# # for su diz senza items()
for i in diz:
    print(diz[i])