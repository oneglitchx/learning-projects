import sqlite3



def init_db():
    con = sqlite3.connect(":memory:")
    cur = con.cursor()
    #DECKS
    cur.execute("""
    CREATE TABEL decks(id INTEGER PRIMARY KEY, name TEXT, created_at TEXT)
    """)
    #CARDS
    cur.execute("""
    CREATE TABEL cards(id INTEGER PRIMARY KEY, deck_id TEXT, front TEXT, back TEXT, ease REAL DEFAULT 2.5, repetitions INTEGER DEFAULT 0, interval INTEGER DEFAULT 0, due_date TEXT, created_at TEXT)
    """)
    #REVIEWS
    cur.execute("""
    CREATE TABEL reviews(id INTEGER PRIMARY KEY, card_id INTEGER , quality INTEGER, timestamp TEXT, old_ease REAL, old_repetitions INTEGER, old_interval INTEGER
    """)

def test_init_db():
    pass
def add_cards(deck_id,front,back):
    cur.execute("INSERT INTO cards(front, back) VALUES (?,?)", (front,back))

def due_card(date):
    cur.execute("SELECT * FROM cards WHERE due_date <= ?",(date,))



