#TwoSum.py

def TwoSum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
    return "No valid pairs found"



nums = [10 , 20 , 50 , 60 ,80 ,90,]
print("Two Sum Algo")
results = TwoSum(nums, 110)
print(results)
