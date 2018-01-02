class Solution:
    # @param {integer} n
    # @return {integer}
    def climbStairs(self, n):
        def fact(n):
            result=1
            for i in range(1,n+1):
                result*=i
            return result
        total=0
        for i in range(n/2+1):
            total+=fact(i+n-2*i)/fact(i)/fact(n-2*i)
        return total
