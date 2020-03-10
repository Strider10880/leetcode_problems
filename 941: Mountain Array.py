'''
20: Mountain Array

Given an array A of integers, return true if and only if it is a valid mountain array.

Recall that A is a mountain array if and only if:

1. A.length >= 3
2. There exists some i with 0 < i < A.length - 1 such that:
    (i)  A[0] < A[1] < ... A[i-1] < A[i]
    (ii) A[i] > A[i+1] > ... > A[A.length - 1]

__________________________________________
|| 0 || 2 || 3 || 4 || 5 || 2 || 1 || 0 ||
------------------------------------------

Here, the array is strictly increasing from index 0 to 4, and strictly decreasing from index 4 to 7. Hence the array is a mountain array.

__________________________________________
|| 0 || 2 || 3 || 3 || 5 || 2 || 1 || 0 ||
------------------------------------------
Here, the array is increasing but not strictly from index 0 to 4. The value at index 2 and 3 are same i.e. 3. Hence the array is not a mountain array.

Example 1:

Input: [2,1]
Output: false

Example 2:

Input: [3,5,5]
Output: false

Example 3:

Input: [0,3,2,1]
Output: true
 
Note:

1. 0 <= A.length <= 10000
2. 0 <= A[i] <= 10000 

'''
class Solution:
    def validMountainArray(self, A) -> bool:
        i=0
        if len(A)<3:
            return False
        elif A.index(max(A))==0 or A.index(max(A))==len(A)-1:
            return False
        while i<len(A)-1:
            if A[i+1]==A[i]:
                return False
            elif A[i+1]<A[i]:
                i+=1
                break
            else:
                pass
            i+=1
        while i<len(A)-1:
            if A[i+1]>=A[i]:
                return False
            i+=1
        return True
                