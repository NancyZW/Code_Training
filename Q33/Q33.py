# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if len(sequence) == 0:
            return False
        if len(sequence) <= 2:
            print(sequence)
            return True
        root = sequence.pop()
        leftseq = []
        rightseq = []
        flag = 0
        for i in sequence:
            if i<root and len(rightseq) == 0:
                leftseq.append(i)
            elif i>root:
                rightseq.append(i)
            else:
                return False
        if len(leftseq) > 2 and len(rightseq) >2:
            return self.VerifySquenceOfBST(leftseq) and self.VerifySquenceOfBST(rightseq)
        elif len(leftseq) > 2:
            return self.VerifySquenceOfBST(leftseq)
        elif len(rightseq) >2:
            return self.VerifySquenceOfBST(rightseq)
        else:
            return True


if __name__ == "__main__":
    sequence = [1,2,3,4,5]
    sol = Solution()
    ans = sol.VerifySquenceOfBST(sequence)
    print(ans)