# Time complexity: O(n.log(n))
# Space complexity: O(1)
def USingShorting(list):
    list.sort()
    for i in range(len(list)-1):
        if list[i] == list[i+1]:
            print(list[i])


# Time complexity: O(n)
# Space complexity O(n)
def UsingSet(list):
    numbers = set()
    for i in range(len(list)):
        if list[i] in numbers:
            print(list[i])
        else:
            numbers.add(list[i])


# If we know the range of the elements, then this is the fastest way to find
# the duplicates.
# Time complexity: O(n)
# Space complexity: O(n)
def UsingHashtable(list, valurange):
    count = [0]*valurange
    for i in range(len(list)):
        if count[list[i]] == 1:
            print(list[i])
        else:
            count[list[i]] += 1


if __name__ == "__main__":
    list = [1, 4, 7, 2, 4, 7, 3, 8, 9]
    UsingHashtable(list, 12)
