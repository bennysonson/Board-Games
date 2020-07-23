Implementation of various board games ran on the command line with AI

## Tic Tac Toe
The goal is to get 3 in a row! At level 1, the AI places moves randomly. At level 99, the AI uses the minimax algorithm to perform the most optimal moves. During the AIs turn, the minimax algorithm recursively plays out every sequence of moves and assigns a value based on the results of each possible move. Assuming a perfectly optimal opponent, the game will always tie whether the AI goes first or second.

![Sample 1](BoardGames/images/TicTacToeExample.png?raw=true "Title")

## Connect 4
The goal is to get 4 in a row! There is gravity now. At level 1, the AI places moves randomly. At level 77, the AI uses the minimax algorithm again to perform the most optimal moves. Because the Connect 4 board is much bigger than the Tic Tac Toe board, the same minimax algorithm takes too long to compute. Several heuristics are used to improve the search. Alpha beta pruning is the concept of stopping further search once a move is proven to be worse than a previous one. In conjunction with this, minimax moves are played out in an optimal order (the middle columns first then outer), since more winning combinations are possible from pieces played near the middle. Even with these heuristics, the AI takes too long to move, especially during the starting turns, so the AI is set to only look between 9 and 11 moves into the future. This results in a sub-optimal AI, but is still very hard to beat.

![Sample 2](BoardGames/images/Connect4Example.png?raw=true "Title")

**TODO**
* GUI for games
* 100% Unbeatable connect 4 AI
