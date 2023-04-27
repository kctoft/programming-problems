# Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
# link: https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/

## Description:
# Given an array of integers `arr` and two integers `k` and `threshold`,
# return the number of sub-arrays of size `k` and average greater than or equal to `threshold`.
def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        res = 0 # num qualified sub arrays
        cur_sum = sum(arr[:k-1]) # current sum of first window

        for l in range(len(arr) - k + 1):
            cur_sum += arr[l + k - 1] # calculate the sum each iteration in O(1)

            # check if subarray qualifies
            if (cur_sum / k) >= threshold:
                res += 1

            cur_sum -= arr[l]

        return res
