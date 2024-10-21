class Solution:
    def detectCapitalUse(self, word: str) -> bool: 
        if word.upper() == word or word.lower() == word or word == (word[0].upper() + word[1:].lower()):
            return True
        else:
            return False