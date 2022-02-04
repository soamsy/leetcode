import random
class Codec:
    
    chars = "abcdefghijklmnopqrstuvwxyz0123456789"
    
    def __init__(self):
        self.urlToCode = {}
        self.codeToUrl = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        
        if longUrl in self.urlToCode:
            return self.urlToCode[longUrl]
        
        choice = None
        while not choice or choice in self.codeToUrl:
            choice = ''.join(random.choices(self.chars, k=7))
            
        self.urlToCode[longUrl] = choice
        self.codeToUrl[choice] = longUrl
        
        shortUrl = 'https://ti.ny/' + choice
        return shortUrl
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.codeToUrl.get(shortUrl[-7:], "Error. URL doesn't exist :(")