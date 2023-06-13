# Contains Duplicate
## Link: https://leetcode.com/problems/contains-duplicate/description/
def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hash_map = dict()
        for i in nums:
            if i in hash_map:
                return True
            else:
                hash_map[i] = 1
        return False
