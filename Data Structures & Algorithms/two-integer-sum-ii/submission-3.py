class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            diff = target - numbers[l]
            if numbers[r] > diff:
                r -= 1
            elif numbers[r] < diff:
                l += 1
            else:
                print(numbers[l], numbers[r])
                return[l + 1, r + 1]