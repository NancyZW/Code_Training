# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        n_str = str(n)
        len_n = len(n_str)
        num = 0
        for i in range(1,len_n+1):
            high = n // (10**i)
            low = n % (10**(i-1))
            if int(n_str[-i]) == 1:
                num += high * 10 ** (i-1) + low+1
            elif int(n_str[-i]) > 1:
                num += (high+1)*10**(i-1)
            else:
                num += high*10**(i-1)
        return num
if __name__ == "__main__":
    n = 13
    sol = Solution()
    ans = sol.NumberOf1Between1AndN_Solution(n)
    print(ans)



