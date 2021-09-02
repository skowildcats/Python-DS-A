def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
    dic = {}

    for word in s1.split(" "):
        dic[word] = dic.get(word, 0) + 1
    for word in s2.split(" "):
        dic[word] = dic.get(word, 0) + 1

    return [word for word in dic if dic[word] == 1]

# Time Complexity: O(n + m)
# Space COmplexity: O(1)

