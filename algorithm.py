import heapq as hp
class trie:
    class node:
        def __init__(self, group, fa, id):
            self.group=group
            self.father=fa
            self.children={}
            self.char=" "
            self.id=id
            self.color=False
        def insert(self, stri):
            self.char=stri[0]
            if len(stri)==1:
                self.color=True
                return None
            else:
                if self.children.get(stri[1], -1)==-1:
                    self.group.append(trie.node(self.group, self.id, len(self.group)))
                    self.children[stri[1]]=len(self.group)-1
                self.group[self.children[stri[1]]].insert(stri[1:])
        def query(self, pre):
            ret=[]
            for i in self.children:
                ret.append(self.group[self.children[i]].query(pre+self.char))
            if self.color:
                ret.append(pre+self.char)
            return ret
        def query_pre(self, pre, deep):
            if deep==len(pre):
                data=self.query(pre[:-1])
                ret=[]
                def process_data(data):#展开嵌套列表
                    nonlocal ret
                    for i in data:
                        if isinstance(i, str):
                            ret.append(i)
                        else:
                            process_data(i)
                process_data(data)
                ret.sort(key=lambda x:"B"+x if " " in x else "A"+x)
                return ret
            else:
                if pre[deep] in self.children:
                    return self.group[self.children[pre[deep]]].query_pre(pre, deep+1)
                else:
                    return []
            
        
    def __init__(self):
        self.group=[]
        self.group.append(trie.node(self.group, -1, 0))
    def insert(self, stri):
        self.group[0].insert(" "+stri)
    def query(self, pre):
        return self.group[0].query_pre(pre, 0)
class correct:
    class word:
        def __init__(self, word, distance):
            self.word, self.distance=word, distance
        def __lt__(self, other):
            return self.word < other.word if self.distance==other.distance else self.distance<other.distance
        def __eq__(self, other):
            return self.word==other.word and self.distance==other.distance
        def __le__(self, other):
            return self.__lt__(other) or self.__eq__(other)
        def __gt__(self, other):
            return not self.__le__(other)
        def __ge__(self, other):
            return not self.__lt__(other)
    def __init__(self, dic):
        self.dic=dic
    def edit_distance(self, a, b, limit):
        if abs(len(a)-len(b))>int(max(len(a), len(b))*limit):
            return 499
        dp=[[0]*(len(b)+1) for i in range(len(a)+1)]
        for i in range(len(a)+1):
            for j in range(len(b)+1):
                if min(i, j)==0:
                    dp[i][j]=max(i, j)
                else:
                    dp[i][j]=min(
                        dp[i-1][j]+1,
                        dp[i][j-1]+1,
                        dp[i-1][j-1]+int(a[i-1]!=b[j-1])*2
                    )
        return dp[-1][-1]
    def query(self, word, word_limit=10, edit_limit=0.36):
        heap=[]
        count=[0]*500
        for i in self.dic:
            d=self.edit_distance(word, i, edit_limit)
            hp.heappush(heap, self.word(i, d))
            count[d]+=1
        for i in range(1, len(count)):
            count[i]+=count[i-1]
            if count[i]>=word_limit:
                result=[]
                x=hp.heappop(heap)
                while x.distance<=max(1, i-1):
                    result.append(x.word)
                    x=hp.heappop(heap)
                return result
        return [i.word for i in heap]
