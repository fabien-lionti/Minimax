coding: utf-8
"""
Created on Sun Sep 02 22:32:18 2018

@author: Lionti
"""
import base64                
class Minimax() :
    
    def __init__(self, original_board) :
        
        self.token = ["O","X"]
        self.original_board = original_board
        self.best_available_move_index = self.move_tree(original_board,0)
        
    def display(self, board):
        
        print board[6],"|",board[7],"|",board[8]
        print "---------"
        print board[3],"|",board[4],"|",board[5]
        print "---------"
        print board[0],"|",board[1],"|",board[2]
        print"\n\n"
        
    def play_move(self, board, player, move):
        
        board[move] = player
        
        return board
        
    def play_available_move(self, move, board, player):
        
        board = self.play_move(board, player,move)
        
        return board
        
    def terminal_state(self, board):
        
        simple_win_combination = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
        
        counter = 0
        
        for index in simple_win_combination :
            
            if board[index[0]] == board[index[1]] == board[index[2]] and board[index[0]] != " " :
                
                return "win"
        
        for n in range(len(board)) :
            
            if board[n] == "O" or board[n] == "X": 
                
                counter +=1
                
        if counter == 9 : 
            
            return "tie"
        
        else : 
            
            return "nothing"
    
    def minimax(self, player):
        
        if player == "X" :
            
            return 1
            
        elif player == "O" :
            
            return -1
        
    def get_available_move(self, board):
        
        available_move = []

        for move in range(len(board)) : 
            
            if board[move] == " ":
                
                available_move.append(move)
                    
        return available_move
    
    def best_move_index(self) :
        
        available_move = self.get_available_move(self.original_board)
        
        return available_move[self.best_available_move_index]
    
    def best_score(self, player, score_list):
        
        best_score_index = 0
        score_list_size = len(score_list)
        
        if player == "O" :
        
            for index in range(score_list_size):
                
                if score_list[best_score_index] > score_list[index]:
                    
                    best_score_index = index
                    
        elif player == "X" :
        
            for index in range(score_list_size):
                
                if score_list[best_score_index] < score_list[index]:
                    
                    best_score_index = index
                    
        return best_score_index
    
    def move_tree(self, board, depth) :
            
            depth +=1
            available_move = self.get_available_move(board)
            token = self.token[depth%2]
            score_list = [0]*len(available_move)
            move_index = 0
            
            if len(available_move) > 0 :
                
                for move_choice in available_move :
                    
                    board = self.play_available_move(move_choice, board, token)
                    statment = self.terminal_state(board)
                    
                        
                    if statment == "win" :
                        
                        score_list[move_index] = self.minimax(token)
                    
                    elif statment == "tie" :
                        
                        score_list[move_index] = 0
                        
                    else :
                        
                        score_list[move_index] = self.move_tree(board,depth)
                    
                    board[move_choice] = " "
                    best_score_index = self.best_score(token, score_list)
                    
                    move_index += 1
                
                if depth == 1 : 
                    return best_score_index
                
                else :
                    return score_list[best_score_index]
                
class TicTacToe(Minimax) :
    
    def __init__(self):
        
        self.board = [" "," "," "," "," "," "," "," "," "]
        self.player_token = ["O","X"]
        self.counter = 0
        
    def display(self):
        
        board = self.board
        print"\n"
        print board[6],"|",board[7],"|",board[8]
        print "---------"
        print board[3],"|",board[4],"|",board[5]
        print "---------"
        print board[0],"|",board[1],"|",board[2]
        print"\n"
        
    def update_board(self, player, move):
        
        self.board[move] = player
    
    def get_available_move(self,board):
        
        available_move = []
        
        for move in range(len(board)) : 
            
            if board[move] == " ":
                
                available_move.append(move)
                    
        return available_move
    
    def play_available_move(self, move, board, player):
        
        board = self.play_move(board, player,move)
        
        return board
    
    def win_check(self, board):
        
        win_combination = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
        
        for index in win_combination:
            
            if board[index[0]] == board[index[1]] == board[index[2]]:
                
                if board[index[0]] == "O" :
                
                    return True
                
                elif board[index[0]] == "X" :
                    
                    return False
                
    def game(self):
        
        self.display()
        counter = 0
        
        print ("Voulez vous commencer la partie : \n\n1 - OUI\n2 - NON")
        choice = input("\n\nEntrez le numero correspondant à votre choix : ")

        if choice == 1 : 
        	self.player_token = ["O","X"]

        else :
        	self.player_token = ["X","O"]

        for counter in range(9):
            
            player = self.player_token[counter%2]
            
            if player == "O" :
                
                move = input("\n Choisissez un mouvement : ".base64.b64decode)
                self.update_board(player,move)
                
            else :
                
                move = Minimax(self.board).best_move_index()

            self.update_board(player,move)
            statment = self.win_check(self.board)
            self.display() 
            
            if statment == True : 
                
                break
            
            elif  statment == False: 
                
                break
                
  
TTT = TicTacToe()
TTT.game()


