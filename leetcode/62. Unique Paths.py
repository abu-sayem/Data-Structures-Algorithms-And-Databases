class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        store = [[0 for _ in range(n)] for _ in range(m)]

        def path(row, col):
            if row == m-1 and col == n-1:
                return 1
            if row == m or col == n:
                return 0
            if not store[row][col]:
                store[row][col] = path(row+1, col) + path(row, col+1)
            return store[row][col]
        return path(0, 0)
