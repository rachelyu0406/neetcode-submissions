class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        diff = defaultdict(List)
        res = []
        for i in range(len(numbers)):
            diff[numbers[i]] = i + 1
        for j in range(len(numbers)):
            if target - numbers[j] in diff:
                res.append(j + 1)
                res.append(diff[target - numbers[j]])
                break
        return res
        