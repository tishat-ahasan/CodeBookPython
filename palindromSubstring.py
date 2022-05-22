class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        for center in range(2*len(s)-1):
            left = int(center/2)
            right = int(left+ int(center)%2)
            # print(left, right)
            while left>=0 and right <len(s) and s[left]==s[right]:
                ans += 1
                left -= 1
                right += 1
        return ans
        
