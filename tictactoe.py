import math

class Board:
    def __init__(self):
        self.__boardList = {
                            0: [Cell(), Cell(), Cell()] ,
                            1: [Cell(), Cell(), Cell()], 
                            2: [Cell(), Cell(), Cell()]
                            }
        self.__game_running = True
        self.winner = None
        self.playerI = Player()
    
    def get_board(self):
        return self.__boardList
    
    def get_game_state(self):
        return self.__game_running
    
    def print_winner(self):
        if self.__game_running == False:
            if self.winner != None:
                return f"{self.winner} has won."
            return "Tie game!"
    
    def validate_win(self):
        """
            Checks if anyone has won by making 3, validations: row, column or diagnoal
            since there is only 3 ways to win in tic tac toe
        """
        
        # first checking if the game is a tie
        if self.__game_running and all(self.__boardList[0] + self.__boardList[1] + self.__boardList[2]):
            self.__game_running = False
        
        # row validation 
        row_result_0 = all(self.__boardList[0])
        row_result_1 = all(self.__boardList[1])
        row_result_2 = all(self.__boardList[2])
        

        if row_result_0:
            self.__check_winner(self.__boardList[0])
        elif row_result_1:
            self.__check_winner(self.__boardList[1])
        elif row_result_2:
            self.__check_winner(self.__boardList[2])
         
        # column validation
        col1 = [self.__boardList[0][0], self.__boardList[1][0], self.__boardList[2][0]]
        col2 = [self.__boardList[0][1], self.__boardList[1][1], self.__boardList[2][1]]
        col3 = [self.__boardList[0][2], self.__boardList[1][2], self.__boardList[2][2]]
        
        column_validation_1 = all(col1)
        column_validation_2 = all(col2)
        column_validation_3 = all(col3)

        if column_validation_1:
            self.__check_winner(col1)
        elif column_validation_2:
            self.__check_winner(col2)
        elif column_validation_3:
            self.__check_winner(col3)
    
        #diagnoal validation
        col1 = [self.__boardList[0][0], self.__boardList[1][1], self.__boardList[2][2]]
        col2 = [self.__boardList[0][2], self.__boardList[1][1], self.__boardList[2][0]]
        
        diagnoal_validation_1 = all(col1)
        diagnoal_validation_2 = all(col2)

        if diagnoal_validation_1:
            self.__check_winner(col1)
            return f"{self.winner} has won the game!"
        elif diagnoal_validation_2:
            self.__check_winner(col2)
            return f"{self.winner} has won the game!"
            
    def __check_winner(self, row):
        """ Validates/ Checks which player won, player X or player O,
            by checking if all the values in a row are all X or all O

        Board looks like this:
        {
            0: [0,1,2], <- this is a row
            1: [0,1,2],
            2: [0,1,2]
        }
        
        Args:
            row (list): A list that has the current row were checking.
        """
        
        # checking if player x won
        player_x_won = all(cell == "X" for cell in row)
        if player_x_won:
                self.winner = self.playerI.get_player_1()
                self.__game_running = False
        # checking if player O won
        elif all(cell == "O" for cell in row): 
                self.winner = self.playerI.get_player_2()
                self.__game_running = False
        
    def __str__(self):
        print("")
        print(str(self.__boardList[0]))
        print(str(self.__boardList[1]))
        print(str(self.__boardList[2]))
        return ""
    
    
class Cell:
    def __init__(self):
        self.cell = None
    
    def __str__(self):
        return str(self.cell)
    
    def __repr__(self):
        return str(self.cell)
    
    def __bool__(self):
        # true: cell isnt empty; false: cell is empty
        if self.cell is None:
            return False
        return self.cell
    
    
class Player:
    def __init__(self):
        self.__player1 = "X"
        self.__player2 = "O"
        self.currentPlayer = self.__player1
    
    def get_player_1(self):
        return self.__player1
    
    def get_player_2(self):
        return self.__player2  
    
    def change_turn(self):
        """
        Changes the users turn
        """
        if self.currentPlayer == self.__player1:
            self.currentPlayer = self.__player2
        else:
            self.currentPlayer = self.__player1
            
    def make_move(self, input: int, board):
        """
        Makes a new move on the grid. 

        Args:
            input (Number): User inputted move (0-9) depending on where they want to go
            board (Board):  Current instance of the board
        """
        
        # if we grab the input and divide by 3 + round it down we can get the current
        # row the input is in ex: 9th cell / 3 = 3 (3rd row)
        
        row = math.floor(input / 3)
        
        # we can also get the index of the current cell the input is at with mod
        # ex: 7. 7/3 = 2nd row. 7 % 3 = 1. 2nd row, 1st index.
        
        index = input % 3
        
        board[row][index] = self.currentPlayer
        self.change_turn()
        
    def __str__(self):
        return str(self.currentPlayer)
        

def check_user_input(user_input: int):
    """Checks if user input is valid

    Args:
        userinput (int): User-inputted value
    """
    
    while user_input not in range(0, 9):
        user_input = int(input("Please enter a digit between (0-8)"))

    if user_input in range(0,9):
        current_board = board.get_board()   
        all_values = current_board[0] + current_board[1] + current_board[2]  
        
        if bool(all_values[user_input]) == True:
            raise Exception("That spot is currently taken.")
        
        return user_input 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
board = Board()
player = Player()

while(board.get_game_state()):
    try:
        print(board)
        user_input = int(input("Where would you like to make a move? (0-8) "))
        check_user_input(user_input)
        player.make_move(user_input, board.get_board())
        board.validate_win()
        
        
    except ValueError as e:
        print("\n Please enter a correct value.")
    except KeyboardInterrupt as e:
        print("\n Thank you for using the program. Please click run if you want to try again.")
        break
    except Exception as e:
        print(e)

print(board.print_winner())
