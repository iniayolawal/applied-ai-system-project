# 🎮 Glitchy Guesser AI: Reliable Hint Generation System

## Project Overview

### Original Project: Game Glitch Investigator: The Impossible Guesser

Game Glitch Investigator was originally a Streamlit-based number guessing game created to practice debugging AI-generated code. The goal was to identify and repair issues such as incorrect hint logic, broken game state management, invalid input handling, and inconsistent difficulty settings.

The original system allowed players to select a difficulty level, guess a randomly generated number, receive higher/lower hints, track attempts, and maintain a score. The project focused on using AI coding assistants to investigate bugs, refactor code, and create automated tests.

## Applied AI Extension

For this final project, I extended the guessing game into an AI-assisted hint generation system.

The updated system uses:
- Retrieval-Augmented Generation (RAG) to retrieve context-aware hints from a hint knowledge base.
- Guardrails to validate that generated hints do not contradict the actual game state.
- Logging to track AI decisions and validation results.
- An evaluation harness to measure system reliability.

Instead of directly returning static hints, the system classifies the player's guess, retrieves an appropriate hint, validates the hint, and then displays the final response.

# Architecture Overview

The system follows this workflow:

1. The user enters a guess through the Streamlit interface.
2. `classify_guess()` determines the player's position relative to the secret number.
3. `retrieve_hint()` uses the classification category to retrieve a relevant hint from the knowledge base.
4. `validate_hint()` checks that the hint is logically consistent.
5. The validated hint is displayed and logged.
6. `evaluate_system.py` tests classification, retrieval, and validation behavior.

See `architecture.mmd` for the Mermaid architecture diagram.

# Setup Instructions

## Clone the repository

```
git clone <repository-url>
cd applied-ai-system-final
```
## Create environment
```
python3 -m venv .venv
source .venv/bin/activate
```
## Install dependencies
```
pip install -r requirements.txt
```
## Run the application
```
python3 -m streamlit run app.py
```

# Sample Interactions

The following examples demonstrate how the system processes a user's guess through classification, retrieval, validation, and final output.

---

## Example 1: User Makes a Far Low Guess

### Input
Secret number: 50
User guess: 20
### AI Processing
The system classifies the guess:
far_low
The RAG component retrieves a hint associated with the `far_low` category:
Retrieved Hint:
"Consider guessing closer to the middle of the remaining range."
The guardrail system validates that the hint matches the game state:
Validation Result:
PASS
### Final Output to User
Your guess is too low.
Hint: Consider guessing closer to the middle of the remaining range.
---

## Example 2: User Makes a Slightly High Guess

### Input
Secret number: 50
User guess: 58
### AI Processing
The system classifies the guess:
Classification:
slightly_high
The RAG component retrieves a context-appropriate hint:
Retrieved Hint:
"Only a small adjustment downward may be needed."
The guardrail validates the response:
Validation Result:
PASS
### Final Output to User
Your guess is too high.
Hint: Only a small adjustment downward may be needed.

---

## Example 3: User Correctly Guesses the Number

### Input
Secret number: 52
User guess: 52
### AI Processing
The system identifies an exact match:
Classification:
correct
The RAG component retrieves the success response:
Retrieved Hint:
"Great job! Your strategy paid off."
The guardrail validates the response:
Validation Result:
PASS
### Final Output to User
Correct! You found the secret number.
Hint: Great job! Your strategy paid off.
---

## Example 4: Guardrail Prevents a Misleading Hint

### Input
Secret number: 50
User guess: 20
The system correctly classifies the guess:
Classification:
far_low
A misleading hint is detected:
Generated Hint:
"Try going lower."
The guardrail checks whether the hint contradicts the actual game state:
Validation Result:
FAIL
Reason:
A low guess should not receive instructions to guess lower.
The system rejects the incorrect hint and prevents it from being shown to the user.


# Design Decisions

## Why RAG?

The original game used fixed hint logic. I introduced retrieval so hints could be stored separately from the game logic and expanded without changing application code.

## Why Guardrails?

Language models and AI systems can produce incorrect outputs. The validation layer ensures hints remain consistent with the player's actual guess direction.

## Trade-offs

A retrieval-based approach adds additional complexity compared to hardcoded hints, but it improves maintainability, transparency, and reliability.

The system does not use a large language model directly for generation, which reduces unpredictability but limits the variety of possible hints.

# Testing Summary

## Reliability and Evaluation

To ensure the AI-assisted hint system behaves consistently, the project includes automated evaluation, guardrails, and logging mechanisms.

## Automated Evaluation

The `evaluate_system.py` script tests the reliability of the major AI system components:

- Guess classification
- Hint retrieval
- Hint validation

Evaluation results:
```
[PASS] classify_guess exact match
[PASS] classify_guess far low
[PASS] classify_guess slightly high
[PASS] retrieve_hint returns a non-empty string
[PASS] guardrail accepts matching low hint
[PASS] guardrail rejects misleading low hint
[PASS] guardrail rejects misleading high hint

Overall success rate: 7/7 (100.0%)
```

## Guardrail Validation

The guardrail system prevents incorrect hints from being shown to users.

For example:

| Test Input | Expected Behavior | Result |
|---|---|---|
| Guess: 20, Secret: 50 | Hint should encourage increasing the guess | Pass |
| Guess: 58, Secret: 50 | Hint should encourage decreasing the guess | Pass |
| Guess: 20, Secret: 50 with misleading hint "Try going lower" | System should reject incorrect guidance | Pass |

## Logging and Error Handling

The system logs AI hint decisions and validation results in `hint_events.log`.

Each log entry records:

- Timestamp
- User guess
- Secret number
- Guess classification category
- Retrieved hint
- Validation result

Example:
```
timestamp=2026-08-06T00:46:45Z | guess=45 | secret=17 | category=far_high | hint=Consider reducing your guess significantly. | validation_result=True
```

This allows the system behavior to be reviewed after execution and helps identify incorrect AI behavior.

## Reliability Improvements

The original guessing game relied on fixed hint logic that could produce misleading responses. By adding retrieval, validation, and evaluation, the system became more reliable because AI-generated hints are checked before reaching the user.

The evaluation process showed that all tested classification, retrieval, and validation cases passed successfully.

# Reflection

This project showed me that building reliable AI systems requires more than adding AI functionality. The most important part was designing checks around AI behavior and validating that outputs remained accurate and useful.

By combining retrieval, guardrails, logging, and evaluation, the system became more predictable and easier to debug.
