def SumOfSquares(n):
    """
    sum of squares of 1st n natural numbers
   Formula:  n(n+1)(2n+1) / 6
    """
    ans = n * (n+1) * (2*n + 1)//6
    return ans
print(SumOfSquares(5))
