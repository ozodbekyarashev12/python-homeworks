def reverse_list(lst):
    reversed_lst = []
    for i in range(len(lst)):
        reversed_lst.append(lst.pop())
    return reversed_lst

# Example usage
my_list = [1, 2, 3, 4, 5]
print(f"The reversed list is {reverse_list(my_list)}.")
