def bubbleSort(list):
    issorted = False
    while not issorted:
        issorted = True
        for i in range(len(list) - 1):
            if(list[i] > list[i+1]):
                list[i], list[i+1] = list[i+1], list[i]
                issorted = False


if __name__ == "__main__":
    list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    bubbleSort(list)
    print(list)
