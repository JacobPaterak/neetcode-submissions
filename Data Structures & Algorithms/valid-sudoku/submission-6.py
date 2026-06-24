class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hashset = set()
        for i in range(9):
            hashset.clear()
            for num in board[i]:
                
                if num in hashset:
                    return False
              
                if num != ".":
                    hashset.add(num)

        for i in range(9):
            hashset.clear()
            for j in range(9):
                if board[j][i] in hashset:
                    return False
                if board[j][i] != ".":
                    hashset.add(board[j][i])
    
       

        t = -1
        total = 0
        offset = 0
        while total <9:
            hashset.clear()
            if t ==8:
                t = -1
                offset +=3
            for i in range(3):
                print(hashset)
                t+=1
                b= offset-1
                for j in range(3):
                    b +=1
                    print(board[t][b])
                    if board[t][b] in hashset:
                        return False
                    if board[t][b] != ".":
                        hashset.add(board[t][b])
            total+=1
            




        return True