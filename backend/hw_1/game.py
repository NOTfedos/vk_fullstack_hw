class TicTacGame:
    symbols = {0: "O", 1: "X"}
    sep_count = 16

    def __init__(self):
        self.board = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]
        self.player = 0
        self.winner = None

    def show_board(self):
        print("-"*self.sep_count)
        for line in self.board:
            print("".join(line))

    def validate_input(self):
        print(f"PLAYER {self.player + 1}, symbol={self.symbols[self.player]}")
        print("INSERT x AND y OF NEW SYMBOL IN FORMAT <x> <y>"
              ", in range from 1 to 3, from down left edge")

        # If incorrect input
        try:
            x, y = list(map(int, input().split()))
        except ValueError:
            print("INCORRECT INPUT, please try again")
            self.validate_input()
            return

        # If this place is occupied
        if self.board[3-y][x-1] != ".":
            print("THIS PLACE IS NOT FREE, please try again")
            self.validate_input()
            return

        # Put his symbol
        self.board[3 - y][x - 1] = self.symbols[self.player]

        # Change player
        self.player = 1 - self.player

    def start_game(self):
        print("--- NEW GAME ---")

        self.show_board()

        # While game doesnt stop
        while self.check_winner():
            self.validate_input()
            self.show_board()

        self.end_game()

    def check_winner(self):
        # Check straights
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ".":
                self.winner = self.board[i][0]
                return False
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ".":
                self.winner = self.board[0][i]
                return False

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ".":
            self.winner = self.board[1][1]
            return False

        if self.board[2][0] == self.board[1][1] == self.board[0][2] != ".":
            self.winner = self.board[1][1]
            return False

        # Check if no free fields
        free = False
        for i in range(3):
            for j in range(3):
                free = free or (self.board[i][j] == ".")

        # If not free, end game
        if not free:
            return False

        return True

    def end_game(self):
        print("-"*self.sep_count)
        winner = self.winner if self.winner is not None else "FRIENDSHIP"
        print(f"GAME IS OVER, winner is {winner}")


if __name__ == '__main__':
    game = TicTacGame()
    game.start_game()
