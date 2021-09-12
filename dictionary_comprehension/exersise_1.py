word_counter = "How many words are there is this sentence"

#we can convert a string into a list by using .split() function

word = {word:len(word) for word in word_counter.split()}
print(word)