def twoSum( nums, target):
        for i,n in enumerate(nums):
            print(i,n)
            for i2,n2 in enumerate(nums):
                if i!=i2:
                    if n+n2==target:
                        return([i-1,i2-1])


print(twoSum([3,2,4],6))