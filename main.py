import time 
import os

class Board:
    def __init__(self,size):
        self.board =  [[0 for i in range(size)] for i in range(size)]
    
    def printboard(self,board="True"):
        if board == "True":
            board = self.board

        state_index = lambda state : " " if state == 0 else "X"
        for row in board:
            for item in row:
                # print(f'| {item.state}',end=" ")
                print(f'| {state_index(item)}',end=" ")
            print("|")
        print()


    def set_cell(self,row,col):
        self.board[row][col] = 1

    def count_neighbours(self,in_row,in_col,board):
        start_row = in_row - 1
        start_col = in_col - 1
        alive_neighbours = 0 
        for row in range(start_row,start_row + 3):
            for col in range(start_col,start_col + 3):
                if row >= 0 and col >= 0 and row < len(board) and col < len(board):
                    if board[row][col] != 0:
                        alive_neighbours += 1
                        if row == in_row and col == in_col:
                            alive_neighbours -= 1

        return alive_neighbours

    def next_gen(self):
        temp = [row.copy() for row in self.board]

        for row_index in range(len(self.board)):
            for col_index in range(len(self.board)):

                alive_neighbours = self.count_neighbours(row_index,col_index,self.board)

                # Rules for populated cell
                if self.board[row_index][col_index] != 0:
                    # Death by solitude 
                    if alive_neighbours <= 1:
                        temp[row_index][col_index] = 0
                        continue 

                    # Death by overpopulation
                    if alive_neighbours >=4 :
                        temp[row_index][col_index] = 0
                        continue 

                    if alive_neighbours == 2 or alive_neighbours == 3:
                        continue 

                else:
                    if alive_neighbours == 3 :
                        temp[row_index][col_index] = 1

        self.board = temp

class Game:
    def __init__(self,time,size):
        self.time = time
        self.board = Board(size)

    def main(self):
        self.board.printboard()
        while True:
            self.board.next_gen()
            self.board.printboard()
            time.sleep(self.time)
            os.system('clear')

    def user_inp(self):
        self.board.printboard()
        inp = (input("Enter cords: "))
        flag = True

        while flag:
            if inp:
                inp = eval(inp)
                for x,y in inp:
                    self.board.set_cell(x,y)
                self.board.printboard()
                inp = input("Enter cords: ")

            else:
                flag = False



game = Game(float(input("Enter Time gap: ")),int(input("Enter board size: ")))
print('Enter cords like this: [(x1,y1),(x2,y2)]')
print('To stop, press Enter')
game.user_inp()
game.main()

# [(18,17),(19,19),(20,17),(20,16),(20,21),(20,22),(20,20)]  Acorn
#  [(2,4),(2,3),(2,2),(1,4),(0,3)] Glider 
