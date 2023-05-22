# Maximum Product Subarray
## Link: https://leetcode.com/problems/maximum-product-subarray/
# DYNAMIC PROGRAMMING problem
def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # brute force: linear search TC: O(n^2)
        # use dynamic programming --> reduces TC to O(n) and SC to O(1)

        # use subarrays, set for 1st element
        res = nums[0]
        cur_max, cur_min = 1, 1

        for i in nums:
            temp = cur_max * i
            cur_max = max(cur_max * i, cur_min * i,  i)
            cur_min = min(temp, cur_min * i,  i)
            res = max(res, cur_max)

        return res
