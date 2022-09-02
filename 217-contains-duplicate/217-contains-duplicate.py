class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        uni = {}
        
        for num in nums:
            if num in uni:
                return True
                
            else:
                uni[num] = '0'
                
                
        return False
            
        
                
                
        