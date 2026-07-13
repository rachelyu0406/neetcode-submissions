# start from end, keep shifting the goal back 
# (if a prev location can reach the end, new goal is the prev location)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        if goal == 0:
            return True
        else:
            return False
        