# Python Quiz

A simple command-line multiple-choice quiz written in Python. Questions are loaded from a text file, 5 random ones are asked each round, and your score is shown at the end with a performance message.

## Features

- Questions loaded from `questions.txt`
- 5 random questions each round
- One question at a time with options A, B, C, D
- Input validation (only A/B/C/D, upper or lowercase)
- Instant feedback: correct or wrong, with the right answer shown
- Final score with a performance message
- Replay as many times as you like

## Files

| File            | Purpose                          |
|-----------------|----------------------------------|
| `quiz.py`       | The quiz program                 |
| `questions.txt` | The questions, options, answers  |
| `README.md`     | This documentation               |

## How to run

1. Install Python 3 (https://www.python.org/downloads/).
2. Put `quiz.py` and `questions.txt` in the same folder.
3. Open a terminal in that folder.
4. Run:

```
python quiz.py
```

(Use `python3 quiz.py` if `python` doesn't work.)

5. Type A, B, C or D for each question and press Enter.
6. At the end, type `y` to play again or anything else to quit.

## Questions format

Each question is **one line** in `questions.txt`, with 6 parts separated by commas:

```
question,A) option,B) option,C) option,D) option,correct letter
```

Example:

```
Which keyword defines a function in Python?,A) func,B) def,C) function,D) define,B
What does len('hi') return?,A) 1,B) 2,C) 3,D) Error,B
```

Rules:

- Exactly 6 parts per line: the question, four options, and the answer.
- The answer must be a single **capital** letter: `A`, `B`, `C` or `D`.
- Do **not** use commas inside the question or the options, because commas separate the parts.
- Do not leave blank lines.
- The file needs **at least 5 questions**, since each round picks 5.

## Scoring rules

- Correct answer: **+1 point**
- Wrong answer: **0 points** (no penalty)
- Maximum score per round: **5**

| Score | Message          |
|-------|------------------|
| 5/5   | Perfect Score!   |
| 4/5   | Great Job!       |
| 3/5   | Good effort!     |
| 0-2   | Keep Practicing  |

## Example output

```
Welcome to the Python Quiz!
1 Which keyword defines a function in Python?
A) func
B) def
C) function
D) define
Enter your answer (A/B/C/D):b
Correct Answer!!!
```

## Concepts practiced

Classes and methods, file handling, lists, loops, input validation, `random.sample`, and string methods (`strip`, `split`, `upper`).
