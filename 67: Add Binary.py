'''
67: Add Binary

Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"

Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

Each string consists only of '0' or '1' characters.
1 <= a.length, b.length <= 10^4
Each string is either "0" or doesn't contain any leading zero.

'''

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a=a[::-1]
        b=b[::-1]
        z=zip_longest(a,b,fillvalue='0')
        c=0
        res=''
        for i,j in z:
            if int(i)+int(j)+c==0 :
                res+='0'
                c=0
            elif int(i)+int(j)+c==1 :
                res+='1'
                c=0
            elif int(i)+int(j)+c==2 :
                res+='0'
                c=1
            else:
                res+='1'
                c=1
        if c==1:
            res+='1'
        return res[::-1] #returns the sum of the both binary number