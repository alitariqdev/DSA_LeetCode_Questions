class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        output =[]
        board = [["." for _ in range(n)] for _ in range(n)]
        
        columns = set()
        pos_diag = set()
        neg_diag = set()

        def dfs(row):

            if row == n:
                output.append(["".join(r) for r in board])
                return

            for col in range(n):
                if col in columns or (row+col) in pos_diag or (row-col) in neg_diag:
                    continue

                board[row][col] = "Q"
                columns.add(col)
                pos_diag.add(row + col)
                neg_diag.add(row - col)

                dfs(row + 1)

                board[row][col] = "."
                columns.remove(col)
                pos_diag.remove(row + col)
                neg_diag.remove(row - col)


        dfs(0)
        return output
