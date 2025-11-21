class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        '''
        Input: beginWord, endWord, and wordList
        Output: integer representing shortest transformation steps to reach end word    
        Goal:
            return shortest steps take to move from begin word to end word
            return 0 if you can;t reach end word

        constraints:
            move one step at a time with each word differs by one letter
            begin word may not be in wordList

        
        Questions:
            min size of word list? 1
            max size of word list? 5000
            min size of word? 1
            max size of word? 10
            can begin word == end word? no
            beginWord.length == endWord.length? yes
            does wordlist only contain letters? yes 
            lower case letters? yes

        beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
        hit => hot => dot => dog => cog
        

        hit => _it, h_t, hi_

        _it: hit
        h_t: hot
        hi_: hit


        [hit]
        for each unique word: pull all matching patterns and add to queue
        start from begin word. add to queue
        pop queue and find all neighbours from hashmap of patterns
        if popped_value == endword: return length of transformation
        maintain a visit set to visit each word once
        Uses BFS approach
        
        run time: o(len(wordList) * o(len(word))
        space:  o(len(wordList) * o(len(word))

        '''
        pattern_map = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "_" + word[i+1:] 
                pattern_map[pattern].append(word)

        queue = deque([beginWord])
        visit = set()
        length = 1

        while queue:
            for i in range(len(queue)):
                curr_word = queue.popleft() #curr word
                if curr_word == endWord:
                    return length

                if curr_word in visit:
                    continue

                visit.add(curr_word)

                for i in range(len(curr_word)):
                    pattern = curr_word[:i] + "_" + curr_word[i+1:] 
                    for matching_word in pattern_map[pattern]:
                        if matching_word not in visit:
                            queue.append(matching_word)
            
            length += 1

        return 0