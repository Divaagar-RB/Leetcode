class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        storage = dict()
        for i in range(len(list1)):
            storage[list1[i]]=i
        ans = [[] for _ in range(len(list1)*len(list2))]
        
        for i in range(len(list2)):
            if list2[i] in storage:
                ans[i+storage[list2[i]]].append(list2[i])
                
        for a in ans:
            if len(a)!=0:
                return a
               
       