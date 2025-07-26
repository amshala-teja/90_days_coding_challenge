# 3622. Check Divisibility by Digit Sum and Product

# You are given a positive integer n. Determine whether n is divisible by the sum of the 
# following two values:

# The digit sum of n (the sum of its digits).

# The digit product of n (the product of its digits).

# Return true if n is divisible by this sum; otherwise, return false.

 

# Example 1:

# Input: n = 99

# Output: true

# Explanation:

# Since 99 is divisible by the sum (9 + 9 = 18) plus product (9 * 9 = 81) of its digits 
# (total 99), the output is true.

class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        digit_sum = 0
        digit_product = 1
        temp = n
        while temp > 0:
            digit = temp%10
            digit_sum += digit
            digit_product *= digit
            temp //= 10
        total = digit_sum + digit_product
        return n % total == 0