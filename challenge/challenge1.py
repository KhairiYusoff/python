def merge_lists(list1, list2):
    combined_list = list1 + list2
    unique_list = list(set(combined_list))  # Remove duplicates
    sorted_list = sorted(unique_list)       # Sort the list
    return sorted_list

# Test the function
print(merge_lists([1, 2, 3], [2, 3, 4, 5]))  # Expected output: [1, 2, 3, 4, 5]