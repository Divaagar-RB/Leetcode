class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        value_count = dict()
        res = []
        for i in range(k):
            if nums[i] in value_count:
                value_count[nums[i]]+=1
            else:
                value_count[nums[i]]=1
        def findX():
            temp = dict(sorted(value_count.items() , key=lambda item:(item[1],item[0]) ,reverse = True ))
            print(temp)
            count = 0
            sum = 0
            for key , values in temp.items():
                if count < x:
                    print(key)
                    print(values)
                    sum = sum+(key*values)
                    count+=1
                else:
                    break

            res.append(sum)
        findX()
        j = 0
        for i in range(k,len(nums)):
            
            value_count[nums[j]]-=1
            if nums[i] in value_count:
                value_count[nums[i]]+=1
            else:
                value_count[nums[i]]=1
            findX()
            j+=1


           
        return res
            
