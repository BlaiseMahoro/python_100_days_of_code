
"""
Python program to simulate the treasure Island game. 
Treasure Island is built on a finite state machine. 
This state machine can be represented by a n-ary tree (cleaner) 
or a bunch if/else conditionals.
"""

def easy_way():
    print('Welcome to Treasure Island. \nYou Mission is to find the treasure.')
    if input().lower() != 'left':
        print('Fall into a hole. Game Over.')
        return
    if input('swim or wait \n').lower() != 'wait':
        print('Attacked by trout. Game Over.')
        return
    door = input('Which door? \n')

    if door == 'yellow':
        print('You Win!')
        return
    if door == 'blue':
        print('Eaten by beasts. Game Over')
        return
    if door == 'red':
        print('Burned by fire. Game Over.')
        return
    print('Game Over.')


def hard_way():
    print('Welcome to Treasure Island. \nYou Mission is to find the treasure.')
    
    decision_tree = {
        'left': {
            'swim':'Attacked by trout. Game Over.',
            'wait':{
                'red': 'Burned by fire. Game Over.',
                'blue': 'Eaten by beasts. Game Over.',
                'yellow': 'You Win!',
                'default': 'Game Over.'
            },
            'default':'Attacked by trout. Game Over.'
            },
        'right':'Fall into a hole. Game Over.',
        'default': 'Fall into a hole. Game Over.'
    }
    messages = ['left or right?', 'swim or wait?', 'which door?']
    count = 0 
    node = decision_tree
    while True:
        ans = input(messages[count] + '\n').strip()
        if ans not in node:
            print(node['default'])
            return 
        node = node[ans.lower()]
        if isinstance(node, str):
            print(node)
            return
        count += 1



def main():
    # comment one or the other to test
    # easy_way()
    hard_way() #this is more efficient when you have thousands of states and decisions.
main()
