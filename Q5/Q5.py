# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        ans = ''

        for i in s:
            if i == ' ':
                ans = ans + '%20'
            else:
                ans = ans + i

        return ans

s = 'We Are Happy'
ans = Solution().replaceSpace(s)
print(ans)
