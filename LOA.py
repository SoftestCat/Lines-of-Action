from MiniMax_Node import MiniMaxNode
from Board import Board
import time
import random

def get_human_move(game, current_player):
    while True:
        try:
            print("Enter move (format: start row start col end row end col): ")
            move = input().strip().split()
            
            if len(move) != 4:
                print("Invalid input! Please enter 4 numbers.")
                continue
                
            start_row, start_col, end_row, end_col = map(int, move)
            start = (start_row, start_col)
            end = (end_row, end_col)
            
            if game.isLegalMove(start, end, current_player):
                return start, end
            else:
                print("Illegal move! Try again.")
                
        except ValueError:
            print("Invalid input! Please enter numbers only.")

def get_difficulty():
    print("Please select a dificulty for Black")
    print("1) Easy")
    print("2) Normal")
    print("3) Hard")

    BuserInput = int(input())

    if not (0 < BuserInput <= 3):
        print("Invalid input! Please try again")
        return
    
    if BuserInput == 3:
        BuserInput += 1
    Bdepth = BuserInput

    print("Please select a dificulty for White")
    print("1) Easy")
    print("2) Normal")
    print("3) Hard")

    WuserInput = int(input())

    if not (0 < WuserInput <= 3):
        print("Invalid input! Please try again")
        return
    
    if WuserInput == 3:
        WuserInput += 1

    Wdepth = WuserInput

    return Wdepth, Bdepth

def getAIdifficulty():
    print("Please select a dificulty for the AI")
    print("1) Easy")
    print("2) Normal")
    print("3) Hard")

    userInput = int(input())

    if not (0 < userInput <= 3):
        print("Invalid input! Please try again")
        return
    
    if userInput != 1:
        userInput += 1
    depth = userInput

    return depth

def human_vs_ai():
    game = Board()
    human = True
    ai = not human
    Human = "B" 
    Ai = "W"
    depth = getAIdifficulty()

    while not game.isGameOver():
        ai = not human
        game.printBoard()
        symbol = Human if human else Ai
        print(f"Player {symbol}'s turn")

        if human:
            start, end = get_human_move(game, Human)
        else:
            print("AI thinking...")
            node = MiniMaxNode(game, True)

            start_time = time.time()
            bestMove = node.minimax_run(True, depth)
            start, end = bestMove
            end_time = time.time()
            print(f"Move: {start} -> {end}")
            print(f"Time taken: {end_time - start_time:.2f} seconds")
            
        game.makeMove((start, end), symbol)
        human = True if ai else False

    # Game over
    game.printBoard()
    winner = game.getWinner()
    print(f"Game Over! Winner: {'Black (Human)' if winner == 'B' else 'White (AI)'}")

def ai_vs_ai():
    game = Board()
    # starting player is Black and Black is NOT MAXIMIXING PLAYER
    maximizingPlayer = False
    symbol = "B"
    Wdepth, Bdepth = get_difficulty()

    while not game.isGameOver():
        game.printBoard()
        symbol = "W" if maximizingPlayer else "B"
        print(f"Player {symbol}'s turn")
        
        node = MiniMaxNode(game, maximizingPlayer)
        depth = Wdepth if maximizingPlayer else Bdepth

        start_time = time.time()
        bestMove = node.minimax_run(maximizingPlayer, depth)
        start, end = bestMove
        end_time = time.time()
        print(f"Move: {start} -> {end}")
        print(f"Time taken: {end_time - start_time:.2f} seconds")

        game.makeMove((start, end), symbol)
        maximizingPlayer = False if maximizingPlayer else True

        time.sleep(0.5)

    game.printBoard() # Game Over
    winner = game.getWinner()
    print(f"Game Over! Winner: Player {winner}")
           
def ai_vs_random():
    game = Board()
    # starting player is Black and Black is NOT MAXIMIXING PLAYER
    maximizingPlayer = False
    symbol = "B"
    depth = getAIdifficulty()

    while not game.isGameOver():
        game.printBoard()
        symbol = "W" if maximizingPlayer else "B"
        print(f"Player {symbol}'s turn")
        start_time = time.time()

        if maximizingPlayer:
            possibleMoves = game.getAllPossibleMoves(symbol)
            move = random.choice(possibleMoves)
            start, end = move
        else:
            node = MiniMaxNode(game, maximizingPlayer)
            bestMove = node.minimax_run(maximizingPlayer, depth)
            start, end = bestMove

        end_time = time.time()    
        print(f"Move: {start} -> {end}")
        print(f"Time taken: {end_time - start_time:.2f} seconds")
        game.makeMove((start, end), symbol)
        maximizingPlayer = False if maximizingPlayer else True
        time.sleep(0.5)

    game.printBoard() # Game Over
    winner = game.getWinner()
    print(f"Game Over! Winner: Player {winner}")


print("Choose test mode:")
print("1. Human vs AI")
print("2. AI vs AI")
print("3. AI vs Random")

choice = input("Enter choice: ")

if choice == "1":
    human_vs_ai()
elif choice == "2":
    ai_vs_ai()
elif choice == "3":
    ai_vs_random()
else:
    print("Invalid choice!") 
    