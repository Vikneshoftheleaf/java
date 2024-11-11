def remove_ith_occurrence(word_list, word, i):
count = 0
for index, w in enumerate(word_list):
if w == word:
count += 1
if count == i:
del word_list[index]
break
return word_list
# Example usage
my_list = ["apple", "banana", "apple", "cherry", "apple"]
word_to_remove = "apple"
ith_occurrence = 2
updated_list = remove_ith_occurrence(my_list, word_to_remove, ith_occurrence)
print(updated_list)
