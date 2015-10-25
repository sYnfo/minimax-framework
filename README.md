# minimax

Framework for two-player CLI games that gives you a simple minimax AI for
'free'.

## Usage

To use the framework you have to create a class representing the game you want
to implement, that includes the following methods:

### over

Returns True iff the game is over, False otherwise.

### available_moves

Returns an iterator with all the valid moves from the current game state.

### get_new_state

argument: move

Returns an instance of the game class with the game state modified according
to the move.

### score

Returns a numerical representation of how the current player is doing. Used by
the minimax algorithm.

### display (optional)

For example implementation of couple games see the ```games``` folder.

### variable: help_text

### variable: move_explanation

### variable: ply
