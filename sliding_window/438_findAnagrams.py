"""
给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。


示例 1:

输入: s = "cbaebabacd", p = "abc"
输出: [0,6]
解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
 示例 2:

输入: s = "abab", p = "ab"
输出: [0,1,2]
解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。
 

提示:

1 <= s.length, p.length <= 3 * 104
s 和 p 仅包含小写字母
"""
from typing import List

# Sliding window + Count
def findAnagrams(self, s: str, p: str) -> List[int]:
    from collections import Counter
    p = list(p)
    p_len = len(p)
    s_len = len(s)
    entries = []

    if p_len > s_len:
        return entries

    p_count = Counter(p)
    s_count = Counter()
    
    l = 0

    for i in range(p_len):
        s_count[s[i]] += 1 # 初始化第一个窗口为第一组长p len的子集
    
    if p_count == s_count:
        entries.append(0) # 第一个窗口就对上了，添加
        if p_len == s_len:
            return entries

    for r in range(p_len, s_len):
        # 改变窗口位置
        # 右指针右移
        s_count[s[r]] += 1

        # 左指针右移
        l = r - p_len
        s_count[s[l]] -= 1

        if s_count[s[l]] == 0:# 除去为0的内容防止与p_count比较出错
            del s_count[s[l]]

        if s_count == p_count:
            entries.append(l+1)

    return entries

def findAnagrams(s: str, p: str) -> List[int]:
    l = len(p)
    p_list=list(p) # 转化成list看全等
    p_list.sort() # sort是原地方法，没有返回值
    s_list=list(s)
    res=[]
    for left in range(0,len(s_list)-l+1):
        tmp = s_list[left:left+l]
        tmp.sort()
        if tmp == p_list:
            res.append(left)
    return res

# 时间复杂度：O(m+(n−m)×Σ)，其中 n 为字符串 s 的长度，m 为字符串 p 的长度，Σ 为所有可能的字符数。
# 我们需要 O(m) 来统计字符串 p 中每种字母的数量；需要 O(m) 来初始化滑动窗口；需要判断 n−m+1 个滑动窗口中每种字母的数量是否与字符串 p 中每种字母的数量相同，每次判断需要 O(Σ) 。因为 s 和 p 仅包含小写字母，所以 Σ=26。
# 空间复杂度：O(Σ)。用于存储字符串 p 和滑动窗口中每种字母的数量。