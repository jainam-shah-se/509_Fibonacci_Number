class Solution:
    def countOdds(self, low: int, high: int) -> int:
        diff =  (high - low)
        if low % 2 == 0 and high % 2 == 0 :
            return int (diff / 2)
        elif low % 2 == 0 and high % 2 != 0 :
            return int ((diff + 1) / 2)
        elif low % 2 != 0 and high % 2 == 0 :
            return int ((diff + 1) / 2)
        elif low % 2 != 0 and high % 2 != 0 :
            return int ((diff / 2) + 1)
        
    