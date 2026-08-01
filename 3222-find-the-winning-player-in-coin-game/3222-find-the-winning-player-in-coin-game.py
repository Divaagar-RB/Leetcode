class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        a = min(x,y//4)
        if a%2==1:
            return "Alice"
        else:
            return "Bob"
