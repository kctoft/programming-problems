# Search a 2D Matrix
# Link: https://leetcode.com/problems/search-a-2d-matrix/

## Linear Search -- Time Complexity: O(m*n)
# def searchMatrix(self, matrix, target):
#         """
#         :type matrix: List[List[int]]
#         :type target: int
#         :rtype: bool
#         """
#         for i in range(len(matrix)):
#             for j in range(len(matrix[0])):
#                 if matrix[i][j] == target: return True
#         return False

## Iterative Binary Search -- Time Complexity: O(logm) + O(logn) = O(log(m*n))
def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rows = len(matrix)
        cols = len(matrix[0])
        start = 0
        end = rows * cols - 1

        while start <= end:
            mid = start + (end - start) // 2
            mid_val = matrix[mid / cols][mid % cols]

            if mid_val > target:
                end = mid - 1
            elif mid_val < target:
                start = mid + 1
            else:
                return True

        return False

