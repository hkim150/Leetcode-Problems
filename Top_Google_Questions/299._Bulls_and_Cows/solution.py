class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # get bulls
        d1 = {}
        d2 = {}
        bulls = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                d1[secret[i]] = d1.get(secret[i], 0) + 1
                d2[guess[i]] = d2.get(guess[i], 0) + 1
        
        # get cows
        cows = 0
        for k, v in d1.items():
            if k in d2:
                cows += min(v, d2[k])
        
        return str(bulls) + 'A' + str(cows) + 'B'