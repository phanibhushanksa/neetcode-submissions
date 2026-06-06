class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_array = [1] * len(nums)
        prefix = 1

        for i in range(len(nums)-1):
            prefix_array[i+1] = prefix*nums[i]
            prefix = prefix_array[i+1]


        suffix_array = [1]*len(nums)

        suffix = 1
        for i in range(len(nums)-1,0,-1):
            suffix_array[i-1] = nums[i]*suffix
            suffix = suffix_array[i-1]

        result=[]

        for i in range(len(nums)):
            result.append(prefix_array[i]*suffix_array[i])

        return result