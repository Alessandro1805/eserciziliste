from re import S


l=[0,0,0,0]
n1=int(input("inserisci un numero"))
n2=int(input("inserisci un numero"))
l[0]=n1*n1+n2*n2
l[1]=(n1+n2)*(n1+n2)
l[2]=(n1*n1)-(n2+n2)
l[3]=(n1-n2)*(n1-n2)
print(l)