# Leecode 经验总结

[TOC]

---

## 题目导航汇总

| **序号** | **题目序号** | **题目名称** | **Hot 100** | **难度** | **核心算法/数据结构** | **所属体系** |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 283 | [移动零](#lc-283) | 🔥 | 🟢 简单 | 双指针 (同向) | 线性扫描 / 滑动窗口 |
| 2 | 3 | [无重复字符的最长子串](#lc-3) | 🔥 | 🟡 中等 | 滑动窗口 (变长-最长) | 线性扫描 / 滑动窗口 |
| 3 | 76 | [最小覆盖子串](#lc-76) | 🔥 | 🔴 困难 | 滑动窗口 (变长-最短) | 线性扫描 / 滑动窗口 |
| 4 | 438 | [找到字符串中所有字母异位词](#lc-438) | 🔥 | 🟡 中等 | 滑动窗口 (定长+计数) | 线性扫描 / 滑动窗口 |
| 5 | 11 | [盛最多水的容器](#lc-11) | 🔥 | 🟡 中等 | 双指针 (左右对撞) | 线性扫描 / 双向双指针 |
| 6 | 42 | [接雨水](#lc-42) | 🔥 | 🔴 困难 | 双指针 / 单调栈 | 线性扫描 / 双向双指针 |
| 7 | 167 | [两数之和 II (有序版)](#lc-167) | | 🟡 中等 | 双指针 (左右对撞) | 线性扫描 / 双向双指针 |
| 8 | 15 | [三数之和](#lc-15) | 🔥 | 🟡 中等 | 排序 + 双指针 | 线性扫描 / 双向双指针 |
| 9 | 53 | [最大子数组和](#lc-53) | 🔥 | 🟡 中等 | Kadane (贪心/DP) | 线性扫描 / Kadane |
| 10 | 56 | [合并区间](#lc-56) | 🔥 | 🟡 中等 | 排序 + 区间合并 | 线性扫描 / 区间合并 |
| 11 | 560 | [和为 K 的子数组](#lc-560) | 🔥 | 🟡 中等 | 前缀和 + 哈希表 | 空间权衡优化 |
| 12 | 1 | [两数之和](#lc-1) | 🔥 | 🟢 简单 | 哈希表 | 空间权衡优化 |
| 13 | 20 | [有效的括号](#lc-20) | 🔥 | 🟢 简单 | 基础栈 | 数据结构 / 基础栈 |
| 14 | 32 | [最长有效括号](#lc-32) | 🔥 | 🔴 困难 | 栈 (存索引) | 数据结构 / 基础栈 |
| 15 | 739 | [每日温度](#lc-739) | 🔥 | 🟡 中等 | 单调栈 (找下一个更大) | 数据结构 / 单调栈 |
| 16 | 84 | [柱状图中的最大矩形](#lc-84) | 🔥 | 🔴 困难 | 单调栈 (找左右边界) | 数据结构 / 单调栈 |
| 17 | 85 | [最大矩形](#lc-85) | 🔥 | 🔴 困难 | 单调栈 (降维) | 数据结构 / 单调栈 |
| 18 | 239 | [滑动窗口最大值](#lc-239) | 🔥 | 🔴 困难 | 单调队列 | 数据结构 / 单调队列 |
| 19 | 33 | [搜索旋转排序数组](#lc-33) | 🔥 | 🟡 中等 | 二分查找（双坡） | 下标二分 |
| 20 | 34 | [在排序数组中查找元素...](#lc-34) | 🔥 | 🟡 中等 | 二分查找 | 下标二分 |
| 21 | 153 | [寻找旋转排序数组中的最小值](#lc-153) | 🔥 | 🟡 中等 | 二分查找（双坡） | 下标二分 |
| 22 | 74 | [搜索二维矩阵](#lc-74) | 🔥 | 🟡 中等 | 二分查找 | 下标二分 |
| 23 | 875 | [爱吃香蕉的珂珂](#lc-875) | | 🟡 中等 | 二分查找（转换） | 值域二分 |
| 24 | 410 | [分割数组的最大值](#lc-410) | | 🔴 困难 | 二分查找 | 值域二分 |
| 25 | 1004 | [最大连续1的个数 III](#lc-1004) | | 🟡 中等 | 滑动窗口/二分查找 | 值域二分 |
| 26 | 200 | [岛屿数量](#lc-200) | 🔥 | 🟡 中等 | 网格 DFS/BFS | 图论 / 网格搜索 |
| 27 | 695 | [岛屿的最大面积](#lc-695) | | 🟡 中等 | 网格 DFS/BFS | 图论 / 网格搜索 |
| 28 | 994 | [腐烂的橘子](#lc-994) | 🔥 | 🟡 中等 | 多源 BFS | 图论 / 网格搜索 |
| 29 | 79 | [单词搜索](#lc-79) | 🔥 | 🟡 中等 | DFS / 网格回溯 | 图论 / 网格搜索 |
| 30 | 207 | [课程表](#lc-207) | 🔥 | 🟡 中等 | 拓扑排序 (Kahn算法) | 图论 / 依赖解析 |
| 31 | 210 | [课程表 II](#lc-210) | | 🟡 中等 | 拓扑排序 (输出路径) | 图论 / 依赖解析 |
| 32 | 133 | [克隆图](#lc-133) | | 🟡 中等 | DFS/BFS + 哈希表 | 图论 / 普通遍历 |
| 33 | 208 | [实现 Trie (前缀树)](#lc-208) | 🔥 | 🟡 中等 | 树 | 图论 / 树 |
| 34 | 70 | [爬楼梯](#lc-70) | 🔥 | 🟢 简单 | 线性 DP (斐波那契) | 动态规划 / 线性 DP |
| 35 | 198 | [打家劫舍](#lc-198) | 🔥 | 🟡 中等 | 线性 DP (相邻约束) | 动态规划 / 线性 DP |
| 36 | 121 | [买卖股票的最佳时机](#lc-121) | 🔥 | 🟢 简单 | 一次遍历 / 状态机 | 动态规划 / 线性 DP |
| 37 | 62 | [不同路径](#lc-62) | 🔥 | 🟡 中等 | 网格 DP | 动态规划 / 网格 DP |
| 38 | 64 | [最小路径和](#lc-64) | 🔥 | 🟡 中等 | 网格 DP | 动态规划 / 网格 DP |
| 39 | 322 | [零钱兑换](#lc-322) | 🔥 | 🟡 中等 | 完全背包 (最少硬币) | 动态规划 / 背包问题 |
| 40 | 5 | [最长回文子串](#lc-5) | 🔥 | 🟡 中等 | 区间 DP / 中心扩散 | 动态规划 / 序列 DP |
| 41 | 46 | [全排列](#lc-46) | 🔥 | 🟡 中等 | 回溯 (Visited 数组) | 回溯 / 全排列 |
| 42 | 78 | [子集](#lc-78) | 🔥 | 🟡 中等 | 回溯 (StartIndex) | 回溯 / 子集 |
| 43 | 39 | [组合总和](#lc-39) | 🔥 | 🟡 中等 | 回溯 (StartIndex) | 回溯 / 组合 |
| 44 | 77 | [组合](#lc-77) | | 🟡 中等 | 回溯 (StartIndex) | 回溯 / 组合 |
| 45 | 131 | [分割回文串](#lc-131) | 🔥 | 🟡 中等 | 回溯 (切割线) | 字符串分割 |
| 46 | 79 | [单词搜索](#lc-79) | 🔥 | 🟡 中等 | 网格回溯 (原地修改) | 二维网格路径 |
| 47 | 17 | [电话号码的字母组合](#lc-17) | 🔥 | 🟡 中等 | 回溯 (层级映射) | 映射回溯 |
| 48 | 51 | [N 皇后](#lc-51) | | 🔴 困难 | 回溯 | 回溯 |
| 49 | 22 | [括号生成](#lc-22) | 🔥 | 🟡 中等 | 回溯 | 回溯 |
| 50      | 206          | [反转链表](#lc-206) | 🔥           | 🟢 简单   | 迭代 / 递归           | 结构修改 (反转)       |
| 51      | 21           | [合并两个有序链表](#lc-21) | 🔥           | 🟢 简单   | 双指针 + 哨兵         | 合并逻辑              |
| 52      | 160          | [相交链表](#lc-160) | 🔥           | 🟢 简单   | 双指针 (A+B路径)      | **双指针 (路径拼接)** |
| 53      | 141          | [环形链表](#lc-141) | 🔥           | 🟢 简单   | 快慢指针 (Floyd 判圈) | 快慢指针              |
| 54      | 142          | [环形链表 II](#lc-142) | 🔥           | 🟡 中等   | 快慢指针 (数学推导)   | **快慢指针**          |
| 55      | 19           | [删除链表的倒数...](#lc-19) | 🔥           | 🟡 中等   | 快慢指针 (固定间距)   | 快慢指针              |
| 56      | 25           | [K 个一组翻转链表](#lc-25) | 🔥           | 🔴 困难   | 分组迭代 / 递归       | 结构修改 (进阶)       |
| 5欧修改7 | 92 | [反转链表II](#lc-92) |  | 🟡 中等 | 双指针结构变形 | 结构修改（反转） |

---

## 模块一：线性扫描优化 (Linear Scan Optimization)

| **算法类型**        | **核心要求**            | **典型失效场景**           | **替代方案**         |
| ------------------- | ----------------------- | -------------------------- | -------------------- |
| **滑动窗口**        | **非负数** (和的单调性) | 数组包含**负数**且求区间和 | **前缀和 + 哈希表**  |
| **对撞指针 (求和)** | **数组有序**            | 数组无序                   | 先排序，或使用哈希表 |
| **对撞指针 (容器)** | **左右边界限制**        | 无特殊限制 (利用木桶原理)  | -                    |

我们总结这一部分为四大核心体系：

### 体系一：单向双指针 - 滑动窗口 (Sliding Window)

左右指针同向移动。利用数据的**单调性**（例如窗口变长，和/计数单调增加）。这是数组/字符串处理中**最重要**的技巧，没有之一。

- **核心逻辑**：

  维护一个窗口 [l, r]，右指针 r 主动向右扩张寻找可行解，左指针 l 被动向右收缩以优化解（或维持窗口大小）。**要求**：窗口的和/状态必须随窗口的扩张单调增加，随窗口的收缩单调减少。这对数字数组非常重要，例如：

  - **如果数组中有负数：** 当你向右移动 `r` 增加一个元素时，窗口的和可能反而变小；当你移动 `l` 移除一个元素时，窗口的和可能反而变大。这会导致无法确定何时该收缩左指针，单调性被破坏，逻辑就会失效。

- **适用场景**

  - 题目要在 **线性数据**（数组/字符串）中找 **“连续”** 的子区间。
  - 关键词：**“连续子串”、“连续子数组”**。
  - 目标：求最长、最短、或者计数。

- **为什么适配**：

  暴力解法通常是 $O(N^2)$，滑动窗口利用了单调性（即右指针只进不退，左指针只进不退），将复杂度降为 $O(N)$。

- **包含题目**：

  - **283.移动 0**（变长窗口）<a id="lc-283"></a>

    - 循环直到右指针到达字符串尾部

    - 左指针指向左边第一个0，右指针指向非0就交换左右指针对应位置的值

    - 右指针不断扩张

      ```python
      def moveZeroes(self, nums) -> None:
          """
          Do not return anything, modify nums in-place instead.
          """
          # nums.sort(key=bool, reverse=True) # this used timsort
          n = len(nums)
          left = right = 0 # 左指针指向永远下一个非零元素应该放置的位置， 右指针遍历数组
          # Note if the array does not contain a 0, the left pointer always merged with right （二者同步前进）
          while right < n:
              if nums[right] != 0:
                  nums[left], nums[right] = nums[right], nums[left]
                  left += 1
              right += 1
          print(nums)
      ```

  - **3. 无重复字符的最长子串** (变长窗口 - 求最长) <a id="lc-3"></a>

    - 循环直到右指针到达字符串尾部

    - 右指针没有重复，移动右指针（扩张）

    - 右指针有重复，被动移动左指针直到没有重复

      ```python
      def lengthOfLongestSubstring_self(s: str) -> int:
          if s == "":
              return 0
          l = r = 0
          lls = 0
          went = dict()
      
          while r != len(s):
              if s[r] not in went:# 无重复，判断，并扩张右指针
                  went[s[r]] = 1
                  if r - l > lls:
                      lls = r - l
                  r += 1
              else:
                  del went[s[l]]
                  l += 1 # 有重复，收缩左指针
      
          return lls + 1
      ```

  - **76. 最小覆盖子串** (变长窗口 - 求最短) <a id="lc-76"></a>

    - 循环直到右指针到达字符串尾部

    - 右指针扩张（左指针冻结），Counter(s) >= Counter(t)满足即包含所有子串

    - 此时左指针（右指针冻结）再逐步扩张缩小字串范围直到不满足上述条件

      ```python
      from collections import Counter
      # 1 双counter
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
      
      # 2 不用双counter，只使用一个 + count计数器
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
      ```
  
  - **438. 找到字符串s中所有匹配p字符串中的字母异位词的子串**, e.g. p =abc, 则bac,cab(定长窗口) <a id="lc-438"></a>
  
    - 循环直到右指针到达字符串尾部的前一个窗口长度的位置(len(s)-len(p)+1)
  
    - j将p转成可以直接对比的对象，比如list.sort(), 或者Counter
  
    - 维护定长窗口检索，左右指针一起移动（实际上只移动一个就行，另外一个相当于当前指针加或减一个窗口的定长）
  
    - 对每一个窗口与p的可对比对象比较，符合则添加
  
      ```python
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
      ```

#### 核心模板 (Python)

```python
def slidingWindow(s):
    # 初始化
    window = collections.Counter()
    l = 0
    ans = ... # 根据题目要求初始化

    for r, char in enumerate(s):
        # 1. 进窗口：加入右边元素
        window[char] += 1
        
        # 2. 判定条件：当窗口需要收缩时 (例如：不满足条件了，或者找到了可行解要优化)
        while valid_condition(window): 
            # 更新结果 (如果是求最短，在这里更新)
            # ans = min(ans, r - l + 1)
            
            # 3. 出窗口：移出左边元素
            d = s[l]
            window[d] -= 1
            if window[d] == 0: del window[d] # 可选，保持干净
            l += 1
            
        # 更新结果 (如果是求最长，通常在这里更新)
        # ans = max(ans, r - l + 1)
        
    return ans
```



### 体系二：双向双指针 (Two Pointers - 左右对撞)

左右指针相对移动，向中间收缩。这是一种空间换时间的技巧，通常用于解决“容器”类或者“两数之和”的变体。

- **核心逻辑**：

  定义 left = 0, right = n-1。根据两边的“短板”向中间移动。这类算法对数组的**要求**通常是**有序性**（数组必须是**有序**的）或符合**特定的物理结构**（如高度）。

- **适用场景**：

  - 利用**木桶效应**或
  - **排序后的有序性**，或有序数组求和。

- **包含题目**：

  - **11. 盛最多水的容器** (容器，类似思想) <a id="lc-11"></a>

    - 基础，双指针中心碰撞，短边先收缩

      ```python
      from typing import List
      def maxArea(height: List[int]) -> int:
          # 双指针，中心碰撞
      
          l,r = 0, len(height)-1
          max_volume = cur_volume = 0
      
          # volume = min_height * (r - l )
      
          while l < r:
              min_height = min(height[l], height[r])
              cur_volume = min_height * (r -l)
              max_volume = max(max_volume, cur_volume)
      
              # 哪边短，收缩哪边
              if height[l] >= height[r]:
                  r -= 1
              else:
                  l += 1
      
          return max_volume
      ```
  
  - **42. 接雨水** (容器，高频 Hard 题) <a id="lc-42"></a>
  
    - 雨水的高度取决于**木桶效应**（左右两边最高柱子的较小值）。
  
    - 维护 `left_max` 和 `right_max`。
  
    - 如果 `left_max < right_max`，说明左边是短板，左边位置能装的水就确定了（取决于 `left_max`），计算并移动左指针；反之亦然。
  
      ```python
      def trap(height: List[int]) -> int:
          """
          与其一层层切片，不如计算每一列（每一个索引）能接多少水。
          对于下标为 i 的柱子，它能接的水量取决于：
              左边最高的柱子高度 L。
              右边最高的柱子高度 R。
              该柱子能接的水量为 min(L, R) - height[i]（如果结果大于 0）。
      
          本算法相当于，我们只知道边界两墙的信息，只计算两墙之中水量，短板效应从矮墙看起
          每遇到一个更高的墙，就划分新区间，重新开始两墙的计算
          """
          l = 0
          r = len(height) - 1
          max_l = max_r = 0
          volume = 0
      
          while l < r:
              # 处理较矮的一边, 这点很重要，相当于两墙之中看矮墙
              if height[l] < height[r]:
                  # 左边
                  if height[l] > max_l:
                 # 如果更高，相当于要换区间，当前区间不能接水，所以只更新高度
                      max_l = height[l]
                  else:
                      # 要更新水量 = 最高水位-高度
                      volume += max_l - height[l]
                  l += 1
              else:# 右边
                  if height[r] > max_r:
                 # 如果更高，相当于要换区间，当前区间不能接水，所以只更新高度
                      max_r = height[r]
                  else:
                      # 要更新高度, 最高水位-高度
                      volume += max_r - height[r]
                  r -= 1
      
          return volume
      ```
    
  - **1.两数之和** II（有序版， 有序数组求和）<a id="lc-1-ordered"></a>
  
    - 基础，双指针中心碰撞
  
  - **15.三数之和**（有序数组求和）<a id="lc-15"></a>
  
    - 正常：可以正常多一次循环+转换two sum去做
  
      ```python
      def threeSum_hash(nums: List[int]) -> List[List[int]]:
              nums.sort()
              n = len(nums)
              res_set = set()
      
              for i in range(n):
                  # 提前去重：相同 i 值只做一次
                  # 防止看到[-1, -1, 0, 1, 2, ...]，两次看到同样数字，产生同样结果
                  # 前提是，已经排序，后面不会在该循环中看到相同数字
                  if nums[i] > 0: # 排序后超过0不可能成为首位数
                      break
                  if i > 0 and nums[i] == nums[i-1]: 
                      continue # 连续相等的数字不应该重复计算
      
                  target = 0-nums[i] # 设nums[i]为首位数
                  seen = set()  # 存已见到的数
                  # transit to two sum
                  for j in range(i+1, n):
                      need = target - nums[j]
                      if need in seen:
                          res_set.add((nums[i], need, nums[j]))  # 三元组已按升序
                      seen.add(nums[j])
      
              return [list(t) for t in res_set]
      ```
  
      或者双指针：
  
    - **排序原数组**（有序性对这种算法至关重要），循环一次数组，再循环中从当前数字右侧开始遍历（即当前i为最小）
  
    - l = i+1，r = n-1， while l < r:# 边界条件：排序后l<r
  
    - num_sum = nums[i] + nums[l] + nums[r] == 0，判断不重复，就添加，并同时向中间收缩双指针以保证单调性
  
    - 若num_sum != 0, 若>0, 则和较大，回缩右指针；反之若<0, 则扩张左指针
  
      ```python
      def threeSum_doublePointer(nums: List[int]) -> List[List[int]]:
          # 双指针
          nums.sort()
          n = len(nums)
          res = []
          
          for i in range(n):
              # 相同剪枝
              if nums[i] > 0:
                  break
              if i >= 1 and nums[i] == nums[i-1]:
                  continue
      
              # 构造双指针
              l = i+1
              r = n-1
              while l < r:# 边界条件：排序后l<r
                  num_sum = nums[i] + nums[l] + nums[r]
                  if num_sum == 0:
                      # 双指针 l 和 r 一次次收缩，遍历过程中生成的解是按升序来的。所以重复一定会相邻出现
                      # 只需要作相邻去重(即res最后一个数组和当前不一样即可)
                      if len(res) == 0 or [nums[i], nums[l], nums[r]] != res[-1]:# 防止数字重复
                          res.append([nums[i], nums[l], nums[r]])
                      l += 1 # 无论如何，都要双边改变指针
                      r -= 1
                  elif num_sum > 0:
                      r -= 1
                  elif num_sum < 0:
                      l += 1
          return res
      ```
  
      

### 体系三：Kadane 算法 (贪心/动态规划)

这是解决“最大子数组和”问题的专用解法。

- **包含题目**：

  - **53. 最大子数组和** <a id="lc-53"></a>

    - $dp[i] = \max(nums[i], dp[i-1] + nums[i])$

      ```python
      def maxSubArray(nums):
          cur_sum = 0
          max_sum = nums[0]
          
          for num in nums:
              # 贪心逻辑：如果之前的和是负数，直接抛弃，从当前数字重新开始
              cur_sum = max(num, cur_sum + num) # 相当于：如果 cur_sum > 0 就加，否则重置
              max_sum = max(max_sum, cur_sum) # 每一轮都做max，这样就不会错过任何和
              
          return max_sum
      ```

- **核心逻辑**：

  “之前的负担如果太重，就丢掉重新开始”。遍历数组，维护一个 current_sum。如果 current_sum 变成了负数，那么它对于后面的元素来说就是一种“拖累”，直接抛弃它，将 current_sum 重置为当前的数字。



### 体系四：区间合并与排序 (Intervals & Sorting)

这类题目通常不涉及复杂的算法，而是考察逻辑思维和排序的应用。

- **包含题目**：

  - **56. 合并区间** <a id="lc-56"></a>

    - ```python
      def merge(intervals: List[List[int]]) -> List[List[int]]:
          intervals.sort(key=lambda x:x[0]) #keep in mind 这种用法
          merged = []
      
          for i in intervals:# 因为已经按照下界排过顺序，只用考虑最后区间一个就好
              if merged == [] or merged[-1][1]<i[0]:# 合并集是空集，或者当前区间的下界在合并集的最后区间以外
                  merged.append(i) # 直接添加当前区间
              else:
                  merged[-1][1] = max(merged[-1][1],i[1])# 比较当前区间的上届和合并集的最后区间的上届，替换掉较小的一面
                  # 逻辑：因为下界顺序排列（当前区间下界大于最后区间下界）且当前区间下界小于最后区间的上届，意味着当前区间必然和最后区间重叠，且不会干涉之前的区间
          return merged
      ```

- 核心逻辑：

  “先排序，后扫描”。也就是：只要涉及到区间重叠问题，第一步永远是按照区间的 Start Time 进行排序。

- **适用场景**：

  - 关键词：**“区间”、“重叠”、“合并”、“会议室安排”**。


---

## 模块二：空间权衡优化 (Space-Time Trade-off)

### 体系一：前缀和 + 哈希表 (Prefix Sum + Hash Map)

这是处理**子数组求和**问题的终极武器，特别是当数组中包含**负数**时。

- **包含题目**：

  - **560. 和为 K 的子数组** (经典母题) <a id="lc-560"></a>

    - 双指针/滑动窗口”只在所有元素非负时才成立（窗口右扩和左缩才能单调地让和增/减）。一旦有负数，窗口和不再单调，双指针会漏数或死循环。因此这题不能用双指针做对。

      ```python
      def subarraySum(self, nums: List[int], k: int) -> int:
          """
          当我们走到位置 i,只要过去某个位置 j 的前缀和等于 pre_sum[i] - k,那么 j+1..i 这一段就是一个和为 k 的子数组。
          于是只需记录“历史上每个前缀和出现过多少次”，每次在 pre_sum 更新后，把 cnt[pre_sum - k] 加到答案里即可。
          """
          cnt = defaultdict(int)
          cnt[0] = 1            # 前缀和为0在起点时出现一次（空前缀）
          pre_sum = 0           # 当前前缀和
          ans = 0
      
          for x in nums:
              pre_sum += x
              ans += cnt[pre_sum - k]   # 以当前为右端点，能形成和为k的子数组数量
              cnt[pre_sum] += 1         # 当前前缀和出现次数+1
      
          return ans
      ```

  - **1. 两数之和** (虽然不是区间，但核心思想一致：`target - current` 是否存在) <a id="lc-1"></a>

    ```python
    def twoSum(nums, target:int):
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i] # this avoid same num but only for two sum
            hashtable[num] = i
        return []
    ```
  
- 核心逻辑：

  将“区间和”问题转化为“端点差值”问题。

  公式：$Sum(i, j) = PreSum[j] - PreSum[i-1]$。

  如果我们想找 $Sum(i, j) == K$，等价于找 $PreSum[i-1] == PreSum[j] - K$。

- **适用场景**：

  - 关键词：**“连续子数组”**、**“和为 K”**。
  - **关键特征**：数组中可能包含**负数**（这是它区别于滑动窗口的关键。如果有负数，窗口加长不一定变大，导致滑动窗口失效）。

- 哈希表的作用：

  用来存 PreSum 出现的次数或索引，从而实现 $O(1)$ 的查找。

#### 核心模板

```python
def subarraySum(nums, k):
    count_map = {0: 1} # 初始化：前缀和为0出现1次
    pre_sum = 0
    ans = 0
    
    for num in nums:
        pre_sum += num
        # 公式：寻找之前的某个前缀和 == pre_sum - k
        if (pre_sum - k) in count_map:
            ans += count_map[pre_sum - k]
        
        count_map[pre_sum] = count_map.get(pre_sum, 0) + 1
    return ans
```

---

## 模块三：数据结构驱动的线性优化 (容器驱动)

这一部分的核心逻辑是：**利用特定数据结构的“存取规则”，自动过滤（剔除）掉那些对寻找最终答案无用的信息。**

| **需求**                           | **推荐工具** | **关键操作**                 |
| ---------------------------------- | ------------ | ---------------------------- |
| 处理**嵌套**逻辑（如括号、路径）   | **基础栈**   | 匹配即消除                   |
| 找**下一个/上一个**更大或更小      | **单调栈**   | 破坏单调性即弹出并记录答案   |
| 确定以某点为高度的**最大扩散区间** | **单调栈**   | 同时找左右第一个比它小的边界 |
| 维护**滑动窗口**内的最值           | **单调队列** | 弹出较小者 + 弹出过期者      |

### 体系一：基础栈 (Basic Stack) —— “匹配与消除”

栈(stack)是处理具有**对称性**或**嵌套关系**数据的天然工具。它是一种遵循后进先出（LIFO）原则的数据结构。这个类将包含以下几个基本操作：

1. `push(item)`：将`item` 推入栈顶（末尾）。
2. `pop()`：同时**移除**并**返回**栈顶的元素。
3. `peek()`：只返回栈顶的元素但**不移除**它。
4. `is_empty()`：判断栈是否为空。
5. `size()`：计算当前栈中元素的数量。

通常我们使用python的list或者基于字典的链表来实现栈。

- **核心逻辑**：

  - **先进后出 (LIFO)**。
  - 遇到“待处理”元素（如左括号）先入栈缓存，遇到“可处理”元素（如右括号）立即取出最近的一个进行抵消。

- **适用场景**：
  - 关键词：**“对称”、“嵌套”、“回溯路径”、“递归转迭代”**。
  - 只要问题具有“后产生的需求先满足”的特征，就考虑基础栈。

- **包含题目**：

  - **20. 有效的括号**：左括号进栈，遇到右括号与栈顶匹配消除。<a id="lc-20"></a>

    ```python
    def isValid(self, s: str) -> bool:
        # stack
        if len(s) == 1:
            return False
    
        bracket_dict = {'(':')','{':'}','[':']'}
        stack = []
    
        for c in s:
            if c in bracket_dict: # 只要是前括号就可以进栈
                stack.append(c)
            elif c not in bracket_dict:
                if stack == []:# 空栈进后括号直接结束
                    return False
                if bracket_dict[stack.pop()] != c:#进不属于栈顶的后括号也直接结束
                    return False
        # 空栈说明全部匹配
        return True if not stack else False
    ```

  - **32. 最长有效括号（hard）**：进阶应用，利用栈存储索引来计算两个匹配点之间的间距。<a id="lc-32"></a>

    - 本题的重点：与20不同，栈中不能只放左边括号，也要在适合的是后加入右边括号以分割参考位置，从而划分不同的起点。

      ```python
      def longestValidParentheses(self, s: str) -> int:
          if len(s) <= 1: # 剪枝
              return 0
          n = len(s)
          max_len = 0
          stack = [-1] # 栈底用于放置“参照物”（分割点）
      
          for i in range(n):
              if s[i] == "(":
                  stack.append(i)
              else:
                  # 遇到 ）
                  stack.pop() # 先尝试匹配
      
                  if not stack:
                      # 如果栈空了，说明刚才弹出的是“参照物”
                      # 这意味着当前的 ')' 没有匹配，它变成了新的“参照物”
                      # 此时，-1消失，但是当前位置取代了它的作用
                      stack.append(i)
                  else:
                      # 如果栈不空，说明刚才弹出的是 '('，匹配成功
                      # 此时 stack[-1] 是这一段匹配的“参照物”下标
                      max_len = max(max_len, i - stack[-1])
      
          return max_len
      ```



### 体系二：单调栈 (Monotonic Stack) —— “寻找邻居与范围扩散”

这是线性优化中最具威力的技巧之一。它通过保持栈内元素的单调性，强制剔除不可能成为答案的选项。

留在栈里的，都是**还没有找到比自己大的后续数字**的人。 一旦出现一个大的，它就会把栈中那些比它小或者大的统统“消除”掉。 所以，**能留在栈里没被消除的，一定是一个单调的（或者说没法被后面的数“吃掉”的）。**

- **核心逻辑**：
  
  - **“及时止损”**：以单调递增栈为例，当新元素比栈顶小时，它会直接把栈顶“踢出”，因为对于后面的元素来说，这个新元素更小、更有可能作为左边界，旧的栈顶已经失去了存在的意义。
  - **时间复杂度**：虽然有嵌套循环的既视感，但每个元素**最多进栈一次、出栈一次**，因此是严格的 $O(N)$。
  
- **适用场景**：

  - 关键词：**“下一个更大/更小”、“左/右第一个比它大/小的数”、“最大矩形面积”**。
  - 逻辑定位：专门解决**“寻找最近的邻居”**这一类问题。

- **包含题目**：
  
  - **739. 每日温度**：寻找“下一个更大”的元素。<a id="lc-739"></a>
  
    ```python
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = [] # 存索引
    
        for i, temp in enumerate(temperatures):
            # 当栈不为空，且当前温度比栈顶索引对应的温度高
            # 说明栈顶那个元素的“下一个更高温度”找到了，就是当前这个 temp
            while stack and temp > temperatures[stack[-1]]:
                # 遍历所有小于当前温度的天数并且pop
                # 在栈中的天数都是没有找到最近高温的
                prev_index = stack.pop()
                ans[prev_index] = i - prev_index # 计算距离
    
            # 把当前索引入栈，等待它的“更高温度”出现
            stack.append(i)
    
        return ans
    ```
  
  - **84. 柱状图中的最大矩形**（hard）：寻找“左右第一个更小”的边界。<a id="lc-84"></a>
  
    ```python
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 技巧：首尾加 0 (哨兵)
        # 左边的 0 防止栈空，右边的 0 强迫所有元素出栈计算
        heights = [0] + heights + [0]
        stack = [] # 存索引
        max_area = 0
        for i, h in enumerate(heights):
            # 循环条件：当前高度 < 栈顶高度
            # 说明栈顶那个柱子遇到了右边的“矮子”，无法延伸了，必须结算！
            while stack and h < heights[stack[-1]]:
                # 核心逻辑：弹栈，算面积
                cur_height_index = stack.pop()
                cur_height = heights[cur_height_index]
                # 此时：
                # i 是cur_height_index右边界 (right boundary) -> 第一个比它矮的
                # stack[-1] 是左边界 (left boundary) -> 栈里剩下的那个肯定是比它矮的
                left_boundary = stack[-1]
                right_boundary = i
                # 宽度计算公式：(右 - 左 - 1), 即面积最多延伸到两边边界（两百年第一个小的数）的上一个
                # 这样可以保证最大化面积
                width = right_boundary - left_boundary - 1
                max_area = max(max_area, cur_height * width)
    
            #满足单调递增，入栈
            stack.append(i)
        return max_area
    ```
  
  - **85. 最大矩形（hard）**: 本题是84题的升维版本。我们只要把矩阵看成是m个84题那样的柱状图就好。 <a id="lc-85"></a>
  
    ```python
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # 这是 84 题的原题代码，直接搬过来作为 helper function
        def largestRectangleArea(heights: List[int]) -> int:
            heights = [0] + heights + [0] # 哨兵技巧
            stack = []
            max_area = 0
            for i, h in enumerate(heights):
                while stack and h < heights[stack[-1]]:
                    h_idx = stack.pop()
                    width = i - stack[-1] - 1
                    max_area = max(max_area, heights[h_idx] * width)
                stack.append(i)
            return max_area
    
        if not matrix: return 0
        n = len(matrix[0])
        heights = [0] * n  # 初始化高度数组，相当于把二维压扁成一维
        max_matrix_area = 0
    
        # 逐行遍历
        for row in matrix:
            for i in range(n):
                if row[i] == "1":
                    heights[i] += 1  # 累加高度
                else:
                    heights[i] = 0   # 遇到 0，柱子断裂，高度重置
            # 每一行更新完后，都调用一次 84 题的逻辑
            current_layer_max = largestRectangleArea(heights)
            max_matrix_area = max(max_matrix_area, current_layer_max)
    
        return max_matrix_area
    ```
  
    

### 体系三：单调队列 (Monotonic Queue) —— “滑动窗口极值”

单调队列是单调栈的变体，它允许从两端操作，解决了“过期数据”的问题。

- **包含题目**：
  
  - **239. 滑动窗口最大值**。<a id="lc-239"></a>
  
    ```python
    # 存储数值
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        if not nums or k == 0: return []
        n = len(nums)
        max_list = []
        mdeque = deque() # 单调队列
    
        # 第一个窗口内全部遍历, 以构建完整单减队列
        for i in range(k):
            while mdeque and mdeque[-1] < nums[i]:
                mdeque.pop() # 这里新来的元素大于deque末尾，说明其不可能成为最大值直接弹出
            # 构建递减队列
            mdeque.append(nums[i])
        max_list.append(mdeque[0])
    
        # 处理后面所有的数字
        for i in range(k, n):# 可以把i想象成是右指针，此时左指针还在上一轮滑窗的起始位置
            # 开始滑窗，相当于先移动右指针
            if mdeque[0] == nums[i-k]:# 如果最大值对应左指针（移位前）位置的数字
                mdeque.popleft() # 弹出旧的左指针位置的值（因为当前左指针的值不在未来的滑窗内了），然后相当于默认左指针移动到 i-k+1
            while mdeque and mdeque[-1] < nums[i]:
                mdeque.pop()
            mdeque.append(nums[i])
            # 对当前滑窗结果处理完毕，记录最大值，即deque的左值
            max_list.append(mdeque[0])
    
        return max_list
    
    
    # 存储下标
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
            # 存下标 index
            q = deque() 
            result = []
            
            for i, num in enumerate(nums):
                # 1. 入队前清理min值（维护单调递减）
                # 如果新来的 num 比队尾元素大，那么队尾元素这辈子都不可能成为最大值了
                # 因为 num 比它大，还比它活得久
                while q and nums[q[-1]] < num:
                    q.pop() # O(1) 尾部弹出
                
                # 2. 入队
                q.append(i)
                
                # 3. 出队过期元素（维护窗口大小）
                # 检查队头元素是否已经滑出了 k 的范围
                # 当前窗口范围是 [i - k + 1, i]，如果队头下标 < i - k + 1，说明过期
                if q[0] == i - k:
                    q.popleft() # O(1) 头部弹出
                
                # 4. 记录结果
                # 当窗口形成后（即 i >= k - 1），队头永远是当前窗口的最大值
                if i >= k - 1:
                    result.append(nums[q[0]])
                    
            return result
    ```
  
- **核心逻辑**：
  - **“强龙不压地头蛇 + 岁月不饶人”**：
    1. **强龙不压地头蛇**：新进入窗口的元素如果比队尾大，说明队尾永远不可能成为最大值了（因为它比新来的小还比新来的老），直接弹出队尾。
    2. **岁月不饶人**：检查队首元素，如果它的索引已经滑出了窗口范围，直接弹出队首。
  - 这样，**队首永远是当前窗口的最值**。
  
- **适用场景**：
  - 关键词：**“连续滑动窗口”、“区间最大/最小值”**。
  - 逻辑定位：它是对“体系一：滑动窗口”的补全。当窗口移动时需要快速获取最值，就用单调队列。

---

## 模块四：对数时间优化  —— 二分查找

**核心口诀**：

1. **有序**（单调）是二分的前提。
2. **无序**如果要二分，必须具备**“二段性”**（能通过某种逻辑把数组切分成两半，一半满足条件，一半不满足）。

### 核心难点攻克：二分区间与边界模板

这是二分查找最容易写死循环的地方。为了统一记忆，我强烈建议使用 **“红蓝染色法”** 或 **“前闭后闭区间模板”**。

这里为您推荐最通用、最不易出错的 **前闭后闭 `[left, right]` 模板**。

#### 1. 通用模板：前闭后闭 `[left, right]`

这种写法的核心思想是：**left 和 right 都在有效搜索范围内**。

```Python
def binarySearch(nums, target):
    left, right = 0, len(nums) - 1  # 1. 定义：[left, right] 都是闭区间
    
    while left <= right:            # 2. 终止条件：因为是闭区间，left == right 时区间内还有一个元素，必须继续检查，所以要有 =
        
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            return mid              # 找到直接返回
        elif nums[mid] < target:
            left = mid + 1          # 3. 移动：mid 已经检查过了太小，搜索区间变为 [mid+1, right]
        else:
            right = mid - 1         # 4. 移动：mid 已经检查过了太大，搜索区间变为 [left, mid-1]
            
    return -1                       # 循环结束 left > right，说明没找到
```

#### 2. 进阶：寻找左/右边界 (针对题 34, 875, 410)

当题目要求“满足条件的最小值”或“最大值”时，我们不再找到就 `return`，而是**记录答案，继续收缩**。场景：找满足条件的最小值 (例如 875 题求最小速度) ——这是最常用的模板，用于**“值域二分”**。

```Python
def searchMinimize(left, right):
    ans = -1
    while left <= right:             # 依然使用前闭后闭
        mid = left + (right - left) // 2
        
        if check(mid):               # check函数判断 mid 是否满足条件
            ans = mid                # 1. 记录这个可行解
            right = mid - 1          # 2. 贪心：尝试找更小的 (向左收缩)
        else:
            left = mid + 1           # 3. 不满足，必须变大才行
            
    return ans                       # 或者 return left (循环结束后 left 指向的就是最小满足值)
```

#### 3. 为什么有时候会死循环？

死循环通常发生在以下组合（**错误的搭配**）：

- **错误 A**：`while left < right` 配合 `right = mid`。
  - 当区间只剩两个数 `[0, 1]` 时，`mid` 算出来是 `0`。如果逻辑走进 `left = mid`，`left` 还是 `0`，区间永远是 `[0, 1]`，死循环。
- **错误 B**：`while left <= right` 配合 `right = mid`。
  - 因为 `<=` 会运行到 `left == right`，此时 `right = mid` 会导致 `right` 不动，死循环。

**✅ 避坑总结（黄金法则）：**

1. 永远使用 `while left <= right`。
2. 永远手动排除 mid：
   - `left = mid + 1`
   - `right = mid - 1`
3. 如果是找边界，用一个变量 `ans` 记录中间结果，而不是最后去纠结返回 `left` 还是 `right`。

### 体系一：下标二分 (Index Search) —— 在数组里找位置

这是最传统的二分，在一个显式的数组中查找目标值的下标。

- **核心逻辑**：通过比较 nums[mid] 和 target 的大小，缩小 [left, right] 的下标范围。

- **包含题目**：

  - **33. 搜索旋转排序数组** (二段性分析) <a id="lc-33"></a>

    - **难点**：数组被旋转了（如 `[4,5,6,7,0,1,2]`），不再整体有序。

    - **破局**：虽然整体无序，但**切一刀后，必定有一半是有序的**。

    - **逻辑**：

      1. 计算 `mid`。
      2. 如果 `nums[0] <= nums[mid]`，说明 **[0, mid] (左半边) 是有序的**。
      3. 如果 `target` 落在左半边范围内，`right = mid - 1`；否则去右半边找 `left = mid + 1`。
      4. 反之亦然。

      ```python
      def search(self, nums: List[int], target: int) -> int:
          l, r = 0, len(nums) - 1
      
          while l <= r:
              mid = (l + r) // 2
              # 找到目标，直接返回
              if nums[mid] == target:
                  return mid
      
              # mid 落在左半边的有序区间（高坡）
              # 左半坡是单调的，所有数字一定 >= nums[0]
              if nums[0] <= nums[mid]:
                  # A-1：判断 target 是否在这个有序的 [0, mid) 区间内
                  # 必须用 nums[0] <= target，target 可能就是起点
                  if nums[0] <= target < nums[mid]:
                      r = mid - 1  # target 在左单增区间，缩右边界
                  else:
                      l = mid + 1  # target 在单调的右边或者更右边的无序区间（可能在左坡的后半段，也可能在右坡）
      
              # mid 落在右半边的有序区间（矮坡）
              # 隐含条件：nums[mid] < nums[0]
              else:
                  # B-1：判断 target 是否在这个有序的右区间内
                  # 必须用 target <= nums[len-1]，target可能是终点
                  if nums[mid] < target <= nums[-1]:
                      l = mid + 1  # target 在右边，缩左边界
                  else:
                      r = mid - 1  # target 不在这，去左边找（可能在右坡的前半段，也可能在左坡）
      
          return -1
      ```

  - 类似：162 寻找峰顶；153 寻找旋转排序数组中的最小值 <a id="lc-153"></a>

    ```python
    # 153
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l, r = 0, len(nums)-1
    
        while l <= r:
            mid = (l + r) // 2
    		# 保证半坡的一致性
            if nums[mid] <= nums[-1]:
                r = mid - 1
            else:
                l = mid + 1
    
        return nums[l]
    ```

  - **34. 在排序数组中查找元素的第一个和最后一个位置** (边界查找) <a id="lc-34"></a>

    - **难点**：数组中有重复元素（如 `[5,7,7,8,8,10]` 找 8），普通的二分找到一个 8 就会停止，但我们需要找边界。

    - **逻辑**：

      - **找左边界 (Lower Bound)**：找到 `mid` 等于 target 时，**不要停**，然后**继续向左收缩** (`right = mid - 1`)，看前面还有没有。
      - **找右边界 (Upper Bound)**：找到 `mid` 等于 target 时，**不要停**，然后**继续向右收缩** (`left = mid + 1`)。
      - 两种做法，都是分别计算上下bound，但是可以分别构建（1），或者采用技巧只构建一次搜索（2）

      ```python
      #（1）
      def searchRange(self, nums: List[int], target: int)
          if len(nums) == 0:
              return [-1, -1]
      
          # 双指针，下标处碰撞
          def lower_bound(nums: List[int], target: int):
              l , r = 0, len(nums) -1 # 闭区间 [0, n-1]
      
              while l <= r: # 闭区间结束条件：l跑到r右边
                  mid = (l + r) // 2 # 向下取整
                  if nums[mid] < target:
                      # 左指针扩张
                      l = mid + 1 # 区间 [mid+1, r]
                  elif nums[mid] >= target:# 寻找下标，相等也不断缩小大的范围
                      # 右指针缩小
                      r = mid - 1 # 区间 [l, mid-1]
              # 闭区间返回左指针，最后一次右指针一定会缩小而左指针留在原位
              return l 
          
      	# 双指针，上标处碰撞
          def upper_bound(nums: List[int], target: int):
              l , r = 0, len(nums) -1 # 闭区间 [0, n-1]
      
              while l <= r: # 闭区间结束条件：l跑到r右边
                  mid = (l + r) // 2 # 向下取整
                  if nums[mid] <= target:#寻找上标，相等也不断扩张小的范围
                      # 左指针扩张
                      l = mid + 1 # 区间 [mid+1, r]
                  elif nums[mid] > target:
                      # 右指针缩小
                      r = mid - 1 # 区间 [l, mid-1]
              # 闭区间返回右指针，最后一次左指针一定会扩张而右指针留在原位
              return r 
                       # 这是由等于号的放置的位置决定的
      
      
          lower = lower_bound(nums, target)
          # 额外情况： 
          # 1. l遍历的数组没找到（不在数组范围内）
          # 2. 再数组范围内但是数组中没有这个target
          if lower == len(nums) or nums[lower] != target:
              return [-1, -1]
      
          upper = upper_bound(nums, target)
          return [lower, upper]
      
      # 2
      def searchRange(self, nums: List[int], target: int) -
          if not nums: return [-1, -1]
      
          # 这是一个通用的找“左侧边界”的模版 (>= target 的第一个位置)
          def find_start(target_val):
              l, r = 0, len(nums) - 1
              while l <= r:
                  mid = (l + r) // 2
                  if nums[mid] < target_val:
                      l = mid + 1
                  else:
                      # nums[mid] >= target_val
                      # 我们希望锁定左边界，所以即使相等，也要让 r 向左收缩
                      r = mid - 1
              return l
      
          # 1. 找 target 的起始位置
          start_idx = find_start(target)
      
          # 校验 start_idx 是否越界，或者是否真的等于 target
          if start_idx == len(nums) or nums[start_idx] != target:
              return [-1, -1]
      
          # 2. 找 target 的结束位置
          # 技巧：找 (target + 1) 的左边界，它的前一个位置一定是 target 的结束位置
          # 例如 [5, 7, 7, 8, 8, 10], target=8
          # find_start(8) 返回下标 3 (第一个8)
          # find_start(9) 返回下标 5 (数字10的位置)
          # 结束位置 = 5 - 1 = 4
          end_idx = find_start(target + 1) - 1
      
          return [start_idx, end_idx]
      ```

  
  - **74.[搜索二维矩阵](https://leetcode.cn/problems/search-a-2d-matrix/)**(矩阵一维化) <a id="lc-74"></a>
  
    - 问题：寻找一个递增顺序排列m * n的矩阵中的target
    - 矩阵虽然多维，但是整体单调，相当于一个单调数组，展平即可
    - 展平后该题相当于一个二分查找target的数组题
  
       ```python
       def searchMatrix(self, matrix: List[List[int]], target: int) -
           def get_r_c(ind, r, c):# 展平拆分下标ind
               i = ind // c 
               j = ind % c 
               return i,j
       
           row_nums, col_nums = len(matrix),len(matrix[0])
           l,r = 0, row_nums * col_nums-1
       
           while l <= r: # 二分开始，闭区间
               mid = (l + r) // 2
               i,j = get_r_c(mid, row_nums, col_nums)
       
               if matrix[i][j] == target:
                   return True
               elif matrix[i][j] < target:
                   l = mid + 1
               else:
                   r = mid - 1
       
           return False
       ```
  
    

### 体系二：值域二分 (Binary Search on Answer) —— 在答案范围里找结果

这类题目**不再是在数组里找下标**，而是题目要求的**答案本身**具有单调性。我们需要对**答案的取值范围**进行二分。

- **核心逻辑**：
  1. 确定答案的**最小可能值 (left)** 和 **最大可能值 (right)**。
  
  2. 猜一个中间值 `mid`。
  
  3. 写一个辅助函数 `check(mid)`：如果 `mid` 这个答案满足条件，尝试更优解（通常是更小或更大）；如果不满足，则缩小范围。
  
  4. 注意：这类题有一个小的共性，一般二分的目标和对象，不会是数组本身，而是实际要求的目标值或者次目标值，例如：
  
     - 我们给某数组分组。可以推测出分组的最大值上下界，那就对这个分组值做二分
  
     所以，我们可以以寻找上下界为突破口快速识别二分对象。
  
- **包含题目**：
  - **875. 爱吃香蕉的珂珂** (典型值域二分)  <a id="lc-875"></a>
    
    - **问题**：求最小的吃香蕉速度 `k`。
    - **单调性**：速度 `k` 越快，耗时越短。如果速度 `k` 能吃完，那么 `k+1` 肯定也能吃完（**满足单调性**）。
    - **范围**：最小速度 1，最大速度 `max(piles)`。
    - **check(speed)**：计算以当前速度吃完所有香蕉需要多少小时。如果 `耗时 <= h`，说明速度够快，记录答案，尝试减速 (`right = mid - 1`) 找更小的 `k`。
    
    ```python
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 速度 `k` 越快，耗时越短。如果速度 `k` 能吃完，那么 `k+1` 肯定也能吃完（**满足单调性**）--> 二分法解决
        def is_k_enough(k, piles, h):
            total_h = 0
            for pile in piles:# O(n)遍历
                if pile % k == 0: total_h += pile // k
                else : total_h += pile // k + 1 
            return total_h <= h
    
        max_k = max(piles)
        min_k = max_k
        l,r = 1, max_k
    
        while l <= r:
            mid = (l + r) // 2 # O(logn) bisect 查找
            if is_k_enough(mid, piles, h) == True:
                min_k = min(mid, min_k)
                r = mid - 1
            else:
                l = mid + 1
    
        return min_k
    
    ```
    
  - **410. 分割数组的最大值** (Hard 级值域二分) <a id="lc-410"></a>
    
    - **问题**：将数组分成 `m` 段，使得这 `m` 段中**和最大的一段**尽可能小。
    
    - **范围**：
      
      - 下界 `left`：`max(nums)` (因为最大和至少要是数组中最大的那个单独元素)。
      - 上界 `right`：`sum(nums)` (把整个数组当成一段)。
      
    - **check(max_sum)**：如果你限制每一段的和不能超过 `max_sum`，我最少需要把数组分成几段？
      - 如果 `分成的段数 <= m`，说明限制太宽松了，可以尝试缩小 `max_sum` (`right = mid - 1`)。
      - 和上题很像，但是875
      
      ```python
      def splitArray(self, nums: List[int], k: int) -> int:
          def can(max_value, k):
              splits = 1 # 分割的次数
              cur_split_val = 0 # 当前分割点的累加值
              for x in nums:
              	# 小于max的时候一直累加
                  if cur_split_val + x <= max_value: 
                      cur_split_val += x
                  else: # 大于的时候直接划分下一批次
                      splits += 1
                      cur_split_val = x # 下一分割批次的初始和为为当前x
                      # 超过k组说明当前分组太多, max_value太小，提前剪枝
                      if splits > k:  
                          return False
              return True
      
          low, high = max(nums), sum(nums)
      
          while low <= high:
              mid = (low + high) // 2
              if can(mid,k):
                  high = mid - 1
              else:
                  low = mid + 1
          return low
      ```
      
    
  - **1004. 最大连续1的个数 III** <a id="lc-1004"></a>
    
    - **最优解是滑动窗口**。
    - **二分做法**：可以对“最长长度”进行二分。猜一个长度 `len`，检查数组中是否存在一个长度为 `len` 的子数组，其包含的 0 的个数不超过 `k`。复杂度 $O(N \log N)$，不如滑动窗口 $O(N)$。

---

## 模块五：图论与搜索 (Graph Theory & Search)

我们把图论题分为两种背景：

1. **具象图（网格 Grid）**：在这个世界里，节点是矩阵中的格子 `(r, c)`，边是“上下左右”四个方向。
2. **抽象图（邻接表 Adjacency List）**：在这个世界里，节点是 ID（0, 1, 2...），边是依赖关系（课程表、社交网络）。

### 体系一：网格图搜索 (Grid DFS/BFS) —— “岛屿问题”

这是图论中最直观的类型。核心是**“沉没法”**（避免使用额外的 visited 数组，直接修改原数组标记已访问）。

| **算法选择**            | **适用场景**                             | **典型题目**    |
| ----------------------- | ---------------------------------------- | --------------- |
| **DFS (递归)**          | 找连通块数量、找最大面积（不求最短路径） | 200. 岛屿数量   |
| **BFS (队列)**          | **多源**扩散、求**最短**路径/层数        | 994. 腐烂的橘子 |
| **回溯 (Backtracking)** | 找特定路径（走不通要回头）               | 79. 单词搜索    |

这里，DFS（深度优先搜索）和 BFS（广度优先搜索）本质上都是**图的遍历算法**。它们的区别在于**“遍历的顺序”**以及**“使用的数据结构”**。我们来总结一下他们的用法：

#### 1. DFS：深度优先搜索 (Depth-First Search)

**核心口诀**：“不撞南墙不回头”。

- **行为模式**：一条路走到头。从起点出发，选定一个方向一直往下钻，直到无路可走（碰到边界或已访问节点），然后回溯（Backtrack）到上一个路口，换个方向继续钻。
- **数据结构**：**栈 (Stack)**。
  - 通常使用 **递归 (Recursion)** 实现，利用系统调用栈（System Call Stack）。
  - 也可以手动维护一个栈来实现迭代版本。
- **适用场景**：
  - **找连通性**：判断两点是否相通（如 200. 岛屿数量）。
  - **找所有解**：虽然这也是回溯的范畴，但 DFS 是基础。
  - **拓扑排序**（后序遍历）。

**DFS 通用模板 (递归版 - 最常用)**

以**网格图 (Grid)** 为例（如岛屿问题），这是面试中最常见的 DFS 场景。

```Python
def dfs_grid(grid, r, c):# visited grid, row, col
    # 1. Base Case (终止条件)
    # 越界，或者遇到了边界条件，或者遇到了已经访问过的节点
    if not (0 <= r < len(grid) and 0 <= c < len(grid[0])) or grid[r][c] != '1':
        return

    # 2. Mark Visited (标记已访问)
    # 在网格题中，通常直接修改原数组来标记（如把陆地变成海水），避免使用额外的 visited 集合
    grid[r][c] = '2' # 标记为 2 表示已访问，或者直接变 '0' 沉没

    # 3. Recursion (递归访问邻居)
    # 上下左右四个方向
    dfs_grid(grid, r - 1, c) # 上
    dfs_grid(grid, r + 1, c) # 下
    dfs_grid(grid, r, c - 1) # 左
    dfs_grid(grid, r, c + 1) # 右

# 调用入口
# for i in range(rows):
#     for j in range(cols):
#         if grid[i][j] == '1':
#             dfs_grid(grid, i, j)
```

#### 2. BFS：广度优先搜索 (Breadth-First Search)

**核心口诀**：“层层推进，地毯式搜索”。

- **行为模式**：像水波纹扩散一样。先访问**离起点最近**的所有节点（第1层），再访问离起点距离为2的所有节点（第2层）, 以此类推。
- **数据结构**：**队列 (Queue)**。
  - 由于我们寻找的是每时每刻离当前起点最近的邻接点，所以需要维护一个类似于先入先出的队列，并且要随时retrieve队列的头部值。
  - 必须使用 `collections.deque`，因为列表的 `pop(0)` 是 $O(N)$，而 deque 的 `popleft()` 是 $O(1)$。
- **适用场景**：
  - **最短路径 (Shortest Path)**：这是 BFS 的杀手锏。在**无权图**中，BFS 第一次找到目标时走过的步数一定是最少的（如 994. 腐烂的橘子）。
  - **层序遍历**：如二叉树的层序遍历。

**BFS 通用模板 (层序遍历版 - 强烈推荐)**

这个模板非常重要，因为它包含了一个 `for _ in range(size)` 的循环，这样你可以清楚地知道**当前是在第几层**（也就是走了几步）。这对于计算“最短路径”或“腐烂需要几分钟”至关重要。BFS的开始通常是：**找到这个图的起点先入队**！

```Python
from collections import deque

def bfs(start_node, target_node):
    # 1. 初始化队列和 visited 集合
    queue = deque([start_node])
    # 避免走回头路，但是这个像dfs一样直接用原grid中使用不同状态取代
    visited = set([start_node]) 
    step = 0 # 记录扩散的步数（层数）

    while queue:
        # 2. 获取当前层级的节点数量
        # 这一步很关键！它锁定了当前层有多少个节点
        size = len(queue)
        
        # 3. 遍历当前层的所有节点
        for _ in range(size):
            cur = queue.popleft()
            
            # 4. 判断是否到达终点
            if cur == target_node:
                return step
            
            # 5. 将所有未访问的邻居加入队列
            # get_neighbors 是一个假设函数，根据题目不同而定
            for neighbor in get_neighbors(cur):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        # 6. 当前层遍历结束，步数 +1
        step += 1
    
    return -1 # 没找到
```



#### DFS vs BFS 核心对比表格

为了方便记忆，我们可以做一个简单的对比：

| **特性**       | **DFS (深度优先)**          | **BFS (广度优先)**       |
| -------------- | --------------------------- | ------------------------ |
| **比喻**       | 走迷宫 (一条路走到黑)       | 水波纹 (一圈圈扩散)      |
| **数据结构**   | **Stack** (递归/系统栈)     | **Queue** (队列)         |
| **最短路径?**  | 不能保证最短                | **一定是最短** (无权图)  |
| **空间复杂度** | $O(H)$ (H为树高/递归深度)   | $O(W)$ (W为最大宽度)     |
| **典型例题**   | 岛屿数量 (200), 全排列 (46) | 腐烂橘子 (994), 最小步数 |
| **代码风格**   | 递归简洁，逻辑深奥          | 迭代清晰，模板固定       |

问题：既然直接改 Grid 这么爽，为什么我们还会看到很多代码在DFS/BFS时用 `seen`？主要有三个原因：

1. **题目不允许修改输入 (Read-only)**： 有的面试官会要求：“输入矩阵代表地图，你不能把地图改坏了，后面还要用”。这时候必须用 `seen`。
2. **状态回溯 (Backtracking)**： 比如 **79. 单词搜索**。这条路走不通，我要退回来，把标记擦掉。如果直接修改 grid ，回退时还得记住原来的值改回去。用 `visited` 集合（或局部标记）更方便逻辑管理。
3. **复杂的图结构**： 比如 **133. 克隆图** 或者 **207. 课程表**。这些题目给的不是二维矩阵，而是邻接表。你没法像在矩阵里那样简单地把 `1` 变成 `0`。你必须用一个哈希表或数组来记录哪个节点 ID 被访问过。

下面我们来直接看典型的题目

- **包含题目**：

  - **200. 岛屿数量** (Grid DFS 母题) <a id="lc-200"></a>

    - **核心逻辑**：遍历矩阵，遇到 `'1'` (陆地) 就让计数器 +1，然后立马启动 DFS，把这块陆地连同和它相连的所有陆地都变成 `'0'` (沉没)。这样主循环下次就不会再重复统计它们了。

    ```Python
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        m, n = len(grid), len(grid[0])
        count = 0
    
        def dfs(r, c):
            # 越界或者不是陆地，直接返回
            if not (0 <= r < m and 0 <= c < n and grid[r][c] == '1'):
                return
    
            grid[r][c] = '0' # 核沉没它！标记为已访问
    
            # 向四个方向扩散
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
    
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j) # dfs相当于将该岛屿直接沉没
        return count
    ```

    当然，本题也可以用BFS求解。本题是单源bfs，每个岛屿当作独立事件来处理：**“把属于当前这个岛屿的所有陆地全部挖出来（标记为已访问）”**

    ```python
    def numIslands(self, grid: List[List[str]]) -> int:
        from collections import deque
    
        island_count = 0
        r, c = len(grid), len(grid[0])
    
        def bfs(i,j):
            queue = deque() # 起点入队， 并且立即沉没
            queue.append([i,j])
            grid[i][j] = '0' 
    
            while queue:
                i, j = queue.popleft()
    
                for pos_i, pos_j in [(-1,0), (1,0), (0,-1), (0,1)]:
                    cur_i, cur_j = i + pos_i,  j + pos_j
    
                    if 0 <= cur_i < len(grid) and 0 <= cur_j < len(grid[0]):
                        if grid[cur_i][cur_j] == '1': 
                            # 一样，加入队列，然后立即沉没
                            queue.append([cur_i, cur_j])    
                            grid[cur_i][cur_j] = '0'
                            # 相当于他们是同一“组”
    
        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1":
                    island_count += 1
                    bfs(i,j)
    
        return island_count
    ```

  - **[695. 岛屿的最大面积](https://leetcode.cn/problems/max-area-of-island/)** <a id="lc-695"></a>

    - 与200类似，只增加了一个面积

    ```python
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        max_area = 0
    
        def dfs(i, j, r, c, cur_area):
            if 0 <= i < r and 0 <= j < c and grid[i][j] == 1:
                grid[i][j] = 0 # 沉没
                cur_area += 1
            else:# 终止条件：返回当前面积
                return cur_area
    
            # dfs adjacent nodes
            for pos_i, pos_j in [(-1,0),(1,0),(0,-1),(0,1)]:
                cur_area = dfs(i+pos_i, j+pos_j, r, c, cur_area)
            return cur_area
    
        cur_area = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    cur_area = dfs(i, j, r, c, cur_area)
                    max_area = max(max_area, cur_area)
                    cur_area = 0
    
        return max_area
    ```
    
  - **994. 腐烂的橘子** (**多源** BFS) <a id="lc-994"></a>
  
    - **核心逻辑**：
  
      1. 这题求的是“最小分钟数”（最短路径），所以**必须用 BFS**，不能用 DFS。
      2. 这是一个**“多源 BFS”**，一开始队列里可能有多个烂橘子。它们是同时向外扩散的。所以，这个图的起点就是第一批腐烂的橘子，我们先将他们入队
      3. 每一轮（level）扩散，时间 +1。
      4. 注意：因为腐烂过程是 **“并发” (Parallel)** 的。而我们的目的是求所有源头同时扩散的最短时间，所以在一开始（队列起点）就要入队所有源头。这也是被称作多源bfs的原因。
  
      ```python
      def orangesRotting(self, grid: List[List[int]]) -> int:
          from collections import deque
      
          queue = deque() # deque可以把pop(0)的复杂度变为O(1)
          minutes = 0
          fresh = 0
          r, c = len(grid), len(grid[0])
      
          # 将腐烂的橘子做为起点入队
          for i in range(r):
              for j in range(c):
                  if grid[i][j] == 2:
                      queue.append([i,j])
                  elif grid[i][j] == 1:
                      fresh += 1 # 记录新鲜橘子数量以满足-1返回
      
          if len(queue) == 0 and fresh > 0: # 
              return -1
          elif len(queue) == 0 and fresh == 0:
              return 0
      
          # BFS 开始
          while queue and fresh > 0:# 条件：当前队列中仍然有邻接的腐烂橘子，或者没有新鲜橘子了
          #第二个条件对最少时间至关重要，否则去三年后i
              for ro in range(len(queue)):# 遍历当前所有的腐烂橘子
                  i,j = queue.popleft() # 从最近的开始
      
                  # 它的四周开始腐烂
                  for pos_i, pos_j in [(-1,0), (1,0), (0,-1), (0,1)]:
                      cur_i, cur_j = i + pos_i, j + pos_j
      
                      # 边界条件
                      if 0 <= cur_i < len(grid) and 0 <= cur_j < len(grid[0]):
                          if grid[cur_i][cur_j] == 1: # 找到新鲜橘子
                              grid[cur_i][cur_j] = 2
                              queue.append([cur_i, cur_j]) # 新的腐烂橘子入队
                              fresh -= 1
              minutes += 1
      
          if fresh > 0: # queue空了（所有腐烂橘子均已遍历，没有邻接的新鲜橘子），
          # 但是还有新鲜橘子数量还有，说明剩下的新鲜橘子，均不与腐烂橘子邻接
              return -1
          return minutes
      ```
  
  - **79. 单词搜索** (网格回溯) <a id="lc-79"></a>
  
    - **核心逻辑**：在网格里找一条路径。不同于“岛屿沉没”，这里如果路走不通，需要**撤销选择**（把标记过的格子还原），以便别的路径还能用这个格子。
    
    ```python
    def exist(self, board: List[List[str]], word: str) -> bool:
        r, c = len(board), len(board[0])
        L = len(word)
        if L > r * c: # 大于总board数量直接返回
            return False
    
        def dfs(i: int, j: int, k: int) -> bool:
            # k 表示正在匹配 word[k]
            if board[i][j] != word[k]:# 非当前字符直接false
                return False
            if k == L - 1: # 
                return True
    
            ch = board[i][j]
            board[i][j] = "#"  # 标记访问
    
            for pos_i, pos_j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                now_i, now_j = i + pos_i, j + pos_j
                if 0 <= now_i < r and 0 <= now_j < c and board[now_i][now_j] != "#":
                    if dfs(now_i, now_j, k + 1):
                        board[i][j] = ch  # 恢复
                        return True
    
            board[i][j] = ch  # 恢复，即撤销之前的visited更改
            return False
    
        for i in range(r):
            for j in range(c):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
        return False
    ```
    

### 体系二：拓扑排序 (Topological Sort) —— “依赖解析”

遇到 **“课程表”、“依赖关系”、“先后顺序”、“死锁检测”** 这类关键词，直接上拓扑排序。

- **核心工具**：**入度表 (Indegree Array)** + **BFS (Kahn 算法)**。

- **包含题目**：

  - **207. 课程表** (检测有向图是否有环) <a id="lc-207"></a>

    - **核心逻辑**：
      1. **建图**：用邻接表 `adj = {前置课: [后继课1, 后继课2]}`。
      2. **入度**：统计每一门课还要等几门前置课才能修 `indegree[i]`。
      3. **启动**：把所有“入度为 0”（不需要前置课）的课放入 Queue。
      4. **BFS**：每修一门课，就把它的后继课入度减 1。如果某后继课入度减为 0，说明它也能修了，入队。
      5. **判断**：最后看修完的课程数量是否等于总课程数。

    ```Python
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 需要注意的是，虽然提示中提到prerequisites[i].length == 2
        # 但是一节课依然可以有多节先修，通过多个prerequisites pair表示，所以一定要建立入度表
        from collections import deque, defaultdict
    
        cres_queue = deque([])
        adj = defaultdict(list) # 邻接表，建图
        # 入度表，代表有多少个“前置条件”，包括多跳前置课程
        indegree = defaultdict(int) 
        total_cres = 0
    
        for cres, pre in prerequisites:
            adj[pre].append(cres)
            indegree[cres] += 1
    
        for cres in range(numCourses):# 没有依赖的课程直接修，入队
            if indegree[cres] == 0:
                cres_queue.append(cres)
    
        if len(cres_queue) == numCourses: # 满足直接返回True
            return True
    
        while cres_queue:# BFS开始，从入队的课程逐渐向所有课程扩散
            pre = cres_queue.popleft()
            total_cres += 1
            # 寻找没有度（没有依赖）的课程是哪些课程的依赖，这些课程可以减度
            for cres in adj[pre]:
                indegree[cres] -= 1
                if indegree[cres] == 0:
                    cres_queue.append(cres)
    
        return total_cres == numCourses
    ```
  
  - **210. 课程表 II** (输出拓扑排序结果) <a id="lc-210"></a>
  
    - **逻辑**：和 207 完全一样，只不过需要用一个列表 `res` 记录每次 `pop` 出来的课程顺序。

### 体系三：普通图的遍历 (Graph Traversal)

处理一般的无向图或有向图，核心是 **“防止走回头路”** (visited set) 和 **“深拷贝”**。

- **包含题目**：
  - **133. 克隆图** (图的深拷贝) <a id="lc-133"></a>
  
    - **核心逻辑**：由于图可能有环，通过 `HashMap` 来记录 `原节点 -> 克隆节点` 的映射。如果一个节点已经克隆过（在 Map 里），直接返回 Map 里的引用，否则创建新节点并递归克隆邻居。
  
  - **208. Trie前缀树**（树，以空间换时间）<a id="lc-208"></a>
  
    - 利用字符串的**公共前缀**来降低查询时间的开销。它不是把单词存在一个平铺的字典里，而是存成一棵树。
    - 例如，插入 "apple" 和 "app"，树的结构是： `root -> a -> p -> p (end) -> l -> e (end)`
    - 我们需要定义一个树节点 `TrieNode`，每个节点包含：
      1. `children`: 一个字典（或数组），指向下一个字符的节点。
      2. `isEnd`: 一个布尔值，标记当前节点是否是一个单词的结尾。
  
    ```python
    class TrieNode:
        def __init__(self):
            # key: char, value: TrieNode
            self.children = {} 
            # 标记是否是单词结尾（比如 'apple' 里的 'e' 是 True，中间的 'p' 是 False）
            self.isEnd = False
    
    class Trie:
    
        def __init__(self):
            self.root = TrieNode()
    
        def insert(self, word: str) -> None:
            node = self.root
            for char in word:
                # 如果当前字符不在子节点中，创建一个新节点
                if char not in node.children:
                    node.children[char] = TrieNode()
                # 移动到子节点
                node = node.children[char]
            # 单词遍历完，在最后一个节点标记为单词结束
            node.isEnd = True
    
        def search(self, word: str) -> bool:
            node = self.searchPrefix(word)
            # 两个条件：
            # 1. 节点存在 (即路径走通了)
            # 2. isEnd 为 True (必须是完整单词，不能只是别人的前缀)
            return node is not None and node.isEnd
    
        def startsWith(self, prefix: str) -> bool:
            node = self.searchPrefix(prefix)
            # 只要能走完前缀的路径，就返回 True，不需要管 isEnd
            return node is not None
    
        # 辅助函数：专门用来走路径
        def searchPrefix(self, prefix: str) -> TrieNode:
            node = self.root
            for char in prefix:
                if char not in node.children:
                    return None # 路径断了，说明不存在
                node = node.children[char]
            return node
    ```
  

---

## 模块六：回溯算法 (Backtracking) —— “撤销的艺术”

核心思路：

回溯法本质上是在一棵决策树上进行深度优先遍历（DFS）。它的运作流程永远是：

1. **路径 (Path)**：已经做出的选择。
2. **选择列表 (Choices)**：当前可以做的选择。
3. **结束条件 (Goal)**：到达决策树底层，无法再做选择。

公式：**回溯 = DFS + 状态重置**。如果不重置状态（pop），上一层递归遗留的数据会带入下一层，导致结果混乱。

### 体系一：Visited数组

这是回溯最原始的形态。每个位置都可以选剩下的任意数字。

- **特点**：

  - 需要记录哪些数字已经被选过（`used` 数组或 `path` 查重）。
  - 顺序不同视为不同结果（`[1,2]` $\neq$ `[2,1]`）。

- **包含题目**：

  - **46. 全排列** (Hot 100)<a id="lc-46"></a>

    - **分析**：这是回溯的“母题”。因为所有数字都互不相同，我们可以直接用 `if num in path` 来判断是否已选。

    ```python
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = [] # 唯一的共享状态
    
        def backtrack(available_nums):
            # 结束条件
            if len(path) == len(nums):
                # 必须拷贝一份当前路径到结果
                # 切忌用append(path)，path到最后已经被pop清空了
                res.append(path[:]) 
                return
    
            for i in range(len(available_nums)):
                num = available_nums[i]
    
                # --- A. 做选择 (Do) ---
                path.append(num) 
    
                # --- B. 递归 (Recurse) ---
                # 下一层决策树：剩下的数字里选 (这里用切片模拟了 used 数组)
                backtrack(available_nums[:i] + available_nums[i+1:])
    
                # --- C. 状态重置 (Undo/Reset) ---
                # 回溯的核心：把刚才放进去的 num 拿出来
                # 否则下一次循环尝试别的数字时，path 里就还有这个 num
                # 例子：从 [1,2,3] 返回到 [1,2]
                # 如果不 pop 掉 3，path 依然是 [1,2,3]。
                # 当我们想去尝试其他分支（比如 [1,2,4]）时，(假设有)
                # path 就会变成错误的 [1,2,3,4]，带着上一次的“脏数据”。
                path.pop() 
    
        backtrack(nums)
        return res
    # -----------------------------------------------------------
    # 或者使用visitied模板
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        # used 数组：记录 nums[i] 是否已经在当前 path 里
        # $O(1)$ 的查重
        used = [False] * len(nums)
    
        def backtrack():
            if len(path) == len(nums):
                res.append(path[:])
                return
    
            for i in range(len(nums)):
             # 关键点：如果 used[i] 是 True，说明这个数字在 path 里了，跳过
                if used[i]: 
                    continue
    
                # 做选择并标记
                used[i] = True
                path.append(nums[i])
    
                # 递归
                backtrack()
    
                # 状态重置 (回溯)
                used[i] = False
                path.pop()
    
        backtrack()
        return res
    ```

    

### 体系二：子集与组合 (Subsets & Combinations) —— “引入 start_index”

这是 Hot 100 中考察频率最高的体系。与全排列不同，这里要求**不走回头路**（`[1,2]` 和 `[2,1]` 是重复的）。

- **核心模板变化**：
  
  - 引入参数 **`start_index`**。
  - 每一层递归循环时，只能从 `start_index` 往后选，从而保证元素的相对顺序固定，避免重复。
  
- **包含题目**：
  
  - **78. 子集** <a id="lc-78"></a>
    
    - **分析**：全排列是收集“叶子节点”，子集是收集树上的**每一个节点**。
    - **逻辑**：每次进入递归都 `res.append(path[:])`。递归调用时传入 `i + 1`。
    
    ```python
    def subsets(self, nums: List[int]) -> List[List[int]]: 
            res = [[]]
            path = []
            n = len(nums)
            if n == 0:
                return res
    
            def backtrace(i):
                path.append(nums[i])
                res.append(path[:])
                # 中止条件：全部都加到数组了
                if i >= n-1:
                    return
                # 遍历当前以后的，因为不能回头
                for j in range(i+1, n):
                    backtrace(j)
                    # 同一阶段，pop掉最后的值才能继续连接新值
                    # 比如 [1,2](下一步值循环一次就返回了),[1,2,3]（不循环直接返回） -> [1,3]
                    path.pop()
    
                return
            
    
            for i in range(n):
                path = []
                backtrace(i)
    
            return res
    ```
    
  - **39. 组合总和**<a id="lc-39"></a>
    
    - **分析**：数字可以**被无限制重复选取**。
    - **区别**：递归调用时传入 **`i`** 而不是 `i + 1`。这意味着“当前这个数字，我下一层还可以接着选它”。
    - **剪枝**：如果 `sum > target`，直接返回。
    
    ```python
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        n = len(candidates)
        
        # 优化点 1: 排序 (为了后续的剪枝)
        candidates.sort()
    
        # 参数优化: 传入 start_index 控制去重，传入 remain 避免重复计算 sum
        # 之前使用了sum(path[:]), O(n),导致时间复杂度高
        def backtrack(start_index, remain):
            # 终止条件 1: 刚好凑满
            if remain == 0:
                res.append(path[:])
                return
            
            # 循环选择
            for i in range(start_index, n):
                num = candidates[i]
                
                # 优化点 2: 剪枝 (Pruning)
                # 如果当前这个数已经比剩下的目标大了，后面的数肯定更大
                # 这里体现了排序的重要性
                if num > remain:
                    break 
                
                # 做选择
                path.append(num)
                
                # 递归
                # 关键点: 传入 i 而不是 i+1，表示当前数字可以重复使用
                # 优化点 3: 传入 remain - num，O(1) 更新状态
                cur_target_sum = remain - num
                backtrack(i, cur_target_sum)
                
                # 撤销选择 (回溯)
                path.pop()
    
        backtrack(0, target)
        return res
    ```
    
  - **77. 组合**<a id="lc-77"></a>
    
    - **分析**：返回范围 `[1, n]` 中所有 `k` 个数的组合。
    - **逻辑**：标准的 `start_index` 控制，递归调用传入 `i + 1`。

### 体系三：分割问题 (Partitioning) —— “切蛋糕”

这类题目表面是字符串处理，实则是组合问题。

- **核心思路**：

  - **“选择”** = **“在哪里切一刀”**。
  - 例如字符串 `aab`，第一刀可以切在 `a|ab`，也可以切在 `aa|b`。

- **包含题目**：

  - **131. 分割回文串** (Hot 100)<a id="lc-131"></a>

    - **分析**：把字符串切成若干块，要求每一块都是回文串。

    - **逻辑**：

      ```python
      def partition(self, s: str) -> List[List[str]]:
          path = []
          res = []
          n = len(s)
      
          def backtraces(i):
              # 题目要求切割字串，则必须连续
              # 又要求是回文, 判断回文是主要的
      
              # 终止条件
              if i == n:
                  res.append(path[:])
                  return
      
              # 以当前下标i作为起点，迭代子串直到尾部
              # 
              for j in range(i, n):
                  if s[i] == s[j]:# 剪枝
                      # 切片当前子串
                      sub = s[i:j+1]
      
                      # 判断回文
                      if sub == sub[::-1]:
                          # 如果是回文，加入当前子串，并在这个位置切一刀
                          path.append(sub)
                          # 递归到切割后的下一个位置，相当于起点变更到j+1
                          backtraces(j+1)
                          # 拿掉上一个添加的回文串，重新在i起点的下一个子串
                          path.pop()
      
              return
      
          backtraces(0)
          return res
      
      
      # 更快的办法: 回溯 + memo
      def partition(self, s: str) -> List[List[str]]:
          n = len(s)
      
          @cache 
          def dfs(i):
              if i == n:
                  return [[]]  # 返回由空列表组成的列表，表示找到一种基准情况
      
              ans = []
              for j in range(i, n):
                  # 先比对首尾字符，不相等则绝不可能是回文
                  if s[i] == s[j]: 
                      sub = s[i:j+1]
                      if sub == sub[::-1]: # 切片检查
                          # 获取当前回文子串的所有的切分结果
                          suffix_partitions = dfs(j + 1)
                          # 将所有后续的回文串拼接到sub后面
                          for p in suffix_partitions:
                              ans.append([sub] + p)
              return ans
      
          return dfs(0)
      
      ```
  
  - **22. 括号组合**<a id="lc-22"></a>
  
    - 左右括号要有顺序插入, 不能随机打乱; 只有剩余的右括号比左括号多（说明加的左括号比右括号多），才能加右括号。
  
    ```python
    def generateParenthesis(self, n: int) -> List[str]:
        path = []
        res = []
        max_len = n * 2
        fq_count = bq_count = n
    
        def backtraces(fq_count, bq_count):
            # 终止条件
            if len(path) == max_len:
                str_path = "".join(path)
                res.append(str_path)
                return
    
            # 每次进来都回溯两次，一次加前括号，一次加后括号
            # 先加左括号,只要还有就一直加
            if fq_count > 0:
                path.append("(")
                backtraces(fq_count-1, bq_count)
                path.pop()
    
        # 只有剩余的右括号比左括号多（说明加的左括号比右括号多），才能加右括号
            if bq_count > fq_count:
                path.append(")")
                backtraces(fq_count, bq_count-1)
                # 会一直pop直到fq_count!=0
                path.pop()
    
            return
        backtraces(fq_count, bq_count)
    
        return res
    ```
  
    

### 体系四：网格回溯 (Grid Backtracking) —— “二维重置”

在二维矩阵中找路径，状态重置体现为**“修路与拆路”**。

- **包含题目**：

  - **79. 单词搜索** (在DFS中已经学习过，再复习一遍)

    - **分析**：在网格中找单词，不能重复走同一个格子。

    - **状态重置**：

      1. **做选择**：`temp = board[i][j]`，然后 `board[i][j] = '#'`（标记为已访问）。
      2. **递归**：向上下左右四个方向 DFS。
      3. **撤销**：`board[i][j] = temp`（恢复原来的字母）。

      - **注意**：这里必须恢复，因为这条路虽然走不通，但别的路径可能还会经过这个格子。

### 体系五：电话号码 (Mapping) —— “层级映射”

每一层递归面对的选择列表是不同的。

- **包含题目**：
  - **17. 电话号码的字母组合** (Hot 100) <a id="lc-17"></a>
    - **分析**：输入 "23"，第一层面对 'abc' (2)，第二层面对 'def' (3)。
    - **逻辑**：`start_index` 在这里代表的是“输入数字字符串的第几位”。

---

## 模块七：动态规划 (Dynamic Programming) —— “状态转移”

核心口诀：状态定义 (State) + 转移方程 (Transition) + 初始条件 (Base Case)。DP 的本质是 “把大问题拆成重叠的小问题（分治），并记下小问题的答案（记忆化）”。

这个记忆化，主要有两种形式：

1. 正常的记忆库 `memo = {}`直接储存所有计算过的节点。这一部分也可以使用python 的@cache来实现

   ```python
   def rob(self, nums: List[int]) -> int:
           @cache  # <--- 这一行自动实现了 memo={} 的所有逻辑
           # 省略了 memo[state] = res 这一填表的步骤
           def dfs(i):
               if i < 0: return 0
               return max(dfs(i-1), dfs(i-2) + nums[i])
   
           return dfs(len(nums) - 1)
   ```

2. 在一些线性DP中，我们只关注有限步以内的数值（比如斐波那契数列），那么我们就不需要显性地维护所有的memo，而是将有限的需要记忆的数值直接转成 **滚动变量 (空间 O(1))**。参考70, 198

### 体系一：线性 DP (1D Array) —— “一步步递推”

数组中第 $i$ 个位置的状态只与 $i-1, i-2$ 等前面的几个状态有关。

- **包含题目**：
  
  - **70. 爬楼梯** (入门)：典型斐波那契数列<a id="lc-70"></a>
    
    - **状态**：$dp[i]$ 表示爬到第 $i$ 阶的方法数。
    - **方程**：$dp[i] = dp[i-1] + dp[i-2]$。**要想上第 $i$ 阶，只能从 $i-1$ 迈一步或者从 $i-2$ 迈两步。**
    - **技巧**：滚动数组优化空间至 $O(1)$。
    
    ```python
    def climbStairs(self, n: int) -> int:
        rec = {}
        rec[2] = 2
        rec[1] = 1
    
        def f(n):
            if n in rec:
                return rec[n]
            res = f(n-1) + f(n-2)
            if res not in rec:
                rec[n] = res
            return res
    
        return f(n)
    
    # 或者还有更加简单的方法，我们要算 f(n)，只需要知道 f(n-1) 和 f(n-2)。至于 f(n-3) 是多少，对当前这一步来说完全不重要（只关注当下）。相当于，爬楼梯的时候，只需要盯着脚下的台阶和前一级台阶。
    def climbStairs(self, n: int) -> int:
        # p 相当于 f(n-2), q 相当于 f(n-1)
        # 初始状态：从 0 级和 1 级开始推导（兼容 n=1 的情况）
        p, q = 0, 1
    
        for _ in range(n): # O(1) 空间转换
            temp = q       # 先把旧的 q 存起来，防止丢失
            q = p + q      # q 变成新值 f(n)
            p = temp       # p 变成旧的 q (从 temp 取回)
    
        return q
    ```
    
  - **198. 打家劫舍** (相邻约束)， 斐波那契数列<a id="lc-198"></a>
    
    - **状态**：$dp[i]$ 表示偷前 $i$ 间房子的最大金额。
    - **方程**：$dp[i] = \max(dp[i-1], \quad dp[i-2] + nums[i])$。
      - 如果不偷第 $i$ 间：利润等于偷前 $i-1$ 间的最大值。
      - 如果偷第 $i$ 间：那么第 $i-1$ 间不能偷，利润等于前 $i-2$ 间的最大值 + 当前房子的钱。
    
    ```python
    # 解法一： DP， 如果要偷 i，只需要访问 dp[i-2]，状态方程：
    # dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    def rob(self, nums: List[int]) -> int:
        @cache
        def f_max(i):
            # 越界处理 (Base Case)
            if i < 0:
                return 0
            # 核心转移方程：
            # max(不偷这家, 偷这家并加上前两家的最大值)
            return max(f_max(i-1), f_max(i-2) + nums[i])
    
        # 从最后一家开始往前推
        return f_max(len(nums) - 1)
    
    # 这种解法也有更加节约空间的
    def rob(self, nums: List[int]) -> int:
        if not nums: 
            return 0
        if len(nums) <= 2: 
            return max(nums)
    
        last_last_rob_max = 0 
        last_rob_max = nums[0]
    
        # 由于我们起始last_rob_max已经假设偷了，所以必须从第二家开始迭代
        for i in range(1, len(nums)):
            # 要么直接拿上一次的最大值，即不偷当前
            # 要么偷当前，但是要加上上次（两步开外）的最大值
            cur_max = max(last_rob_max, last_last_rob_max + nums[i])
    
            last_last_rob_max = last_rob_max # 整体步进 1，所以上上次最大赋值上次最大
            last_rob_max = cur_max
    
    
        return last_rob_max
    
    # 解法二：暴力递归+memo，时间O(N**2)+空间O(N)
    def rob(self, nums: List[int]) -> int:
        # 可以将题目理解为，分治加记忆化
        # 当前只能偷(n-2)!的家庭, 并且最大利润为cur_max + cur_rob
        if len(nums) <= 2:
            return max(nums)
    
        rec = {} # 用于储存已经迭代过的数值
        rec[0] = nums[0]
        rec[1] = nums[1]
        res = []
    
        def f_max(i):
            if i in rec:
                return rec[i]
            cur_max = 0
            # 从 n-2开始，遍历(n-2)!求max
            #需要注意由于range取不到最后一个值，所以必须是range(i-1)不是i-2
            for j in reversed(range(i-1)):
                cur_max = max(cur_max, f_max(j) + nums[i])
            rec[i] = cur_max
    
            return cur_max
    	# 遍历名配合f_max中的i-1，这里要从1开始遍历
        for i in range(1, len(nums)):
            res.append(f_max(i))
    
        return max(res)
    ```
    
  - **121. 买卖股票的最佳时机**(简单状态机) <a id="lc-121"></a>
    
    - 虽然是 DP，但常作为贪心处理。
    - **状态**：记录“历史最低价格” `min_price`。
    - **方程**：$profit = \max(profit, \text{current\_price} - \text{min\_price})$。
    
    ```python
    # 双指针 Greedy
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        max_profit = 0
    
        for r in range(len(prices)):
            # 已经遍历过的天数反正也不能反向再卖出，所以在当前之前最低价格买入
            # 就是当前的全局最大利润的下界
            max_profit = max(max_profit, prices[r] - prices[l])
            # 等到后面的价格下降，再更新左指针
            if prices[r] < prices[l]:
                l = r
    
        return max_profit
    
    # DP
    def maxProfit(self, prices: List[int]) -> int:
        # dp 
        # cur = max(next cur_p) - cur_p # dp
        # max = max(cur)
        max_profit = 0
    
        if len(prices) <= 1:
            return max_profit
    
        @cache
        def max_p(i):
            if i >= len(prices)-1:
                return prices[-1]
            return max(prices[i], max_p(i+1))
    
        for i in range(len(prices)):
            cur_profit = max_p(i+1) - prices[i] 
            max_profit = max(max_profit, cur_profit)
    
        return max_profit
    ```
    
    

### 体系二：网格 DP (Grid DP) —— “机器人走路” 

这是 Hot 100 中不可或缺的一类 DP，通常在二维矩阵上进行。

- **包含题目**：
  - **62. 不同路径** <a id="lc-62"></a>
    - **题目**：机器人从左上走到右下，只能向下或向右，有多少种走法？
    - **状态**：$dp[i][j]$ 表示走到 $(i, j)$ 的路径数。
    - **方程**：$dp[i][j] = dp[i-1][j] + dp[i][j-1]$。（走到当前格子的方法 = 从上面走下来 + 从左边走过来）。
  - **64. 最小路径和** <a id="lc-64"></a>
    - **题目**：网格中有数字，求路径数字之和最小。
    - **方程**：$dp[i][j] = \min(dp[i-1][j], dp[i][j-1]) + grid[i][j]$。



### 体系三：背包与零钱 (Knapsack) —— “组合最值” 

这是面试中最常见的“完全背包”模型。

- **包含题目**：
  - **322. 零钱兑换** <a id="lc-322"></a>
    - **题目**：凑成总金额 `amount` 最少需要几枚硬币（硬币无限用）。
    - **状态**：$dp[i]$ 表示金额为 $i$ 时最少需要的硬币数。
    - **方程**：$dp[i] = \min(dp[i], dp[i - \text{coin}] + 1)$。对于每一个硬币面额，我都可以尝试选它，然后加上“剩下的金额所需的最少硬币数”。



### 体系四：序列/字符串 DP —— “回文与公共子串”

- **包含题目**：
  - **5. 最长回文子串** <a id="lc-5"></a>
    - **状态**：$dp[i][j]$ 表示子串 $s[i..j]$ 是否是回文串。
    - **方程**：$dp[i][j] = (s[i] == s[j]) \text{ and } dp[i+1][j-1]$。
    - **注**：此题也可以用“中心扩散法”解决，空间更省。

---

## 模块八：链表 (Linked List) 

**核心思路**：

1. **哨兵节点 (Dummy Node)**：只要头节点可能发生变化（如删除头节点、合并链表），无脑使用 Dummy 节点指向 head，最后返回 `dummy.next`。
2. **双指针 (Two Pointers)**：
   - **快慢指针**：解决环、中点、倒数第 N 个节点问题。
   - **合并指针**：类似归并排序的 merge 过程。
3. **断链与重连**：操作 `next` 指针时，务必先用临时变量 `temp` 保存下一个节点，防止链表断裂丢失。

### 体系一：结构修改 (Reversal) 

这一类题目的核心是**修改 `next` 指针的方向**。

- **包含题目**：

  - **206. 反转链表** (Hot 100) <a id="lc-206"></a>

    - **分析**：链表基本功。虽然有递归写法，但**迭代法**是必须掌握的肌肉记忆。

    - **模板**：

      ```python
      # Definition for singly-linked list.
      # class ListNode:
      #     def __init__(self, val=0, next=None):
      #         self.val = val
      #         self.next = next
      class Solution:
          def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
          # prev: 指向“已经反转好的链表”的头节点（初始化为 None）
          # curr: 指向“当前正在处理”的节点
          prev, curr = None, head
      
          while curr:
              # 记录当前节点在原链表中的下一个节点地址
              # 如果不存，原链表的后续部分就丢失了
              temp = curr.next
      
              # 正式开始反转
              # 将当前节点的 next 指针指向 prev
              # 这一步实现了当前节点与原后继节点的断开，并指向了新前驱节点
              curr.next = prev 
      
              # prev 指针向后移动一位，现在的 curr 变成了下一轮的 prev
              prev = curr
      
              # curr 指针跳转到保存的 temp 位置，准备处理原链表的下一个节点
              curr = temp
      
          # 循环结束时，curr 指向 None，prev 指向原链表的最后一个节点
          return prev
      ```

  - **92. 反转链表 II** <a id="lc-92"></a>

    - 分析：部分修改链表内容，还可以借鉴206题的思路

    - 核心逻辑：

      1. 注意结束后，把反转的链表的首尾与原链表pre和tail连接。
      2. 要引入哨兵节点，否则当反转的左节点 是节点1 本身的时候，它会找不到pre前节点，导致后面无法进行。

      2. 还有一个要注意的是尾部的赋值涉及到python变量的赋值问题。节点可以看作是对象（object）是被永久分配地址的，但是变量诸如tail和curr则会和当前被分配的对象的变化情况保持一致，具体可以看下面代码中对tail的注释。

    ```python
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # 直接剪枝
        if not head or left == right:
            return head
        # 用哨兵节点，否则处理不了 left=1
        dummy = ListNode(0, head)
        pre = dummy # pre 是left节点的前节点
        n = right - left
    
        for _ in range(left-1):
            pre = pre.next
    
        prev, curr = None, pre.next # curr指向left节点
        # tail锁定现节点，也是反转后的链表尾节点
        # 这里tail指向和curr一样的对象的地址（left节点），
        # 只要节点变了它也会变（区分curr和left节点）
        tail = curr
    
        # 这里需要循环n+1次，因为left到right共有right-left+1个节点
        for _ in range(n+1):
            temp = curr.next
            # 此时 tail和curr依然指向相同的left节点，所以
            # tail也会在这里做一次改变。但只做一次，原因看下一条注释
            curr.next = prev
            prev = curr
            # 注意，这个时候curr要和原来的left节点，tail节点脱钩
            # 所以以后curr的变化不会引起tail变化
            curr = temp
    
        # 把两端的节点接回反转后的链表
        tail.next = curr
        pre.next = prev
    
        return dummy.next
    ```

  - **25. K 个一组翻转链表** (Hot 100)<a id="lc-25"></a>

    - **分析**：链表题的**终极 Boss** (Hard)。它是 LC 206 的进阶版。
    - **核心逻辑**：
      1. **分组**：先判断剩余节点够不够 K 个，不够直接返回。
      2. **子反转**：编写一个 `reverse(head, tail)` 辅助函数。
      3. **拼接**：利用 `prev` 和 `next` 指针把反转后的子链表重新接回主链表。
    - **技巧**：这道题递归写法比迭代写法好写很多，面试如果没限制空间复杂度，优先用递归。

  - **160. 相交链表 (Intersection of Two Linked Lists)**<a id="lc-160"></a>

    - **推荐理由**：如何在 $O(1)$ 空间下找到两个链表的交点
    
    - **核心逻辑**：
      - **问题**：链表 A 长度为 $a$，链表 B 长度为 $b$，公共部分长度为 $c$。
      - **难点**：$a$ 和 $b$ 不一样长，两个指针同时走，永远不会在交点相遇。
      - **技巧**：
        - 指针 A 走完链表 A 后，转而去走链表 B。
        - 指针 B 走完链表 B 后，转而去走链表 A。
      
      ```python
      def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
          # 双指针
          ptr1, ptr2 = headA, headB
      
          while ptr1 != ptr2:
              # 指针 A 走完链表 A 后，转而去走链表 B
              ptr1 = ptr1.next if ptr1 else headB
              # 同时，指针 B 走完链表 B 后，转而去走链表 A
              ptr2 = ptr2.next if ptr2 else headA
              # 他们会相遇在相交的地方
              # 因为此时他们第一次走了<相同的路程>
              # 如果没有相交，会停在重点（1，2都完整遍历了headA和headB）
      
          return ptr1
      
      # 或者使用更简单的哈希算法
      def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
          visited = set()
          temp = headA
          while temp:
              visited.add(temp)
              temp = temp.next
              
          temp = headB
          while temp:
              if temp in visited:
                  return temp
              temp = temp.next
              
          return None
      ```

### 体系二：快慢指针 (Fast & Slow) 

利用两个指针移动速度或启动时间的差异，来解决位置查找问题。

- **包含题目**：

  - **141. 环形链表**  <a id="lc-141">

    - **分析**：判断链表是否有环。

    - **口诀**：快指针走两步，慢指针走一步。如果有环，两人必会在环内相遇（套圈）。

      ```python
      def hasCycle(self, head: Optional[ListNode]) -> bool:
          # 快慢指针都从头开始
          slow = fast = head
      
          # 只需要检查快指针能否继续走（慢指针一定在快指针后面，不需要检查）
          while fast and fast.next:
              slow = slow.next
              fast = fast.next.next
      
              # 追击相遇
              if slow == fast:
                  return True
          # 出循环说明指向None，无环
          return False
      ```
  
  - **142. 环形链表 II (Linked List Cycle II)** <a id="lc-142"></a>
  
    - **分析**：它是 141 题的**必然延伸**。面试中，面试官问完“有没有环”之后，99% 会紧接着问“环的入口在哪”。我们可以简单使用哈希表，也可以直接
  
    - **核心逻辑**：
      
      - **阶段一 (判断环)**：和 141 一样，快慢指针相遇，说明有环。
      
      - **阶段二 (找入口)**：这是一个纯数学推导结论。以下来自官方题解：
        
        - 设链表中环外部分的长度为 a。slow 指针进入环后，又走了 b 的距离与 fast 相遇。从相遇点到入环点的前向距离为c。此时，fast 指针已经走完了环的 n 圈，因此它走过的总距离为 `a+n(b+c)+b=a+(n+1)b+nc`；
        
        - 据题意，任意时刻，fast 指针走过的距离都为 slow 指针的 2 倍。因此，我们有:
        
          `a+(n+1)b+nc=2(a+b)⟹a=c+(n−1)(b+c)`
          有了 `a=c+(n−1)(b+c)` 的等量关系，我们会发现：从相遇点到入环点的距离(c)加上 n−1 圈的环长(b+c)，恰好等于从链表头部到入环点的距离。
        
        - 因此，当发现 slow 与 fast 相遇时，我们再额外使用一个指针 ptr。起始，它指向链表头部；随后，它和 slow 每次向后移动一个位置。最终，它们会在入环点相遇。 此时ptr走了a，slow又走了c + (n-1)圈。
      
      ```python
      # 加一个哈希表来记录
      def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
          visited = set()
          node = head
          while node:
              if node in visited:
                  return node
              else:
                  visited.add(node)
              node = node.next
          return None
      
      # 纯快慢指针数学推导法
      def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
          # 快慢指针都从头开始
          slow = fast = head
      
          while fast and fast.next:
              slow = slow.next
              fast = fast.next.next
      
              if slow == fast:
                  # 设置新指针，走a
                  ptr = head
                  while ptr != slow:
                      ptr = ptr.next
                      # slow走c + (n-1)圈
                      slow = slow.next
                  # 在环入口相遇
                  return ptr
      
          return None
      ```
      
      
  
  - **19. 删除链表的倒数第 N 个结点** </a><a id="lc-19"></a>
  
    - **分析**：经典面试题。如何只遍历一次找到倒数第 N 个？
    - **技巧**：**固定窗口**。让 `fast` 先走 `N` 步，然后 `fast` 和 `slow` 同时走。当 `fast` 走到尽头（None）时，`slow` 刚好站在倒数第 `N` 个节点的前一个位置（前提是有哨兵节点）。
    - **注意**：必须使用 **哨兵节点**，因为如果要删除的是头节点（倒数第 length 个），没有哨兵会很难处理。



### 体系三：合并逻辑 (Merging) 

- **包含题目**：
  - **21. 合并两个有序链表** (Hot 100) <a id="lc-21"></a>
    - **分析**：归并排序的最后一步。
    - **核心**：谁小移谁。
    - **哨兵**：使用 `dummy` 节点作为新链表的头，可以避免初始化 `head` 的繁琐判断。
    - **收尾**：循环结束后，如果还有一个链表没走完，直接把剩下的接在后面（`cur.next = l1 if l1 else l2`）。
