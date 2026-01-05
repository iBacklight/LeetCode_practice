"""
128. 最长连续序列
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

请你设计并实现时间复杂度为 O(n) 的算法解决此问题。
"""
# 解题要点（LeetCode 128 最长连续序列）
# 1. 用 set 去重 + 提供 O(1) 的查找效率。lower layer of the set is hashtable, so O(1)
# 2. 遍历每个元素，只有当它是“连续序列的起点”（x-1 不在 set 中）时，才开始往右扩展。
# 3. while 循环扩展：不断检查 x+1, x+2 ... 是否在集合中，统计序列长度。
# 4. 每个元素最多被访问两次（一次在 for，最多一次在 while），所以整体复杂度 O(n)。
# 5. 维护一个全局最大长度 max_len，更新答案。
# 6. 这样避免了排序 O(n log n)，真正做到线性时间解法。

def longestConsecutive(nums):
        num_set = set(nums)
        best = 0

        for x in num_set:
            # 只从“起点”开始扩展，避免重复计数
            # That means it would not be processed if the number is not the start point
            if x - 1 not in num_set: # there is no need for considering overflow since using "in"
                cur = x
                length = 1
                # 向右扩展到连续段的末端
                while cur + 1 in num_set:
                    cur += 1
                    length += 1
                best = max(best, length)

        return best


def longestConsecutive_optimal(self, nums) -> int:
        st = set(nums)  # 把 nums 转成哈希集合
        ans = 0
        for x in st:  # 遍历哈希集合
            if x - 1 in st:  # 如果 x 不是序列的起点，直接跳过
                continue
            # x 是序列的起点
            y = x + 1
            while y in st:  # 不断查找下一个数是否在哈希集合中
                y += 1
            # 循环结束后，y-1 是最后一个在哈希集合中的数
            ans = max(ans, y - x)  # 从 x 到 y-1 一共 y-x 个数
        return ans



def longestConsecutive_low(nums) -> int:
    num_set = set(nums)
    print(num_set)
    cur_num = 0
    temp_max_num = 0
    for i, num in enumerate(sorted(num_set)):
        if i!= 0 and (num-1) not in num_set:
            # previous val broken
            temp_max_num = max(cur_num, temp_max_num)
            cur_num = 0
        cur_num +=1
    temp_max_num = max(cur_num, temp_max_num)
    return temp_max_num

print(longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6]))