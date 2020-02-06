# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        minN = 0
        ArrayLen = len(rotateArray)
        if ArrayLen == 0:
            return minN
        idx_1 = 0
        idx_2 = ArrayLen-1
        v1 = rotateArray[0]
        v2 = rotateArray[-1]
        while True:
            # print(idx_1,idx_2)
            if idx_1==idx_2-1:
                minN = min(rotateArray[idx_1],rotateArray[idx_2])
                break
            MidIndex = int((idx_1+idx_2) / 2)
            # print(MidIndex)
            minN = rotateArray[MidIndex]
            if minN == rotateArray[idx_1] and minN == rotateArray[idx_2]:
                for i in range(idx_1,idx_2):
                    minN = min(minN, rotateArray[i])
                return minN
            elif minN >= rotateArray[idx_1]:
                idx_1 = MidIndex
            else:
                idx_2 = MidIndex
        return minN
rotateArray = [1,1,1,0,1]
ans = Solution().minNumberInRotateArray(rotateArray)
print(ans)
