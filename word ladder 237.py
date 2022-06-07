from collections import deque
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        m = len(wordList[0])
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        wordList.add(beginWord)
        matrix = collections.defaultdict(list)
        for word in wordList:
            for i in range(m):
                s = word[:i] + '_' + word[i+1:]
                matrix[s].append(word)
                
        queue = [beginWord]
        mark = set()
        mark.add(beginWord)
        dist = 1
        while queue:
            next_queue = []
            while queue:
                word = queue.pop(0)
                for i in range(m):
                    s = word[:i] + '_' + word[i+1:]
                    for next_word in matrix[s]:
                        if next_word not in mark:
                            if next_word == endWord:
                                return dist + 1
                            mark.add(next_word)
                            next_queue.append(next_word)
            queue = next_queue
            dist += 1
        return 0
