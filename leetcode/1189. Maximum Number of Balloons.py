class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        value = {'b': 1, 'a': 1, 'l': 2, 'o': 2, 'n': 1}
        store = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}
        for letter in text:
            if letter in value:
                store[letter] += 1
        return min(store['b']//value['b'], store['a']//value['a'], store['l']//value['l'], store['o']//value['o'], store['n']//value['n'])
