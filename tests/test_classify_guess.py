from logic_utils import classify_guess


def test_classifies_correct_guess():
    assert classify_guess(50, 50) == "correct"


def test_classifies_far_low_and_high():
    assert classify_guess(20, 50) == "far_low"
    assert classify_guess(80, 50) == "far_high"


def test_classifies_slightly_low_and_high():
    assert classify_guess(42, 50) == "slightly_low"
    assert classify_guess(58, 50) == "slightly_high"
