class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        no_cnt = {}
        ans = []
        for no in nums:
            
            if no in no_cnt:
                no_cnt[no] += 1
            else:
                no_cnt[no] = 1
        
        no_cnt = sorted(no_cnt.items(), key=lambda item: item[1], reverse=True)
        for i in range(0, k):
           ans.append(no_cnt[i][0])
        return ans
        
            