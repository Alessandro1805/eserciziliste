num=int(input("inserisci un numero"))
ind=0
for i in range(2,num-1):
    if (num%2==0):
        ind=ind+1
if (ind==0):
    print("il numero è primo")
else:
    print("numero non primo")
    
