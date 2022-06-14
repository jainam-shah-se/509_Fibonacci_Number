class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        
        
        valid = {}
        for i in range(0, len(points)):
            if points[i][0] == x:  
                valid[i] = points[i]  
            elif points[i][1] == y:
                valid[i] = points[i]
            elif points[i][0] == x and points[i][1] == y:
                return i
        if len(valid) == 0:
            return -1
        elif len(valid) == 1:
            res = list(valid.keys())[0]
            return res
        else:
            res = list(valid.keys())[0]
            d = abs(x - points[res][0]) + abs(y - points[res][1])
            print(d)
            for key in valid:
                temp_d = abs(x - points[key][0]) + abs(y - points[key][1])
                if (temp_d < d):
                    d = temp_d
                    res = key
            return res
                
            
        
        