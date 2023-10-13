#p.s i cant use the minimax code you use as an example sir it breaks the game for some reason..
#i think its my skill issue, so i use one from the internet

import math
import copy

class TicTacToe:
    def __init__(self):
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.player_marker = 1
        self.bot_marker = -1

    def display_board(self):
        for row in self.board:
            print(' '.join(['X' if cell == 1 else 'O' if cell == -1 else ' ' for cell in row]))

    def make_move(self, row, col, val):
        if self.board[row][col] == 0:
            self.board[row][col] = val
            return True
        return False

    def check_win(self, marker):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == marker:
                return True

        for i in range(3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i] == marker:
                return True

        if self.board[0][0] == self.board[1][1] == self.board[2][2] == marker:
            return True

        if self.board[0][2] == self.board[1][1] == self.board[2][0] == marker:
            return True

        return False

    def is_board_full(self):
        return all(cell != 0 for row in self.board for cell in row)

    def expand_state(self):
        children = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    child = [i, j]
                    children.append(child)
        return children

    def minimax(self, state, depth, is_maximizing, alpha, beta):
        if self.check_win(self.bot_marker):
            return 10
        if self.check_win(self.player_marker):
            return -10
        if self.is_board_full():
            return 0
        if depth == 0:
            return 0

        if is_maximizing:
            best_score = -math.inf
            children = self.expand_state()
            for child in children:
                row, col = child
                state[row][col] = self.bot_marker
                score = self.minimax(copy.deepcopy(state), depth - 1, False, alpha, beta)
                state[row][col] = 0
                best_score = max(best_score, score)
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break
            return best_score
        else:
            best_score = math.inf
            children = self.expand_state()
            for child in children:
                row, col = child
                state[row][col] = self.player_marker
                score = self.minimax(copy.deepcopy(state), depth - 1, True, alpha, beta)
                state[row][col] = 0
                best_score = min(best_score, score)
                beta = min(beta, best_score)
                if beta <= alpha:
                    break
            return best_score

    def bot_move(self):
        best_score = -math.inf
        best_move = None
        children = self.expand_state()
        for child in children:
            row, col = child
            self.board[row][col] = self.bot_marker
            score = self.minimax(copy.deepcopy(self.board), 9, False, -math.inf, math.inf)
            self.board[row][col] = 0
            if score > best_score:
                best_score = score
                best_move = child
        return best_move

    def play_game(self):
        while True:
            self.display_board()

            if self.check_win(self.player_marker):
                print("Player 'X' wins!")
                break

            if self.check_win(self.bot_marker):
                print("Player 'O' wins!")
                break

            if self.is_board_full():
                print("It's a tie!")
                break

            while True:
                move = input("Enter your move (row col): ")
                row, col = map(int, move.split())
                if self.make_move(row, col, self.player_marker):
                    break
                else:
                    print("Invalid move. Try again.")

            if not self.is_board_full():
                print("Bot's move:")
                bot_move = self.bot_move()
                self.make_move(bot_move[0], bot_move[1], self.bot_marker)

if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()

