import random 
list_of_words=["united","senegal","pizza","impossible","unlucky"]
lives=10

word=random.choice(list_of_words)
listed_word=list(word)
print(word)
#what we can do is first ask user input of a letter in this "word", then iterate through that word to see if the user 
# is matching their guesses with the letters
for letter in listed_word:
    guess=input("Guess a letter in a random word:> ")
    if guess==letter:
        print(f"Correct,{letter} is a part of the word")