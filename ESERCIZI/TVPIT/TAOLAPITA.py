def uploadlist():
    l1=[[i*t for i in range(0,11)]for t in range(0,11)]
    return  l1
def write(l1,file):
    for l in l1:
        for c in l:
            print(c, end='\t')
            file.write(f"{c}\t")
        file.write("\n")
        print("\n")
def main():
    l1=uploadlist();
    file = open("tavola.txt", 'w')
    write(l1,file)
if __name__=="__main__":
    main()