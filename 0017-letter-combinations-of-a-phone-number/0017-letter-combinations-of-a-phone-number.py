from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        ans = []
        size = len(digits)
        def backtrack(i , current):
            if len(current) == size:
                ans.append(current)
                return
            digit = phone[digits[i]]
            for cha in digit:
                backtrack(i+1, current+cha)
            return
        backtrack(0,"")
        return ans
        