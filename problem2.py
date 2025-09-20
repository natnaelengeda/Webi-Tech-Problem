from typing import List

class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        max_val = float('-inf') 

        for indexi, i in enumerate(points):
            num1 = i[0]
            num1_y = i[1]

            for indexj, j in enumerate(points[indexi + 1:], start=indexi + 1):
                num2 = j[0]
                num2_y = j[1]

                diff = num2 - num1  
                if diff > k:
                    break  

                diffy = num1_y + num2_y + diff  
                print(diffy)
                if diffy > max_val:
                    max_val = diffy

        print("Maximum value:", max_val)
        return max_val


sol = Solution()
points = [[1,3],[2,0],[5,10],[6,-10]]
k = 1

sol.findMaxValueOfEquation(points,k)
