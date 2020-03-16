# -*- coding:utf-8 -*-
import heapq
class Solution:
    def __init__(self):
        self.minheap = []
        self.maxheap = []
    def Insert(self, num):
        # write code here
        if len(self.minheap) <= len(self.maxheap):
            if len(self.maxheap) == 0:
                heapq.heappush(self.minheap, num)
            else:
                v = -heapq.heappop(self.maxheap)
                if num < v:
                    heapq.heappush(self.minheap, v)
                    heapq.heappush(self.maxheap, -num)
                else:
                    heapq.heappush(self.maxheap, -v)
                    heapq.heappush(self.minheap, num)
        else:
            if len(self.minheap) == 0:
                heapq.heappush(self.maxheap, -num)
            else:
                v = heapq.heappop(self.minheap)
                if num < v:
                    heapq.heappush(self.minheap, v)
                    heapq.heappush(self.maxheap, -num)
                else:
                    heapq.heappush(self.maxheap, -v)
                    heapq.heappush(self.minheap, num)
    def GetMedian(self):
        # write code here
        # print(self.minheap.pop(),self.maxheap.pop())
        if len(self.minheap) == 0 and len(self.maxheap) == 0:
            return 0
        elif len(self.minheap) == len(self.maxheap):
            return (heapq.nsmallest(1,self.minheap)[0]-heapq.nsmallest(1,self.maxheap)[0])*0.5
        elif len(self.minheap) > len(self.maxheap):
            return heapq.nsmallest(1,self.minheap)[0]
        else:
            return -heapq.nsmallest(1,self.maxheap)

if __name__ == "__main__":
    sol = Solution()
    sol.Insert(5)
    sol.Insert(2)
    # sol.Insert(3)
    # sol.Insert(4)
    # sol.Insert(1)
    # sol.Insert(6)
    # sol.Insert(7)
    # sol.Insert(0)
    # sol.Insert(8)

    ans = sol.GetMedian()
    print(ans)