messaggio=input("inserisci il messaggio")
d={"a":"b","b":"c","c":"d","d":"e","e":"f","f":"g","g":"h","h":"i","i":"j","j":"k","k":"l","l":"m",
"m":"n","n":"o","o":"p","p":"q","q":"r","r":"s","s":"t","t":"u","u":"v","v":"z","z":"a"," ":"*"}
messaggioc=""
for lettera in messaggio:
    messaggioc=messaggioc + d[lettera]
print(messaggioc)
#for k,v in dizionario.items()























