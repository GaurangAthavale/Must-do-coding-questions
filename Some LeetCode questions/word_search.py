def search(i,j,index,board,word,visited):
    if(index == len(word)):
        return True
    
    if(i<0 or i>=len(board) or j<0 or j>=len(board[i]) or board[i][j]!=word[index] or visited[i][j]):
        return False
    
    visited[i][j] = True
    if(search(i-1,j,index+1,board,word,visited) or search(i,j-1,index+1,board,word,visited) or search(i+1,j,index+1,board,word,visited) or search(i,j+1,index+1,board,word,visited)):
        return True
    
    visited[i][j] = False
    return False

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = [[False for i in range(len(board[0]))] for j in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[i])):
                if(board[i][j] == word[0] and search(i,j,0,board,word,visited)):
                    return True
        return False
    