import random 
#word=random.choice(list_of_words)


word="randomlol"
picked_letters=[]
#listed_word=list(word)
print(word)
counter=len(word)
#what we can do is first ask user input of a letter in this "word", then iterate through that word to see if the user 
# is matching their guesses with the letters
print(counter)
while True:
    guess=input("Guess a letter in this word:> ")
    
    if guess in word:
        counter-=1
        if guess in picked_letters:
            print("Youve already picked that letter")
        elif guess not in picked_letters:
            print(f"Correct that letter is in the word, only {counter} letters left")
        picked_letters.append(guess)
    elif guess not in word:
        print("Incorrect guess")