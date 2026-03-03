class Solution:
    def multiply(self, m: str, n: str) -> str:
        ans = 0
        place = 0
        for i in range(len(m)-1,-1,-1):
            sum = 0
        
            k = 0
            
            for j in range(len(n)-1,-1,-1):

                sum = sum   + int(n[j])*int(m[i])*10**k
                k+=1
            ans = ans +( sum * 10 ** place)
            place+=1
        
        return str(ans)      