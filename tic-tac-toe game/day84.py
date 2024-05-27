import os
import time

class TicTacToe:
    
    def __init__(self):
        self.board_grid = [' '] * 10
        self.player = 1
        self.win = 1
        self.draw = -1
        self.running = 0
        self.game = self.running

    
    def create_board_grid(self):
        print(f" {self.board_grid[1]} | {self.board_grid[2]} | {self.board_grid[3]} ")
        print("___|___|___")
        print(f" {self.board_grid[4]} | {self.board_grid[5]} | {self.board_grid[6]} ")
        print("___|___|___")
        print(f" {self.board_grid[7]} | {self.board_grid[8]} | {self.board_grid[9]} ")
        print("   |   | ")

    
    def position(self, x):
        if self.board_grid[x] == ' ':
            return True
        else:
            return False
    

    def check_win(self):

        # horizontal wins
        if self.board_grid[1] == self.board_grid[2] and self.board_grid[2] == self.board_grid[3] != ' ':
            self.game = self.win
        elif self.board_grid[4] == self.board_grid[5] and self.board_grid[5] == self.board_grid[6] != ' ':
            self.game = self.win
        elif self.board_grid[7] == self.board_grid[8] and self.board_grid[8] == self.board_grid[9] != ' ':
            self.game = self.win

        # vertical wins
        elif self.board_grid[1] == self.board_grid[4] and self.board_grid[4] == self.board_grid[7] != ' ':
            self.game = self.win
        elif self.board_grid[2] == self.board_grid[5] and self.board_grid[5] == self.board_grid[8] != ' ':
            self.game = self.win
        elif self.board_grid[3] == self.board_grid[6] and self.board_grid[6] == self.board_grid[9] != ' ':
            self.game = self.win

        # diagonal wins
        elif self.board_grid[1] == self.board_grid[5] and self.board_grid[5] == self.board_grid[9] != ' ':
            self.game = self.win
        elif self.board_grid[3] == self.board_grid[5] and self.board_grid[5] == self.board_grid[7] != ' ':
            self.game = self.win

        # draws
        elif self.board_grid[1] != ' ' and self.board_grid[2] != ' ' and self.board_grid[3] != ' ' and \
             self.board_grid[4] != ' ' and self.board_grid[5] != ' ' and self.board_grid[6] != ' ' and \
             self.board_grid[7] != ' ' and self.board_grid[8] != ' ' and self.board_grid[9] != ' ':
            self.game = self.draw
        else:
            self.game = self.running


    def play_game(self):
        print("Tic-Tac-Toe game Designed By Wiredu Clement")

        p1 = input("Player 1, choose your mark (X or O): ").upper()
        while p1 not in ['X', 'O']:
            p1 = input("Invalid mark! Please choose 'X' or 'O': ").upper()
        p2 = 'X' if p1 == 'O' else 'O'

        print()
        print("Please wait...")
        time.sleep(2)

        while self.game == self.running:
            os.system("cls")
            self.create_board_grid()

            if self.player % 2 != 0:
                print("Player 1's chance")
                mark = p1
            else:
                print("Player 2's chance")
                mark = p2

            choice = int(input("Enter the position between 1-9 where you want to mark: "))
            if self.position(choice):
                self.board_grid[choice] = mark
                self.player += 1
                self.check_win()

            os.system('cls')
            self.create_board_grid()

            if self.game == self.draw:
                print("Draw game")
            elif self.game == self.win:
                self.player -= 1
                if self.player % 2 != 0:
                    print("Player 1 won")
                else:
                    print("Player 2 won")


if __name__ == "__main__":
    game_instance = TicTacToe()
    game_instance.play_game()