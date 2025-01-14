import copy


class Board:
    def __init__(self, use_pre_field=True):
        self.column_mapping = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
        self.back_column_mapping = {1:'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F', 7:'G', 8:'H'}
        self.figures = [[] for _ in range(8)]
        if use_pre_field:
            self.figures[0] = [Rook(is_white=True), Knight(is_white=True), Bishop(is_white=True), Queen(is_white=True), King(is_white=True), Bishop(is_white=True), Knight(is_white=True), Rook(is_white=True)]
            self.figures[1] = [Pawn(is_white=True) for _ in range(0,8)]
            for i in range(2,6):
                self.figures[i] = [None for _ in range(8)]
            self.figures[7] = [Rook(is_white=False), Knight(is_white=False), Bishop(is_white=False), Queen(is_white=False), King(is_white=False), Bishop(is_white=False), Knight(is_white=False), Rook(is_white=False)]
            self.figures[6] = [Pawn(is_white=False) for _ in range(0,8)]
        else:
            for i in range(8):
                    self.figures[i] = [None for _ in range(8)]

        self.game_active = True
        self.white_turn = True
        self.white_is_winner = None
        self.w_rochade_psb = True
        self.b_rochade_psb = True
        self.return_codes = {0: 'Figure was placed', 1: 'Cannot move this figure that way', 2: 'Checkmate, white has won', 3: 'Checkmate, black has won', 4: 'Incorrect pos syntax!', 5: 'Game has already ended'}



    def add_element(self, pos:tuple, chess_obj):
        if self.check_coordinate_in_field_range(pos[0]) and self.check_coordinate_in_field_range(pos[1]):
            if type(chess_obj) not in [Rook, Knight, Bishop, Queen, King, Pawn]: raise ValueError('chess_obj must be of type Rook, Knight, Bishop, Queen, King or Pawn')
            self.figures[pos[0]][pos[1]] = chess_obj
        else:
            raise ValueError('Coordinates out of field range!')

    def del_element(self, pos:tuple):
        self.figures[pos[0]][pos[1]] = None 

    def check_move(self, a:list, b:list) -> bool:
        if self.figures[a[0]][a[1]] == None: return False
        elif self.figures[a[0]][a[1]].move_possible(a, b, self, self.check_coordinate_in_field_range) and self.figures[a[0]][a[1]].is_white is self.white_turn: return True
        else: return False
    

    def convert_chess_coordinates(self, str_pos:str) -> list:
        if self.check_right_str_coordinates(str_pos):
            return [int(str_pos[1])-1, self.column_mapping[str_pos[0]]-1] #first element of list marks y-coordinate -> important for the list-field (more readable)
        else:
            raise ValueError('Incorrect pos syntax!')
    
    def convert_coordinates_in_str(self, pos:list) -> str:
        pos = pos.copy()
        pos[0] += 1
        pos[1] += 1
        return self.back_column_mapping[pos[1]] + str(pos[0])



    def check_coordinate_in_field_range(self, pos:list) -> bool:
        if ((0<= pos[0] <= 7) and (0<= pos[1] <= 7)):
            return True
        else:
            return False
        
    def check_right_str_coordinates(self, str_pos:str) -> bool:
        if len(str_pos) == 2:
            if str_pos[0] in self.column_mapping.keys() and 49 <= ord(str_pos[1]) <= 56: 
                return True
        else:
            return False


    def get_pos_kings(self) -> list:
        pos_kings = [None, None]

        for i in range(0, 8):
            for j in range(0, 8):
                if type(self.figures[i][j]) is King:
                    if self.figures[i][j].is_white:
                        pos_kings[0] = [i, j]
                    else:
                        pos_kings[1] = [i, j]

        return pos_kings



    def place_figure(self, a, b) -> None:
        self.figures[b[0]][b[1]] = self.figures[a[0]][a[1]]
        self.figures[a[0]][a[1]] = None



    def get_psb_moves(self, str_pos:str) -> list:
        pos = self.convert_chess_coordinates(str_pos)
        fig = self.figures[pos[0]][pos[1]]
        pos_lst = fig.next_psb_moves(pos, self, self.check_coordinate_in_field_range)
        str_pos_lst = [] 
        for e in pos_lst:
            str_pos_lst.append(self.convert_coordinates_in_str(e))
        return str_pos_lst


    def main(self, a:list, b:list) -> int:
        if self.game_active:
            coordinates_right = False
            if self.check_coordinate_in_field_range(a) and self.check_coordinate_in_field_range(b): 
                coordinates_right = True
                coordinates = [a, b]
            else: return 4

            if coordinates_right and self.check_move(*coordinates):
                check_field = copy.deepcopy(self.figures)
                self.place_figure(*coordinates)
                if self.check_if_check(ref_king_is_white=self.white_turn): #check that your own move doesnt check your king
                    self.figures = check_field
                    return 1
                
                if type(self.figures[b[0]][b[1]]) is King: #rochade
                    if self.w_rochade_psb and self.white_turn or self.b_rochade_psb and (self.white_turn is False):
                        if self.white_turn:
                            y = 0
                        else:
                            y = 7

                        if a == [y, 4] and b == [y, 1]:
                            self.place_figure([y, 0], [y, 2])
                        elif a == [y, 4] and b == [y, 6]:
                            self.place_figure([y, 7], [y, 5])

                    if self.white_turn:
                        self.w_rochade_psb = False
                    else:
                        self.b_rochade_psb = False
                
                if type(self.figures[b[0]][b[1]]) is Rook:
                    if self.white_turn:
                        self.w_rochade_psb = False
                    else:
                        self.b_rochade_psb = False

                if self.white_turn and (self.check_checkmate(ref_king_is_white=False) == True):
                    self.white_is_winner = True
                    self.game_active = False
                    return 2
                elif (self.white_turn == False) and (self.check_checkmate(ref_king_is_white=True) == True):
                    self.white_is_winner = False
                    self.game_active = False
                    return 3
                
                self.white_turn = not self.white_turn
                return 0
            else:
                return 1
        else:
            return 5
        

    def get_pos_all_elements(self, is_white) -> list:
        lst = []
        for i in range(0, 8):
            for j in range(0, 8):
                if self.figures[i][j] is not None and self.figures[i][j].is_white == is_white:
                    lst.append([i, j])

        return lst
    

    def check_if_check(self, ref_king_is_white):
        if ref_king_is_white: curr_king = self.get_pos_kings()[0]
        else: curr_king = self.get_pos_kings()[1]

        psb_moves_opponent_element = []
        pos_opponent_elements = self.get_pos_all_elements(is_white=(not ref_king_is_white))


        for e in pos_opponent_elements:
            psb_moves_opponent_element.append(self.figures[e[0]][e[1]].next_psb_moves(e, self, self.check_coordinate_in_field_range))

        for moves_per_figure in psb_moves_opponent_element:
            if curr_king in moves_per_figure:
                return True
        return False
    
    

    def check_checkmate(self, ref_king_is_white) -> list:
        if ref_king_is_white: curr_king = self.get_pos_kings()[0]
        else: curr_king = self.get_pos_kings()[1]

        if self.check_if_check(ref_king_is_white=ref_king_is_white):
            if ref_king_is_white:
                self.white_ever_checked = True
                print("White is checked")
            else:
                self.black_ever_checked = True
                print("Black is checked")
            psb_moves_king = self.figures[curr_king[0]][curr_king[1]].next_psb_moves(curr_king, self, self.check_coordinate_in_field_range)
            n_possible_moves_king = len(psb_moves_king)

            if n_possible_moves_king > 0:
                for e in psb_moves_king:
                    check_field = copy.deepcopy(self.figures)
                    self.place_figure(curr_king, e)
                    if self.check_if_check(ref_king_is_white=ref_king_is_white) is True:
                        n_possible_moves_king -= 1
                    self.figures = check_field

            #print(f'King has {n_possible_moves_king} moves')

            if n_possible_moves_king == 0:#when n_possible_moves_king = 0 and checked -> king cannot move
                #checking if any figure with same color as the threatened king can uncheck
                figure_can_unckeck = False
                pos_own_elements = self.get_pos_all_elements(is_white=ref_king_is_white)
                psb_moves_own_elements = []
                for pos_figure in pos_own_elements:
                    psb_moves_own_elements.append(self.figures[pos_figure[0]][pos_figure[1]].next_psb_moves(pos_figure, self, self.check_coordinate_in_field_range))
                for i_moves_per_figure in range(len(psb_moves_own_elements)):
                    for move in psb_moves_own_elements[i_moves_per_figure]:
                        check_field = copy.deepcopy(self.figures)
                        self.place_figure(pos_own_elements[i_moves_per_figure], move)
                        if self.check_if_check(ref_king_is_white=ref_king_is_white) is False:
                            figure_can_unckeck = True
                            print(f"Figure at {self.convert_coordinates_in_str(pos_own_elements[i_moves_per_figure])} can uncheck when going to {self.convert_coordinates_in_str(move)}!")
                        
                        self.figures = check_field

                return not figure_can_unckeck
            else:
                """for move in psb_moves_king: #Only to see, how the king can move into safety, else returns always false
                    check_field = copy.deepcopy(self.figures)
                    self.place_figure(curr_king, move)
                    if self.check_if_check(ref_king_is_white=ref_king_is_white) is False:
                        print(f"King at {self.convert_coordinates_in_str(curr_king)} can escape, when going to {self.convert_coordinates_in_str(move)}!")                  
                    self.figures = check_field"""
                return False

                
        else: return False

