class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lst = []
        for i in range(0, len(nums1)):
            x = nums1[i]
            print(x)
            for j in range(0, len(nums2)):
                if x == nums2[j]:
                    print(j)
                    for k in range(j, len(nums2)):
                        if x < nums2[k]:
                            lst.append(nums2[k])
                            break
                        if k == len(nums2) - 1:
                            lst.append(-1)
                            
        return lst      