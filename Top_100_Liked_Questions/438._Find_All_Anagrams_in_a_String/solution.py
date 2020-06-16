class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # sliding window method
        if not s or not p:
            return []
        
        len_p = len(p)
        if len_p > len(s):
            return []
        
        ord_a = ord('a')
        
        cnt_p = [0] * 26
        curr_cnt = [0] * 26
        
        for i in range(len_p):
            cnt_p[ord(p[i]) - ord_a] += 1
            curr_cnt[ord(s[i]) - ord_a] += 1
        
        ans = []
        if curr_cnt == cnt_p:
            ans.append(0)
            
        for i in range(len(s)-len_p):
            if s[i] != s[i+len_p]:
                curr_cnt[ord(s[i]) - ord_a] -= 1
                curr_cnt[ord(s[i+len_p]) - ord_a] += 1
            
            if curr_cnt == cnt_p:
                ans.append(i+1)
        
        return ans