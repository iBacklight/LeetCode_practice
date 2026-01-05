"""
给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
"""
def groupAnagrams(strs):
        if len(strs) <=1 :
            return [strs]

        hash = {}
        temp_str = ""
        for cur_str in strs:
            s_str = sorted(cur_str)
            temp_str = "".join(s_str)
            # print(temp_str)
            if temp_str not in hash:
                hash[temp_str] = [cur_str]
            else:
                hash[temp_str].append(cur_str)
        
        return list(hash.values())

import collections
def groupAnagrams_official(strs):
    """
    LeetCode 49: Group Anagrams
    知识点总结：
    1. 异位词：字母相同，顺序不同。
    2. 分组思路：找到唯一 key，把所有异位词放到同一桶里。
       - 方法1：排序字符串作为 key，O(k log k)
       - 方法2：26个字母计数作为 key，O(k)
    3. 哈希表：用 dict / defaultdict 进行分组。
    4. Python 技巧：
       - ''.join(sorted(s)) 把字符串排序后拼接。
       - tuple(counts) 可作为 key（因为不可变且可哈希）。
       - defaultdict(list) 自动创建空列表，避免手动检查 key。
    """
    mp = collections.defaultdict(list)

    for st in strs:
        key = "".join(sorted(st))
        mp[key].append(st)
    
    return list(mp.values())




print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))