# 面试题11：旋转数组的最小数字

错误尝试：第一反应是二分递归，写着写着发现并不能排除任何部分，这时间复杂度岂不是跟遍历一样？

解题思路：利用排好序的特征，将中间元素值和第一个元素与最后一个元素比较。由此排除一半元素。

注意事项： （1）二分终止条件不是idx_1==idx_2, 而是idx_1==idx_2-1 （2）当中间元素值和第一个元素与最后一个元素值都相等时，不能排除任何一部分，必须遍历数组！！！