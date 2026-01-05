'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. 
Return the answer in any order. A mapping of digits to letters (just like on the telephone buttons) is given below. 
Note that 1 does not map to any letters.

本题属于backtrack算法, 


'''
def letterCombinations(digits: str):
    if not digits:
        return []
    # 使用哈希表存储每个数字对应的所有可能的字母
    phone = {
        '2': 'abc', '3': 'def',
        '4': 'ghi', '5': 'jkl', '6': 'mno',
        '7': 'pqrs','8': 'tuv','9': 'wxyz'
    }

    res = []

    def backtrack(i: int, path: list[str]):
        if i == len(digits):                 # 递归出口：数字用完了
            res.append(''.join(path))
            return
        for ch in phone[digits[i]]:          # 遍历当前数字对应的所有字母
            path.append(ch)                  # ① 选择
            backtrack(i + 1, path)           # ② 递归
            path.pop()                       # ③ 撤销选择（回溯）

    backtrack(0, [])
    return res

# Examples
print(letterCombinations("23"))   # ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
print(letterCombinations(""))     # []
print(letterCombinations("7"))    # ['p', 'q', 'r', 's']
