class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carryOn = 1
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += carryOn
            if digits[i] < 10:
                return digits
            else:
                digits[i] = 0
                carryOn = 1
        return [carryOn] + digits
        