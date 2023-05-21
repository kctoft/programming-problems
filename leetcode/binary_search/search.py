# Binary Search
## Link: https://leetcode.com/problems/binary-search/
def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # create pointer for either end of the list
        l, r = 0, len(nums) - 1

        # iterate over all elements
        while l <= r:
                # update the midpoint each time, use floor division
                m = (l + r) // 2

                # check if m is bigger than target, if so, update RHS pointer
                if target > nums[m]:
                        r = m - 1
                # check if m is smaller than target, if so, update LHS pointer
                elif target < nums[m]:
                        l = m + 1
                # else, there is a MATCH
                else:
                        return nums[m]
        # otherwise, return -1
        return -1
