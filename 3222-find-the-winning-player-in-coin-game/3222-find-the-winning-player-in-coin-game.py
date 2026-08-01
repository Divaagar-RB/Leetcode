class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        i = 0
        while x > 0 and y >= 4:
            
           
            x = x-1
            y = y-4
            i+=1
      
        return "Alice" if i%2==1 else "Bob"