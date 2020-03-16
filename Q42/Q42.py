# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if len(array) == 0:
            return 0
        dp = [array[0]]
        for i in range(1,len(array)):
            dp.append(max(dp[i-1]+array[i],array[i]))
        return max(dp)
if __name__ == "__main__":
    array = [2,8,1,5,9]
    sol = Solution()
    ans = sol.FindGreatestSumOfSubArray(array)
    print(ans)



