# Maximum Subarray
## Link: https://leetcode.com/problems/maximum-subarray/description/
def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur_subar = max_subar = nums[0]

        for n in nums[1:]:
            cur_subar = max(n, cur_subar + n)
            max_subar = max(max_subar, cur_subar)

        return max_subar
