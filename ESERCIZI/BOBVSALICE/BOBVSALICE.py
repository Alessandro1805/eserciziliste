import random
MAXL=6
MINL=1
NLANCI=10
bob=[random.randrange(MINL,MAXL) for i in range(NLANCI)]
alice=[random.randrange(MINL,MAXL) for i in range(NLANCI)]
file=open("risultati.txt","w");
print(bob)
print(alice)
for rb,ra in zip(bob,alice):
    file.write(f"{str(rb)},{str(ra)}")
    file.write("\n")