def somma(n,n1):
    n=n+n1
def diff(n,n1):
    n=n-n1
def prod(n,n1):
    n=n*n1
def div(n,n1):
    n=n//n1
n=int(input("inseriaci un numero"))#in base all'operatore fa divese operazioni
n1=int(input("inseriaci un numero"))
d={"+":somma(n,n1),"-":diff(n,n1),"/":div(n,n1),"*":prod(n,n1)}
print(d[input("inserisci operazine")])