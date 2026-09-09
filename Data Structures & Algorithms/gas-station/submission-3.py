#  greedy

# find diff of gas - cost and answer is the index where you can start and reach the end when you add the diff since answer is unique

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        total = 0
        start = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]

            if total < 0:
                total = 0
                start = i + 1
        
        return start

        

        