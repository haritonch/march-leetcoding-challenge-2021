class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ''
        numbers = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        symbols = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
        i = len(numbers) - 1
        while num:
            q, num = divmod(num, numbers[i])
            while q:
                ans += symbols[i]
                q -= 1
            i -= 1
        return ans
