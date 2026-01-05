# 17—Letter Combinations of a Phone Number

本题属于backtrack算法， 回溯问题经常有排列，组合，子集的变种。本题属于组合。

## 解法一：回溯

下面把这题当作“回溯-组合”问题系统讲一遍

### 1) 抽象成回溯五要素

- **状态（State）**：当前正在处理到第几个数字 `i`，以及已经拼出来的部分字符串 `path`。
- **选择（Choices）**：对当前数字 `digits[i]`，可选的字母集合（如 `'2'→"abc"`）。
- **约束（Constraints）**：必须按数字顺序逐位选择；`1/0` 无字母，跳过或直接返回空。
- **目标（Goal）**：当 `i == len(digits)`，得到一个完整组合，把 `"".join(path)` 加入结果。
- **撤销（Unchoose）**：从 `path` 弹出刚压入的字符，恢复到上一步状态。

这也对应经典“三步”：**选择 → 递归 → 撤销**。

### 2) 代码结构如何体现回溯

```python
def backtrack(i: int, path: list[str]):
    if i == len(digits):            # 递归出口：组合长度达到目标
        res.append(''.join(path))
        return
    for ch in phone[digits[i]]:     # 遍历当前位的所有“选择”
        path.append(ch)             # ① 选择
        backtrack(i + 1, path)      # ② 递归到下一位
        path.pop()                  # ③ 撤销（回溯）
```

- `path.append(ch)` 与 `path.pop()` 就是“做—撤销”的成对操作。
- `i` 单调递增，确保按位向前，不会重复回到旧位；因此是**组合**而非**排列**。

### 3) 为什么属于“组合”而不是“排列/子集”

- **组合**：位置顺序是固定的（第 1 位来自第 1 个数字…），每一位只从各自的字母表里取一个——最终长度固定、位次固定，**不对位次做重排**。
- **排列**：会对同一批元素做**顺序重排**（本题没有）。
- **子集**：会允许“选或不选”，长度可变（本题长度固定为 `len(digits)`）。

### 4) 复杂度

- **时间**：每一位平均分支 ~3（7/9 为 4），深度 `n=len(digits)`
   ⇒ 约 `O(3^n)`（最坏 `O(4^n)`），每次输出时拼接字符串 `O(n)`，总体常写为 `O(3^n * n)`。
- **空间**：递归深度 `O(n)` + 路径 `O(n)`。

### 5）回溯的过程

假设输入是 `"23"`：

1. path第一添加的是数字“2”（第一层）的"a"， 然后进入backtrace函数递归，直接递归"3"（第二层）的“d”，此时path为["ad"]
2. 此时再次进入backtrace时，相当于进入了第三层（本例中相当于backtrack(2, path)）触发i == len(digits)，所以把当前的path赋给res, 然后return
3. return后回到了第二层的path.pop,此时会将最后输入的"d"移出path，此时path再次只剩下"a"，然后继续遍历第二层的第二个字符“e”
4. 以此类推，直到第二层全部遍历结束，该函数（backtrack(1, path)）退出，回到第一层的pop，结束后path为空
5. 然后继续遍历第一层的第二个字符“b”, 之后以此类推。

最终得到 `["ad","ae","af","bd","be","bf","cd","ce","cf"]`。

解法二：迭代BFS

```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num2c = {
            "2":"abc","3":"def","4":"ghi","5":"jkl",
            "6":"mno","7":"pqrs","8":"tuv","9":"wxyz"
        }
        if not digits or any(d not in num2c for d in digits):  # 防 0/1
            return []

        res = ['']  # 用空串作为“种子”
        for d in digits:
            res = [k + ch for k in res for ch in num2c[d]]
        return res
```

- 思想：每处理一位 `d`，把现有的每个前缀 `k` 与该位的每个字母 `ch` 拼接，得到新一层 `res`。
- 这就是“组合”枚举的层序展开。

**复杂度**：仍是 $O(3^n\cdot n)$（最坏含 7/9 时 $O(4^n\cdot n)$），空间 $O(3^n)$。和回溯同阶，但常数更优。