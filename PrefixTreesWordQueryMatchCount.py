"""
Prefix Match Count

Problem Statement:
Given two arrays of strings, `names[]` and `queries[]`,
determine how many strings in `names[]` start with each string in `queries[]` as their prefix.

Note: A prefix must start from the beginning of a string.
For example, "cat" is not a prefix of "cat",
but a prefix of "caterpillar" or "cate".

Similarly, "steve" is a prefix of "stevens", but NOT a prefix of "steve".

Input:
1. An integer `n` (size of `names[]`) followed by `n` strings.
2. An integer `q` (size of `queries[]`) followed by `q` strings.

Output:
    # Test Case 1
    [
        "stevens", "danny", "steves", "dan", "john", 
        "johnny", "joe", "alex", "alexander", "steve"
    ]
    queries = ["steve", "alex", "joe", "john", "dan"]
    # Expected Output: [2, 1, 0, 1, 1]
    
    # Test Case 2
    [
        "apple", "apricot", "banana", "berry", 
        "cherry", "chocolate", "grape"
    ]
    queries = ["ap", "ch", "be", "gra"]
    # Expected Output: [2, 2, 1, 1]
"""

from collections import defaultdict, deque

class TrieNode:
    def __init__(self):
        self.kids = defaultdict(TrieNode)
        self.letter_count = 1
        self.word_end_count = 0

# Insert word into prefix tree
def insert(word, root):
    cur_node = root
    for letter in word:
        if letter not in cur_node.kids:
            cur_node.kids[letter] = TrieNode()
        else:
            cur_node.kids[letter].letter_count += 1
        cur_node = cur_node.kids[letter]
    cur_node.word_end_count += 1

# Insert the word inside prefix tree
def search(word, root):
    cur_node = root
    for letter in word:
        if letter not in cur_node.kids:
            return 0
        cur_node = cur_node.kids[letter]

    if len(cur_node.kids) > 0:
        return cur_node.letter_count - cur_node.word_end_count

    return 0

def print_trie_bfs(root_node):
    nodes_queue = deque([(root_node, '*')])
    while nodes_queue:
        level = []
        for level_size in range(len(nodes_queue)):
            (cur_node, cur_letter) = nodes_queue.popleft()
            level.append((cur_letter, cur_node.letter_count))

            for kid_letter, next_node in cur_node.kids.items():
                nodes_queue.append((next_node, kid_letter))

        for (letter, count) in level:
            print(letter + str(count), end=" ")
        print()
        level.clear()

def print_trie_dfs(cur_node):
    if len(cur_node.kids) == 0:
        print("#", end="\n\n")
        return

    for next_letter, next_node in cur_node.kids.items():
        print(next_letter + str(next_node.letter_count), end=" ")
        print_trie_dfs(next_node)

def find_all_prefixes(names, queries):
    root = TrieNode()

    for name in names:
        # print("name: ", name)
        insert(name, root)

    # print_trie_bfs(root)
    # print_trie_dfs(root)

    answers = []
    for query in queries:
        count = search(query, root)
        # print("query: ", query, count)
        answers.append(count)

    return answers

if __name__ == "__main__":
    # Test Case 1: Orijinal Test Case
    names1 = [
        "stevens", "danny", "steves", "dan", "john", 
        "johnny", "joe", "alex", "alexander", "steve"
    ]
    queries1 = ["steve", "alex", "joe", "john", "dan"]
    print("Test Case 1 Output:", find_all_prefixes(names1, queries1))
    # Expected Output: [2, 1, 0, 1, 1]

    # Test Case 2: Empty Names Array
    names2 = []
    queries2 = ["steve", "alex", "joe", "john", "dan"]
    print("Test Case 2 Output:", find_all_prefixes(names2, queries2))
    # Expected Output: [0, 0, 0, 0, 0]

    # Test Case 3: Empty Queries Array
    names3 = [
        "apple", "apricot", "banana", "berry", 
        "cherry", "chocolate", "grape"
    ]
    queries3 = []
    print("Test Case 3 Output:", find_all_prefixes(names3, queries3))
    # Expected Output: []

    # Test Case 4: Single Character Prefixes
    names4 = ["ant", "anchor", "banana", "berry", "apple", "axe"]
    queries4 = ["a", "b", "c"]
    print("Test Case 4 Output:", find_all_prefixes(names4, queries4))
    # Expected Output: [4, 2, 0]

    # Test Case 5: Multiple Matches for Single Query
    names5 = ["cat", "caterpillar", "catalog", "dog", "dot"]
    queries5 = ["cat", "do"]
    print("Test Case 5 Output:", find_all_prefixes(names5, queries5))
    # Expected Output: [2, 2]

    # Test Case 6: Exact Matches Only
    names6 = ["exact", "exactly", "excavate", "example"]
    queries6 = ["exact"]
    print("Test Case 6 Output:", find_all_prefixes(names6, queries6))
    # Expected Output: [1]
