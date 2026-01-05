def twoSum(nums, target:int):
    # low_mark = {}
    # for ind, num in enumerate(nums):
    #     low_mark[ind] = num # avoid the same num for different index
        
    # for ind, num in low_mark.items():   
    #     for s_ind, s_num in low_mark.items():
    #         if s_ind == ind:
    #             continue
    #         if (num+s_num) == target:
    #             return [ind, s_ind]
    
    hashtable = dict()
    for i, num in enumerate(nums):
        if target - num in hashtable:
            return [hashtable[target - num], i] # this avoid same num but only for two sum
        hashtable[num] = i
    return []

print(twoSum([3,3],6))