from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            candidate = target - num
            if num in seen:
                return [seen[num], i]
            seen[candidate] = i

        return []
