from dataclasses import dataclass

@dataclass
class Card:
    id: int
    front: str
    back: str
    ease: float = 2.5
    repetations: int = 0
    interval: int = 0
    due_date: str = ""

def test_card_creation():
    card = Card(1,"Mayank","Moon")
    assert card.id == 1
    assert card.front == "Mayank"
    assert card.back == "Moon"
    assert card.back != "Monkey"
    
    
# card = Card(1,"Mayank","Moon")
# print(card)

