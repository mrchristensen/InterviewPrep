# https://leetcode.com/problems/word-search-ii/

# DFS Approach:
# Times out (too slow)

# 1 hour

# Time Complexity: O(n^2)
# Space Complexity: O(n)

class Solution:
    def __init__(self):
        self.found_words = set()

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.n, self.m = len(board), len(board[0])
        self.board = board
        # print("board:", self.board)
        # Find all of the letters that start the words we're looking for
        first_letters = {}
        for word in words:
            if word[0] not in first_letters:
                first_letters[word[0]] = []
            first_letters[word[0]].append(word)
        # print("first_letters:", first_letters)

        for i in range(self.n):
            for j in range(self.m):
                letter = board[i][j][0]
                # If we're at the start of a word we're looking for
                if(letter in first_letters):
                    target_words = first_letters[letter]
                    # Check to see if any of the words we're looking is a single letter
                    for index in range(len(target_words)):
                        if(len(target_words[index]) == 1):
                            self.found_words.add(target_words[index])
                            first_letters[letter].pop(index)
                            break

                    self.dfs(i, j, 1, first_letters[letter], set())
                    # If we found all the words, stop
                    if(len(self.found_words) == len(words)):
                        return self.found_words

        return self.found_words


    def dfs(self, i, j, k, words, visited):
        # print("dfs at:", i, j, k, "words:", words)
        neighbors = [[1,0], [-1,0], [0,1], [0,-1]]
        new_visited = set(visited)
        new_visited.add((i, j))
        # print("visited:", visited)

        for delta in neighbors:
            # print("delta:", delta)
            new_i = i + delta[0]
            new_j = j + delta[1]
            # print("new_i/j:", new_i, new_j)

            # If we've visited it before, skip
            if((new_i, new_j) in visited):
                continue

            # If in bounds
            if(0 <= new_i < self.n and 0 <= new_j < self.m):
                # print("neighbor is in bounds:", new_i, new_j)
                new_words = []
                # For all the words we're looking for
                for word in words:
                    # If we found the next letter for the word
                    if(self.board[new_i][new_j] == word[k]):
                        # If we found the whole word
                        if(k == len(word) - 1):
                            self.found_words.add(word)
                            # print("we found wordL", word)
                        # If we have more letters to find
                        else:
                            new_words.append(word)
                            # print("needs more letters to be found for:", word)

                # If we are looking for more letters to finish the words
                if(len(new_words) > 0):
                    self.dfs(new_i, new_j, k+1, new_words, new_visited)
