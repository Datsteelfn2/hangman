import random 
#word=random.choice(list_of_words)


word="randomlol"

#listed_word=list(word)
print(word)
counter=len(word)
#what we can do is first ask user input of a letter in this "word", then iterate through that word to see if the user 
# is matching their guesses with the letters
for letter in range(len(word)):
    guess=input("Guess a letter in a random word:> ")
    if guess in word:
        counter-=1
        print(f"Correct,{letter} is a part of the word, only {counter} letters left")
    elif guess not in word:
        print(f"Not quite,{counter} guesses left")
