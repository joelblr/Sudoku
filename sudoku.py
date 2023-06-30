# #!/usr/bin/python3


# #TODO : Score Board
# #TODO : Two-Player-Network or AI
# #TODO : GUI


class Fg :
    BLACK   = '\033[30m'
    RED     = '\033[31m'
    GREEN   = '\033[32m'
    YELLOW  = '\033[33m'
    BLUE    = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN    = '\033[36m'
    WHITE   = '\033[37m'
    RESET   = '\033[39m'

class Bg :
    BLACK   = '\033[40m'
    RED     = '\033[41m'
    GREEN   = '\033[42m'
    YELLOW  = '\033[43m'
    BLUE    = '\033[44m'
    MAGENTA = '\033[45m'
    CYAN    = '\033[46m'
    WHITE   = '\033[47m'
    RESET   = '\033[49m'

class Style :
    BRIGHT    = '\033[1m'
    DIM       = '\033[2m'
    NORMAL    = '\033[22m'
    RESET = '\033[0m'


class Text_Modify :

    def __init__(self) :

        fg = Fg()
        stl = Style()

        self.bold = stl.BRIGHT
        self.reset = fg.RESET + stl.RESET

        self.color = {
                        "black"    :  fg.BLACK,
                        "red"      :  fg.RED,
                        "green"    :  fg.GREEN,
                        "yellow"   :  fg.YELLOW,
                        "blue"     :  fg.BLUE,
                        "magenta"  :  fg.MAGENTA,
                        "cyan"     :  fg.CYAN,
                        "white"    :  fg.WHITE,
                        "reset"    :  fg.RESET,
                    }

    def Color(self, clr, text) :
        return self.bold + self.color[clr] + text + self.reset



# import os
# class Sudoku() :

#     def __init__(self) :

#         self.tm = Text_Modify()
#         self.turn = 1

#         self.xox = {
#                         "X" : 0,
#                         "O" : 0,
#                     }
#         self.board = {
#                         0 : ["1", "2", "3"],
#                         1 : ["4", "5", "6"],
#                         2 : ["7", "8", "9"],
#                     }
#         self.plot = {
#                         1 : (0,0), 2 : (0,1), 3 : (0,2),
#                         4 : (1,0), 5 : (1,1), 6 : (1,2),
#                         7 : (2,0), 8 : (2,1), 9 : (2,2),
#                     }
#         self.check = {
#                         "row" : {
#                             "X" : [0, 0, 0],
#                             "O" : [0, 0, 0],
#                         },
#                         "column" : {
#                             "X" : [0, 0, 0],
#                             "O" : [0, 0, 0],
#                         },
#                         "diagonal" : {
#                             "X" : [0, 0],
#                             "O" : [0, 0],
#                         },
#                     }


#     def xox_update(self, row, col, who) :

#         self.check["row"][who][row] += 1
#         self.check["column"][who][col] += 1
#         if row == col == 1 :
#             self.check["diagonal"][who][0] += 1
#             self.check["diagonal"][who][1] += 1
#         elif row == col :
#             self.check["diagonal"][who][0] += 1
#         elif row + col == 2 :
#             self.check["diagonal"][who][1] += 1


#     def board_update(self) :

#         print("-"*35)
#         print(f"{self.tm.mX}", end = " ") if self.turn else print(f"{self.tm.mO}", end = " ")
#         print("to Play.")

#         try :
#             num = int( input(f"Enter a {self.tm.mN('Number')} : "))
#             if (num < 1 or num > 9) :
#                 raise IOError

#         except IOError :
#             print("Out of Bounce: Numbers 1 to 9 only!")
#             return self.board_update()

#         except ValueError :
#             print("Wrong Number: Numbers 1 to 9 only!")
#             return self.board_update()

#         except (KeyboardInterrupt, EOFError) :
#             print("\nPlz Play: Numbers 1 to 9, Ezy.")
#             return self.board_update()

#         row, col = self.plot.get(num)
#         if self.board[row][col] in ["X", "O"] :
#             print("Same Number, Try Again !")
#             return self.board_update()

