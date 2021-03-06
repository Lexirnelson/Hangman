#Alexa Nelson

print('welcome to hangman')
print('enter your secret word ;)')
word = input('WORD > ')
listed_word = []
listed_word += word #puts the letters in the word in a list
word_len = len(listed_word)
blank_word = []
letter_position = 0 
win = 'Congratulations! You guessed the secret word'
lose = 'You ran out of guesses! Better luck next time!'
right = 'Success! You guessed a character in the word!'
wrong = 'Boo! You guessed incorrectly'
num_guesses = 0

for x in listed_word:
    blank_word += '_' #shows what the word will look like
    
print(' '.join(blank_word))


print('Enter the number of guesses allowed')
guesses = int(input('NUM> '))

word_guessed = False #variable to tell program when the word is guessed
guess_list = [] #the list of guesses
current_letter = 'nothing' 

while word_guessed == False and num_guesses < guesses:
    print('please enter a character:') 
    current_letter = input('CHAR> ')
    if current_letter in guess_list:
        while current_letter in guess_list: #tells user if they already guessed a letter
            print('you already entered that letter please enter a new character')
            current_letter = input('CHAR> ')
            
    guess_list += current_letter
    guesses -= 1
    if current_letter in listed_word: #code that happens if it's correct
        letter_occurences = 0 #counts how many times letter shows up
        for x in listed_word:
            if x == current_letter:
                letter_occurences += 1
        word_len -= letter_occurences #number of letters left
        letter_position = listed_word.index(current_letter) #fixes the blank word
        blank_word[letter_position] = current_letter
        letter_occurences -= 1
        while letter_occurences > 0: #loop that catches repeat letters
            letter_position = listed_word.index(current_letter,(letter_position+1))
            blank_word[letter_position] = current_letter
            letter_occurences -= 1

        if word_len == 0:
            print('OUTPUT', win)
            print(guesses, 'guesses remaining')
            print(guess_list)
            print('OUTPUT secret word: ', word)
            word_guessed = True
        else:
            print('OUTPUT', right)
            print(guesses, 'guesses remaining')
            print('Characters guessed', guess_list)
            print('OUTPUT secret word:', ' '.join(blank_word))
            print('')
    else:
        if guesses == 0:
            print('OUTPUT', lose)
            print('OUTPUT Secret word: ', word)
        else:
            print(wrong)
            print('Characters guessed', guess_list)
            print('OUTPUT Secret word: ', ' '.join(blank_word))
            print('')
            
        
            

