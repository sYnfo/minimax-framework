class nim():
    help_text = "Nim is a two player game where the players " \
                "take turns removing elements from heaps, the " \
                "player to play last loses"

    move_explanations = (("Which heap to take from?", int),
                         ("How much to take?", int))

    ply = 5

    def __init__(self, heaps=[3, 4, 5], active_turn="player"):
        self.heaps = heaps
        self.active_turn = active_turn

    def over(self):
        return not any(self.heaps)

    def available_moves(self):
        """ Move is a tuple (heap_index, take_away) where
            heap_index is number of the heap from which to
            take pieces and take_away is a number of pieces
            to take away"""

        heaps = range(len(self.heaps))
        return [(h, take) for h in range(len(self.heaps))
                          for take in range(1, self.heaps[h] + 1)]

    def get_new_state(self, move):
        heap_index, take = move

        if self.heaps[heap_index] < take:
            raise BadMoveException("Can't take more that how much there is")

        new_heaps = self.heaps[:]
        new_heaps[move[0]] -= move[1]
        new_player = "player" if self.active_turn == "opponent" else "opponent"

        return nim(heaps=new_heaps, active_turn=new_player)

    def score(self):
        if not self.over():
            return 0
        if self.active_turn == "player":
            return 10
        else:
            return -10
