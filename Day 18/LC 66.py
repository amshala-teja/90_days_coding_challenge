# 66. Plus One

# You are given a large integer represented as an integer array digits, 
# where each digits[i] is the ith digit of the integer. 
# The digits are ordered from most significant to least significant in left-to-right order. 
# The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

 

# Example 1:

# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].
# Example 2:

# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0 
        arr = []
        for digit in digits:
            num = (num * 10) + digit
        number  = num+1
        while number > 0:
            arr.append(number%10)
            number //= 10
        return arr[: : -1]
    
    # here the time and space complexity is O(n) where n is the number of digits in the input array.
# we can also do it in place with O(1) space complexity and O(n) time complexity
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # Traverse from the last digit backward
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                # No carry: just increment and return immediately
                digits[i] += 1
                return digits
            # digit was 9 → becomes 0, carry continues
            digits[i] = 0

        # If all digits were 9, we have an extra carry at the front
        return [1] + digits