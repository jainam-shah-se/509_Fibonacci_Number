class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        uni = set()
        
        for num in nums:
            if num in uni:
                return True
                
            uni.add(num)
            
                
                
        return False
            
        
                
                
        