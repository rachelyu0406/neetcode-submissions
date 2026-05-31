class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        one, two = cost[0], cost[1]
        cost.append(0)
        for i in range(2, n):
            temp = cost[i] + min(one, two)
            one = two
            two = temp
        return min(one, two)


        """
        # not optimized
        n = len(cost)
        minCost = [float("inf")] * (n + 1)
        minCost[0] = cost[0]
        minCost[1] = cost[1]
        cost.append(0)
        for i in range(2, n + 1):
            minCost[i] = cost[i] + min(minCost[i - 1], minCost[i - 2])
        return minCost[n]
        """
        