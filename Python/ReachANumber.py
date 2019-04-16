# coding=utf-8
"""
754. Reach a Number
在一根无限长的数轴上，你站在0的位置。终点在target的位置。
每次你可以选择向左或向右移动。第 n 次移动（从 1 开始），可以走 n 步。
返回到达终点需要的最小移动次数。

首先这个问题肯定是有解的，我们已左右来代表轴的负和正
如果想到达1，那么就向右边走一步即可(即右1)。到2的话`右1左2右3`，
到3的话`右1左2右3左4右5`，所以一定是可以到达所有的坐标的，到负轴同理。

所以要想最少的步数到达，就一定要朝着一个方向移动，由于正坐标负坐标相同，所以我们
都把它们转换到正，即target=abs(target)
假设sum = 1+2+3+4+...+k
如果sum==target，那么k即为最终答案
如果sum>target，这时要分情况讨论
1.如果sum-target为偶数，上面式子可转化为sum = 1+...+ (sum-target)/2 +...+ k
两边同时减去sum-target，即sum-(sum-target) = 1+...- (sum-target)/2 +...+ k=target
也即是说在(sum-target)/2的地方向左走就可以在k步到达最终位置
2.如果sum-target为奇数，那么sum-target+1为偶数
所以sum-(sum-target+1) = 1 + ... - (sum-target+1)/2 + k = target-1
因为这是只走到target-1的位置，走到target位置按道理还需要两步还需要两步，
即向左走k+1步，再向右走k+2步。这时候需要k+2步，但是是不是还有最优解呢？

这时我们假设k为偶数，那么我们第k/2步的时候向左，
即1+... - (sum-target+1)/2 - k/2 +...+k = target-1 -k
这时再走k+1，即1+... - (sum-target+1)/2 - k/2 +..+k+ k+1 = target
所以这时k+1步就够了
如果k为奇数，1+2+...-(sum-target+1)/2 + k - (k+1) + k+2 = 
sum-(sum-target+1)+1 = target
所以这时候需要k+2步。

other:
1+2+3+4+... step>target 然后 zong-target 是偶数 那么之前某一步反转即可 
zong-target 是奇数 那完蛋了啊 之前的步子怎么反转总步数都只会减去一个偶数 
所以我们需要让 zong-target是偶数 那就多走几步嘛 那答案就是step+1 & step+2 
取决于这俩哪个是奇数
"""
class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        target = abs(target)
        k = 0
        sum = 0
        while target > sum:
            k += 1
            sum += k
        if (sum - target) % 2 == 0:
            return k
        if k % 2 == 0:
            return k + 1
        else:
            return k + 2
