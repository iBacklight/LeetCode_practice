# Leecode 经验总结

[TOC]

---

## 题目导航汇总

| 序号 | 题目序号 | 题目名称                                             | 难度   | 核心算法/数据结构     | 所属体系              |
| ---- | :------- | :--------------------------------------------------- | :----- | :-------------------- | :-------------------- |
| 1    | 283      | [移动 0](#lc-283)                                    | 🟢 简单 | 双指针 (同向)         | 线性扫描 / 滑动窗口   |
| 2    | 3        | [无重复字符的最长子串](#lc-3)                        | 🟡 中等 | 滑动窗口 (变长-最长)  | 线性扫描 / 滑动窗口   |
| 3    | 76       | [最小覆盖子串](#lc-76)                               | 🔴 困难 | 滑动窗口 (变长-最短)  | 线性扫描 / 滑动窗口   |
| 4    | 438      | [找到字符串中所有字母异位词](#lc-438)                | 🟡 中等 | 滑动窗口 (定长+计数)  | 线性扫描 / 滑动窗口   |
| 5    | 11       | [盛最多水的容器](#lc-11)                             | 🟡 中等 | 双指针 (左右对撞)     | 线性扫描 / 双向双指针 |
| 6    | 42       | [接雨水](#lc-42)                                     | 🔴 困难 | 双指针 / 单调栈       | 线性扫描 / 双向双指针 |
| 7    | 167      | [两数之和 II (有序版)](#lc-1-ordered)                | 🟡 中等 | 双指针 (左右对撞)     | 线性扫描 / 双向双指针 |
| 8    | 15       | [三数之和](#lc-15)                                   | 🟡 中等 | 排序 + 双指针         | 线性扫描 / 双向双指针 |
| 9    | 53       | [最大子数组和](#lc-53)                               | 🟡 中等 | Kadane (贪心/DP)      | 线性扫描 / Kadane     |
| 10   | 56       | [合并区间](#lc-56)                                   | 🟡 中等 | 排序 + 区间合并       | 线性扫描 / 区间合并   |
| 11   | 560      | [和为 K 的子数组](#lc-560)                           | 🟡 中等 | 前缀和 + 哈希表       | 空间权衡优化          |
| 12   | 1        | [两数之和](#lc-1)                                    | 🟢 简单 | 哈希表                | 空间权衡优化          |
| 13   | 20       | [有效的括号](#lc-20)                                 | 🟢 简单 | 基础栈                | 数据结构 / 基础栈     |
| 14   | 32       | [最长有效括号](#lc-32)                               | 🔴 困难 | 栈 (存索引)           | 数据结构 / 基础栈     |
| 15   | 739      | [每日温度](#lc-739)                                  | 🟡 中等 | 单调栈 (找下一个更大) | 数据结构 / 单调栈     |
| 16   | 84       | [柱状图中的最大矩形](#lc-84)                         | 🔴 困难 | 单调栈 (找左右边界)   | 数据结构 / 单调栈     |
| 17   | 85       | [最大矩形](#lc-85)                                   | 🔴 困难 | 单调栈 (降维)         | 数据结构 / 单调栈     |
| 18   | 239      | [滑动窗口最大值](#lc-239)                            | 🔴 困难 | 单调队列              | 数据结构 / 单调队列   |
| 19   | 33       | [搜索旋转排序数组](#lc-33)                           | 🟡 中等 | 二分查找（双坡）      | 下标二分              |
| 20   | 34       | [在排序数组中查找元素的第一个和最后一个位置](#lc-34) | 🟡 中等 | 二分查找              | 下标二分              |
| 21   | 153      | [寻找旋转排序数组中的最小值](#lc-153)                | 🟡 中等 | 二分查找（双坡）      | 下标二分              |
| 22   | 74       | [搜索二维矩阵](#lc-74)                               | 🟡 中等 | 二分查找              | 下标二分              |
| 23   | 875      | [爱吃香蕉的珂珂](#lc-875)                            | 🟡 中等 | 二分查找（转换）      | 值域二分              |
| 24   | 410      | [分割数组的最大值](#lc-410)                          | 🔴 困难 | 二分查找              | 值域二分              |
| 25   | 1004     | [最大连续1的个数 III](#lc-1004)                      | 🟡 中等 | 滑动窗口/二分查找     | 值域二分              |

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
      # 1
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



## 模块三：数据结构驱动的线性优化 (容器驱动)

这一部分的核心逻辑是：**利用特定数据结构的“存取规则”，自动过滤（剔除）掉那些对寻找最终答案无用的信息。**

| **需求**                           | **推荐工具** | **关键操作**                 |
| ---------------------------------- | ------------ | ---------------------------- |
| 处理**嵌套**逻辑（如括号、路径）   | **基础栈**   | 匹配即消除                   |
| 找**下一个/上一个**更大或更小      | **单调栈**   | 破坏单调性即弹出并记录答案   |
| 确定以某点为高度的**最大扩散区间** | **单调栈**   | 同时找左右第一个比它小的边界 |
| 维护**滑动窗口**内的最值           | **单调队列** | 弹出较小者 + 弹出过期者      |

------

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

- 核心逻辑：

  通过比较 nums[mid] 和 target 的大小，缩小 [left, right] 的下标范围。

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
      
      
    
  - *注：**1004. 最大连续1的个数 III*** <a id="lc-1004"></a>
    
    - **最优解是滑动窗口**。
    - **二分做法**：可以对“最长长度”进行二分。猜一个长度 `len`，检查数组中是否存在一个长度为 `len` 的子数组，其包含的 0 的个数不超过 `k`。复杂度 $O(N \log N)$，不如滑动窗口 $O(N)$。
