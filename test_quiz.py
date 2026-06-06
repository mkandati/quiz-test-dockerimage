import unittest
from quiz import app, game_state, QUIZ_DATA

class QuizAppTestCase(unittest.TestCase):

    def setUp(self):
        # Configure Flask for testing
        app.config['TESTING'] = True
        self.client = app.test_client()
        
        # Reset game state before every single test
        game_state["q_index"] = 0
        game_state["score"] = 0

    def test_homepage_loads(self):
        """Test that the main page loads successfully and shows the first question"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        # Check if the first question text is present in the HTML response
        self.assertIn(QUIZ_DATA[0]["question"].encode(), response.data)

    def test_correct_answer_increments_score(self):
        """Test that submitting a correct answer increases the score"""
        correct_answer = QUIZ_DATA[0]["answer"]
        
        # Simulate selecting the right radio option and clicking submit
        response = self.client.post('/answer', data={'user_answer': correct_answer}, follow_redirects=True)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(game_state["score"], 1)
        self.assertEqual(game_state["q_index"], 1)

    def test_wrong_answer_does_not_increment_score(self):
        """Test that a wrong answer doesn't give points but moves to next question"""
        # Purposely send a wrong answer
        response = self.client.post('/answer', data={'user_answer': 'WrongAnswer!!!'}, follow_redirects=True)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(game_state["score"], 0)
        self.assertEqual(game_state["q_index"], 1)

    def test_game_over_and_reset(self):
        """Test that completing all questions shows game over and reset works"""
        # Force the game state to the end of the quiz
        game_state["q_index"] = len(QUIZ_DATA)
        
        response = self.client.get('/')
        self.assertIn(b"Quiz Finished!", response.data)
        
        # Test the reset route
        reset_response = self.client.get('/reset', follow_redirects=True)
        self.assertEqual(game_state["q_index"], 0)
        self.assertEqual(game_state["score"], 0)

if __name__ == '__main__':
    unittest.main()