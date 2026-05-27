class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        if word == abbr:
            return True

        i = 0
        j = 0

        while i < len(word) and j < len(abbr):
            steps = ""
            if abbr[j].isnumeric():
                if int(abbr[j]) == 0:
                    return False
                else:
                    while j < len(abbr) and abbr[j].isnumeric():
                        
                        steps += abbr[j]
                        j += 1
                    
                    steps = int(steps)
                    i += steps

            else:
                if word[i] != abbr[j]:
                    return False
                
                i += 1
                j += 1
        return i == len(word) and j == len(abbr)