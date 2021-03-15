from random import choice

class Codec:
    def __init__(self):
        self.map = dict()
        self.inverse = dict()
        
    def generate_random_string(self):
        characters = list('1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')
        return ''.join(choice(characters) for _ in range(6))
    
    def encode(self, longUrl: str) -> str:
        shortUrl = self.generate_random_string()
        while shortUrl in self.map:
            shortUrl = generate_random_string()
        self.map[longUrl] = shortUrl
        self.inverse[shortUrl] = longUrl
        return shortUrl

    def decode(self, shortUrl: str) -> str:
        return self.inverse[shortUrl]