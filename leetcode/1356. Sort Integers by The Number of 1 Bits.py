class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        newlist = []
        result = []
        for i in arr:
            newlist.append([i, bin(i).count('1')])
            print(str(bin(i)).count('1'))
        newlist.sort(key=lambda x: (x[1], x[0]))
        for i in newlist:
            result.append(i[0])
        return result
