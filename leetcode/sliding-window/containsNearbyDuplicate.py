# 219. Contains Duplicate II
# Link: https://leetcode.com/problems/contains-duplicate-ii/

## Description
# Given an integer array `nums`` and an integer `k``, return true if there
# are two distinct indices `i`` and `j`` in the array such that
# `nums[i] == nums[j]` and `abs(i - j) <= k`.

# Approach: Use a hashmap to store each element & keep track of the indicies.
        #           Then check if a repeated element is found by checking the abs difference
        #           between indicies i and j equals k. Greater than/equal return True, otherwise False.
def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # create a dictrionary lookup (hashmap) for storing previous k elements
        idx_hashmap = {}

        # iterate over all elements in `nums`
        for i in range(len(nums)):
            # check if an element already exists in the dict & check for abs difference
            if nums[i] in idx_hashmap and abs(i - idx_hashmap[nums[i]]) <= k:
                return True

            # add element in hashmap with respective index
            idx_hashmap[nums[i]] = i

        # otherwise, we haven't found any repeated values
        return False
