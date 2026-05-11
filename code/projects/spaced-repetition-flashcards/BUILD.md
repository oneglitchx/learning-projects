# Build Plan: Spaced-Repetition Flashcards

## Current State (assessed)

| File | Status | Issues |
|------|--------|--------|
| `models.py` | Done | Passes test. Typo: `repetations` -> `repetitions` |
| `db.py` | Broken | `TABEL` -> `TABLE`, `FORM` -> `FROM`, missing `)` in reviews table, `fetchall()` needs `cur.`, connection not shared between functions, uses `:memory:` (needs file-based for real use) |
| `venv/` | Ready | pytest installed |

## Goal

A working CLI app: `python flashcards.py` can create decks, add cards, study them with SM-2 scheduling, and the data persists in a file.

## The Sessions

Each session = 30-60 min. If you hit something new, open `code/playground.py` first, poke it for 10 min, then use it.

### Session 1: Fix db.py

Bugs to fix:
- `TABEL` -> `TABLE` (3 times)
- `FORM` -> `FROM`
- Add missing `)` to reviews table
- `fetchall()` -> `cur.fetchall()`
- `add_cards` and `due_card` need `con.commit()` and to return data
- Switch `:memory:` to a file `flashcards.db`

File structure: `init_db()` creates tables if not exist. Other functions open their own connection or accept one.

**Done when:** Running `python db.py` prints existing table names without errors.

### Session 2: Create srs.py

Pure function. No DB. Input → output only.

```python
def update_card(card, quality, today):
    """Takes card dict, quality (0-5), today string. Returns updated card dict."""
```

Logic:
- quality < 3 → reset (repetitions=0, interval=1)
- quality >= 3 → ease += 0.1 - (5-quality) * (0.08 + (5-quality) * 0.02), clamp ease >= 1.3, increment repetitions, interval = 1/6/round(interval*ease)
- due_date = today + interval days

**Done when:** You can call it from `playground.py` with test values and get correct output.

### Session 3: Create flashcards.py CLI

Use `argparse`. Commands:
- `python flashcards.py create-deck "Spanish"`
- `python flashcards.py add-card --deck "Spanish" --front "hola" --back "hello"`
- `python flashcards.py study --deck "Spanish"`

Start with just the CLI skeleton (print the args, do nothing else).

**Done when:** Running each command prints what you expect.

### Session 4: Wire CLI to db.py + srs.py

- `create-deck` → calls db to insert deck
- `add-card` → calls db to insert card
- `study` → loads due cards, shows front, asks quality, calls srs.update_card, saves to db

**Done when:** You can run through a full cycle: create deck → add card → study → see next review scheduled.

### Session 5: Polish

- Add `stats` command (count due cards)
- Error handling (bad deck name, invalid quality)
- Verify it works on a fresh start

**Done when:** The project is usable without you. Someone else could clone and run it.

## When You Hit Something Unknown

1. Stop. Don't panic.
2. Open `code/playground.py`
3. Search "[thing] python example" or ask AI
4. Write 3 working lines
5. Close playground. Use it in the project.

That's it. That's the entire skill you're learning here.

## Extras (only if the MVP works first)

- Export/import decks as CSV
- Tests with pytest
- Stats summary
- Tkinter GUI
