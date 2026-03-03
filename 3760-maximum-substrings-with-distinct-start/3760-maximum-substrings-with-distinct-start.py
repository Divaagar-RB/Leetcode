class Solution:
    def maxDistinct(self, s: str) -> int:
        ans = set()
        for c in s:
            ans.add(c)

        return len(ans)
        