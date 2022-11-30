#non esiste privato o publicco
MAXSB=32
class IPadress():
    def __init__(self,ip_stringa):
        self.ip_notazione=ip_stringa
        self.ip_bin=None
    def toList(self):
        l_string=self.ip_notazione.split(".")
        return[int(gruppo) for gruppo in l_string]
    def dec2bin(self):
        l_string=self.ip_notazione.split(".")
        s=""
        for i in l_string:
            conv=bin(int(i))[2:]
            conv="0"*(8-len(conv))+conv
            listbin=[]
            listbin.append(conv)
            print(listbin)
            s=s+conv+"."
        self.ip_bin=s[:-1]
    def ipbrodcast(self,subnetmusk="/24"):
        sbm=subnetmusk[1:]
        warsp="."
        newnum=""
        self.dec2bin()
        supp=""
        supp=self.ip_bin[:8]+self.ip_bin[9:17]+self.ip_bin[18:26]+self.ip_bin[27:35]
        print(supp)
        nuno=MAXSB-int(sbm)
        newnum=supp[:-nuno]+'1' * (MAXSB-nuno)
        var=newnum[0:8]+'.'+newnum[9:18]+'.'+newnum[18:26]+'.'+newnum[27:35]
        newnum=str(int(var[0:8],base=2))+'.'+str(int(var[10:18],base=2))
        print(newnum)
        print(var)
def main():
    indirizzoIP=IPadress("192.169.0.1")
    print(indirizzoIP.ip_notazione)
    print(indirizzoIP.toList())
    print(indirizzoIP.dec2bin())
    indirizzoIP.ipbrodcast("/24")
if __name__=="__main__":
    main()