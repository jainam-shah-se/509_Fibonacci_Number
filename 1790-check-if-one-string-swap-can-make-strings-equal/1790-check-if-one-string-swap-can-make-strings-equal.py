class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        else:
            lst = []
            for i in range(0, len(s2)):
                tlst = []
                if s1[i] != s2[i]:
                    tlst.append(s1[i])
                    tlst.append(s2[i])
                    lst.append(tlst)
                    tlist = []
            if len(lst) > 2:
                return False
            elif len(lst) == 2:
                
                lst[0].reverse()
                if lst[0] == lst[1]:
                    return True
                else:
                    return False
            else:
                return False
                
            
                    
            
        