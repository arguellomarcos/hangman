print("Hello welcome to the hangman game.")
word_to_guess = input("Enter in a word for someone to guess: ")
print("You have 10 attempts to try and guess the word:")
word_displayed = "-"*len(word_to_guess)
print(word_displayed)
word_displayed = list(word_displayed)

count = 1
letters_guessed = []
flag = False

while count <= 10:
    letter = input("Enter guess character: ")
    if letter not in letters_guessed:
        letters_guessed.append(letter)
    else:
        print("You already guessed that letter. Please pick another one.")
        letter = input("Enter guess character: ")

    if letter in word_to_guess:
        print("Correct! Guess again")
        for index in range(len(word_to_guess)):
            if word_to_guess[index] == letter:
                word_displayed[index] = letter
    else:
        print("Wrong. Try again.")

    word_displayed = ''.join(word_displayed)
    print(word_displayed)

    if word_to_guess == word_displayed:
        print("You guessed the right word!")
        flag = True
        break
    else:
        word_displayed = list(word_displayed)

    count += 1

if flag == False:
    print("\nSorry you ran out of tries.")






