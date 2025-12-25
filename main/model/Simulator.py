from collections.abc import Iterator
from .Evaluator import Evaluator
from .Card import Card
from .Deck import Deck

class Simulator:
    @staticmethod
    def simulate_equity(hand: list[Card], 
                        board: list[Card] | None = None,
                        players: int = 2, 
                        trials: int = 100000) -> Iterator[tuple[int, float, float, float]]:
        assert 2 <= players <= 6
        assert len(hand) == 2

        wins = 0
        ties = 0

        if board is None:
            board = []

        missing_board = 5 - len(board)
        assert 0 <= missing_board <= 5

        equity_sum = 0.0

        for trial in range(trials):
            assert len(set((c.rank, c.suit) for c in hand + board)) == len(hand + board)
            
            deck = Deck()
            deck.shuffle()
            deck.removeCards(hand + board)

            villains = []
            for num in range(players - 1):
                villains.append([deck.draw(), deck.draw()])

            rest_of_board = deck.deal(missing_board)

            full_board = board + rest_of_board

            hero_eval = Evaluator.mapper(Evaluator.best_hand(hand + full_board))
            
            villain_evals = []
            for v in villains:
                best = Evaluator.best_hand(v + full_board)
                villain_evals.append(Evaluator.mapper(best))

            all_evals = [hero_eval] + villain_evals
            best_eval = max(all_evals)

            if hero_eval == best_eval:
                tied = sum(1 for e in all_evals if e == best_eval)
                equity_sum += 1.0 / tied

            yield trial + 1, equity_sum / (trial + 1)