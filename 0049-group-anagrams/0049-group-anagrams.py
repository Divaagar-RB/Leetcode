class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = dict()
        for c in strs:
            temp = sorted(c)
            temp =''.join(temp)
            if temp in hashmap:
                hashmap[temp].append(c)
            else:
                hashmap[temp]=[c]
        res = []
        for values in hashmap.values():
            res.append(values)

        
        return res
        