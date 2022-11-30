dizionario={"w":"avanti","a":"sinistra","s":"destra","d":"dietro","i":"avanti","j":"sinistra","l":"destra","k":"dietro"}
comando="avanti"
indice=[]
for chiave in dizionario:#Dato un comando carica in una lista con il tasto corrispondente
  if dizionario[chiave]==comando:
    indice.append(chiave)
print(indice)
for indice,elemento in enumerate(dizionario):#ciclo for su un dizionairo
    print(indice,elemento)