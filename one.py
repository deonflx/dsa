class Solution(object):
    def singleNumber(self, nums):
        for i in range(len(nums)):
            if nums.count(nums[i]) == 1:
                return nums[i]
    print( singleNumber(1,[1, 2, 3, 4, 5, 1, 2, 3, 4]))



        