class Bishop:
    def __init__(self, is_white):
        if type(is_white) is not bool: raise ValueError('is_white must be of type bool')
        self.is_white = is_white
    
    def move_possible(self, a:tuple,b:tuple, board:Board, func_check) -> bool:
        if b in self.next_psb_moves(a, board, func_check): return True
        else: return False

    def next_psb_moves(self, a, board:Board, func_check) -> list:
        moves_lst = []
        curr_pos = a.copy() #avoid pass-by reference

        while True:
            curr_pos[0] += 1
            curr_pos[1] += 1
            if func_check(curr_pos):
                if board.figures[curr_pos[0]][curr_pos[1]] == None:
                    moves_lst.append(curr_pos.copy()) #avoid pass-by reference
                elif board.figures[curr_pos[0]][curr_pos[1]].is_white != self.is_white:
                    moves_lst.append(curr_pos.copy()) #avoid pass-by reference
                    break
                else:
                    break
            else:
                break



        curr_pos = a.copy()
        while True:
            curr_pos[0] += 1
            curr_pos[1] -= 1
            if func_check(curr_pos):
                if board.figures[curr_pos[0]][curr_pos[1]] == None:
                    moves_lst.append(curr_pos.copy()) #avoid pass-by reference
                elif board.figures[curr_pos[0]][curr_pos[1]].is_white != self.is_white:
                    moves_lst.append(curr_pos.copy()) #avoid pass-by reference
                    break
                else:
                    break
            else:
                break

        curr_pos = a.copy()
        while True:
            curr_pos[0] -= 1
            curr_pos[1] += 1
            if func_check(curr_pos):
                if board.figures[curr_pos[0]][curr_pos[1]] == None:
                    moves_lst.append(curr_pos.copy()) #avoid pass-by reference
                elif board.figures[curr_pos[0]][curr_pos[1]].is_white != self.is_white:
                    moves_lst.append(curr_pos.copy()) #avoid pass-by reference
                    break
                else:
                    break
            else:
                break

        curr_pos = a.copy()
        while True:
            curr_pos[0] -= 1
            curr_pos[1] -= 1
            if func_check(curr_pos):
                if board.figures[curr_pos[0]][curr_pos[1]] == None:
                    moves_lst.append(curr_pos.copy()) #avoid pass-by reference
                elif board.figures[curr_pos[0]][curr_pos[1]].is_white != self.is_white:
                    moves_lst.append(curr_pos.copy()) #avoid pass-by reference
                    break
                else:
                    break
            else:
                break

        return moves_lst

        

