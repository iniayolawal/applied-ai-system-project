import random

# FIX: Fixed New Game reset to properly clear score, history, and re-enable input.
def start_new_game(session_state, low: int, high: int):
    """Reset all game state to begin a fresh game within [low, high]."""
    session_state.secret = random.randint(low, high) # REFACTOR: Updated secret number generation to use (low, high) from difficulty settings.
    session_state.attempts = 0
    session_state.score = 0
    session_state.status = "playing"
    session_state.history = []


def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def classify_guess(guess, secret):
    """Classify a guess relative to the secret number.

    The game uses simple distance-based thresholds so the hint system can
    distinguish between a guess that is very far away and one that is close.
    - Exact match is always considered correct.
    - A difference of 10 or more is treated as far away.
    - A difference smaller than 10 is treated as slightly off.
    """
    if guess == secret:
        return "correct"

    distance = abs(guess - secret)

    if distance >= 10:
        if guess < secret:
            return "far_low"
        return "far_high"

    if guess < secret:
        return "slightly_low"
    return "slightly_high"


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")

# FIX: Corrected reversed hint logic (low/high comparison was inverted) and moved to logic_utils.py using agent mode.
def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    try:
        if guess > secret:
            return "Too High", "📉 Go LOWER!"
        else:
            return "Too Low", "📈 Go HIGHER!"
    except TypeError:
        g = str(guess)
        if g == secret:
            return "Win", "🎉 Correct!"
        if g > secret:
            return "Too High", "📉 Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")
