# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index == 0:
            return 0
        ugly = [1]
        T2 = 0
        T3 = 0
        T5 = 0
        x2 = 1
        x3 = 1
        x5 = 1
        while len(ugly) < index:
            curr_max = ugly[-1]
            # print(T2,len(ugly)-1)
            for i in range(T2,len(ugly)):
                # print(T2,i,ugly[i], curr_max)
                if ugly[i]*2 > curr_max:
                    T2 = i
                    x2 = ugly[i]*2
                    break
            for j in range(T3,len(ugly)):
                if ugly[j]*3 > curr_max:
                    T3 = j
                    x3 = ugly[j]*3
                    break
            for k in range(T5,len(ugly)):
                if ugly[k]*5 > curr_max:
                    T5 = k
                    x5 = ugly[k]*5
                    break
            # print(ugly)
            ugly.append(min(x2,x3,x5))
        return ugly[index-1]

if __name__ == "__main__":
    n = 10
    sol = Solution()
    ans = sol.GetUglyNumber_Solution(n)
    print(ans)



