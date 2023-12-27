#to check if two strings are anagrams of each other

str1=input("enter the first string:")
str2=input("enter the second string:")

for i in str1:
    if i in str2:
        continue
    else:
      print("its not the anagram")
      exit()

print("Its the anagram")

