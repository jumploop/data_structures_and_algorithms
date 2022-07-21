#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
567. 字符串的排列

给你两个字符串 s1 和 s2 ，写一个函数来判断 s2 是否包含 s1 的排列。如果是，返回 true ；否则，返回 false 。

换句话说，s1 的排列之一是 s2 的 子串 。

 

示例 1：

输入：s1 = "ab" s2 = "eidbaooo"
输出：true
解释：s2 包含 s1 的排列之一 ("ba").
示例 2：

输入：s1= "ab" s2 = "eidboaoo"
输出：false
 

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/permutation-in-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = {c: 0 for c in s1}
        need = defaultdict(int)
        for c in s1:
            need[c] += 1
        left = right = vaild = 0
        while right < len(s2):
            # c 是将移入窗口的字符
            c = s2[right]
            # 扩大窗口
            right += 1
            # 进行窗口内数据的一系列更新
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    vaild += 1
            # 判断左侧窗口是否要收缩
            while (right - left) >= len(s1):
                # 在这里判断是否找到了合法的子串
                if vaild == len(need):
                    return True
                # d 是将移出窗口的字符
                d = s2[left]
                # 缩小窗口
                left += 1
                # 进行窗口内数据的一系列更新
                if d in need:
                    if window[d] == need[d]:
                        vaild -= 1
                    window[d] -= 1
        # 未找到符合条件的子串
        return False
