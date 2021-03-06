class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        s = set(words)
        for word in words:
            if word in s:
                for i in range(1,len(word)):
                    s.discard(word[i:])
        return len("#".join(list(s))) + 1
