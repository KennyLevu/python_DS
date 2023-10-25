# Insertion sort is an intuitive sorting algorithm
# that sorts like the way we sort playing cards in our hands
# The array is split into a sorted and unsorted array, values from the unsorted array
# are placed in the correct position within the sorted array
# We sort two the first two elements in the beginning and then
# pick the 3rd element to find its proper position within the sorted array.
# Insertion sort will gradually sort the rest of the elements this way via "insertion"

# Time Complexity: O(N^2)
# Auxiliary Space: O(1)

def insertion_sort(unsorted_list):
    # start from the second element since the first element is considered sorted
    for i in range(1, len(unsorted_list)):
        # variable keeps track of previous element's index
        j = i-1
        # stores element to be inserted
        nxt_element = unsorted_list[i]

        # inserts current element among the previous elements
        # shift larger elements to the right until we find the correct position
        while (unsorted_list[j] > nxt_element) and (j >= 0):
            # shift larger element to the right
            unsorted_list[j + 1] = unsorted_list[j]
            # move one position to the left
            j=j-1
        # insert current element into correct position in the sorted part of the list
        unsorted_list[j + 1] = nxt_element
    return unsorted_list

