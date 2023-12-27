#3rd

str1=input("Enter the string :- ")
str2=input("Enter the string :- ")

words1=str1.split()
words2=str2.split()

uncommon_word=[]

for i in words1:
 if i not in words2 and i not in uncommon_word:
      uncommon_word.append(i)

for j in words2:
  if j not in words1 and j not in uncommon_word:
      uncommon_word.append(j)

print("Uncommon Words:",uncommon_word)
