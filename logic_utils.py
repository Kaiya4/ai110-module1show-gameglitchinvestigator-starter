# FIX: Extracted all business logic from app.py into logic_utils.py to separate concerns, done collaboratively with AI.

def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        # FIX: AI and I increased the Hard mode upper bound to 200 for proper scaling.
        return 1, 200
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.
    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if not raw:
        return False, None, "Enter a guess."
    try:
        value = int(float(raw))
    except ValueError:
        return False, None, "That is not a number."
    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).
    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "🎉 Correct!"
    if guess > secret:
        # FIX: AI and I corrected the reversed directional hints to accurately reflect the state.
        return "Too High", "📉 Go LOWER!"
    return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        return current_score + max(10, 100 - 10 * (attempt_number + 1))
    if outcome == "Too High":
        return current_score + 5 if attempt_number % 2 == 0 else current_score - 5
    if outcome == "Too Low":
        return current_score - 5
    return current_score