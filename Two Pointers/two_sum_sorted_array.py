class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers)-1
        indx_list = []
        while left < right :
            sum = numbers[left] + numbers[right]
            if sum == target : 
                return [left+1,right+1]
            if sum < target:
                left+=1
            else:
                right-=1
        return [-1,-1]

numbers = [1,7,13,15]
target  = 22
index_list = Solution().twoSum(numbers,target)
print(index_list)