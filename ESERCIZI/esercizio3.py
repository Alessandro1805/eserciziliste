def isprimo(x):
    primo=True
    i=2
    for i in range (2,int(x**0.5)+1):
        if(x%i==0):
            primo=False
            return primo
        i=i+1 
    return primo
n=int(input("inserisci un numero"))
l=[i for i in range(1,n) if isprimo(i)]
print(l)