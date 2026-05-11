````markdown name=PRD_Spaced-Repetition-Flashcards.md
# Product Requirements Document (PRD)
Project: Spaced‑Repetition Flashcards (CLI → optional GUI)  
Repository baseline: oneglitchx/learning-projects (python/mini-projects)

Date: 2025-12-23  
Author: oneglitchx (with AI assistance)

---

## 1. Summary / Purpose
Build a lightweight Spaced‑Repetition Flashcards application as a single mini‑project. Start with a Command‑Line Interface (CLI) MVP that supports creating decks and cards, persistent storage in SQLite, study sessions that record user recall (0–5), and scheduling using the SM‑2 spaced‑repetition algorithm. Provide CSV import/export and unit tests. Optionally add a simple Tkinter GUI later.

This project both produces a useful study tool and teaches several transferable technical skills: data modeling, SQL, algorithm implementation, CLI design, testing, and packaging.

---

## 2. Goals & Success Metrics
Primary goals
- Produce a functioning CLI flashcards app that schedules reviews using SM‑2.
- Persist user data locally in SQLite.
- Make the SRS algorithm implementation testable and well‑documented.

Success metrics (MVP)
- Study sessions load only "due" cards from the DB.
- After a study session, reviews (quality 0–5) update card fields (ease, repetitions, interval, next due date) using SM‑2.
- Deck import/export via CSV works round‑trip for basic fields.
- Automated tests (pytest) cover the SRS logic and basic DB operations.
- README includes setup and quickstart instructions and an example study flow.

Stretch metrics
- Basic stats/summary (due count, recent performance).
- Optional Tkinter study UI.
- Packaging (pip installable) or simple distribution.

---

## 3. Target Users
- Self (developer/learner) — to practice technical skills.
- Individual learners who want a simple, local flashcard tool.
- Anyone wanting an example of SM‑2 implementation and SQLite usage in Python.

---

## 4. Scope
MVP (must-haves)
- Local SQLite persistence (decks, cards, reviews).
- Card model with SRS fields: ease (float), repetitions (int), interval (int days), due_date (date/timestamp).
- SM‑2 implementation (pure function, fully unit tested).
- CLI with commands: create-deck, add-card, edit-card, delete-card, study, export, import.
- CSV import/export (front/back fields at minimum).
- Unit tests for SRS and DB functions (use :memory: SQLite for tests).
- Clear README and developer setup instructions.

Out of scope for MVP (later)
- Multi-user or cloud sync.
- Rich media in cards (images/audio).
- Full Anki feature parity (tags, templates, filters).
- Advanced scheduling heuristics beyond SM‑2.
- Production packaging or distribution pipelines.

---

## 5. Features & Requirements

Functional requirements
- FR1: Initialize and migrate a local SQLite DB.
- FR2: Create, list, edit, delete decks.
- FR3: Add, list, edit, delete cards within a deck.
- FR4: Start a study session which:
  - Loads due cards for a deck (due_date <= today).
  - For each card: show front, optionally show back, accept quality score 0–5.
  - Apply SM‑2 to compute new ease, repetitions, interval, and next due_date.
  - Persist review history (timestamp, card_id, quality).
- FR5: Export/import deck as CSV (front, back) — import should create a new deck or add to an existing one.
- FR6: Provide a minimal stats summary (number of due cards, recent average quality).
- FR7: Unit tests for SRS logic and DB functions.

Non‑functional requirements
- NFR1: Local-first; run offline.
- NFR2: Portable: Python 3.10+ on major OSs.
- NFR3: Simple CLI UX and clear error messages.
- NFR4: Use parameterized SQL to avoid injection.
- NFR5: SRS logic pure and isolated (no DB side effects inside algorithm).

Security & privacy
- All data stored locally by default.
- No telemetry or remote APIs.

---

## 6. Architecture & Tech Stack
Core stack (MVP)
- Language: Python 3.10+
- Persistence: SQLite via Python stdlib sqlite3
- CLI: argparse (stdlib) or Click (recommended if you want nicer UX)
- Data modeling: dataclasses
- CSV: csv module
- Testing: pytest
- Dates: Python datetime (store ISO date strings or unix timestamps in sqlite)
- Optional GUI: Tkinter (std lib)

Files (recommended)
- flashcards.py — CLI entrypoint and command wiring
- db.py — SQLite wrapper, connection and CRUD functions, init_db()
- models.py — dataclasses for Deck, Card, Review
- srs.py — SM‑2 algorithm implementation and helpers
- import_export.py — CSV import/export functions
- ui_tk.py — optional GUI study interface
- tests/test_srs.py, tests/test_db.py — pytest tests
- README.md — setup, quickstart, examples

