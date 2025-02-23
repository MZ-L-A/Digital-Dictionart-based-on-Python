import json, sys
with open("format.txt", "r") as pth:
    dic=json.loads(pth.readline())
phrase={}
source={}
for i in dic:
    for j in dic[i]["phrase"]:
        phrase[j]=dic[i]["phrase"][j]
        if j in source:
            source[j]+=","+i
        else:
            source[j]=i
def main():
    def get_argv(equals={}):#equals means the shortcut of the long option
        if len(sys.argv)==1:
            return ((),{"help":True})
        try:
            argv=sys.argv[1:]
            args=[]
            options={}
            for i in argv:
                if (i[0]=='-' and i[1]!='-') or i[0]=='/':
                    for j in i[1:]:
                        if j in equals:
                            options[equals[j]]=True
                        else:
                            options[j]=True
                elif i[0]=='-' and i[1]=='-':
                    n=i[2:].split("=")
                    if len(n)==1:
                        options[n[0]]=True
                    else:
                        options[n[0]]="=".join(n[1:])
                else:
                    args.append(i)
            return (tuple(args), options)
        except:
            return ((),{"help":True})
    args, options=get_argv({"h":"help"})
    def help():
        print('''This program is use for looking up words in a dictionary.
    usage:python3 lookup [word | --help | -h]

        --help, -h        show the usage of this program.
    ''')
        exit(0)
    if options.get("help", False):
        help()
    word=args[0]
    lookup_cui(word)
def lookup_cui(word):
    if not word in dic:
        if not word in phrase:
            print("\"%s\" not found."%word)
            return None
        print("%s(from %s)"%(word, source[word]))
        print("  phr.", phrase[word])
        return None
    print(word)
    m=dic[word]
    for i in m["meaning"]:
        print(" ", i, m["meaning"][i])
    if not m["phrase"] == {}:
        print("phrase")
        for i in m["phrase"]:
            print(" ", i, m["phrase"][i])
def lookup_format(word):
    if not word in dic:
        if not word in phrase:
            return [(1, 0, "The word %s not found."%word)]
        return [(2, 0, "%s(from %s)"%(word, source[word])), (0, 1, "phr. "+phrase[word])]
    result=[(3, 0, word)]
    m=dic[word]
    for i in m["meaning"]:
        result.append((0, 1, i+" "+m["meaning"][i]))
    if not m["phrase"] == {}:
        result.append((2, 0, "phrase"))
        for i in m["phrase"]:
            result.append((0, 1, i+" "+m["phrase"][i]))
    return result
def get_what_to_find():
    x=[]
    x.extend(sorted(dic))
    x.extend(sorted(phrase))
    return x
if __name__=="__main__":
    main()