class Rook:
    def __init__(self, is_white):
        if type(is_white) is not bool: raise ValueError('is_white must be of type bool')
        self.is_white = is_white

    def move_possible(self, a:tuple,b:tuple, board:Board, func_check) -> bool:
        if b in self.next_psb_moves(a, board, func_check): return True
        else: return False

    def next_psb_moves(self, a, board:Board, func_check) -> list:
        moves_lst = []
        curr_pos = a.copy()

        while True:
            curr_pos[1] += 1
            if func_check(curr_pos):
                if board.figures[curr_pos[0]][curr_pos[1]] == None:
                    moves_lst.append(curr_pos.copy()) #avoid pass-by reference
                elif board.figures[curr_pos[0]][curr_pos[1]].is_white != self.is_white:
                    moves_lst.append(curr_pos.copy()) #avoid pass-by reference
                    break
                else:
                    break
            else:
                break

        curr_pos = a.copy()
        while True:
            curr_pos[1] -= 1
            if func_check(curr_pos):
                if board.figures[curr_pos[0]][curr_pos[1]] == None:
                    moves_lst.append(curr_pos.copy()) #avoid pass-by reference
                elif board.figures[curr_pos[0]][curr_pos[1]].is_white != self.is_white:
                    moves_lst.append(curr_pos.copy()) #avoid pass-by reference
                    break
                else:
                    break
            else:
                break

        curr_pos = a.copy()
        while True:
            curr_pos[0] += 1
            if func_check(curr_pos):
                if board.figures[curr_pos[0]][curr_pos[1]] == None:
                    moves_lst.append(curr_pos.copy()) #avoid pass-by reference
                elif board.figures[curr_pos[0]][curr_pos[1]].is_white != self.is_white:
                    moves_lst.append(curr_pos.copy()) #avoid pass-by reference
                    break
                else:
                    break
            else:
                break


        curr_pos = a.copy()
        while True:
            curr_pos[0] -= 1
            if func_check(curr_pos):
                if board.figures[curr_pos[0]][curr_pos[1]] == None:
                    moves_lst.append(curr_pos.copy()) #avoid pass-by reference
                elif board.figures[curr_pos[0]][curr_pos[1]].is_white != self.is_white:
                    moves_lst.append(curr_pos.copy()) #avoid pass-by reference
                    break
                else:
                    break
            else:
                break

        return moves_lst


