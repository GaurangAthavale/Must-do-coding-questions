class Solution:
    def longestValidParentheses(self, s: str) -> int:
        s1 = [-1]
        # print(s)
        ans = 0
        for i in range(len(s)):
            if(s[i] == '('):
                s1.append(i)
            elif(s[i] == ')'):
                s1.pop()
                if(len(s1)==0):
                    s1.append(i)
                else:
                    ans = max(i-s1[-1],ans)
        return ans
        