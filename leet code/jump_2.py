def jump(nums):
    #pitfall number 0 when faethest and next <i 
    fartest = 0
    num_jumps = 0 
    next_fartest = 0
    if nums[0]==0:
        return 0
    for i, number in enumerate(nums):
        if number ==0 and fartest<=i:
            return 0
        if i > fartest:
            num_jumps += 1
            fartest = next_fartest

        next_fartest = next_fartest if next_fartest >  number + i else number + i
        
    return num_jumps

print(jump([1,0,2,3,4]))