class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        
        n = len(arr)
        summ = 0
        
        for i in range(n):
            for j in range(i+1, n+1):
                print(j - i)
                if (j - i) % 2:
                    
                    summ += sum(arr[i:j])
        return summ
        
                     
                    
            
        
        
            
                
        