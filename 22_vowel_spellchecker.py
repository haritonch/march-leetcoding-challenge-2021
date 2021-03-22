class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        
        def devowel(word):
            return '#' + ''.join('*' if c in 'aeiou' else c for c in word.lower())
        
        def decapitalize(word):
            return '$' + word.lower()
        
        lookup = {}
        ans = []
        
        for word in wordlist:
            lookup.setdefault(word, word)
            lookup.setdefault(decapitalize(word), word)
            lookup.setdefault(devowel(word), word)
            
        for query in queries:
            if query in lookup:
                ans.append(lookup[query])
            elif decapitalize(query) in lookup:
                ans.append(lookup[decapitalize(query)])
            elif devowel(query) in lookup:
                ans.append(lookup[devowel(query)])
            else:
                ans.append('')
        return ans