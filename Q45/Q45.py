# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if len(numbers) == 0:
            return ''
        sorted_number = self.quicksort(numbers,0,len(numbers)-1)
        # return numbers
        str_num = map(str,sorted_number)
        ans = ''
        for i in str_num:
            ans += i
        return ans
    def quicksort(self,number,l,r):
        if l >= r:
            return number
        pivot = self.partition(number,l,r)
        self.quicksort(number,l,pivot-1)
        self.quicksort(number,pivot + 1,r)
        return number

    def partition(self,number,l,r):
        low = l
        high = r
        pivot = number[l]
        while low < high:
            # print(pivot,number[high],self.cmp(pivot,number[high]))
            while low < high and self.cmp(pivot,number[high]):
                high -= 1
            # print(pivot, number[low], self.cmp(number[low],pivot))
            while low < high and self.cmp(number[low],pivot):
                low += 1
            tmp = number[high]
            number[high] = number[low]
            number[low] = tmp
        number[l] = number[low]
        number[low] = pivot
        return low
    def cmp(self,a,b):
        a = str(a)
        b = str(b)
        if int(a+b) <= int(b+a):
            return True
        else:
            return False
if __name__ == "__main__":
    n = [1,2,4,3]
    sol = Solution()
    ans = sol.PrintMinNumber(n)
    print(ans)



