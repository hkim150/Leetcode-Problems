class Solution:
    def toLowerCase(self, str: str) -> str:
        ret = ""
        for ch in str:
            ascii_val = ord(ch)
            # check if upper case a.k.a falls in ascii 65~90
            if 65 <= ascii_val <= 90:
                # add 32 to ascii and convert it back to char
                ret += chr(ascii_val + 32)
            else:
                ret += ch
        
        return ret