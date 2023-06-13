# Container With Most Water
## Link: https://leetcode.com/problems/container-with-most-water/description/
def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        # use teh two pointer technique
        l, r = 0, len(height) - 1
        while l < r:
            # res is the max value of the area between the two pointers
            res = max(res, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                # increment LHS by 1 if L is too small
                l += 1
            elif height[r] <= height[l]:
                # otherwise, R is too small, decrement by 1
                r -= 1
        return res
