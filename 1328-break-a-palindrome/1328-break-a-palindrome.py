class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        print(len(palindrome))
        if len(palindrome)==1:
            return ""
        
        temp = "a"
    
        for j in range(len(palindrome)//2):
            if temp!=palindrome[j]:
              
                
                ans = palindrome[:j]+temp+palindrome[j+1:]
                return ans
                
        return palindrome[:len(palindrome)-1]+"b"
        