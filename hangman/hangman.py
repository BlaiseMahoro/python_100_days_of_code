
from collections import defaultdict
from word_generator import WordGenerator
import random

def game():
    
    word_generator = WordGenerator()
    words = word_generator.get_words_with_cache()
    
    if not words:
        print('Unable to find puzzle word. Try again later.')
        return
    
    puzzle_word = ''.join(random.choice(words))
    
    print('puzzle Word: ', puzzle_word) # comment out this to challenge yourself
    word_indexes_map = defaultdict(list)
    
    for i, l in enumerate(puzzle_word):
        word_indexes_map[l].append(i)
        
    word_len = len(puzzle_word)
    
    guessed = ['_'] * word_len
    
    wrong_guesses = 0
    
    while word_len:
        print(' '.join(guessed))
        guess_letter = input('Guess a letter: ').lower()
        if guess_letter not in word_indexes_map:
            wrong_guesses += 1 
            if wrong_guesses == 5:
                print('Failed to solve the puzzle. Try again')
                return
            continue
        for idx in word_indexes_map[guess_letter]:
            guessed[idx] = guess_letter
            word_len -= 1
            
    print('Good job! You guessed the word.')     
    print(''.join(guessed))
            

        



def main():
    game()

main()