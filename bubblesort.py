    # create a bubble_sort functiondef bubble_sort(arr):
    """
    Sort an array using the bubble sort algorithm.
    
    Args:
        arr (list): The list to be sorted
        
    Returns:
        list: The sorted list
    """
    n = len(arr)
    
    # Outer loop for number of passes
    for i in range(n):
        # Flag to optimize the algorithm - if no swaps occur, array is sorted
        swapped = False
        
        # Inner loop for comparing adjacent elements
        # Last i elements are already in place, so we don't need to check them
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                # Swap if they are in wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no swapping occurred in this pass, array is already sorted
        if not swapped:
            break
            
    return arr
# Test the function
numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = bubble_sort(numbers)
print(sorted_numbers)  # Output: [11, 12, 22, 25, 34, 64, 90]

# Test with another example
test = [5, 2, 8, 1, 9]
sorted_test = bubble_sort(test)
print(sorted_test)  # Output: [1, 2, 5, 8, 9]

     