# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:
from random import random
class Solution:
    def guessNumber(self, n: int) -> int:
        num = random()
        val = 2*30
        flag = 0
        before_guess = 0
        while 1:
            if guess(num) ==0:
                return int(num)
            elif guess(num) == 1:
                num+=val
                if before_guess == -1:
                    val/=2
                before_guess = 1
            elif guess(num) == -1:
                num-=val
                if before_guess == 1:
                    val/=2
                before_guess = -1