Design notes
- Keep SM‑2 pure: a function update_card_state(card_state, quality, today) -> updated_state.
- Use a simple DB schema with normalized tables: decks, cards, reviews.
- Store dates consistently (ISO 8601 date string or integer timestamp).
- Use transactions for review writes to maintain consistency.

---

## 7. DB Schema (suggested minimal)
- decks
  - id INTEGER PRIMARY KEY
  - name TEXT NOT NULL
  - created_at TEXT
- cards
  - id INTEGER PRIMARY KEY
  - deck_id INTEGER REFERENCES decks(id)
  - front TEXT NOT NULL
  - back TEXT
  - ease REAL DEFAULT 2.5
  - repetitions INTEGER DEFAULT 0
  - interval INTEGER DEFAULT 0    -- days
  - due_date TEXT                 -- ISO date
  - created_at TEXT
- reviews
  - id INTEGER PRIMARY KEY
  - card_id INTEGER REFERENCES cards(id)
  - quality INTEGER   -- 0..5
  - timestamp TEXT
  - old_ease REAL
  - old_repetitions INTEGER
  - old_interval INTEGER

---

## 8. SM‑2 Algorithm (requirements)
- Implement standard SM‑2 behavior:
  - If quality < 3 → repetitions = 0, interval = 1, keep or reduce ease (algorithm default).
  - Else:
    - Update ease: ease = ease + (0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02))
    - Clamp ease >= 1.3
    - repetitions += 1
    - intervals:
      - if repetitions == 1 → interval = 1
      - if repetitions == 2 → interval = 6
      - else → interval = round(interval * ease)
  - Next due_date = today + interval days
- Tests must cover:
  - Fail case (quality 0 or 1) resets repetitions.
  - Quality 5 increases ease and intervals as expected.
  - Ease clamps at 1.3 minimum.

---

## 9. Milestones & Timeline (estimates)
Milestone 0 — Setup (30–60 min)
- Create repo folder, venv, install pytest, add README skeleton.

Milestone 1 — DB & Models (1–2 hours)
- Implement db.py and init_db() with schema.
- Add models.py dataclasses.

Milestone 2 — Basic CLI & Add Card (1–2 hours)
- Implement add-card and create-deck commands.
- Verify DB insert and list commands.

Milestone 3 — SM‑2 Implementation + Tests (2–3 hours)
- Implement srs.py with update_card_state().
- Write pytest tests for all core cases.

Milestone 4 — Study Loop (1–3 hours)
- Implement study command: load due cards, prompt for quality, call srs, persist review.

Milestone 5 — CSV Import/Export & Stats (1–2 hours)
- Implement import/export and show due count and recent quality average.

Milestone 6 — Polish & Documentation (1–2 hours)
- Add README instructions, examples, and a few unit tests for DB.

Optional Milestone 7 — Tkinter GUI (4–8 hours)
- Simple study UI with front/back toggles and quality buttons.

Total MVP estimate: ~8–16 hours.

---

## 10. Learning Plan (just‑in‑time)
Map of learning topics to milestones:
- Before M1: Python dataclasses, venv basics (15–60 min).
- M1: SQLite basics + parameterized queries (1–2 hours).
- M2: argparse / Click quickstart (30–60 min).
- M3: SM‑2 algorithm theory (30–60 min) + implementation.
- M4: CLI UX and atomic DB transactions.
- Testing: learn pytest basics and write tests starting at M3.

Key resources (concise)
- Python docs, dataclasses, sqlite3 module
- SQLite tutorial: https://www.sqlitetutorial.net/
- SM‑2: Wikipedia and Anki FAQ
- Argparse tutorial or Click docs
- pytest documentation

---

## 11. Risks & Mitigations
Risk: Overengineering (feature creep)
- Mitigation: Strictly follow the MVP scope and the milestone checklist.

Risk: Incorrect SM‑2 behavior causes poor scheduling
- Mitigation: Implement SRS as a pure function and cover with unit tests and example scenarios.

Risk: Bugs in DB migration or schema changes
- Mitigation: Keep schema simple; use small migrations or recreate DB during dev; add tests using :memory: SQLite.

Risk: Time blowout learning new tech
- Mitigation: Learn just‑in‑time, complete small focused tasks per session.

---

## 12. Acceptance Criteria (for MVP)
- The CLI can create a deck, add cards, and list decks/cards.
- A study session loads only cards with due_date <= today.
- After a review, the card's ease, repetitions, interval, and due_date update according to the SM‑2 algorithm.
- Reviews are persisted in reviews table with timestamps and quality values.
- CSV import/export works for simple front/back decks.
- Unit tests for srs.update_card_state() and basic DB reads/writes pass.
- README shows install steps and a sample study flow.

