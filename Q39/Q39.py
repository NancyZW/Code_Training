# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if len(numbers) == 0:
            return 0
        now = numbers[0]
        count = 0
        for i in numbers:
            if i == now:
                count += 1
            else:
                count -= 1
            if count == 0:
                now = i
                count = 1
        now_count = 0
        for i in numbers:
            if i == now:
                now_count += 1
        if 2*now_count > len(numbers):
            return now
        else:
            return 0

if __name__ == "__main__":
    numbers = [1,2,3,2,2,2,5,4,2]
    sol = Solution()
    ans = sol.MoreThanHalfNum_Solution(numbers)
    print(ans)