class Queen(Rook, Bishop):
    def __init__(self, is_white):
        if type(is_white) is not bool: raise ValueError('is_white must be of type bool')
        self.is_white = is_white

    def move_possible(self, a:tuple,b:tuple, board:Board, func_check) -> bool:
        if b in self.next_psb_moves(a, board, func_check): return True
        else: return False

    def next_psb_moves(self, a, board:Board, func_check) -> list:
        return Rook.next_psb_moves(self, a, board, func_check) + Bishop.next_psb_moves(self, a, board, func_check) 

class King:
    def __init__(self, is_white):
        if type(is_white) is not bool: raise ValueError('is_white must be of type bool')
        self.is_white = is_white

    def check_rochade(self, a:tuple, b:tuple, board:Board) -> bool:
        if self.is_white and board.w_rochade_psb:
            y = 0
        elif self.is_white is False and board.b_rochade_psb:
            y = 7
        else:
            return False 
        if a == [y, 4] and b == [y, 1]:
            if board.check_if_check(ref_king_is_white=self.is_white): return False
            for i in range(3, 2, -1):
                if board.figures[y][i] != None: return False
                saved_field = copy.deepcopy(board.figures)
                board.place_figure([y, 4], [y, i])
                if board.check_if_check(ref_king_is_white=self.is_white): 
                    board.figures = saved_field
                    return False
                board.figures = saved_field
            return True
        elif a == [y, 4] and b == [y, 6]:
            if board.check_if_check(ref_king_is_white=self.is_white): return False
            for i in range(5, 7):
                if board.figures[y][i] != None: return False
                saved_field = copy.deepcopy(board.figures)
                board.place_figure([y, 4], [y, i])
                if board.check_if_check(ref_king_is_white=self.is_white): 
                    board.figures = saved_field
                    return False
                board.figures = saved_field
            return True
        else:
            return False



    def move_possible(self, a:tuple,b:tuple, board:Board, func_check) -> bool:
        if b in self.next_psb_moves(a, board, func_check): return True
        elif self.check_rochade(a, b, board): return True
        else: return False


    def next_psb_moves(self, a, board:Board, func_check) -> list:
        moves_lst = []
        if func_check((a[0], a[1]+1)):
            if board.figures[a[0]][a[1]+1] == None:
                moves_lst.append([a[0], a[1]+1])
            elif board.figures[a[0]][a[1]+1].is_white != self.is_white:
                moves_lst.append([a[0], a[1]+1])

        if func_check((a[0], a[1]-1)):
            if board.figures[a[0]][a[1]-1] == None:
                moves_lst.append([a[0], a[1]-1])
            elif board.figures[a[0]][a[1]-1].is_white != self.is_white:
                moves_lst.append([a[0], a[1]-1])

        if func_check((a[0]+1, a[1]+1)):
            if board.figures[a[0]+1][a[1]+1] == None:
                moves_lst.append([a[0]+1, a[1]+1])
            elif board.figures[a[0]+1][a[1]+1].is_white != self.is_white:
                moves_lst.append([a[0]+1, a[1]+1])

        if func_check((a[0]+1, a[1]-1)):
            if board.figures[a[0]+1][a[1]-1] == None:
                moves_lst.append([a[0]+1, a[1]-1])
            elif board.figures[a[0]+1][a[1]-1].is_white != self.is_white:
                moves_lst.append([a[0]+1, a[1]-1])

        if func_check((a[0]-1, a[1]+1)):
            if board.figures[a[0]-1][a[1]+1] == None:
                moves_lst.append([a[0]-1, a[1]+1])
            elif board.figures[a[0]-1][a[1]+1].is_white != self.is_white:
                moves_lst.append([a[0]-1, a[1]+1])

        if func_check((a[0]-1, a[1]-1)):
            if board.figures[a[0]-1][a[1]-1] == None:
                moves_lst.append([a[0]-1, a[1]-1])
            elif board.figures[a[0]-1][a[1]-1].is_white != self.is_white:
                moves_lst.append([a[0]-1, a[1]-1])

        if func_check((a[0]+1, a[1])):
            if board.figures[a[0]+1][a[1]] == None:
                moves_lst.append([a[0]+1, a[1]])
            elif board.figures[a[0]+1][a[1]].is_white != self.is_white:
                moves_lst.append([a[0]+1, a[1]])

        if func_check((a[0]-1, a[1])):
            if board.figures[a[0]-1][a[1]] == None:
                moves_lst.append([a[0]-1, a[1]])
            elif board.figures[a[0]-1][a[1]].is_white != self.is_white:
                moves_lst.append([a[0]-1, a[1]])

        return moves_lst

        

