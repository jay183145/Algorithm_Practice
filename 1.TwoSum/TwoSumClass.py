
class Solution:
    def twoSum(self,nums,target):
        for i in nums:
            if target-i in nums[nums.index(i)+1:]:
                return [nums.index(i),nums.index(target-i)]

print(Solution().twoSum([5,6,7,8,9],16))
print(Solution().twoSum([3,2,4],6))