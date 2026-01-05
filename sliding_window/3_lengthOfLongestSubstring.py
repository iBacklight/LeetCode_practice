"""
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。


示例 1:

输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。注意 "bca" 和 "cab" 也是正确答案。
示例 2:

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

"""
# from typing import List
def lengthOfLongestSubstring(s: str) -> int:
    # 边界情况：只有 1 个字符时，最长不重复子串长度就是 1
    if len(s) == 1:
        return 1
    # 边界情况：空字符串时，结果是 0
    if len(s) == 0:
        return 0

    n = len(s)   # 字符串总长度

    l = 0        # 左指针，滑动窗口的起始位置
    r = 0        # 右指针，滑动窗口的结束位置（即下一个要检查的字符）

    max_re_s = {}      # 哈希表（字典），用来存储窗口中出现的字符及其索引
    max_sub_s_len = 0  # 记录目前找到的最长不重复子串的长度

    # 当右指针还没到字符串末尾时继续
    while r < n and r >= l:
        if s[r] in max_re_s:  
            # 如果 s[r] 已经在当前窗口里，说明出现了重复字符
            # 此时我们要缩小窗口，从左边开始删除字符
            del max_re_s[s[l]]  # 移除窗口最左边的字符
            l += 1              # 左指针右移一位，缩小窗口
        else:
            # 如果 s[r] 没有重复，可以安全加入到窗口
            max_re_s[s[r]] = r  # 把该字符和它的索引存入哈希表
            r += 1              # 右指针右移一位，扩大窗口

        # 更新最长不重复子串长度（窗口大小 = r - l）
        if r - l > max_sub_s_len:
            max_sub_s_len = r - l

    return max_sub_s_len


def lengthOfLongestSubstring_self(s: str) -> int:
        if s == "":
            return 0
        l = r = 0
        lls = 0
        went = dict()

        while r != len(s):
            if s[r] not in went:
                went[s[r]] = 1
                if r - l > lls:
                    lls = r - l
                r += 1
            else:
                del went[s[l]]
                l += 1

        return lls + 1

def lengthOfLongestSubstring_1(s: str) -> int:
    if s == "":
        return 0
    left = 0
    right = 0
    max_len = 1

    for right in range(len(s)-1):
        right+=1
        while s[right] in s[left:right]: #不能用if
            left+=1
        max_len = max(right-left+1,max_len) #要取max

    return max_len

# 时间复杂度：O(N)，其中 N 是字符串的长度。左指针和右指针分别会遍历整个字符串一次。
# 空间复杂度：
# O(∣Σ∣)，其中 Σ 表示字符集（即字符串中可以出现的字符），∣Σ∣ 表示字符集的大小。
# 在本题中没有明确说明字符集，因此可以默认为所有 ASCII 码在 [0,128) 内的字符，即 ∣Σ∣=128。
# 我们需要用到哈希集合来存储出现过的字符，而字符最多有 ∣Σ∣ 个，因此空间复杂度为 O(∣Σ∣)。

print(lengthOfLongestSubstring("abcabcbb"))