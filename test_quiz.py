from quiz import quiz

def test_quiz():
    response = quiz.test_client().get('/')
    assert response.status_code == 200
    assert response.data== b"Hello! Welcome to the quiz!"
