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
    for i in range(1, len(unsorted_list)):
        j = i-1
        nxt_element = unsorted_list[i]
        while (unsorted_list[j] > nxt_element) and (j >= 0):
            unsorted_list[j + 1] = unsorted_list[j]
            j=j-1
        unsorted_list[j + 1] = nxt_element
    return unsorted_list

