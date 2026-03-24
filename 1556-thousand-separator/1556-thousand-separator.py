class Solution:
    def thousandSeparator(self, n: int) -> str:
        ans = ""
        count = 0
        if n == 0:
            return "0"
        while n > 0:
            digit = n % 10
            n = n // 10
            if count == 3:
                ans = str(digit) + "." + ans
                count = 1
                continue
            else:
                ans = str(digit) + ans

            count += 1
        return ans

        