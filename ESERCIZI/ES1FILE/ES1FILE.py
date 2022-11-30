def readFile(name):
    file = open(name, 'r')
    dizMat = {'id': [], 'nomi': []}
    lista_righe = file.readlines()

    for line in lista_righe[1:]:
        arr = line[:-1].split(',')
        dizMat['id'].append(int(arr[0]))
        dizMat['nomi'].append(arr[1][1:])

    file.close()
    return dizMat

diz = readFile('/home/alessandro/Documenti/SISTEMI/ES1FILE/dati.csv')
print(diz)
n=int(input("inserisci id"))
for i,id in enumerate(diz["id"]):
    if(id==n):
        c=i
print(diz["nomi"][c])
