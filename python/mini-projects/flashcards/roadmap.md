# Spaced-Repetition Flashcards Project Roadmap

## Overview
This roadmap is a step-by-step guide to building a CLI-based flashcards app using SM-2 spaced repetition. It's based on the PRD in `project-ideas/firsProject.md` and simplified for learning. Total MVP time: 8-16 hours over 1-2 weeks. Focus on one step per session (30-60 min) to build confidence. Learn just-in-time—read docs only when needed for the current task.

**Goal**: A working CLI app where you can create decks, add cards, study with quality ratings (0-5), and have reviews scheduled via SM-2. No GUI, no advanced features yet.

**What You'll Learn**:
- Python fundamentals (dataclasses, venv).
- SQLite database (storing data locally).
- SM-2 algorithm (math for scheduling reviews).
- CLI building (argparse for user commands).
- Testing (pytest for reliability).
- CSV handling (import/export decks).

**Key Advice for Beginners** (This is Your First Complex Project):
- **Start Small**: Each step builds on the last. Don't skip ahead—test your code after every change.
- **Test Early**: Use pytest for confidence. Write tests even for simple functions.
- **Debug Tip**: Add `print()` statements to see what's happening. Remove them later.
- **Time Management**: Code for 45 min, break for 15 min. If stuck >10 min, note the issue and try again later.
- **Version Control**: Use Git to commit after each step (e.g., `git add . && git commit -m "Added basic CLI"`).
- **Mindset**: It's okay if code is messy at first. Refactor later. Mistakes are learning.
- **Resources**: Keep browser tabs open for Python docs, sqlite3 tutorial, SM-2 Wikipedia.
- **Troubleshooting**: If something doesn't work, Google the error message + "Python". Copy-paste code to ChatGPT for quick help.

## Prerequisites
- Python 3.10+ installed (run `python --version` to check).
- Basic Python knowledge (variables, functions, loops).
- Terminal/command line comfort (running scripts, navigating folders).

## Step-by-Step Plan

### Day 1: Setup & Python Basics (30-60 min)
**Goal**: Get environment ready and practice dataclasses (data structures for cards/decks).

**What is a venv?** Virtual environment—isolates project dependencies so they don't conflict with other projects.
**What is a dataclass?** A simple class for storing data (like a blueprint for cards). Easier than regular classes.

