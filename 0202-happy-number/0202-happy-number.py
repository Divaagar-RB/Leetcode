class Solution:
    def isHappy(self, n: int) -> bool:
        numbers = set()
        happy = False
        res  = 0
        while not happy:
            while n > 0:
                digit = n%10
              
                res = res + digit**2
                n = n//10

            if res == 1:
                return True
            if res in numbers:
                return False
            numbers.add(res)
            n = res
            res = 0
          
        