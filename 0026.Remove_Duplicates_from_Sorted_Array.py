class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums.sort()
        for i,x in enumerate(nums):
            