---

## 13. Deliverables
- Source code files: flashcards.py, db.py, models.py, srs.py, import_export.py, (optional) ui_tk.py
- tests/ with pytest tests for SRS and DB
- README.md with setup and quickstart
- Example CSV sample deck

---

## 14. Next Steps (recommended immediate actions)
Choose one; I can perform it now:
- A) Scaffold the repository with the suggested files and minimal boilerplate (db init, models, CLI skeleton).  
- B) Implement srs.py (SM‑2) plus unit tests (test_srs.py).  
- C) Implement db.py with init_db() and the schema (and a simple add_card/get_due_cards example).

State which option (A/B/C) you want and I will implement it immediately.

---

## 15. Appendix — Quick CLI usage example (MVP flow)
1. Initialize DB:
   - python flashcards.py init-db
2. Create a deck:
   - python flashcards.py create-deck "Spanish"
3. Add a card:
   - python flashcards.py add-card --deck "Spanish" --front "hola" --back "hello"
4. Study:
   - python flashcards.py study --deck "Spanish"
     - Front shown → prompt "Show answer? (Enter)"
     - Show back → prompt "Quality (0–5): "
     - Persist review and schedule next due_date

---

End of PRD.
````


Good — I’ll give a clear, prioritized learning approach tailored to the Spaced‑Repetition Flashcards project. It lists the tech/concepts you’ll meet, why each matters, how to learn it (short resources + micro‑exercises), priority and rough time estimates, and a step‑by‑step project plan you can follow. At the end I’ll suggest the immediate next action I can take for you.

1) High‑level approach (how to learn while building)
- Learn just‑in‑time. Tackle the smallest slice of the project that exercises one new concept, implement it, then move to the next concept.  
- Break work into tiny milestones (30–120 min tasks) with checks (e.g., “I can add a card”, “I can store a review”).  
- Keep the scope MVP: CLI only, SQLite persistence, SM‑2 scheduling, CSV import/export; GUI optional later.  
- Use tests for the algorithm and DB logic early — they give confidence.

2) Tech stack & core concepts (priority order)
- Python fundamentals (dataclasses, stdlib modules, packaging, venv) — must know
- SQLite (via Python’s sqlite3) — persistence
- SM‑2 spaced repetition algorithm — core app logic
- CLI design: argparse (stdlib) or Click (third‑party) — user interface
- CSV import/export (csv module) — deck interchange
- Unit testing with pytest — correctness (especially SRS)
- Basic SQL queries and schema design — DB work
- Optional / later: Tkinter GUI, packaging with setuptools, type hints, logging

3) For each concept: what to learn, short resources, micro‑exercises

A. Python fundamentals (dataclasses, modules, venv)
- Why: base language features used everywhere.
- Learn: Python 3.10+ basics, dataclasses for models, virtualenv/venv.
- Resources:
  - Docs: https://docs.python.org/3/
  - Dataclasses: https://docs.python.org/3/library/dataclasses.html
  - venv: https://docs.python.org/3/library/venv.html
- Exercises (15–60 min each):
  - Create a dataclass Card with fields (id, front, back, ease, interval, repetitions, due_date).
  - Make a venv and pip install pytest; run a trivial test.

Est. time: 2–4 hours if new to Python fundamentals.

B. SQLite with Python (sqlite3)
- Why: lightweight built‑in DB, perfect for local data.
- Learn: basic SQL (CREATE, SELECT, INSERT, UPDATE), sqlite3 usage, parameterized queries, transactions.
- Resources:
  - sqlite3 docs: https://docs.python.org/3/library/sqlite3.html
  - SQLite tutorial: https://www.sqlitetutorial.net/
- Exercises:
  - Create a DB schema: decks, cards, reviews tables.
  - Write a small db.py with connect(), init_db() and functions add_card(deck_id,...), get_due_cards(date).

Est. time: 2–6 hours.

C. SM‑2 algorithm (spaced repetition scheduling)
- Why: core algorithm to compute next review date based on recall quality.
- Learn: how quality (0–5) updates ease, repetitions, interval; calculate next due date.
- Resources:
  - Wikipedia: https://en.wikipedia.org/wiki/SuperMemo#SM-2_algorithm
  - Anki explanation: https://faqs.ankiweb.net/what-spaced-repetition-system-does-anki-use.html
- Exercises:
  - Implement an srs.py function: update_card(card, quality, today) → updated fields and next_due.
  - Write unit tests covering edge cases (fail, low quality, high quality).

