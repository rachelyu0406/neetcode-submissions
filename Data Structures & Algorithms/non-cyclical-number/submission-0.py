class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            temp = 0
            while n > 0:
                digit = n % 10
                n = n // 10
                temp += digit * digit
            if temp in seen:
                return False
            seen.add(temp)
            n = temp
        
        return True
        