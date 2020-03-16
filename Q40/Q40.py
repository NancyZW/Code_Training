# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        def partition(tinput,left,right):
            pivot = tinput[left]
            l = left
            while left < right:
                while left < right and tinput[right] >= pivot:
                    right -= 1
                while left < right and tinput[left] <= pivot:
                    left += 1
                tinput[l] = tinput[right]
                tinput[right] = tinput[left]
                tinput[left] = tinput[l]
            tinput[l] = tinput[left]
            tinput[left] = pivot
            return left

        if k > len(tinput):
            return []
        idx = -1
        left = 0
        right = len(tinput)-1
        while idx != k-1:
            idx = partition(tinput,left,right)
            if idx < k-1:
                left = idx+1
            elif idx > k-1:
                right = idx-1
        return sorted(tinput[:k])

if __name__ == "__main__":
    tinput = [4, 5, 1, 6, 2, 7, 3, 8]
    sol = Solution()
    ans = sol.GetLeastNumbers_Solution(tinput,9)
    print(ans)