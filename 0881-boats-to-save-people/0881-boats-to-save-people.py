class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        numBoats = 0
        people.sort()
        start = 0 
        end = len(people)-1
        while start <= end:
            weight = people[start]+people[end]
            if weight ==limit:
                numBoats+=1
                start+=1
                end-=1
            elif weight > limit:
                numBoats+=1
                end-=1
            else:
                numBoats+=1
                start+=1
                end-=1
        return  numBoats
        