# Search in Rotated Sorted Array
## Link: https://leetcode.com/problems/search-in-rotated-sorted-array/
# HINT: O(log n) means use Binary Search!! Draw out examples with a graph (line & piecewise)
def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2

            if target == nums[m]:
                return m

            # left sorted portion
            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1

            # right sorted portion
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        return -1
