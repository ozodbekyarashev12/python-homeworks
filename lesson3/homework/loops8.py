def slice_list(lst):
    result = []
    for i in range(min(3, len(lst))):  # Limit to 3 elements
        result.append(lst[i])
    return result

# Example usage
my_list = [1, 2, 3, 4, 5]
print(f"The first three elements of the list are {slice_list(my_list)}.")

