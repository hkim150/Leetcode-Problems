class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last_idx = [0] * 26
        ans = []

        for i,ch in enumerate(S):
            last_idx[ord(ch) - ord('a')] = i

        i = 0
        while i < len(S):
            j = i
            part = last_idx[ord(S[j]) - ord('a')]
            while j < part:
                part = max(part, last_idx[ord(S[j]) - ord('a')])
                j += 1

            ans.append(j - i + 1)
            i = j + 1

        return ans
            