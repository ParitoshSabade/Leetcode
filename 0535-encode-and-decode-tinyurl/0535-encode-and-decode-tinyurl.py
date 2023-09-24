import json
class Codec:

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        lmap = {}
    
        for ind,letter in enumerate(longUrl):
            if letter in lmap:
                lmap[letter].append(ind)
            else:
                lmap[letter] = [ind]
                
                
            
       
        str_dict = json.dumps(lmap)
        str_dict += str(len(longUrl))
        
        return str_dict
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        
        str_l = int(shortUrl.split('}')[1])
        
        shortUrl = shortUrl[:len(shortUrl)-len(str(str_l))]
        lmap = json.loads(shortUrl)
        long_arr =[""]*str_l
        
        for key in lmap.keys():
            for i in lmap[key]:
                long_arr[i] = key
        
        long_url = "".join(long_arr)
        return long_url
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))