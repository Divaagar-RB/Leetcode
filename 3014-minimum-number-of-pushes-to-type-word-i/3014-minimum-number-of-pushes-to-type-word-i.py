class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        if n <= 8:
            return n
        res  = 0
        count = 0
        inc = 1
        print(n)
        while n > 0:
            res = res + inc
            print(inc)
            count+=1
            if count == 8:
                inc+=1
                count = 0

            n-=1
        return res

        