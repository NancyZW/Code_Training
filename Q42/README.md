# 面试题42：连续子数组的最大和

解题思路：动态规划，自底向上迭代求解，dp[i] = max(dp[i-1]+array[i],arrat[i])

注意事项：边界条件