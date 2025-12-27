from model.Simulator import Simulator
from model.Deck import Deck
from model.Card import Card
from model.Suit import Suit
from model.Rank import Rank

def main() -> None:
    deck = Deck()
    deck.shuffle()
    board = []

    #hand = deck.deal(2)
    hand = [Card(14,Suit.SPADES), Card(12, Suit.HEARTS)]
    #board = deck.deal(3)
    #board = [Card(8,Suit.SPADES), Card(8,Suit.HEARTS), Card(8,Suit.DIAMONDS)]

    print("hand:")
    for card in hand:
        print(card.display())
    print("board:")
    for card in board:
        print(card.display())

    for trials, equity in Simulator.simulate_equity(hand, board, 3, 100000):
        if trials % 500 == 0:
            print(
                f"\rtrials:{trials:6d} | "
                f"equity={equity:.4f}",
                end="",
                flush=True
            )
    print()

    for trials, equity in Simulator.simulate_equity_in_range(hand, board, 3, [], 100000):
        if trials % 500 == 0:
            print(
                f"\rtrials:{trials:6d} | "
                f"equity={equity:.4f}",
                end="",
                flush=True
            )
    print()

if __name__ == "__main__":
    main()