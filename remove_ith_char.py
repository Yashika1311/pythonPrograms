#to remove ith charecter from string
def remove_ith_character(input_str, i):
    # Check if the index is valid
    if i < 0 or i >= len(input_str):
        print("Invalid index")
        return input_str

    # Remove i-th character using slicing
    modified_str = input_str[:i] + input_str[i + 1:]

    return modified_str

original_string = "Hello World"

modified_string = remove_ith_character(original_string, 3)

print("Original String:", original_string)
print("String after removing 4th character:", modified_string)
