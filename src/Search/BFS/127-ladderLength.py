class Solution(object):
    
    def differ_sum(self, A, B):
        sum = 0
        for i in range(len(A)):
            if A[i] != B[i]:
                sum += 1
        return sum == 1

    def graph(self, wordList):
        word_dict = {}
        for word in wordList:
            word_dict[word] = []
            for candidate in wordList:
                if self.differ_sum(word, candidate):
                    word_dict[word].append(candidate)
        return word_dict

    def ladderLength(self, beginWord, endWord, wordList):
        """
        这种做法超时，建图的时候太复杂，有更低时间复杂度的方法。
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        if beginWord not in wordList:
            wordList.append(beginWord)
        graph = self.graph(wordList)
        q = [beginWord]
        visited = {beginWord}
        ans = 1
        while q:
            ans += 1
            for _ in range(len(q)):
                word = q.pop(0)
                for neighbor in graph[word]:
                    if neighbor in visited:
                        continue
                    if neighbor == endWord:
                        return ans
                    visited.add(neighbor)
                    q.append(neighbor)
        return 0
