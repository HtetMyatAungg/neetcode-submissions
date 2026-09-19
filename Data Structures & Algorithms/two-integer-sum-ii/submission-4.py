class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = {}
        for i, num in enumerate(numbers):
            n[num] = i + 1
        for i in range(len(numbers)):
            if target - numbers[i] in n:
                return[i + 1, n[target - numbers[i]]]