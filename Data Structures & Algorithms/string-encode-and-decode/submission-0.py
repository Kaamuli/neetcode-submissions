class Solution:
    
    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for string in strs:
            encoded_str += string + '£'
        return encoded_str

    def decode(self, s: str) -> List[str]:
        list_of_strs = []
        word = ''
        for char in s:
            if char == '£':
                list_of_strs.append(word)
                word = ''
            else:
                word += char
        return list_of_strs


