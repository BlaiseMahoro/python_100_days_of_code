import unittest
from unittest.mock import patch, MagicMock, mock_open
import turtle
import pandas as pd
from main import setup_screen, load_states_data, get_user_guess, display_state_name, write_states_to_learn



class FiftyStatesGameTest(unittest.TestCase):
    @patch('turtle.Screen')
    def test_setup_screen(self, mock_screen):
        image = 'blank_states_img.gif'
        screen = setup_screen(image)
        mock_screen().title.assert_called_with('U.S States Game')
        mock_screen().addShape.assert_called_with(image)
        self.assertEqual(turtle.shape(), image)
        
    @patch('pandas.read_csv')
    def test_load_states_data(self, mock_read_csv):
        mock_read_csv.return_value = pd.DataFrame({
            'state': ['California', 'Texas', 'New York'],
            'x': [1, 2, 3],
            'y': [4, 5, 6]
        })
        csv_file = '50_states.csv'
        states = load_states_data(csv_file)
        expected_states = {
            'california': (1, 4),
            'texas': (2, 5),
            'new york': (3, 6)
        }
        self.assertEqual(states, expected_states)
        
    @patch('turtle.Screen.textinput')
    def test_get_user_guess(self, mock_textinput):
        mock_textinput.return_value = 'California'
        screen = MagicMock()
        correct_num = 5
        states_num = 50
        answer_state = get_user_guess(screen, correct_num, states_num)
        mock_textinput.assert_called_with(title="Guess the State 5/50", prompt="What's another State?")
        self.assertEqual(answer_state, 'California')

    @patch('turtle.Turtle')
    def test_display_state_name(self, mock_turtle):
        name = 'California'
        position = (1, 4)
        display_state_name(name, position)
        t = mock_turtle()
        t.hideturtle.assert_called_once()
        t.penup.assert_called_once()
        t.goto.assert_called_with(position)
        t.write.assert_called_with(name.capitalize())
        
    @patch('builtins.open', new_callable=mock_open)
    @patch('pandas.DataFrame.to_csv')
    def test_write_states_to_learn(self, mock_to_csv, mock_open):
        file_path = 'states_to_learn.csv'
        data = ['California', 'Texas', 'New York']
        write_states_to_learn(file_path, data)
        expected_df = pd.DataFrame(data)
        mock_to_csv.assert_called_once_with(file_path, sep='\t')

        

if __name__ == '__main__':
    unittest.main()
        
    
        
