class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        return Counter(s) == Counter(t)
        
        ch_dict = {}
        ch_dict2 = {}
        
        for i in s:
            if i in ch_dict:

                cnt = ch_dict.get(i)
                cnt += 1
                # print(cnt)
                ch_dict[i] = cnt
                
            else:
                
                ch_dict[i] = 1
            
        for i in t:
            if i in ch_dict2:

                cnt1 = ch_dict2.get(i)
                cnt1 += 1
                # print(cnt)
                ch_dict2[i] = cnt1
                
            else:
                
                ch_dict2[i] = 1
            
        # print(ch_dict)
        # print(ch_dict2)
        
        if (ch_dict == ch_dict2):
            return True
        return False
            
        
        
        
        