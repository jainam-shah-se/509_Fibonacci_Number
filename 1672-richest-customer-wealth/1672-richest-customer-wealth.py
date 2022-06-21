class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        summ = 0
        lst = []
        n = len(accounts[0])
        for i in range(0, len(accounts)):
            for j in range(0, n):
                summ = summ + accounts[i][j]
            lst.append(summ)
            summ = 0
        print(lst)
        lst.sort(reverse=True)
        return (lst[0])
        