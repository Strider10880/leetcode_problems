'''

1371: Find the Longest Substring Containing Vowels in Even Counts

Given the string s, return the size of the longest substring containing each vowel an even number of times. That is, 'a', 'e', 'i', 'o', and 'u' must appear an even number of times.


Example 1:

Input: s = "eleetminicoworoep"
Output: 13
Explanation: The longest substring is "leetminicowor" which contains two each of the vowels: e, i and o and zero of the vowels: a and u.

Example 2:

Input: s = "leetcodeisgreat"
Output: 5
Explanation: The longest substring is "leetc" which contains two e's.

Example 3:

Input: s = "bcbcbc"
Output: 6
Explanation: In this case, the given string "bcbcbc" is the longest because all vowels: a, e, i, o and u appear zero times.
 

Constraints:

1 <= s.length <= 5 x 10^5
s contains only lowercase English letters.

'''

#SPOILER ALERT! SOLUTION BELOW

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        ref=''
        for i in s:
            if i=='a':
                ref+='1'
            elif i=='e':
                ref+='2'
            elif i=='i':
                ref+='3'            
            elif i=='o':
                ref+='4'            
            elif i=='u':
                ref+='5'
            else:
                ref+='0'
        if ref.count('0')==len(ref):
            return len(ref)
        k=len(s)
        n=k
        r=['1','2','3','4','5']
        while k:
            for i in range(n-k+1):
                flag=1
                for j in r:
                    if ref[i:i+k].count(j)%2!=0:
                        flag=0
                        break
                if flag:
                    return k
            k-=1
        return k