# 3Sum
## Link: https://leetcode.com/problems/3sum/description/
def threeSum(self, nums):
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            # Skip positive integers
            if a > 0:
                break

            # passes over duplicate numbers for the 'a' position
            if i > 0 and a == nums[i - 1]:
                continue

            # solve using two pointers technique
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    # add a set to the res list
                    res.append([a, nums[l], nums[r]])
                    # update the points for next iteration
                    l += 1
                    r -= 1
                    # ensures no duplicate sets
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res
