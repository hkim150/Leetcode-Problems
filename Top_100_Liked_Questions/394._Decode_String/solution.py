class Solution:
    def decodeString(self, s: str) -> str:
        def decode(s, rep):
            # find outer bracket, i.e closing bracket that pops the stack empty, and parse the number of repetitions and its inner string
            # call recursively with the args and swap the substring portion with the returned substring
            # continue until the end of the string and return the final string times repetition param
            stack = 0
            i = 0
            found = False
            par_start = num_start = num = 0
            while i < len(s):
                if found:
                    if s[i] == '[':
                        if par_start == 0:
                            par_start = i
                        if num == 0:
                            num = int(s[num_start:i])
                        stack += 1
                    elif s[i] == ']':
                        stack -= 1
                        if stack == 0:
                            sub_s = decode(s[par_start+1:i], num)
                            s = s[:num_start] + sub_s + s[i+1:]
                            i += len(sub_s) - (i - num_start + 1)
                            found = False
                            par_start = 0
                            num = 0
                else:
                    if s[i].isdigit():
                        found = True
                        num_start = i
                i += 1
                
            return s * rep
        
        return decode(s, 1)