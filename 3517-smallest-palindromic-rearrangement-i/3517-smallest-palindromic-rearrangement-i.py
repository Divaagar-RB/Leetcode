class Solution:
    def smallestPalindrome(self, s: str) -> str:
        res = []
        if len(s)==1:
            return s
        if len(s)%2 == 0:
            n = len(s)//2
            temp = s[:n]
            
            temp =sorted(temp)
            
            res.extend(temp)
            res.extend(temp[::-1])
            
        else:
            n = len(s)//2
         
            temp = s[:n]
            
            temp =sorted(temp)
            
            res.extend(temp)
            res.append(s[n])
            res.extend(temp[::-1])
        return ''.join(res)

        