import random

class Board:

    def __init__(self):
        self.board = self.getBoard()

    def getBoard(self):
        board = [ 
            list(".BBBBBB."),
            list("W......W"),
            list("W......W"),
            list("W......W"),
            list("W......W"),
            list("W......W"),
            list("W......W"),
            list(".BBBBBB.")
        ]
        return board
    
    def printBoard(self):
        print("")
        head = "  "
        header = [0, 1, 2, 3, 4, 5, 6, 7]
        idx = 0
        for number in header:
            head += str(number) + " "
        print(head)
        for row in self.board:
            row_print = "" + str(idx) + " "
            idx += 1
            for element in row:
                row_print += str(element) + " "
            print(row_print)
        print("")


    def getSimulationboard(self):  #Auxilary funtion to test 
        board = [ 
            list("......W."),
            list("........"),
            list("........"),            
            list("B......."),
            list("........"),
            list("........"),
            list("B......."),
            list(".W......")
        ]

        return board
    def __toTuple__(self):
        return tuple(tuple(row) for row in self.board)  


# MOVES, first we get the ammount of moves a piece can make given the coordenates 
# getMoveCount is a helper function that returns the ammount of squares a piece can make given the coordenates and direction
# getDirectionalMove returns a dicitonary of the moves a piece can makes given the coordenates
# get{DIRECTIONAL}MoveEnd returns the coordenates of the end point if the player were to make the move of the piece. it does not update the board


    def getMoveCount(self, y, x, dy, dx) -> int:
        count = 0
        row, col = y, x

        while 0 <= row < 8 and 0 <= col < 8:
            if self.board[row][col] != ".":
                count += 1
            row += dy
            col += dx

        return count

    def getDirectionalMove(self, start) -> dict[str]:
        
        y, x = start

        horizontal = self.getMoveCount(y, x, 0, 1) + self.getMoveCount(y, x, 0, -1) - 1
        vertical = self.getMoveCount(y, x, 1, 0) + self.getMoveCount(y, x, -1, 0) - 1
        diagonal1 = self.getMoveCount(y, x, 1, 1) + self.getMoveCount(y, x, -1, -1) - 1
        diagonal2 = self.getMoveCount(y, x, 1, -1) + self.getMoveCount(y, x, -1, 1) - 1

        return {"H": horizontal, "V": vertical, "D1": diagonal1, "D2": diagonal2}

    def isLegalMove(self, start, end, player_symbol) -> bool:
        y, x = start
        new_y, new_x = end
        piece = self.board[y][x] 

        if piece == "." or piece != player_symbol:
            return False  #Wrong piece or wrong player turn
        
        # Calucalte direction of movement
        
        dy = new_y - y
        dx = new_x - x

        # Normalize the directoin to -1, 0, or 1 (vetor unitario)
        # checks if the direction mathches the number of moves available
        move_counts = self.getDirectionalMove(start)

        if dy == 0 and abs(new_x - x) == move_counts["H"]:
            pass
        elif dx == 0 and abs(new_y - y) == move_counts["V"]:
            pass
        elif dx == dy and abs(new_x - x) == move_counts["D1"] and abs(new_y - y) == move_counts["D1"]:
            pass
        elif dx == -dy and abs(new_x - x) == move_counts["D2"] and abs(new_y - y) == move_counts["D2"]:
            pass
        else: 
            return False
        
        if dy != 0:
            dy //= abs(dy)
        if dx != 0:
            dx //= abs(dx)

        # Make sure piece is not blocked by enemy piece, ensure the capture of a piece
        row, col = y, x
        steps = max(abs(new_y - y), abs(new_x - x))

        for i in range(1, steps):
            row += dy
            col += dx

            if self.board[row][col] not in [".", piece]:
                return False
            
        if self.board[new_y][new_x] == piece:
            return False
        
        return True

    def getHorizontalMoveEnd(self, start, direction) -> tuple:
        y, x = start
        move_count = self.getDirectionalMove(start)["H"]
        new_x = x + (move_count * direction)

        if 0 <= new_x < 8:
            # Check if path is clear
            dx = direction
            col = x + dx
            while col != new_x:
                if self.board[y][col] not in [".", self.board[y][x]]:
                    return None
                col += dx
            return (y, new_x)
        return None

    def getVerticalMoveEnd(self, start, direction) -> tuple:
        y, x = start
        move_count = self.getDirectionalMove(start)["V"]
        new_y = y + (move_count * direction)

        if 0 <= new_y < 8:
            # Check if path is clear
            dy = direction
            row = y + dy
            while row != new_y:
                if self.board[row][x] not in [".", self.board[y][x]]:
                    return None
                row += dy
            return (new_y, x)
        return None

    def getDiagonal1MoveEnd(self, start, direction) -> tuple:
        y, x = start
        move_count = self.getDirectionalMove(start)["D1"]
        new_y = y + (move_count * direction)
        new_x = x + (move_count * direction)

        if 0 <= new_y < 8 and 0 <= new_x < 8:
            # Check if path is clear
            dy = dx = direction
            row, col = y + dy, x + dx
            while row != new_y:  # Could also check col != new_x
                if self.board[row][col] not in [".", self.board[y][x]]:
                    return None
                row += dy
                col += dx
            return (new_y, new_x)
        return None

    def getDiagonal2MoveEnd(self, start, direction) -> tuple:
        y, x = start
        move_count = self.getDirectionalMove(start)["D2"]
        new_y = y + (move_count * direction)
        new_x = x - (move_count * direction)

        if 0 <= new_y < 8 and 0 <= new_x < 8:
            # Check if path is clear
            dy = direction
            dx = -direction
            row, col = y + dy, x + dx
            while row != new_y:  # Could also check col != new_x
                if self.board[row][col] not in [".", self.board[y][x]]:
                    return None
                row += dy
                col += dx
            return (new_y, new_x)
        return None

    def makeMove(self, move, player_symbol):
        start, end = move
        y, x = start 
        new_y, new_x = end

        if self.isLegalMove(start, end, player_symbol):
            # Apply the move to the new copy of the board
            self.board[new_y][new_x] = player_symbol
            self.board[y][x] = "."  # Clear the old position

    def getAllPossibleMoves(self, player_symbol) -> list:
        possibleMoves = []

        for row in range(8):
            for col in range(8):
                if self.board[row][col] == player_symbol:
                    start = (row, col)
                    possibleEnds = [
                        self.getHorizontalMoveEnd(start, 1),
                        self.getHorizontalMoveEnd(start, -1),
                        self.getVerticalMoveEnd(start, 1),
                        self.getVerticalMoveEnd(start, -1),
                        self.getDiagonal1MoveEnd(start, 1),
                        self.getDiagonal1MoveEnd(start, -1),
                        self.getDiagonal2MoveEnd(start, 1),
                        self.getDiagonal2MoveEnd(start, -1)
                        ]

                    for end in possibleEnds:
                        if end is not None and self.isLegalMove(start, end, player_symbol):
                            possibleMoves.append((start, end))
        random.shuffle(possibleMoves) #Shuffle the moves for minimax to make more random moves while pruning

        return possibleMoves
    

