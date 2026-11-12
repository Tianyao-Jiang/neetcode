class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        selected_row = 0

        for i in range(len(matrix)):
            l = matrix[i][0]
            r = matrix[i][-1]

            if l <= target <= r:
                selected_row = i

        l = 0
        r = len(matrix[0]) - 1

        while l <= r:

            mid = l + (r - l) // 2

            if matrix[selected_row][mid] == target:
                return True
            elif matrix[selected_row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False