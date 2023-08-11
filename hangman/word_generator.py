import requests

class WordGenerator:
    def __init__(self) -> None:
        self.url = 'https://www.mit.edu/~ecprice/wordlist.10000'
        
    def get_words(self):
        try:
            response = requests.get(self.url)
            byte_list = response.content.splitlines()
            return [byte_str.decode() for byte_str in byte_list]
        except:
            return ['zipper', 'airplane', 'car', 'radio', 'castle', 'frequent']
        
        
    def get_words_with_cache(self):
        try:
            f = open('my_words.txt', 'r')
            content = f.read()
            if not content:
                raise RuntimeError
            byte_list = content.splitlines()
            return [byte_str for byte_str in byte_list]
            
        except:
            
            f = open('my_words.txt', 'w')
            response = requests.get(self.url)
            content = response.content
            f.write(content.decode())
            byte_list = content.splitlines()
            return [byte_str.decode() for byte_str in byte_list]
        finally:
            f.close()
            

            
        
    
    