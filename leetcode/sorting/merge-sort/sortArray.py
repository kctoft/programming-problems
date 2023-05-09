# Sort an Array
## Link: https://leetcode.com/problems/sort-an-array/

### Merge Sort: recursive Divide and Conquer approach
def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # base case
        if len(nums) < 2: return nums

        # take the floor value for mid point
        mid = len(nums) // 2
        # split the array into two halves
        left = nums[:mid]
        right = nums[mid:]

        # recursive call on each half
        self.sortArray(left)
        self.sortArray(right)

        # two iterators for traversing the two halves
        i = 0
        j = 0

        # iterator for the main list
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                # the value from the left half has been used
                nums[k] = left[i]
                # move the iterator forward
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            # move to the next slot
            k += 1

        # for all the remaining values
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nums[k]=right[j]
            j += 1
            k += 1

        return nums
