import turtle
import time
import pandas as pd

def setup_screen(image):
    screen = turtle.Screen()
    screen.title('U.S. States Game')
    screen.addshape(image)
    turtle.shape(image)
    return screen

def load_states_data(csv_file):
    return  pd.read_csv(csv_file)

def get_user_guess(screen, correct_num, states_num):
    return screen.textinput(title=f"Guess the State {correct_num}/{states_num}", prompt="What's another State?")

def display_state_name(name, position):
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(position)
    t.write(name)
    
def write_states_to_learn(file_path, data):
    new_data_frame = pd.DataFrame(data)
    new_data_frame.to_csv(file_path, sep='\t')  

def main():
    IMAGE = 'blank_states_img.gif'
    CSV_FILE = '50_states.csv'
    STATES_NUM = 50

    screen = setup_screen(IMAGE)
    df = load_states_data(CSV_FILE)
    states = df.state.to_list()
    correct_num = 0
    answered_states = set()

    while correct_num < STATES_NUM:
        answer_state = get_user_guess(screen, correct_num, STATES_NUM).title()
        
        if(answer_state == 'Exit'):
            break
        if answer_state in states:
            correct_num += 1
            answered_states.add(answer_state)
            position = int(df[df.state == answer_state].x), int(df[df.state == answer_state].y),
            display_state_name(answer_state, position)
        else:
            print('Wrong! Try again.')
            
    
    if correct_num < STATES_NUM:
        missing_states = [state for state in states  if state not in answered_states]
        
        write_states_to_learn('states_to_learn.csv', missing_states)
        print(missing_states)
            
                
        


if __name__ == "__main__":
    main()