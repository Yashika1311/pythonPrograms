#take sentence as input and count no of words in it

sentence = input("Enter a sentence: ")

words = sentence.split()

count = len(words)

print("Number of words in the sentence: ", count)