def insertionSort(list):
    for index in range(1, len(list)):
        currentvalue = list[index]
        position = index

        while position > 0 and list[position - 1] > currentvalue:
            list[position] = list[position - 1]
            position = position - 1

        list[position] = currentvalue


if __name__ == "__main__":
    list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    insertionSort(list)
    print(list)
