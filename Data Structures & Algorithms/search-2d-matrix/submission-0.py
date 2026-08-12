class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix)
        for i in range(len(matrix)):
            index = (l+r)//2
            if matrix[index][0] == target:
                return True
            elif matrix[index][0] > target:
                r = index
            else:
                l = index
        l = 0
        r = len(matrix[0])
        for i in range(len(matrix[0])):
            indexj = (l + r)//2
            if matrix[index][indexj] == target:
                return True
            elif matrix[index][indexj] > target:
                r = indexj
            else:
                l = indexj
        return False