# WIN CON

    def count_pieces(self, player_symbol) -> int:
        count = 0
        for row in self.board:
            count += row.count(player_symbol)
        return count

    def _flood_fill(self, start, player_symbol, visited):
        y, x = start # unpack start tuple
        
        # Check if (y, x) is out of bounds or already visited
        if not (0 <= y < 8 and 0 <= x < 8) or (y, x) in visited or self.board[y][x] != player_symbol:
            return

        visited.add((y, x))  # Mark as visited
        
        # Check all 8 directions
        directions = [
            (-1,-1), (-1,0), (-1,1),
            (0,-1),          (0,1),
            (1,-1),  (1,0),  (1,1)
        ]
        
        for dy, dx in directions:
            self._flood_fill((y + dy, x + dx), player_symbol, visited)

    def are_all_pieces_connected(self, player_symbol) -> bool:
        start = None

        for i in range(8):
            for j in range(8):
               if self.board[i][j] == player_symbol:
                    start = i, j
                    break
               
            if start is not None:
                break
        
        visited = set()
        self._flood_fill(start, player_symbol, visited)

        # If all pieces were reached, they're connected
        return len(visited) == self.count_pieces(player_symbol)

    def isGameOver(self) -> bool:
        # Check one piece remaining win condition
        black_count = self.count_pieces("B")
        white_count = self.count_pieces("W")
        
        if black_count == 1 or white_count == 1:
            return True

        # Check connected pieces win condition
        black_connected = self.are_all_pieces_connected("B")
        white_connected = self.are_all_pieces_connected("W")

        return black_connected or white_connected

    def getWinner(self) -> str:
        black_count = self.count_pieces("B")
        white_count = self.count_pieces("W")

            # One piece remaining win condition
        if black_count == 1:
            return "B"
        if white_count == 1:
            return "W"

            # Connected pieces win condition
        black_connected = self.are_all_pieces_connected("B")
        white_connected = self.are_all_pieces_connected("W")

        if black_connected and white_connected:
            return "." # Draw
        if black_connected:
            return "B"
        if white_connected:
            return "w"

        return None  # Game not over
    
