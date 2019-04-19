# 从尾到头打印链表
# 遍历一遍反向输出就不说了
# 也可用递归实现
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def printListReversingly(head):

    def helper(head, res)
        if not head:
            return None
        help(head.next)
        res.append(head.val)

    res = []
    helper(head, res)
    return res