class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        # for i in reversed(range(len(mat))):
        #     print(i)
        
        if len(mat) == 1:
            return mat[0][0]
        summ = 0 
        for i in range (0, len(mat)):
            for j in range (0, len(mat)):
                
                if i == j:
                    print(mat[i][j])
                    summ = summ + mat[i][j]
        
        for i in range(len(mat)):
            mat[i].reverse()
            
        for i in range (0, len(mat)):
            for j in range (0, len(mat)):
                
                if i == j:
                    print(mat[i][j])
                    summ = summ + mat[i][j]
        
        print(len(mat))
        if len(mat) % 2 != 0:
            print("Hello")
            x = int ((len(mat) - 1) / 2)   
            summ = summ - mat[x][x]
        return summ
                
 
    
            
        