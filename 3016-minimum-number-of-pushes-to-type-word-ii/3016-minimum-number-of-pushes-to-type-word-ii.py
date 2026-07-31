class Solution:
    def minimumPushes(self, word: str) -> int:
        wordDict = dict()
        for i in word:
            if i in wordDict:
                wordDict[i]+=1
            else:
                wordDict[i]=1
        sorted_dict =  dict(sorted(wordDict.items(), key=lambda item: item[1], reverse=True))
        
        count = 0
        inc = 1
        res = 0
        for key , value in sorted_dict.items():
            res = res + (value*inc)
            
            count+=1
            if count == 8:
                inc+=1
                count = 0

        return res


        