class Knight:
    def __init__(self, is_white):
        if type(is_white) is not bool: raise ValueError('is_white must be of type bool')
        self.is_white = is_white


    def move_possible(self, a:tuple,b:tuple, board:Board, func_check) -> bool:
        if b in self.next_psb_moves(a, board, func_check): return True
        else: return False

    def next_psb_moves(self, a, board:Board, func_check) -> list:
        moves_lst = []
        if func_check((a[0]+2, a[1]+1)):
            if board.figures[a[0]+2][a[1]+1] == None:
                moves_lst.append([a[0]+2, a[1]+1])
            elif board.figures[a[0]+2][a[1]+1].is_white != self.is_white:
                moves_lst.append([a[0]+2, a[1]+1])
        if func_check((a[0]+2, a[1]-1)):
            if board.figures[a[0]+2][a[1]-1] == None:
                moves_lst.append([a[0]+2, a[1]-1])
            elif board.figures[a[0]+2][a[1]-1].is_white != self.is_white:
                moves_lst.append([a[0]+2, a[1]-1])
        if func_check((a[0]-2, a[1]+1)):
            if board.figures[a[0]-2][a[1]+1] == None:
                moves_lst.append([a[0]-2, a[1]+1])
            elif board.figures[a[0]-2][a[1]+1].is_white != self.is_white:
                moves_lst.append([a[0]-2, a[1]+1])
        if func_check((a[0]-2, a[1]-1)):
            if board.figures[a[0]-2][a[1]-1] == None:
                moves_lst.append([a[0]-2, a[1]-1])
            elif board.figures[a[0]-2][a[1]-1].is_white != self.is_white:
                moves_lst.append([a[0]-2, a[1]-1])

        if func_check((a[0]+1, a[1]+2)):
            if board.figures[a[0]+1][a[1]+2] == None:
                moves_lst.append([a[0]+1, a[1]+2])
            elif board.figures[a[0]+1][a[1]+2].is_white != self.is_white:
                moves_lst.append([a[0]+1, a[1]+2])    
        if func_check((a[0]+1, a[1]-2)):
            if board.figures[a[0]+1][a[1]-2] == None:
                moves_lst.append([a[0]+1, a[1]-2])
            elif board.figures[a[0]+1][a[1]-2].is_white != self.is_white:
                moves_lst.append([a[0]+1, a[1]-2])
        if func_check((a[0]-1, a[1]+2)):
            if board.figures[a[0]-1][a[1]+2] == None:
                moves_lst.append([a[0]-1, a[1]+2])
            elif board.figures[a[0]-1][a[1]+2].is_white != self.is_white:
                moves_lst.append([a[0]-1, a[1]+2])
        if func_check((a[0]-1, a[1]-2)):
            if board.figures[a[0]-1][a[1]-2] == None:
                moves_lst.append([a[0]-1, a[1]-2])
            elif board.figures[a[0]-1][a[1]-2].is_white != self.is_white:
                moves_lst.append([a[0]-1, a[1]-2])

        return moves_lst
    

