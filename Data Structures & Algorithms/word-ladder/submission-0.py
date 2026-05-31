class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        patterns = defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                patterns[pattern].append(word)

        q = deque([(beginWord, 1)])
        visited = {beginWord} # a set
        
        while q:
            print("queue:", q)
            word, length = q.popleft()
            print("popped:", word, length)

            if word == endWord:
                return length
            
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                print("patterns:", pattern, "nei", patterns[pattern])
                for nei in patterns[pattern]:
                    if nei not in visited:
                        print("add:", nei)
                        q.append((nei, length + 1))
                        visited.add(nei)
        return 0