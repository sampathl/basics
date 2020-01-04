class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        i=j=0
        go_right=1
        go_left=0
        d={"row":[set() for i in range(9)],"column":[set() for i in range(9)],"matrix":[set() for i in range(9)]}
        def check_insert(i,j):
            #print(i,j,board[i][j],go_right,go_left)
            if board[i][j] in d["row"][i] and board[i][j] in d["column"][j] and board[i][j] in d["matrix"][(i//3)*3 + j//3]:
                return False
            else:
                #print(i,j,board[i][j])
                d["row"][i].add(board[i][j])
                d["column"][j].add(board[i][j])
                d["matrix"][(i//3)*3 + j//3].add(board[i][j])
            return True
        while j<=8 and i<=8:
            print(i,j,(i//3)*3 + j//3)
            if go_right==1:
                if j<=7:
                    j+=1
                    if board[i][j]!=".":
                        if not check_insert(i,j):
                            return False

            if go_left==1:
                if j>=1:
                    j-=1
                    if board[i][j]!=".":
                        if not check_insert(i,j):
                            return False
                        """if board[i][j] in d["row"][i] and board[i][j] in d["column"][j] and board[i][j] in d["matrix"][(i//3)*3 + j//3]:
                            return False
                        else:
                            #print("-",i,j,board[i][j])
                            d["row"][i].add(board[i][j])
                            d["column"][j].add(board[i][j])
                            d["matrix"][(i//3)*3 + j//3].add(board[i][j])"""
            if j==0 and go_left:
                if not check_insert(i,j):
                    return False
                i+=1
                go_right=1
                go_left=0
            elif j==8 and go_right:
                if not check_insert(i,j):
                    return False
                i+=1
                go_right=0
                go_left=1
            print()
        return True