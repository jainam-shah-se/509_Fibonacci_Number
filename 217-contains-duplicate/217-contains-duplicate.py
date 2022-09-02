class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        uni = {}
        
        for num in nums:
            if num in uni:
                return True
                print(uni)
                print(num)
            else:
                uni[num] = '0'
                
                print("Hello")
        return False
            
        
                
                
        