# EVAL

    def largest_connected_group(self, player_symbol) -> int:
        visited = set()  # Tracks visited positions
        max_group_size = 0  # Stores the largest found group

        def bfs(start_y, start_x):
            """Breadth-First Search to count connected pieces."""
            queue = [(start_y, start_x)]
            visited.add((start_y, start_x))
            count = 1  # Current group size

            # Possible movement directions in LOA (8 directions)
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]

            while queue:
                x, y = queue.pop(0)  # FIFO queue for BFS
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < 8 and 0 <= ny < 8 and (ny, nx) not in visited and self.board[ny][nx] == player_symbol:
                        visited.add((ny, nx))
                        queue.append((ny, nx))
                        count += 1  # Increase group size
            return count

        # Scan the board and find the largest connected component
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == player_symbol and (i, j) not in visited:
                    max_group_size = max(max_group_size, bfs(i, j))

        return max_group_size  # Return the largest connected component





"""
    def pieces_in_opening_position(self, symbol):
        count = 0
        if symbol == "B":
            for i in range(8):
                if self.board[0][i] == "B":
                    count += 1
                if self.board[7][i] == "B":
                    count += 5
        else:
            for j in range(8):
                if self.board[j][0] == "W":
                    count += 1
                if self.board[j][7] == "W":
                    count += 5
        return count
    
    def isolated_pieces(self, player_symbol) -> int:
        isolated_count = 0
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),          (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]
        
        # Iterate over the board to check each piece of the player
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == player_symbol:
                    # Check if there are any adjacent pieces of the same player
                    is_isolated = True
                    for dy, dx in directions:
                        ni, nj = i + dy, j + dx
                        # Make sure the neighbor is within bounds and is of the same player
                        if 0 <= ni < 8 and 0 <= nj < 8 and self.board[ni][nj] == player_symbol:
                            is_isolated = False  # Found a connected neighbor
                            break  # No need to check further directions
                    
                    if is_isolated:
                        isolated_count += 1  # Increment count if the piece is isolated

        return isolated_count

    def mid_board_presence(self, symbol): 
        count = 0
        for i in range(2, 6):
            for j in range(2, 6):
                if self.board[i][j] == symbol:
                    if i in [3, 4] and j in [3, 4]:
                        count += 3
                    else:
                        count += 1
        return count
""" 
    