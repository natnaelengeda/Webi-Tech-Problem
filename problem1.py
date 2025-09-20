from typing import List

# I wasn't able to achieve 0(n) due to time limit, but this still works;
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
      answers = [1] * len(nums)

      for index1, l in enumerate(nums):
        prev = None
        total = 1

        for index, n in enumerate(nums):
          if(index1 == index):
            continue
          if(prev == None):
            total = n
          else:
            total = n * prev
          prev = total

        answers[index1] = total

      print(answers)  
      return answers

      
sol = Solution()
nums = [1,2,3,4]
nums2 = [4,3,2,1,2]

sol.productExceptSelf(nums2)