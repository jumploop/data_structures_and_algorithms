"""
394. 字符串解码


给定一个经过编码的字符串，返回它解码后的字符串。

编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。

你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

 

示例 1：

输入：s = "3[a]2[bc]"
输出："aaabcbc"

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/decode-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from ast import Num


class Solution:

    def decodeString(self, s: str) -> str:
        stack_str = ['']
        stack_num = []
        num = 0
        for c in s:
            if c >= '0' and c <= '9':
                num = 10 * num + int(c)
            elif c == '[':
                stack_num.append(num)
                stack_str.append('')
                num = 0
            elif c == ']':
                cur_str = stack_str.pop()
                stack_str[-1] += cur_str * stack_num.pop()
            else:
                stack_str[-1] += c
        return stack_str[0]


if __name__ == '__main__':
    solution = Solution()
    print(solution.decodeString("3[a]2[bc]"))
