class Solution(object):
    """
        You are given an n x n integer matrix grid.
        Generate an integer matrix maxLocal of size (n - 2) x (n - 2) such that:

        maxLocal[i][j] is equal to the largest value of the 3 x 3 matrix
        in grid centered around row i + 1 and column j + 1.
        In other words, we want to find the largest value in every contiguous 3 x 3 matrix in grid.
        Return the generated matrix.

        :type grid: List[List[int]]
        :rtype: List[List[int]]

    """

    def largestLocal(self, grid):
        n = len(grid)
        max_local = []

        for i in range(n - 2):
            row = []
            for j in range(n - 2):
                row.append(0)
            max_local.append(row)

        for i in range(n - 2):
            for j in range(n - 2):
                max_value = grid[i + 1][j + 1]
                for k in range(3):
                    for l in range(3):
                        if grid[i + k][j + l] > max_value:
                            max_value = grid[i + k][j + l]
                max_local[i][j] = max_value

        return max_local
