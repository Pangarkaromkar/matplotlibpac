from  typing import List
class solution:
    def solveQueens(self, n:int)-> List[List[str]]:
        col=set()
        posDiag=set()
        negDiag=set()
        res=[]
        board=[["."] * n for _ in range(n)]
        
        def backtrack(r):
            if r == n:
                
                copy=["".join(row) for row in board]
                res.append(copy)
                return
            
                for c in range(n):
                    if c in col or (r + c) in posDiag or (r - c) in negDiag:
                        continue
                        
                    col.add(c)
                    posDiag.add(r+c)
                    negDiag.add(r-c)
                            
                    board[r][c] = "Q"
                    backtrack(r+1)
                            
                    col.remove(c)
                    posDiag.remove(r+c)
                    negDiag.remove(r-c)
                    board[r][c]= "."
                            
                    backtrack(0)
                    return res
                        
solution_instance = solution()
n=4
results= solution_instance.solveQueens(n)
                    
for solution in results:
    for row in solution:
        print(row)
    print()
                        