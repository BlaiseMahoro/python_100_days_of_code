

def encode(word, shiftNumber):
    wordList = list(word)
    for i, el in enumerate(wordList):
        newPos = ord('a') + (ord(el) - ord('a')  + shiftNumber) % 26
        wordList[i] = chr(newPos)
    return ''.join(wordList)


def decode(cipher_text, shiftNumber):
    text_list = list(cipher_text)
    for i, el in enumerate(text_list):
        newPos = ord('a')  + (ord(el) - ord('a') - shiftNumber) % 26
        text_list[i] = chr(newPos)
    return ''.join(text_list)

    
def game():
    print('Caesar Cipher')
    keep_going = True 

    while keep_going:
        mode = input('Would you like to encode (E) or decode (D)? ').upper()
        while mode not in {'D', 'E'}:
            mode = input(
                'Invalid mode selected! Try again. \nWould you like to encode (E) or decode (D)? ').upper()
        inputText = input(
            'Input a string to be processed (only alpha chars/no whitespace): ').strip().lower()
        shiftNumber = int(input('Input the shift number (integers only): '))

        if mode == 'E':
            result = encode(inputText, shiftNumber)
            print('The cipher text is: ', result)
        else:
            result = decode(inputText, shiftNumber)
            print('The original text is: ', result)
            
        user_decision = input('Would you like to keep going? (Y/N)').strip().upper()
        while user_decision not in {'Y', 'N'}:
            user_decision = input('Would you like to keep going? (Y/N)').strip().upper()
        keep_going = user_decision == 'Y'
        
        

def main():
    game()
    
main()