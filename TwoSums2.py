#TwoSums2.py

def TwoSums2(nums,target):
    for i in range(len(nums)):
        print(i)
        for j in range(i+1,len(nums)):
            print(j)
            if nums[i] + nums[j] == target:
                return [i,j]
    return None 

nums = [10, 20 , 30 , 40, 50, 60, 70, 80, 90, 100]

print (TwoSums2(nums, 40))
