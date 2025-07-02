# LC 121

 - Initialize min_price with the first price.
 - Initialize max_profit as 0.
 - Traverse the list:
   - Update min_price if a lower price is found.
   - Calculate the profit if sold on the current day and update max_profit if it's the highest so far.
 - Return max_profit.

This is the most efficient solution for this problem.

Approach
 - Time Complexity: O(n)
 - Space Complexity: O(1)

# LC 88



Algorithm:
 - Initialize two pointers i (pointing to the end of valid elements in nums1) and j (pointing to the end of nums2).
 - Start filling nums1 from the back.
 - Compare the elements from nums1 and nums2 and place the larger element at the end of nums1.
 - If any elements remain in nums2, copy them over.
 - No extra space is used.
 - This is the most efficient in-place merge solution.

Approach
 - Time Complexity: O(m + n)
 - Space Complexity: O(1)



# LC 268

# Solution 1: Using Sum Formula

Algorithm:
 - Calculate the expected sum of numbers from 0 to n using the formula n * (n + 1) // 2.
 - Calculate the actual sum of the given array.
 - The missing number is the difference between the expected sum and the actual sum.
Time Complexity: O(n)
Space Complexity: O(1)


# Sorting Approach:
 - Sort the array.
 - After sorting, the element at index i should be equal to i if no number is missing.
 - Traverse the sorted array and find the first index where nums[i] != i.
 - If all elements are in place, then the missing number is n.

Time Complexity: O(n log n) – Because of the sorting step.
Space Complexity: O(1) – If in-place sort is allowed, otherwise O(n) if sorting uses extra space.


# LC 136
 - The XOR operation is used here because it has the property that a ^ a = 0 and 
 - a ^ 0 = a, which means that when we XOR all the numbers together.
 - This will cancel out all the numbers that appear twice, leaving only the single number.
 - This solution is efficient and meets the problem's requirements for linear runtime complexity and constant space usage.

# Example 
 - nums = [4, 1, 2, 1, 2]

4 = 100
1 = 001
2 = 010

Step 1: 0 ^ 100 = 100 (4)
Step 2: 100 ^ 001 = 101 (5)
Step 3: 101 ^ 010 = 111 (7)
Step 4: 111 ^ 001 = 110 (6)
Step 5: 110 ^ 010 = 100 (4)
 -  The answer is 4, the unique number.

Time Complexity: O(n), where n is the length of the input list nums.
Space Complexity: O(1), as we are using a constant amount of space for the variable result.

# LC 48>

# Approach
 - This Python solution rotates the matrix in-place using the following steps:
Transpose the Matrix
 - Swap matrix[i][j] with matrix[j][i] for all i < j. This reflects the matrix over its main diagonal.
Reverse Each Row
 - Reverse every row in the transposed matrix to achieve a 90-degree clockwise rotation.

# Time and Space Complexity
 - Time Complexity: O(n²) – Each element is visited once during the transpose and once during the row reversal.
 - Space Complexity: O(1) – The rotation is performed in-place with no extra space.