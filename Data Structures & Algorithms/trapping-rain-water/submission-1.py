class Solution:
    def trap(self, height: List[int]) -> int:
        # height of water at each index i is :
        # min(maxheight(left), maxheight(right)) - h[i]
        maxleft = [0] * len(height)
        maxright = [0] * len(height)
        curMax = float("-inf")
        for i in range(len(height)):
            if height[i] > curMax:
                curMax = height[i]
            maxleft[i] = curMax
        curMax = float("-inf")
        for j in range(len(height) - 1, -1, -1):
            if height[j] > curMax:
                curMax = height[j]
            maxright[j] = curMax
        res = 0
        for i in range(1, len(height) - 1):
            left = maxleft[i - 1]
            right = maxright[i + 1]
            water = min(left, right) - height[i]
            if water > 0:
                res += water
        return res
        