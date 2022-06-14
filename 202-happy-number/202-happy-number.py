class Solution:
    def isHappy(self, n: int) -> bool:
        
        no = str(n)
        dic = []
        if no == "1":
            return True
        else:
            while no != "1":
                ss = [int(number) ** 2 for number in no]
                add = sum(ss)
                no = str(add)
                if str(no) in dic:
                    return False
                if(no == "1"):
                    return True
                dic.append(no)
            
            
        
            