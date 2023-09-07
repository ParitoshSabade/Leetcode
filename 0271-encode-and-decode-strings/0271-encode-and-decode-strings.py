class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded_str = ""
        
        for strng in strs:
            if strng == "":
                encoded_str+=" "
            for char in strng:
                
                encoded_str += str(ord(char)) + " "
                
                
            encoded_str+=","
        print(len(encoded_str) )
        print(encoded_str)
        return encoded_str
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        decoded = []
        if s == "":
            return [""]
        words = s.split(",")
        for word in words:
            word_str = ""
            if word != "":
                unicodes = word.split(" ")
                for unicode in unicodes:
                    if unicode != "":
                        word_str += chr(int(unicode))
                decoded.append(word_str)
                
        return decoded
                


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))