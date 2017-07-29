def partition(list, low, high):
    i = (low - 1)  # index of smaller element
    pivot = list[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if list[j] <= pivot:

            # increment index of smaller element
            i = i + 1
            list[i], list[j] = list[j], list[i]

    list[i + 1], list[high] = list[high], list[i + 1]
    return (i + 1)


# The main function that implements QuickSort
# list[] --> listay to be sorted,
# low  --> Starting index,
# high  --> Ending index


# Function to do Quick sort
def quickSort(list, low, high):
    if low < high:

        # pi is partitioning index, list[p] is now
        # at right place
        pi = partition(list, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(list, low, pi - 1)
        quickSort(list, pi + 1, high)


if __name__ == "__main__":
    list = [10, 7, 8, 9, 1, 5]
    n = len(list)
    quickSort(list, 0, n - 1)
    print("Sorted list is:")
    print(list)
