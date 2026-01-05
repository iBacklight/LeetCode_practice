
"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

请注意 ，必须在不复制数组的情况下原地对数组进行操作。

Classic double pointer

"""
def moveZeroes(self, nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    # nums.sort(key=bool, reverse=True) # this used timsort
    n = len(nums)
    left = right = 0 # 左指针永远指向第一个0， 右指针遍历数组
    # Note if the array does not contain a 0, the left pointer always merged with right
    while right < n:
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
        right += 1
    print(nums)

moveZeroes([0,1,0,3,12])