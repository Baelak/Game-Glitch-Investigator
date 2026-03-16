from logic_utils import check_guess, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "🎉 Correct!"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"

# Tests targeting the fixed hint bug: ensure correct messages for edge cases
def test_hint_bug_edge_case_high():
    # Previously, string comparison could give wrong hint; e.g., guess 9 vs secret 10 as string
    # But now fixed, should be correct
    outcome, message = check_guess(9, 10)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"

def test_hint_bug_edge_case_low():
    # Guess 15 vs secret 10, should be Too High
    outcome, message = check_guess(15, 10)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"

# Tests for attempt counter bug: scoring depends on attempt_number
def test_update_score_win_early():
    # Win on attempt 1: points = 100 - 10*(1+1) = 80
    new_score = update_score(0, "Win", 1)
    assert new_score == 80

def test_update_score_win_late():
    # Win on attempt 8: points = 100 - 10*(8+1) = 10 (min 10)
    new_score = update_score(0, "Win", 8)
    assert new_score == 10

def test_update_score_too_high_even_attempt():
    # Too High on even attempt (e.g., 2): +5
    new_score = update_score(0, "Too High", 2)
    assert new_score == 5

def test_update_score_too_high_odd_attempt():
    # Too High on odd attempt (e.g., 1): -5
    new_score = update_score(0, "Too High", 1)
    assert new_score == -5

def test_update_score_too_low():
    # Too Low always -5
    new_score = update_score(0, "Too Low", 1)
    assert new_score == -5