#         self.board[row][col] = "X" if self.turn else "O"
#         self.xox_update(row, col, self.board[row][col])
#         self.turn ^= 1

#         return


#     def board_print(self) :

#         print()
#         for idx in range(3) :
#             row = tuple( self.board[idx])
#             print("\t|-----|-----|-----|")
#             print("\t|  %s  |  %s  |  %s  |" % row)
#         print("\t|-----|-----|-----|")
#         print()

#         return


#     # define our clear function
#     def clear_screen(self) :
#         # for windows
#         if os.name == 'nt' :
#             os.system('cls')
#         # for mac and linux(here, os.name is 'posix')
#         else :
#             os.system('clear')


#     def board_design(self) :

#         self.clear_screen()

#         print()
#         for i in range(9) :

#             row = ( str(i+1),)*9
#             print("\t" + self.tm.m4 * 3 + self.tm.m5)
#             print(f"\t{self.tm.m1}{f'{self.tm.m2}'.join(row)}{self.tm.m3}")

#         print("\t" + self.tm.m6 * 3 + self.tm.m7)
#         print()

#         return


#     def xox_check(self, name, who, idx) :
#         for i in idx :
#             if self.check[name][who][i] == 3 :
#                 self.check[name][who][i] = 0
#                 self.xox[who] += 1


#     def board_check(self, who) :

#         self.xox_check("row", who, [0, 1, 2])
#         self.xox_check("column", who, [0, 1, 2])
#         self.xox_check("diagonal", who, [0, 1])

#         if self.xox[who] >= 1 :
#             return [True, True]
#         if sum( self.check["row"]["X"]) + sum( self.check["row"]["O"]) == 9 :
#             return [False, True]
#         return [False]


#     def winner_print(self) :

#         winner = self.board_check("X" if self.turn^1 else "O")

#         if winner.pop() :
#             import time
#             if winner.pop() :
#                 print(">"*35)
#                 print(f"The Winner is: {self.tm.mX}") if self.turn^1\
#                         else print(f"The Winner is: {self.tm.mO}")
#                 print("<"*35, "\n")

#             else :
#                 print("="*35)
#                 print(f"It's a { self.tm.mN('Draw')} !")
#                 print("="*35, "\n")

#             time.sleep(5)
#             return True

#         return False


# if __name__ == "__main__" :

#     game = Sudoku()

#     game.board_design()
#     # while True :

#     #     game.board_update()
#     #     game.board_design()
#     #     if game.winner_print() :
#     #         break


# # pyinstaller.exe --onefile --windowed --icon=app.ico app.py --name=app


