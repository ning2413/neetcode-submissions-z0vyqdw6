class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix) - 1, len(matrix[0]) - 1
        l_row, r_row = 0, len(matrix) - 1
        row = -1
        while l_row <= r_row:
            mid = (l_row + r_row) // 2
            if target > matrix[mid][0] and target > matrix[mid][n]:
                l_row = mid + 1
            elif target < matrix[mid][0] and target < matrix[mid][n]:
                r_row = mid - 1
            else:
                row = mid
                break;
        if row == -1:
            return False
        print(row, matrix[row])
        l, r = 0, n
        while l <= r:
            mid = (l + r) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False
