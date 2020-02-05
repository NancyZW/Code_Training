# 面试题9：用两个栈实现队列

解题思路：一个stack存数据，另一个stack作为临时中转在pop时使用

注意事项： （1）在class内要初始化两个stack。 （2）pop完成后要将原始数据恢复至stack1中。

看完解答后发现不需要pop完后恢复stack1数据，可以维持原状，push至stack1，pop从stack2，实现在pop2（）中。