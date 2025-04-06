from copy import deepcopy


class MiniMaxNode: 

    def __init__(self, board, maximizingPlayer, parent=None, move=tuple) -> None:
        self.board = board
        self.maximizingPlayer = maximizingPlayer
        self.move = move
        self.parent = parent
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)
        child_node.parent = self

    def get_children(self, maximizingPlayer):
        currentBoard = deepcopy(self.board)
        opponent = "W" if maximizingPlayer else "B"

        for move in currentBoard.getAllPossibleMoves(maximizingPlayer):
            newNode = MiniMaxNode(currentBoard.makeMove(move), opponent, self, move)
            self.add_child(newNode)
        
    def evaluate(self, maximizingPlayer):  #SCORING TOO COMPLICATED

        score = 0

        # reward winning and punishing loss
        if self.board.are_all_pieces_connected("B"):     
            score -= 100
        elif self.board.are_all_pieces_connected("W"):
            score += 100                          
                                                            

        # simple eval heuristic
        score += (self.board.largest_connected_group("W") - self.board.largest_connected_group("B")) 

        return score



    def minimax(self, depth, alpha, beta, maximizingPlayer) -> int:
        if depth == 0 or self.board.isGameOver():
            return self.evaluate(maximizingPlayer), None  # Return (score, no move)

        best_move = None
        symbol = "W" if maximizingPlayer else "B"
        possibleMoves = self.board.getAllPossibleMoves(symbol)

        if maximizingPlayer:
            maxEval = float("-inf")
            for move in possibleMoves:  # Generate moves dynamically
                newBoard = deepcopy(self.board)
                newBoard.makeMove(move, symbol)
                child = MiniMaxNode(newBoard, False, self, move)  # Create a child node

                eval, _ = child.minimax(depth - 1, alpha, beta, False)  # Get score only

                if eval > maxEval:
                    maxEval = eval
                    best_move = move  # Store best move

                alpha = max(alpha, eval)
                if beta <= alpha:  # Alpha-beta pruning
                    break
            return maxEval, best_move  # Return best evaluation and move

        else:
            minEval = float("inf")
            for move in possibleMoves:  # Generate moves dynamically
                newBoard = deepcopy(self.board)   
                newBoard.makeMove(move, symbol)                
                child = MiniMaxNode(newBoard, True, self, move)  # Create a child node

                eval, _ = child.minimax(depth - 1, alpha, beta, True)  # Get score only
                if eval < minEval:
                    minEval = eval
                    best_move = move  # Store best move

                beta = min(beta, eval)
                if beta <= alpha:  # Alpha-beta pruning
                    break
            return minEval, best_move  # Return best evaluation and move


    def minimax_run(self, maximizingPlayer, max_depth=4) -> tuple:
        score, best_next_move = self.minimax(max_depth, float("-inf"), float("inf"), maximizingPlayer)  # Pass depth and maximizingPlayer flag here
        return best_next_move


