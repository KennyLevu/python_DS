# Merge sort is a divide and conquer sorting algoirthm
# It divides an array into subarrays, sorts them, and merges them back together into a sorted array
# Time Complexity: O(N log(N))
# Merge sort is recursive and can be expressed
# by the relation: T(n) = 2T(n/2) + theta(n)
# Auxiliary Space: O(N)
# elements are copied into an auxiliary array
def merge_sort(unsorted_list):
    # Base Case: If the list has 1 or 0 elements, it is sorted
    if len(unsorted_list) <= 1:
        return unsorted_list
    # Find the middle point to divide the list in 2 halves
    middle = len(unsorted_list) // 2

    # Split the list into two halves
    left_list = unsorted_list[:middle]
    right_list = unsorted_list[middle:]

    # Recursively sort the two halves
    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)

    # Merge sorted halves
    return list(merge(left_list, right_list))


# Merge Sorted halves
def merge(left_half, right_half):
    res = []

    # while both left and right halves have elements
    while len(left_half) != 0 and len(right_half) != 0:

        # compare first elements of both list and append the smaller to the result
        # remove the appended element from the respective half
        if left_half[0] < right_half[0]:
            res.append(left_half[0])
            left_half.remove(left_half[0])
        else:
            res.append(right_half[0])
            right_half.remove(right_half[0])
    # append any elements left in either list
    if len(left_half) == 0:
        res = res + right_half
    else:
        res = res + left_half
    return res
