vocali=input("inserisci una parola")#rimuove le vocali
d={"a":"","b":"b","c":"c","d":"d","e":"","f":"f","g":"g","h":"h","i":"","j":"j","k":"k","l":"l",
"m":"m","n":"n","o":"","p":"p","q":"q","r":"r","s":"s","t":"t","u":"","v":"v","z":"z"," ":"*"}
novocali=""
for lettera in vocali:
    novocali=novocali + d[lettera]
print(novocali)
print(vocali)