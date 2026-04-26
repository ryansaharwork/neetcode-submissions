class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myStack = set()

        for num in nums:
            if num in myStack:
                return True
            else:
                myStack.add(num)
        return False
            