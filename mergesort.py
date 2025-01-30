    # create a merge_sort function
import random
     def merge_sort(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        return merge(left, right)

    # create a merge function
    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    # create a binary_search function
    def binary_search(arr, target):
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    # create a main function
    def main():
        arr = [int(x) for x in input("Enter the elements of the array separated by spaces: ").split()]
        sorted_arr = merge_sort(arr)
        print("Sorted array:", sorted_arr)
        target = int(input("Enter the element to search for: "))
        index = binary_search(sorted_arr, target)
        if index != -1:
            print("Element found at index:", index)
        else:
            print("Element not found in the array.")

    # call the main function
    if __name__ == "__main__":
        main()
