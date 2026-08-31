class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ''
        for string in strs:
            len_padded = f"{len(string):03d}"
            len_encode = len_padded.encode('ASCII').hex()
            value_encode = string.encode('ASCII').hex()
            encoded_str += len_encode + value_encode
        return encoded_str

    def decode(self, s: str) -> List[str]:
        result =[]
        len_str = 0
        i = 0 
        while i < len(s):
            len_hex =s[i:i+6]
            len_str = int(bytes.fromhex(len_hex).decode("ASCII"))
            value_start_idx = i + 6
            value_last_idx = value_start_idx + (len_str * 2 )
            value_hex = s[value_start_idx:value_last_idx]
            value_str = bytes.fromhex(value_hex).decode("ASCII")
            result.append(value_str)
            i = value_last_idx
        return result

            


