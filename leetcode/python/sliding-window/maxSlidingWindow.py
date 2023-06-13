# Sliding Window Maximum
## Link: https://leetcode.com/problems/sliding-window-maximum/

# fixed sliding window
def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import deque
        q = deque() # stores the indicies
        res = []

        # pop smaller values from q
        for i, cur in enumerate(nums):
            while q and nums[q[-1]] <= cur:
                q.pop()
            q.append(i)

            # remove first element if it's outside the window (left)
            if q[0] == i - k:
                q.popleft()

            # if window has k elements add to results
            # (first k-1 windows have < k elements because we start from empty window
            # and add 1 element each iteration)
            if i >= k - 1:
                res.append(nums[q[0]])

        return res
