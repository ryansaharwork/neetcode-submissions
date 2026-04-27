class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        # Create a hash map to store frequency of each number
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        # Build a list of [frequency, number] pairs from the map
        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])

        # Sort this list in ascending order based on frequency
        arr.sort()

        # Create an empty result list
        res = []

        # Repeatedly pop from the end of the sorted list (highest frequency)
        # and append the number to the result.
        # Stop when result contains k elements
        while len(res) < k:
            res.append(arr.pop()[1])
        
        # Return the result list
        return res

