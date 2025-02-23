if __name__=="__main__":
    import lookup as lk, os
    from sys import platform
    from algorithm import prefix, correct
    t=prefix(lk.dic)
    cor=correct(lk.dic)
    if platform in ["nt", "win32"]:
        os.system("cls")
    else:
        os.system("clear")
    while True:
        s=input(":")
        if platform in ["nt", "win32"]:
            os.system("cls")
        else:
            os.system("clear")
        c='f'
        if len(s)>1 and s[1]==':':
            c=s[0]
            s=s[2:]
        if c=='f':
            lk.lookup_cui(s)
        if c=='c':
            q=cor.query(s, word_limit=20, edit_limit=0.4)
            if len(q)>=40:
                print("too many (%d) results to show."%len(q))
            if len(q)==0:
                print("no result.")
            print("correct")
            for i in q:
                print("  "+i)
        if c=="p":
            if "-" in s:
                q=t.query_area(s.split("-")[0], s.split("-")[1])
            else:
                q=t.query(s) 
            if len(q)>=160:
                print("too many (%d) results to show."%len(q))
                continue
            x=[[]]
            pos=0
            leng=0
            for i in q:
                leng=max(len(i), leng)
                x[pos].append(i)
                if len(x[pos])>=((2 if len(q)<=30 else 4 )if len(q)<=100 else 5):
                    x.append([])
                    pos+=1
            if len(q)==0:
                print("no result.")
                continue
            print("prefix")
            for i in x:
                print(" ", end="")
                for j in i:
                    print(j, " "*(leng-len(j)), end="")
                print()
        if c=='e':
            break
            
    
else:
    raise Exception("This is not a module. Please run it as a program.")
