# test_quiz.py
import pytest
from quiz import start_game

def test_game_quits_if_not_ready(monkeypatch, capsys):
    # Simulate the user typing "no" when asked if they are ready
    monkeypatch.setattr('builtins.input', lambda _: "no")
    
    start_game()
    
    # Check that it printed the correct refusal message
    captured = capsys.readouterr()
    assert "Okay, maybe next time!" in captured.out


def test_game_perfect_score(monkeypatch, capsys):
    # This simulates a sequence of inputs:
    # 1. "yes" to start
    # 2. "a" for Q1 (Paris)
    # 3. "b" for Q2 (Jupiter)
    # 4. "c" for Q3 (Tokyo)
    responses = iter(["yes", "a", "b", "c"])
    monkeypatch.setattr('builtins.input', lambda _: next(responses))
    
    start_game()
    
    captured = capsys.readouterr()
    
    # Assertions to ensure the logic calculated a perfect score
    assert "Great! Let's get started." in captured.out
    assert "You got 3 questions correct!" in captured.out
    assert "Your final score is: 100.00 %" in captured.out