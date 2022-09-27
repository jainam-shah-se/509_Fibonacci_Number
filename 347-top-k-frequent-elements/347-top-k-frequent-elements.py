class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
#         no_cnt = {}
#         ans = []
#         for no in nums:
            
#             if no in no_cnt:
#                 no_cnt[no] += 1
#             else:
#                 no_cnt[no] = 1
        
#         no_cnt = sorted(no_cnt.items(), key=lambda item: item[1], reverse=True)
#         for i in range(0, k):
#            ans.append(no_cnt[i][0])
#         return ans
        
        count = {}
        freq = [[] for i in range(len(nums)+1)]
        
        for num in nums:
            
            count[num] = 1 + count.get(num, 0)
        
        for n,c in count.items():
            freq[c].append(n)
        
        ans = []
        for i in range(len(freq)-1, 0, -1):
            for j in range(len(freq[i])):
                ans.append(freq[i][j])
                
                if len(ans) == k:
                    return ans