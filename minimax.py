import pprint
from games.village import village
from games.nim import nim

def play(game):
    g = game()
    print(game.help_text)
    print()
    while not g.over():
        for name, value in g.__dict__.items():
            print(name, ": ", value)

        move = []
        for explanation, process_move in game.move_explanations:
            move.append(process_move(input(explanation + " ")))
            
        print(move)

        g = g.get_new_state(move)
        move, _ = minimax(g, ply=game.ply)
        print("I will do ", move)
        g = g.get_new_state(move)


def minimax(game, move=None, ply=5):
    if game.over() or ply == 0:
        return move, game.score()

    moves = []

    for move in game.available_moves():
        possible_game = game.get_new_state(move)
        moves.append((move, minimax(possible_game, move=move, ply=ply-1)[1]))

    if game.active_turn == "player":
        best_move, score = max(moves, key=lambda x: x[1])
        return best_move, score
    else:
        best_move, score = min(moves, key=lambda x: x[1])
        return best_move, score

if __name__ == "__main__":
    #play(village)
    play(nim)
