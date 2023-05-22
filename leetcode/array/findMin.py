# Find Minimum in Rotated Sorted Array (MEDIUM)
## Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
## Tupe: Binary Search -TC:O(log n)
def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # use Binary Search: TC is O(log n), SC is O(1) bc constant space is used
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        return nums[l]
