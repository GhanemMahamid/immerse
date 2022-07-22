import random

def get_masked_word(word):
    ''' Function to get a masked word from a word (drops ~50% of letters)
    e.g. "CAVIAR" -> "C-V--R"; "UNICORN" -> "U-IC-R-"
    input: the word as a string
    output: the masked word (as a string) and a
      dictionary of masked letters with their position in the word.
    Example: get_masked_word("UNICORN") can return the tuple
    ('U-IC---', {'N': [1, 6], 'O': [4], 'R': [5]})
    '''
    # Get unique letters in the word
    unique_letters_list = list(set(word)) # set() finds unique elements in string
    # Shuffling the list of unique letters
    random.shuffle(unique_letters_list)
    # Selecting just 50% of the letters
    split_point = len(unique_letters_list) // 2
    letters_to_mask_list = unique_letters_list[0:split_point]
    # Creating the masked word and the dictionary
    masked_word = ""
    masked_letter_position_dict = {}
    for letter_position, letter in enumerate(word):
        if(letter in letters_to_mask_list):
            masked_word = masked_word + "-"
            # We store the position of the masked letter in a dictionary
            if(letter in masked_letter_position_dict):
                # If the letter is in the dictionary we append the position
                masked_letter_position_dict[letter].append(letter_position)
            else:
                # If the letter is NOT in the dictionary we create the entry (a list)
                masked_letter_position_dict[letter] = [letter_position]
        else:
            masked_word = masked_word + letter        
    # Finished, let's return the masked letters and the
    # dictionary containinng the position of the masked letters.
    return masked_word, masked_letter_position_dict




#0. Define a variable for the game score, e.g. score=3
# where 3 is the maximum number of attempts for guessing the word (score==0 the user lost)
score= (3)
print(score)

#1. Load all the available words in memory (by reading them from a text file, or hard-coding them)
# You can encapsulate this piece of code in the function called load_words_list() above

text_file = open("/Users/ghanemalmhamid/Desktop/mylist1.txt", "r")  

word_list = text_file.readlines()
         


#2. Pick a random word from all the available words.
# You can encapsulate this code into the function called get_random_word() above
word = random.choice(word_list)

if(word[-1]=="\n"):
     word = word[0:-1]
     print(word)

#3. Turn the letters in the word into capital letters, search for the default method .upper()
word = word.upper()


#4. Produce a masked version of the word (hide some letters).
# Write the code for the function get_masked_word().
# For example if the word is PENCIL the function get_masked_word() 
# returns something like P-N-I- or -EN-I- and a dictionary of the masked letters.
# The dictionary will use the masked letter as key, and a list of positions as value.
# e.g. {"a": [1,3], "d": 2} means that the letter "a" is in position 1 and 3 in the word.

masked_word, masked_letters_dictionary = get_masked_word(word)
print(masked_word)


for round in range(10):


    #5. Print on screen the masked word and ask the user to 
    # type a letter in the terminal, you can use the default method input()

    letter_selected = input("Type a letter ")




    #6. You need to check if the user provided more than one letter.
    # Consider just the first character and discard the rest.A

    if len(letter_selected) ==1:
        pass
    else:
        print("you provided more than one letter")
        letter_selected = letter_selected[0]



    #7. Turn the character provided by the user into a capital letter

    letter_selected = letter_selected.upper()
    print(letter_selected)


    #8. Check if the letter provided by the user is a good one or a bad one.
    # - First, check if the letter is already visible (the user did a mistake), decrease the score.
    # - Second, if the letter is in the dictionary of masked letters, the user did a good choice 
    #     (now you need to make those letters visible and remove the letter from the dictionary).
    # - Third, the letter is neither in the visible letters, nor in the masked letters, decrease the score.

    if letter_selected in masked_letters_dictionary :
        letter_position_list = masked_letters_dictionary[letter_selected]
        for position in letter_position_list:
            #masked_word[position] = letter_selected
            tmp_list = list(masked_word)
            tmp_list[position] = letter_selected
            masked_word = "".join(tmp_list)

        #remove element from dictionary

        masked_letters_dictionary.pop(letter_selected)

    else :  
        print("letter is not in the word")
        score = score - 1 
        print("your score has decreased to", score)
    



    #9. Print the current user score, the masked word, and the list of letters already tried.
    # If the score==0 the game is finished, a new match can start (score=3)
    print(masked_word)

    if word == masked_word:
        print("you won!")
        break
    
    if score == 0:
        print("you lost!")
        break

