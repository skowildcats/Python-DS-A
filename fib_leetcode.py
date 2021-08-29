

class Solution:

    def fib(self, n: int, tmp={}) -> int:
        if n in tmp:
            return tmp[n]

        if n == 0:
            retVal = 0
        elif n == 1 or n == 2:
            retVal = 1
        else:
            retVal = self.fib(n - 1, tmp) + self.fib(n - 2, tmp)

        tmp[n] = retVal
        return retVal
