class Solution:
    def average(self, salary: List[int]) -> float:
        
        print(salary)
        salary.sort()
        print(salary)
        salary = salary[1: len(salary)-1]
        print(salary)
        sum_val = sum(salary)
        avg = sum_val / len(salary)
        return avg