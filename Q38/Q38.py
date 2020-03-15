# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        if len(ss)<=1:
            return ss
        per = []
        for i in range(len(ss)):
            for j in self.Permutation(ss[:i]+ss[i+1:]):
                per.append(ss[i]+j)
        per = sorted(set(per))
        return per


if __name__ == "__main__":
    ss = 'aabc'
    sol = Solution()
    ans = sol.Permutation(ss)
    print(ans)