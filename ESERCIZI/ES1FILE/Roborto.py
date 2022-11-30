class Roborto:
        def __init__(self,nome,massa,uma):
            self.setNome(nome)
            self.setMassa(massa)
            self.setUmanoide(uma)
            self.getNome()
            self.isPericoloso()
        def setNome(self,args):
            self.nome=args
        def getNome(self):
            print(self.nome)
        def setMassa(self,mass):
            self.massa=mass;
        def setUmanoide(self,uma):
            self.umanoide=uma
        def isPericoloso(self):
            if(self.umanoide and self.massa>100):
                print("pericoloso")
            else:
                print("innocuo")
def main():
    nome=input("inserisci un nome")
    peso=int(input("inserisci peso"))
    umanoide=bool(input("umanoide?"))
    roborto=Roborto(nome,peso,umanoide)

if __name__=="__main__":
    main()
            
