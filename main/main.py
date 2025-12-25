from model.Simulator import Simulator
from model.Deck import Deck

def main() -> None:
    deck = Deck()
    deck.shuffle()

    hand = deck.deal(2)

    print("hand:")
    for card in hand:
        print(card.display())

    equity = Simulator.simulate_equity(hand)
    print(f"equity: {equity}")

if __name__ == "__main__":
    main()