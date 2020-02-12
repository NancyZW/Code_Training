# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        odd = []
        even = []
        for i in array:
            if i&1 == 1:
                odd.append(i)
            else:
                even.append(i)
        return odd + even

    def reOrderArray2(self, array):
        if len(array) <= 1:
            return array

        for iter_left in range(len(array)-1):
            # print(array)
            if array[iter_left]&1 == 0:
                # print(array)
                iter_right = iter_left + 1
                while iter_right < len(array):
                    if array[iter_right]&1 == 1:
                        val = array[iter_right]
                        for i in range(iter_right, iter_left, -1):
                            array[i] = array[i - 1]
                        array[iter_left] = val
                        # print(array)
                        break
                    else:
                        iter_right += 1
        return array

if __name__ == "__main__":
    array = [1,2,3,4,5]
    sol = Solution()
    ans = sol.reOrderArray2(array)
    print(ans)