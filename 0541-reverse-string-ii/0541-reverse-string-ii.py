class Solution:
    def reverseStr(self, s: str, k: int) -> str:
       
        s = list(s)
        if k > len(s):
            k = len(s)
        for i in range(0,len(s),2*k):
            x = i
            j = i+k-1
            while j< len(s) and x<=j:
                s[x],s[j]=s[j],s[x]
                x+=1
                j-=1
        print(i)
        print(len(s)-i)
        print(k)
        if len(s)-i < k:
            j = len(s)-1
            while i < j:
                s[i],s[j]=s[j],s[i]
                i+=1
                j-=1

        return ''.join(s)



        