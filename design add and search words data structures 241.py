class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
                
            cur = cur.children[c]
            
        cur.isWord = True


    def search(self, word: str) -> bool:
        appropriate_lst = [self.root]
        
        for c in word:
            new_app = []
            
            if c == '.':
                for node in appropriate_lst:
                    new_app.extend(node.children.values())
            else:
                for node in appropriate_lst:
                    if c in node.children:
                        new_app.append(node.children[c])
                
            if not new_app:
                return False

            appropriate_lst = new_app
            
        for node in appropriate_lst:
            if node.isWord:
                return True
        
        return False
