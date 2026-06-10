"""
394. 字符串解码
给定一个经过编码的字符串，返回它解码后的字符串。

编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。

你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

示例 1：

输入：s = "3[a]2[bc]"
输出："aaabcbc"

示例 2：

输入：s = "3[a2[c]]"
输出："accaccacc"

示例 3：

输入：s = "2[abc]3[cd]ef"
输出："abcabccdcdcdef"

medium
"""
def decodeString(s: str) -> str:
    stack = []
    res= ''
    multi= 0
    
    for i, cha in enumerate(s):
        if '0' <= cha <= '9':
            multi = multi*10 + int(cha) # multiple for incoming string

        if cha == '[':
            # append current multi and res string
            # note the muti is used when ] ouccers
            stack.append((multi, res))
            # and now they should be reset for recording the substring inside current []
            multi = 0
            res = ''

        if 'a' <= cha <= 'z':
            res += cha

        if cha == ']':
            # res now record all cha since last [
            # multi is for current recorded res
            # And the multipled recorded res should be appended to prev_res
            cur_multi, prev_res = stack.pop()
            res = prev_res + cur_multi * res

    return res 