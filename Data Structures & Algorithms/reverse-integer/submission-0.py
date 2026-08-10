class Solution:
    def reverse(self, x: int) -> int:
        # reconstruct the interger by adding one digit at a time
        # each time increasing the previous result by 10 times and adding a ones digit
        # before adding that ones digit each time you check if the previous digit is greater than max // 10 or if its equal and the new ones digit is greater than the last digit of max
        # if either is true dont add since you will go over and just return 0
        MIN = -2147483648
        MAX = 2147483648

        res = 0
        while x:
            digit = int(math.fmod(x, 10))
            x = int(x / 10)
            if (res > MAX // 10 or res < MIN // 10) or (res == MAX // 10 and digit > MAX % 10) or (res == MIN // 10 and digit < MIN % 10):
                return 0
            res = res * 10 + digit
        return res
        