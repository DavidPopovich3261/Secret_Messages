




def fi(file):
    with open(file,"r") as f:
        a=[]
        for i in range(0,len(file),2):
            a.append(f.readline())