class Pawn:
    def __init__(self, is_white):
        if type(is_white) is not bool: raise ValueError('is_white must be of type bool')
        self.is_white = is_white

    def move_possible(self, a:tuple,b:tuple, board:Board, func_check) -> bool:
        if b in self.next_psb_moves(a, board, func_check): return True
        else: return False

    def next_psb_moves(self, a, board:Board, func_check) -> list:
        moves_lst = []
        if self.is_white:
            move_dir = +1
            pos_spawn_pawn_line = 1 
        else:
            move_dir = -1
            pos_spawn_pawn_line = 6

        if func_check((a[0]+move_dir, a[1])): #forward 1 step
            if board.figures[a[0]+move_dir][a[1]] == None: moves_lst.append([a[0]+move_dir, a[1]])
        if func_check((a[0]+move_dir*2, a[1])): #forward 2 steps
            if (board.figures[a[0]+move_dir*2][a[1]] == None and a[0] == pos_spawn_pawn_line) and (board.figures[a[0]+move_dir][a[1]] == None): moves_lst.append([a[0]+move_dir*2, a[1]])
        if func_check((a[0]+move_dir, a[1]+1)): #foward right
            if board.figures[a[0]+move_dir][a[1]+1] != None: 
                if board.figures[a[0]+move_dir][a[1]+1].is_white != self.is_white:
                    moves_lst.append([a[0]+move_dir, a[1]+1])
        if func_check((a[0]+move_dir, a[1]-1)): #forward left
            if board.figures[a[0]+move_dir][a[1]-1] != None: 
                if board.figures[a[0]+move_dir][a[1]-1].is_white != self.is_white:
                    moves_lst.append([a[0]+move_dir, a[1]-1])


        return moves_lst




class Game:
    def __init__(self):
        self.board = Board(use_pre_field=True)

    def game(self):
        while self.board.game_active:
            str_a = input('Position of the figure to be moved: ')
            str_b = input('Destination of the figure to be moved: ')
            a = self.board.convert_chess_coordinates(str_a)
            b = self.board.convert_chess_coordinates(str_b)
            match self.board.main(a, b):
                case 0:
                    print(self.board.return_codes[0])
                case 1:
                    print(self.board.return_codes[1])
                case 2:
                    print(self.board.return_codes[2])
                case 3:
                    print(self.board.return_codes[3])
                case 4:
                    print(self.board.return_codes[4])   
                case 5:
                    print(self.board.return_codes[5])


if __name__ == "__main__":
    game = Game()
    game.game()

        