# kinda like fibonacci sequence, start from the end, 
# and add the last two number tgt for the next number
class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for i in range(n - 1):
            temp = one + two
            one = two
            two = temp
        return two
        