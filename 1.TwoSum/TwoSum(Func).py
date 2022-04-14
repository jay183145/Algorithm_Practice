def twoSum(nums,target):
    for i in nums:
        if target-i in nums:
            return [nums.index(i),nums.index(target-i)]

print(twoSum([5,6,7,8,9],16))



