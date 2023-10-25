# BubbleSort is a comparison based sorting algorithm that swaps adjacent elements
# Time Complexity: O(N^2)
# Auxiliary Space: O(1)
def bubblesort(list):
    # python for loop iterates from the end of the list and decrements
    # with each pass
    for iter_num in range(len(list) - 1, 0, -1):
        # loop iterates through the range of the list from the current
        # iteration index to the end of the list
        for idx in range(iter_num):
            # makes comparison to order the list from least to greatest
            if list[idx]>list[idx+1]:
                # swaps the elements, the largest element "bubbles up" to the end of the list
                temp = list[idx]
                list[idx] = list[idx+1]
                list[idx+1] = temp
    return list