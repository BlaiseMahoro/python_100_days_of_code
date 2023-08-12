
from collections import defaultdict
from word_generator import WordGenerator
import random

HANGING_LEVELS = [
    '''''',
    '''
    +-------+
    |       |
    |       O
    |
    |
    |
    |
    ''',
    '''
    +-------+
    |       |
    |       O
    |       |
    |
    |
    |
    ''',
    '''
    +-------+
    |       |
    |       O
    |       |/
    |
    |
    |
    ''',
    '''
    +-------+
    |       |
    |       O
    |      \|/
    |
    |
    |
    ''',
       '''
    +-------+
    |       |
    |       O
    |      \|/
    |       |
    |
    |
    ''',
    '''
    +-------+
    |       |
    |       O
    |      \|/
    |       |
    |      /
    |
    ''',
      '''
    +-------+
    |       |
    |       O
    |      \|/
    |       |
    |      / \\
    |
    ''']


def game():
    
    word_generator = WordGenerator()
    words = word_generator.get_words_with_cache()
    
    if not words:
        print('Unable to find puzzle word. Try again later.')
        return
    
    puzzle_word = ''.join(random.choice(words))
    
    # print('puzzle Word: ', puzzle_word) # uncomment this to test correctness
    word_indexes_map = defaultdict(list)
    
    for i, l in enumerate(puzzle_word):
        word_indexes_map[l].append(i)
        
    word_len = len(puzzle_word)
    
    guessed = ['_'] * word_len
    
    wrong_guesses = 0
    seen = set()
    
    while word_len:
        print('****************************************************')
        print(HANGING_LEVELS[wrong_guesses], end='\t\t\t\t')
        print(' '.join(guessed))
        guess_letter = input('Guess a letter: ').lower()
        if guess_letter not in word_indexes_map or guess_letter in seen:
            wrong_guesses += 1 
            if wrong_guesses == len(HANGING_LEVELS):
                print('Failed to solve the puzzle. Try again. \nThe word was ' + puzzle_word)
                return
            continue
        for idx in word_indexes_map[guess_letter]:
            guessed[idx] = guess_letter
            word_len -= 1
        seen.add(guess_letter)
            
    print('Good job! You guessed the word.', end='\t\t')     
    print(''.join(guessed))           

        
def main():
    game()

main()