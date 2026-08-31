class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        so we have 3 conditions- 1) row 2)column 3) sub-box that should not repeat numbers
        we will iterate once over each element , traversing rows then columns
        The box id for a given row,col = (row//3) * 3 + (col//3)
        we have 9 rows, 9 cols, and 9 sub-boxes
        for each (row,col) of the 9 rows, 
            - we store the number that we see on the board 
            - check if that exists for the given row
        we repeat the same for the 9 columns and 9 sub-boxes all in a single iteration 
        the first row in the values list is for rows,second for cols and third for sub-boxes

        """
        values =[
            [set() for _ in range(9)],
            [set() for _ in range(9)],
            [set() for _ in range(9)]
        ]
        for row in range(len(board)):
            for col in range(len(board[0])):
                box_id = (row//3) *3 + (col//3)
                if board[row][col]!="." and (board[row][col] in values[0][row] \
                 or board[row][col] in values [1][col] or \
                 board[row][col] in values [2][box_id] \
                 ):
                    return False
                else:
                    values[0][row].add(board[row][col])
                    values[1][col].add(board[row][col])
                    values[2][box_id].add(board[row][col])
        return True
                


