"""
76. 最小覆盖子串

给定两个字符串 s 和 t，长度分别是 m 和 n，返回 s 中的 最短窗口 子串，使得该子串包含 t 中的每一个字符（包括重复字符）。如果没有这样的子串，返回空字符串 ""。

测试用例保证答案唯一。

示例 1：

输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"
解释：最小覆盖子串 "BANC" 包含来自字符串 t 的 'A'、'B' 和 'C'。

示例 2：

输入：s = "a", t = "a"
输出："a"
解释：整个字符串 s 是最小覆盖子串。

示例 3:

输入: s = "a", t = "aa"
输出: ""
解释: t 中两个字符 'a' 均应包含在 s 的子串中，
因此没有符合条件的子字符串，返回空字符串。
 

提示：

m == s.length
n == t.length
1 <= m, n <= 105
s 和 t 由英文字母组成

"""
from collections import Counter
def minWindow(s: str, t: str) -> str:
    
    if t == "" or s == "" or len(t) > len(s):
        return ""

    l, r = -1, len(s) # 必须这样设置，否则会无法避免t根本不在s中的情况，例如: s="a", t="b", 则会默认输出"a"

    cnt_s = Counter()
    cnt_t = Counter(t)

    cur_l = 0
    for cur_r, cha in enumerate(s):
        cnt_s[cha] += 1
        while cnt_s >= cnt_t: # 还可以这样比较吗牛逼
        # cnt_s >= cnt_t 的意思是：对于 cnt_t 中的每一个字符，cnt_s 中该字符的数量是否都大于等于 cnt_t 中的数量
        # 它不关心 cnt_s 里是否有 cnt_t 没有的字符（比如 cnt_s 有一堆 'z'，但 cnt_t 不需要 'z'，这不影响结果）。它只关心 cnt_t 需要的字符，cnt_s 是否足够。
            if cur_r - cur_l < r -l:
                r, l = cur_r, cur_l
            cnt_s[s[cur_l]] -= 1 # remove current left pointer
            cur_l += 1 # left pointer move forward
    return s[l:r+1] if l >= 0 else ""

# 详细拆解：Counter(t) 
# 初始化：需要遍历字符串 t 一次。耗时：$O(M)$外层循环 (for cur_r in enumerate(s))：右指针 cur_r 从 0 走到 $N-1$。这个循环固定执行 $N$ 次。
# 内层循环 (while cnt_s >= cnt_t) 和 指针移动：虽然这里有个 while，但左指针 cur_l 在整个函数的生命周期里，最多也是从 0 走到 $N$。它不会回退。所以，cnt_s[s[cur_l]] -= 1 和 cur_l += 1 这些操作，平摊下来总共只执行 $O(N)$ 次。
# 关键瓶颈：cnt_s >= cnt_t 的比较：这是性能的关键点。正如我们之前讨论的，Counter 的比较操作需要遍历 cnt_t 中的所有键（Key）。cnt_t 中最多有多少个键？最多是字符集的大小 $\Sigma$。这个比较操作发生在每一次 for 循环里，以及每一次 while 循环里。
# 因此，这个比较操作总共执行了大约 $2N$ 次。每次比较耗时 $O(\Sigma)$。总耗时：$O(N \cdot \Sigma)$综合来看：如果字符集很小（比如只有小写字母，$\Sigma=26$），这基本上可以看作 $O(N)$。但在严格的算法分析中，或者当字符集很大时，这个 $\Sigma$ 是不能忽略的常数因子。


def minWindow(s: str, t: str) -> str:
    # 1. 记录 t 中每个字符的需求量
    target_cnt = Counter(t)
    # 2. need_count 表示还需要凑齐多少个“有效字符”的总量
    need_count = len(t)
    
    res = (0, float('inf')) # 记录结果的左右边界
    l = 0
    
    for r, char in enumerate(s):
        # 如果当前字符是 t 需要的，且还没拿够，need_count 就减 1
        if target_cnt[char] > 0:
            need_count -= 1
        # 无论是不是需要的，target_cnt 都要减 1（变成负数表示多余）
        target_cnt[char] -= 1
        
        # 3. 当 need_count == 0 时，说明当前窗口已包含所有 t 的字符
        while need_count == 0:
            # 更新最短长度
            if r - l < res[1] - res[0]:
                res = (l, r)
            
            # 4. 尝试移动左指针 l 来缩小窗口
            # 如果即将移出的字符是 t 必需的（即计数回复到 > 0），need_count 加 1
            target_cnt[s[l]] += 1
            if target_cnt[s[l]] > 0:
                need_count += 1
            l += 1
            
    return s[res[0]:res[1]+1] if res[1] != float('inf') else ""