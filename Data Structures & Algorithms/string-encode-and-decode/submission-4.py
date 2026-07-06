class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ''
        
        for string in strs:
            char_count = len(string)
            encoded_str += str(char_count) + '£' + string
        return encoded_str

    def decode(self, s: str) -> List[str]:
        list_of_strs = [] #Output, the list of strings
        i = 0 #Pointer to the current poisition in encoded string
        word = '' #Empty will build out words here
        current_char_count = '' #Will store the number preceeding text

        while i < len(s):

            if s[i].isdigit() and s[i+1] != '£':
                current_char_count += s[i]
                i += 1
            elif s[i].isdigit() and s[i+1] == '£':
                current_char_count += s[i]
                char_count = int(current_char_count) #Stores char count as a number not string
                i += 1
            elif s[i] == '£':
                i += 1
                word = s[i:i+char_count]
                
                list_of_strs.append(word)

                word = ''
                current_char_count = ''
                i += char_count
        return list_of_strs
        
