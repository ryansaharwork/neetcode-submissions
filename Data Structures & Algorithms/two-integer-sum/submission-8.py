class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numSeen = {} # num -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in numSeen:
                return [numSeen[diff], i]
            numSeen[n] = i