# randomize rows, columns and numbers (of valid self.base pattern)
from random import sample
from collections import defaultdict
class SudokuBoard :

    def __init__(self) :

        self.true = 0

        self.base  = 3
        self.side  = self.base ** 2

        tm = Text_Modify()

        b11 = tm.Color("magenta", "║")
        b12 = tm.Color("magenta", "╟")
        b21 = tm.Color("cyan", "│")
        b22 = tm.Color("cyan", "───")
        b23 = tm.Color("cyan", "┼")
        b32 = tm.Color("magenta", "╫")
        b42 = tm.Color("magenta", "╢")

        def expandLine(line) :
            return line[0]+line[5:9].join([line[1:5]*(self.base-1)]*self.base)+line[9:13]

        self.line1  = expandLine("║ . │ . ║ . ║").replace("║", b11).replace("│", b21)
        line2  = expandLine("╟───┼───╫───╢").replace("╟", b12).replace("╢", b42)
        self.line2  = line2.replace("╫", b32).replace("───", b22).replace("┼", b23)

        self.line0  = tm.Color( "magenta", expandLine("╔═══╤═══╦═══╗"))
        # line1  = expandLine("║ . │ . ║ . ║")
        # line2  = expandLine("╟───┼───╫───╢")
        self.line3  = tm.Color( "magenta", expandLine("╠═══╪═══╬═══╣"))
        self.line4  = tm.Color( "magenta", expandLine("╚═══╧═══╩═══╝"))

        self.lvl = { "easy" : 46, "medium" : 36, }

        solution = self.create_solution()
        self.board = self.create_board( [list(row)  for row in  solution],  self.lvl["easy"] )
        self.question = [list(row) for row in self.board]
        self.print_board()


    def create_solution(self) :

        # pattern for a baseline valid solution
        def pattern(r, c) :
            return (self.base * (r % self.base) + r//self.base + c) % self.side

        def shuffle(s) :
            return sample(s, len(s)) 

        rBase = range(self.base) 
        rows  = [ g*self.base + r for g in shuffle(rBase) for r in shuffle(rBase) ] 
        cols  = [ g*self.base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
        nums  = shuffle(range(1, self.base*self.base+1))

        # produce board using randomized baseline pattern
        board = [ [nums[pattern(r, c)] for c in cols] for r in rows ]

        # for line in board :
        #     print(line)

        return board
        # # [6, 2, 5, 8, 4, 3, 7, 9, 1]
        # # [7, 9, 1, 2, 6, 5, 4, 8, 3]
        # # [4, 8, 3, 9, 7, 1, 6, 2, 5]
        # # [8, 1, 4, 5, 9, 7, 2, 3, 6]
        # # [2, 3, 6, 1, 8, 4, 9, 5, 7]
        # # [9, 5, 7, 3, 2, 6, 8, 1, 4]
        # # [5, 6, 9, 4, 3, 2, 1, 7, 8]
        # # [3, 4, 2, 7, 1, 8, 5, 6, 9]
        # # [1, 7, 8, 6, 5, 9, 3, 4, 2]

    def create_board(self, board, k) :

        #  46 - 51 Easy
        # # You can then remove some of the numbers from the sudoku solution to create the puzzle:

        squares = self.side*self.side
        empties =  k  #squares - (81 - 20)        # *3//9 : 27 fills,  
        for p in sample(range(squares),empties):
            board[p//self.side][p%self.side] = 0

        numSize = len( str(self.side))

        # for line in board :
        #     print( *(f"{n or '-' :{numSize}} " for n in line))

        return board
        # # 6  .  .  .  .  3  .  .  1
        # # .  9  .  .  .  .  .  .  3
        # # 4  .  3  .  .  .  6  .  .
        # # .  .  .  5  9  .  2  .  6
        # # .  .  .  .  .  .  .  .  .
        # # .  .  7  .  .  .  .  .  4
        # # .  .  .  .  .  .  1  7  .
        # # .  .  2  .  .  8  .  .  .
        # # .  .  8  .  .  .  .  4  2

    def print_board(self) :

        symbol = " 1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        nums   = [ [""]+[symbol[n] for n in row] for row in self.board ]

        print(self.line0)
        for r in range(1, self.side + 1) :
            print( "".join(n+s for n, s in zip(nums[r-1], self.line1.split("."))) )
            print([self.line2, self.line3, self.line4][(r%self.side == 0)+(r%self.base == 0)])


    def print_question(self) :

        symbol = " 1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        nums   = [ [""]+[symbol[n] for n in row] for row in self.question ]

        print(self.line0)
        for r in range(1, self.side + 1) :
            print( "".join(n+s for n, s in zip(nums[r-1], self.line1.split("."))) )
            print([self.line2, self.line3, self.line4][(r%self.side == 0)+(r%self.base == 0)])


    def print_solution(self) :

        symbol = " 1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        nums   = [ [""]+[symbol[n] for n in row] for row in self.solution ]

        print(self.line0)
        for r in range(1, self.side + 1) :
            print( "".join(n+s for n, s in zip(nums[r-1], self.line1.split("."))) )
            print([self.line2, self.line3, self.line4][(r%self.side == 0)+(r%self.base == 0)])


    def solveSudoku(self, k) :
        self.solve_board()


    def isValidSudoku(self, board) :

        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9) :
            for c in range(9) :
                # if board[r][c] == 0 :
                #     continue

                if (board[r][c] in rows[r] or board[r][c] in cols[c]
                   or board[r][c] in squares[(r//3,c//3)]) :
                    return False

                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])

        return True



if __name__ == "__main__" :

    game = SudokuBoard()
    
    # for k in range(20) :

    #     game.true = 0
    #     flag = True
    #     while flag :
    #     # game.print_board()
    #         flag = game.solveSudoku(k)
    #         if game.true == 10000 :
    #             print(f"K = {k}")
    #             print("100% Passed")
    #             break
    #     else :
    #         pass


            # print(f"{game.true/100}% Passed\n{100 - game.true/100}% Failed.")


    # game.board_design()
    # while True :

    #     game.board_update()
    #     game.board_design()
    #     if game.winner_print() :
    #         break



    """
    # # def solve_board(self) :

    # #     for r in range( len( self.board[0])) :
    # #         for c in range(len(self.board)) :

    # #             if self.board[r][c] == 0 :
    # #                 for i in range(1,10) :
    # #                     if self.isValid( i, r, c) :
    # #                         self.board[r][c] = i
    # #                         if self.solve_board() :
    # #                             return True
    # #                         else :
    # #                             self.board[r][c] = 0
    # #                 return False
    # #     return True


    # # def isValid(self, n, r, c) :

    # #     for i in range(9) :
    # #         if  self.board[r][i] == n or self.board[i][c] == n or\
    # #             self.board[3*(r//3)+(i//3)][3*(c//3)+(i%3)] == n :
    # #             return False
    # #     return True
    # def solve_board(self) :

    #     self.board = [ [str(cell) if cell else "."  for cell in row]  for row in self.board]
    #     squares = []
    #     square_cell_index = []
    #     for i in range(9) :
    #         hi, vi = i // 3, i % 3
    #         square = []
    #         for j in range(hi * 3, hi * 3 + 3) :
    #             square.extend(self.board[j][vi * 3:vi * 3 + 3])
    #         square = [j for j in square if j.isdigit()]
    #         squares.append(square)
    #         cell_index = [(x, y) for x in range(hi * 3, hi * 3 + 3) for y in range(vi * 3, vi * 3 + 3)]
    #         square_cell_index.append(cell_index)

    #     d_num = {}
    #     d_count = {}
    #     nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    #     for i in range(9) :
    #         for j in range(9) :
    #             if not self.board[i][j].isdigit() :
    #                 row = [x for x in self.board[i] if x.isdigit()]
    #                 column = [self.board[x][j] for x in range(9) if self.board[x][j].isdigit()]
    #                 squareIndex = (i // 3) * 3 + j // 3
    #                 square = squares[squareIndex]
    #                 total = set(row + column + square)
    #                 available_nums = [num for num in nums if num not in total]
    #                 d_num[(i, j)] = available_nums
    #                 d_count[(i, j)] = len(available_nums)


    #     def dfs() :
    #         if not d_num :
    #             return True

    #         cell = min(d_count, key=d_count.get)
    #         i, j = cell[0], cell[1]
    #         squareIndex = (i // 3) * 3 + j // 3
    #         candidates = d_num[cell]
    #         num_candidate = d_count[cell]
    #         del d_num[cell]
    #         del d_count[cell]
    #         for candidate in candidates :
    #             updated_cells = []
    #             failed = False
    #             row_share = [(i, x) for x in range(9) if (i, x) in d_num]
    #             column_share = [(x, j) for x in range(9) if (x, j) in d_num]
    #             square_share = [x for x in square_cell_index[squareIndex] if x in d_num]
    #             for x in set(row_share + column_share + square_share) :
    #                 if candidate in d_num[x] :
    #                     d_num[x].remove(candidate)
    #                     d_count[x] -= 1
    #                     updated_cells.append(x)
    #                     if not d_num[x]:
    #                         failed = True
    #                         break

    #             if not failed and dfs() :
    #                 self.board[i][j] = candidate
    #                 return True
    #             for cell in updated_cells :
    #                 d_num[cell].append(candidate)
    #                 d_count[cell] += 1
    #         d_num[(i, j)] = candidates
    #         d_count[(i, j)] = num_candidate
    #         return False

    #     if not dfs() :
    #         raise RuntimeError('No solution possible for given self.board')

    #     self.board = [ [int(cell)  for cell in row]  for row in self.board]
    #     return self.board

    """
