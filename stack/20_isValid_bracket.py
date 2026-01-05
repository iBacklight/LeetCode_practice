"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足:

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
每个右括号都有一个对应的相同类型的左括号。
 

示例 1:

输入:s = "()"

输出:true

示例 2:

输入:s = "()[]{}"

输出:true

示例 3:

输入:s = "(]"

输出:false

示例 4:

输入:s = "([])"

输出:true

示例 5:

输入:s = "([)]"

输出:false

easy

"""
def isValid(s: str) -> bool:
    back2fore_sign = {")": "(", "}": "{", "]": "["}
    fore_signs = ["(", "{", "["]

    stack = []
    s = list(s)
    for sign in s:
        if sign in fore_signs:
            stack.append(sign)
        else:
            if len(stack) == 0:
                return False
            last_fore_sign = stack.pop()
            if back2fore_sign[sign] != last_fore_sign:
                return False
    if len(stack) == 0:
        return True
    
    return False

def isValid(self, s: str) -> bool:
    # stack
    if len(s) == 1:
        return False

    bracket_dict = {'(':')','{':'}','[':']'}
    stack = []

    for c in s:
        if c in bracket_dict:
            stack.append(c)
        elif c not in bracket_dict:
            if stack == []:
                return False
            
            if bracket_dict[stack.pop()] != c:
                return False
    
    if stack == []:
        return True
    else:
        return False 