**Steps**:
1. In `python/mini-projects/`, create folder: `mkdir flashcards`.
2. Create venv: `python -m venv venv` (creates a folder with isolated Python).
3. Activate venv: `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows)—your terminal prompt changes.
4. Install pytest: `pip install pytest` (pytest is a tool for automated testing).
5. Create `models.py` and define a `Card` dataclass with fields: `id` (int), `front` (str), `back` (str), `ease` (float), `repetitions` (int), `interval` (int), `due_date` (str). Example:
   ```python
   from dataclasses import dataclass

   @dataclass
   class Card:
       id: int
       front: str
       back: str
       ease: float = 2.5
       repetitions: int = 0
       interval: int = 0
       due_date: str = ""
   ```
6. In `models.py`, instantiate a Card and print it: `card = Card(1, "Hello", "Hola"); print(card)`.
7. Add a simple test: `def test_card_creation(): card = Card(1, "test", ""); assert card.front == "test"`.
8. Run test: `pytest models.py`.

**Check Success**: Venv works, dataclass created, test passes.
**Advice**: Dataclasses are like blueprints—easy to use for data. If stuck, read Python dataclass docs (5 min). Example code is your friend.
**Troubleshooting**: If pytest not found, check venv is activated. If import error, ensure dataclasses is imported.

### Day 2: SQLite Basics (1-2 hours)
**Goal**: Learn to store data in a local DB (no app yet).

**What is SQLite?** A lightweight database that stores data in files (or memory). No server needed—perfect for local apps.
**What is a parameterized query?** SQL with placeholders (`?`) to safely insert user data (prevents hacking).

**Steps**:
1. Create `db.py`.
2. Import `sqlite3` (Python's built-in DB module).
3. Create `init_db()` function: Use `sqlite3.connect(':memory:')` for now (in-memory, fast for testing—no files created).
4. In `init_db()`, execute SQL to create tables:
   - decks: id (INTEGER PRIMARY KEY), name (TEXT), created_at (TEXT).
   - cards: id (INTEGER PRIMARY KEY), deck_id (INTEGER), front (TEXT), back (TEXT), ease (REAL DEFAULT 2.5), repetitions (INTEGER DEFAULT 0), interval (INTEGER DEFAULT 0), due_date (TEXT), created_at (TEXT).
   - reviews: id (INTEGER PRIMARY KEY), card_id (INTEGER), quality (INTEGER), timestamp (TEXT), old_ease (REAL), old_repetitions (INTEGER), old_interval (INTEGER).
   Example SQL: `cursor.execute('CREATE TABLE cards (id INTEGER PRIMARY KEY, front TEXT, ...)')`.
5. Add `add_card(deck_id, front, back)`: Insert into cards table using parameterized query (`?` placeholders). Example: `cursor.execute('INSERT INTO cards (front, back) VALUES (?, ?)', (front, back))`.
6. Add `get_due_cards(date)`: Query cards where due_date <= date. Example: `cursor.execute('SELECT * FROM cards WHERE due_date <= ?', (date,))`.
7. In `test_db.py`, write tests for init_db, add_card, get_due_cards. Example: `def test_add_card(): init_db(); add_card(1, 'hi', 'hello'); assert get_due_cards('2025-01-01') == [...]`.
8. Run tests: `pytest test_db.py`.

**Check Success**: DB tables created, can insert/query cards.
**Advice**: SQL is like English—CREATE TABLE, INSERT INTO. Use :memory: for tests (no files). Parameterized queries prevent security issues.
**Troubleshooting**: If DB errors, check SQL syntax. Use `print(cursor.fetchall())` to debug queries.

### Day 3: SM-2 Algorithm (2-3 hours)
**Goal**: Implement the core scheduling logic.

**What is SM-2?** Spaced repetition algorithm—math to decide when to review cards based on how well you remember them (quality 0-5).

**Steps**:
1. Read SM-2 Wikipedia (10 min): Quality 0-5 updates ease/repetitions/interval.
2. Create `srs.py`.
3. Define `update_card(card, quality, today)` function:
   - If quality < 3: repetitions = 0, interval = 1.
   - Else: Update ease = ease + (0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02)), clamp >= 1.3.
   - repetitions += 1.
   - Interval: 1 if repetitions==1, 6 if ==2, else round(interval * ease).
   - due_date = today + interval days (use datetime).
   - Return updated card dict.
   Example code: Use `from datetime import datetime, timedelta`.
4. Write tests in `test_srs.py`: Cover quality 0, 1, 3, 5; check ease clamp, repetitions reset.
5. Run tests: `pytest test_srs.py`.

**Success Check**: Function updates correctly (e.g., quality 5 increases interval).
**Advice**: SM-2 is math—don't worry if it's confusing; hardcode examples from docs first. Test with known inputs/outputs.
**Troubleshooting**: If math wrong, compare with Anki examples. Use floats carefully.

### Day 4: Basic CLI (1 hour)
**Goal**: Learn to make a simple command-line interface.

**What is argparse?** Python module to handle command-line arguments (like --front "hi").

**Steps**:
1. In `flashcards.py`, use `argparse` to create a command like `add-card` that takes `--front` and `--back` options.
2. For now, just print the inputs (no DB yet). Example: `parser = argparse.ArgumentParser(); parser.add_argument('--front'); args = parser.parse_args(); print(args.front)`.
3. Run it: `python flashcards.py add-card --front "Hello" --back "Hola"`.

**Check Success**: CLI accepts arguments and prints them.
**Advice**: Argparse handles user input—start simple, add more commands later.
**Troubleshooting**: If args not recognized, check spelling. Run without args to see help.

### Day 5: Integrate DB & CLI (1-2 hours)
**Goal**: Connect what you've learned—add cards to DB via CLI.

**Steps**:
1. Combine `test_db.py` into `db.py` with functions like `add_card`.
2. Update `flashcards.py` to call `add_card` from DB. Import db and call it in the command.
3. Test: Add a card via CLI, then query DB manually to confirm (add print in db.py).

**Check Success**: You can add cards persistently.
**Advice**: Integration is where bugs happen—test one piece at a time. Use print to verify DB saves.
**Troubleshooting**: If DB not saving, check connections are committed.

### Day 6: Study Loop (2 hours)
**Goal**: Implement the core study feature.

**What is a study loop?** Code that shows cards, asks for quality, updates with SM-2.

**Steps**:
1. Add study command in CLI (e.g., `study --deck "Spanish"`).
2. In study: Load due cards, show front, prompt for quality (`input()`), call update_card, save review.
3. Use transactions for DB writes (commit all or none).
4. Example: Loop over cards, print front, get quality, update.

**Check Success**: Study session updates cards correctly.
**Advice**: User input is tricky—use try/except for errors. Test with fake data first.
**Troubleshooting**: If loop infinite, add break. Validate quality 0-5.

### Day 7: Polish & Extras (1-2 hours)
**Goal**: Add CSV import/export, more tests, README.

**What is CSV?** Comma-separated values—simple file format for data like Excel.

**Steps**:
1. Implement CSV functions in `import_export.py` (use `import csv`).
2. Add stats command (count due cards).
3. Write README with setup and usage.
4. Run full tests.

**Check Success**: Full MVP works end-to-end.
**Advice**: Document as you go—helps learning. CSV is easy: `csv.reader()` for import.
**Troubleshooting**: If CSV fails, check file paths.

## Final Tips
- **Track Progress**: After each day, update a journal.md file with what you learned/stuck on.
- **Get Help**: For specific errors, paste the code and error message.
- **Celebrate**: Each working test is progress.
- **Next After MVP**: Add GUI with Tkinter, or package with setuptools.
- **Resources Links**:
  - Python: https://docs.python.org/3/
  - Dataclasses: https://docs.python.org/3/library/dataclasses.html
  - SQLite: https://www.sqlitetutorial.net/
  - SM-2: https://en.wikipedia.org/wiki/SuperMemo#SM-2_algorithm
  - Argparse: https://docs.python.org/3/library/argparse.html
  - Pytest: https://docs.pytest.org/

This is your first complex project—be patient. Start with Day 1 now! If something is unclear, ask about that specific part.

This is your first complex project—be patient. Start with Day 1 now!