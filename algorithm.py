import heapq as hp
def search(item, table):
    p, step=0, len(table)>>1
    while step>0:
        if p+step<len(table) and table[p+step]<=item:
            p+=step
        else:
            step=step>>1
    return p
class prefix:
    def __init__(self, words=[]):
        self.words=sorted(words)
    def query(self, pre, b=None):
        p=pre
        q=b
        if b==None:
            q=pre+"~"
        return self.query_area(p, q)
    def query_area(self, p, q):
        r=search(p, self.words)
        s=search(q, self.words)
        return sorted(self.words[r+(self.words[r]!=p):s+1], key=lambda x:(int(" " in x), x))
    

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
