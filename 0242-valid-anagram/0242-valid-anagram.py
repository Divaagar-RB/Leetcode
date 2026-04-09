class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        hashmap = dict()
        for c in s:
            if c in hashmap:
                hashmap[c]+=1
            else:
                hashmap[c]=1
        
        for c in t:
            if c in hashmap:
                if hashmap[c]>0:
                    hashmap[c]-=1
                else:
                    return False

              
            else:
                print(c)
                return False

        return True
      
        
        