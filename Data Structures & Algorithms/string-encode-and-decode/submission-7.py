class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in range(len(strs)):
            s += strs[i]
            s += "\n"
        return s

        

        
    def decode(self, s: str) -> List[str]:
        back = ""
        out = []
        for i in range(len(s)):
            if s[i] == "\n":
                out.append(back)
                back = ""
            else:
                back += s[i]

        return out