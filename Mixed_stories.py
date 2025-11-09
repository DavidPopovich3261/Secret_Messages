




def fi(file):
    with open(file,"r") as f:
        a=''
        b=''
        for i in range(1,len(file),2):
            a+=(f.readline())
            b+=(f.readline())
        a1=open('story_A.txt',"w")
        a1.write(str(a))
        b1=open("story_B.txt","w")
        b1.write(str(b))
        a1.close()
        b1.close()
        a2=open('story_A.txt')
        print(a2.read())
        b2=open("story_B.txt")
        print(b2.read())


fi('mixed_stories.txt')