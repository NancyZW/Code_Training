# 面试题41：数据流中的中位数

解题思路：用两个heap存储，maxheap存储小的一半，minheap存储大的一半

注意事项：每次存储时将数值存到较小的heap中，同时比较heaptop判断是否需要交换top值 heapq实现maxheap可将值取负存储