Est. time: 2–4 hours to implement + tests.

D. CLI (argparse or Click)
- Why: initial user interface.
- Learn: build commands (create-deck, add-card, study), subcommands, prompts.
- Resources:
  - Argparse: https://docs.python.org/3/library/argparse.html
  - Click: https://click.palletsprojects.com/
  - Tutorial: https://realpython.com/command-line-interfaces-python-argparse/
- Exercises:
  - Implement a simple CLI command add-card that prompts front/back and inserts into DB.
  - Implement study command that loads due cards, shows card front, asks for score, calls srs.update.

Est. time: 1–3 hours.

E. CSV import/export (csv module)
- Why: share decks, seed data.
- Learn: Python csv module basics, encoding considerations.
- Resources: https://docs.python.org/3/library/csv.html
- Exercises:
  - Implement export_deck(deck_id, path) and import_deck(path).

Est. time: 1–2 hours.

F. Testing with pytest
- Why: prevent regressions and validate SRS logic.
- Learn: write unit tests, fixtures, simple DB test with temp DB.
- Resources: https://docs.pytest.org/
- Exercises:
  - Write tests for srs.update_card() covering quality 0–5.
  - Write tests for db functions (use :memory: sqlite).

Est. time: 1–3 hours.

G. Optional: Tkinter GUI
- Why: nicer UX later.
- Learn: basic Tkinter window, buttons, text widgets.
- Resources: https://realpython.com/python-gui-tkinter/
- Exercises:
  - Make a simple study window showing front and a “Show answer” button.

Est. time: 4–8 hours.

4) Minimal project roadmap (milestones + time estimates)
- Milestone 0 — Setup: repo, venv, precommit, basic README (30–60 min)
- M1 — DB schema + db.py (init_db, add/get) (1–2 hours)
- M2 — Card dataclass + add-card CLI (1–2 hours)
- M3 — srs.py implement SM‑2 + unit tests (2–3 hours)
- M4 — study CLI loop that loads due cards and records reviews (1–3 hours)
- M5 — CSV import/export and some more tests (1–2 hours)
- M6 — polish, stats (due count, streaks), README and examples (1–3 hours)
Total MVP: ~8–16 hours spread across several days.

5) Recommended learning sequence (what to learn when)
- Day 1: Python dataclasses + venv + simple dataclass test; set up repo.
- Day 2: SQLite basics + create DB schema + db.py functions.
- Day 3: Implement card add & CLI command; test DB insert/get.
- Day 4: Learn SM‑2, implement srs.update, write tests.
- Day 5: Implement study loop; refine UX; add import/export.
- Optional followups: add tests, add GUI, package project.

6) Quick starter commands & tips
- Create venv and install pytest:
  - python -m venv .venv
  - source .venv/bin/activate (or .\.venv\Scripts\activate on Windows)
  - python -m pip install --upgrade pip
  - python -m pip install pytest click  # if using click
- Use sqlite :memory: for fast tests, and a repo file for development.
- Store dates as ISO strings (YYYY-MM-DD) or unix timestamps; sqlite has date functions.

7) Common pitfalls & how to avoid them
- Don’t overengineer schema. Keep fields minimal: ease (float), repetitions (int), interval (int days), due_date (date).
- Beware SQL injection — always use parameterized queries (DBAPI ? placeholders).
- Keep SRS pure and testable (no DB side effects inside algorithm).
- Use small incremental commits and tests.

8) Learning resources (summary links)
- Python official docs: https://docs.python.org/3/
- Dataclasses: https://docs.python.org/3/library/dataclasses.html
- sqlite3 + tutorial: https://docs.python.org/3/library/sqlite3.html and https://www.sqlitetutorial.net/
- SM‑2 algorithm: https://en.wikipedia.org/wiki/SuperMemo#SM-2_algorithm and https://faqs.ankiweb.net/what-spaced-repetition-system-does-anki-use.html
- Argparse tutorial: https://realpython.com/command-line-interfaces-python-argparse/
- Click docs: https://click.palletsprojects.com/
- pytest: https://docs.pytest.org/
- CSV: https://docs.python.org/3/library/csv.html
- Tkinter (optional): https://realpython.com/python-gui-tkinter/

9) What I can do now (pick one)
- Scaffold the repo with the files listed earlier (db.py, models.py, srs.py, flashcards.py CLI) and minimal boilerplate so you can run the first milestone.  
- Or implement srs.py (SM‑2) plus unit tests you can run immediately.  
- Or create db.py with init_db() and example schema.

Which one would you like me to do right now? I’ll scaffold or implement it immediately.