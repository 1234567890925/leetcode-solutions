1# The guess API is already defined for you.
2# @param num, your guess
3# @return -1 if num is higher than the picked number
4#          1 if num is lower than the picked number
5#          otherwise return 0
6# def guess(num: int) -> int:
7
8class Solution:
9    def guessNumber(self, n: int) -> int:
10        l, r = 1, n
11
12        while l < r:
13            mid = (l + r) // 2
14            guessed = guess(mid)
15
16            #(following consider the returned reply from the guess API)
17            if guessed == 0:
18                return mid
19            elif guessed == 1:
20                l = mid + 1
21            elif guessed == -1:
22                r = mid - 1
23        return l
24
25