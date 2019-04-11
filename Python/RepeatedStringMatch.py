# 686. Repeated String Match
# Given two strings A and B, 
# find the minimum number of times A has to be repeated such that B is a substring of it.
# If no such solution, return -1.
# For example, with A = "abcd" and B = "cdabcdab".
# Return 3, because by repeating A three times (“abcdabcdabcd”), 
# B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").
# Note:
# The length of A and B will be between 1 and 10000.
# 大致题意是A重复几次后，可以使B成为其字串。
# 想要B是A的字串，A的长度必须要大于B，因此可以循环A直到A长度大于B，这是如果B不是A的字串
# 最后在进行一次，如果B不是，那就不是，是就是了。
class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        if not set(B).issubset(set(A)):
            return -1
        times = 1
        resA = A
        while len(resA) < len(B):
            resA += A
            times += 1
        if B in resA:
            return times
        resA += A
        times += 1
        print resA
        if B in resA:
            return times
        return -1
    def repeatedStringMatch1(self, A, B):
        if set(A) < set(B):
            return -1
        times = len(B) / len(A)
        if times * len(A) < len(B):
            times += 1
        if B in A * times:
            return times
        if B in A * (times + 1):
            return times + 1
        return -1

# For example, with A = "abcd" and B = "cdabcdab".
# A = "abc" B = "cabcabca"
# A = "aaaaaaaaaaaaaaaaaaaaaab" B = "ba"
print Solution().repeatedStringMatch1("aaaaaaaaaaaaaaaaaaaaaab", "ba")