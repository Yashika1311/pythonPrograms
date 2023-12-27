#least frequency

# 5. Python program to find the least frequent character in the string.

def leastfreqchar (input_string):
    count = {}

    for char in input_string:
        count[char] = count.get(char, 0) + 1

    mincount = min(count.values(), default=0)

    leastchars = [char for char, count in count.items() if count == mincount]

    return leastchars

def main():
    user_input = input("Enter a string: ")

    result = leastfreqchar (user_input)

    if result:
        print("Least frequent characters:", ", ".join(result))
    else:
        print("No characters in the input.")

if __name__ == "__main__":
    main()