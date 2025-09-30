import random

def blackjack():
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] 
    hand = random.sample(cards, 2)
    total = sum(hand)
    print(f"Your cards: {hand}, Total: {total}")

# Start game
blackjack()
