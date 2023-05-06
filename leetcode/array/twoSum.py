# Two Sum
## Link: https://leetcode.com/problems/two-sum/description/
def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = {}   # value -> index

        for idx, value in enumerate(nums):
            diff = target - value
            if diff in hash_map:
                return [hash_map[diff], idx]
            hash_map[value] = idx
