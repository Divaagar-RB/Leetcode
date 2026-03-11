class Solution:
    def maximumXor(self, s: str, t: str) -> str:
        zero = 0
        ones = 0
        for i in t:
            if i == "0":
                zero+=1
            else:
                ones+=1
        res = ""
        for i in s:
            if i == "1" :
                if zero != 0:
                    res = res + "1"
                    zero-=1
                else:
                    res = res + "0"
            else:
                if ones != 0:
                    res = res + "1"
                    ones-=1
                else:
                    res = res + "0"

        return res
