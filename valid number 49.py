class Solution:
    def isNumber(self, s: str) -> bool:
        return re.match(f"^[-+]?(([0-9]+[.]?[0-9]*)|([.][0-9]+))([eE][-+]?[0-9]+)?$", s)
