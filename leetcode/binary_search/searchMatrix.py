# Search a 2D Matrix
# Link: https://leetcode.com/problems/search-a-2d-matrix/

## Linear Search: O(m*n)
def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == target: return True
        return False

# def searchMatrix(self, matrix, target):
#         """
#         :type matrix: List[List[int]]
#         :type target: int
#         :rtype: bool
#         """

#         return False
