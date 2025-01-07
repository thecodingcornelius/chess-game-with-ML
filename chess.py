import copy

class Bishop:
    def __init__(self, is_white):
        self.is_white = is_white
    
    def move_possible(self, a:tuple,b:tuple, field, func_check) -> bool:
        if b in self.next_psb_moves(a, field, func_check): return True
        else: return False

    def next_psb_moves(self, a, field, func_check) -> list:
        moves_lst = []
        curr_pos = a.copy() #auch wegen Referenzweitergabe

        while True:
            curr_pos[0] += 1
            curr_pos[1] += 1
            if func_check(curr_pos):
                if field[curr_pos[0]][curr_pos[1]] == None:
                    moves_lst.append(curr_pos.copy()) #Referenzweitergabe umgehen!
                elif field[curr_pos[0]][curr_pos[1]].is_white != self.is_white:
                    moves_lst.append(curr_pos.copy()) #Referenzweitergabe umgehen!
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
                if field[curr_pos[0]][curr_pos[1]] == None:
                    moves_lst.append(curr_pos.copy()) #Referenzweitergabe umgehen!
                elif field[curr_pos[0]][curr_pos[1]].is_white != self.is_white:
                    moves_lst.append(curr_pos.copy()) #Referenzweitergabe umgehen!
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
                if field[curr_pos[0]][curr_pos[1]] == None:
                    moves_lst.append(curr_pos.copy()) #Referenzweitergabe umgehen!
                elif field[curr_pos[0]][curr_pos[1]].is_white != self.is_white:
                    moves_lst.append(curr_pos.copy()) #Referenzweitergabe umgehen!
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
                if field[curr_pos[0]][curr_pos[1]] == None:
                    moves_lst.append(curr_pos.copy()) #Referenzweitergabe umgehen!
                elif field[curr_pos[0]][curr_pos[1]].is_white != self.is_white:
                    moves_lst.append(curr_pos.copy()) #Referenzweitergabe umgehen!
                    break
                else:
                    break
            else:
                break

        return moves_lst

        

class Rook:
    def __init__(self, is_white):
        self.is_white = is_white

    def move_possible(self, a:tuple,b:tuple, field, func_check) -> bool:
        if b in self.next_psb_moves(a, field, func_check): return True
        else: return False

    def next_psb_moves(self, a, field, func_check) -> list:
        moves_lst = []
        curr_pos = a.copy()

        while True:
            curr_pos[1] += 1
            if func_check(curr_pos):
                if field[curr_pos[0]][curr_pos[1]] == None:
                    moves_lst.append(curr_pos.copy()) #Referenzweitergabe umgehen!
                elif field[curr_pos[0]][curr_pos[1]].is_white != self.is_white:
                    moves_lst.append(curr_pos.copy()) #Referenzweitergabe umgehen!
                    break
                else:
                    break
            else:
                break

        curr_pos = a.copy()
        while True:
            curr_pos[1] -= 1
            if func_check(curr_pos):
                if field[curr_pos[0]][curr_pos[1]] == None:
                    moves_lst.append(curr_pos.copy()) #Referenzweitergabe umgehen!
                elif field[curr_pos[0]][curr_pos[1]].is_white != self.is_white:
                    moves_lst.append(curr_pos.copy()) #Referenzweitergabe umgehen!
                    break
                else:
                    break
            else:
                break

        curr_pos = a.copy()
        while True:
            curr_pos[0] += 1
            if func_check(curr_pos):
                if field[curr_pos[0]][curr_pos[1]] == None:
                    moves_lst.append(curr_pos.copy()) #Referenzweitergabe umgehen!
                elif field[curr_pos[0]][curr_pos[1]].is_white != self.is_white:
                    moves_lst.append(curr_pos.copy()) #Referenzweitergabe umgehen!
                    break
                else:
                    break
            else:
                break


        curr_pos = a.copy()
        while True:
            curr_pos[0] -= 1
            if func_check(curr_pos):
                if field[curr_pos[0]][curr_pos[1]] == None:
                    moves_lst.append(curr_pos.copy()) #Referenzweitergabe umgehen!
                elif field[curr_pos[0]][curr_pos[1]].is_white != self.is_white:
                    moves_lst.append(curr_pos.copy()) #Referenzweitergabe umgehen!
                    break
                else:
                    break
            else:
                break

        return moves_lst


class Queen(Rook, Bishop):
    def __init__(self, is_white):
        self.is_white = is_white

    def move_possible(self, a:tuple,b:tuple, field, func_check) -> bool:
        if b in self.next_psb_moves(a, field, func_check): return True
        else: return False

    def next_psb_moves(self, a, field, func_check) -> list:
        return Rook.next_psb_moves(self, a, field, func_check) + Bishop.next_psb_moves(self, a, field, func_check) 

class King:
    def __init__(self, is_white):
        self.is_white = is_white

    def move_possible(self, a:tuple,b:tuple, field, func_check) -> bool:
        if b in self.next_psb_moves(a, field, func_check): return True
        else: return False


    def next_psb_moves(self, a, field, func_check) -> list:
        moves_lst = []
        if func_check((a[0], a[1]+1)):
            if field[a[0]][a[1]+1] == None:
                moves_lst.append([a[0], a[1]+1])
            elif field[a[0]][a[1]+1].is_white != self.is_white:
                moves_lst.append([a[0], a[1]+1])

        if func_check((a[0], a[1]-1)):
            if field[a[0]][a[1]-1] == None:
                moves_lst.append([a[0], a[1]-1])
            elif field[a[0]][a[1]-1].is_white != self.is_white:
                moves_lst.append([a[0], a[1]-1])

        if func_check((a[0]+1, a[1]+1)):
            if field[a[0]+1][a[1]+1] == None:
                moves_lst.append([a[0]+1, a[1]+1])
            elif field[a[0]+1][a[1]+1].is_white != self.is_white:
                moves_lst.append([a[0]+1, a[1]+1])

        if func_check((a[0]+1, a[1]-1)):
            if field[a[0]+1][a[1]-1] == None:
                moves_lst.append([a[0]+1, a[1]-1])
            elif field[a[0]+1][a[1]-1].is_white != self.is_white:
                moves_lst.append([a[0]+1, a[1]-1])

        if func_check((a[0]-1, a[1]+1)):
            if field[a[0]-1][a[1]+1] == None:
                moves_lst.append([a[0]-1, a[1]+1])
            elif field[a[0]-1][a[1]+1].is_white != self.is_white:
                moves_lst.append([a[0]-1, a[1]+1])

        if func_check((a[0]-1, a[1]-1)):
            if field[a[0]-1][a[1]-1] == None:
                moves_lst.append([a[0]-1, a[1]-1])
            elif field[a[0]-1][a[1]-1].is_white != self.is_white:
                moves_lst.append([a[0]-1, a[1]-1])

        if func_check((a[0]+1, a[1])):
            if field[a[0]+1][a[1]] == None:
                moves_lst.append([a[0]+1, a[1]])
            elif field[a[0]+1][a[1]].is_white != self.is_white:
                moves_lst.append([a[0]+1, a[1]])

        if func_check((a[0]-1, a[1])):
            if field[a[0]-1][a[1]] == None:
                moves_lst.append([a[0]-1, a[1]])
            elif field[a[0]-1][a[1]].is_white != self.is_white:
                moves_lst.append([a[0]-1, a[1]])

        return moves_lst

        

class Knight:
    def __init__(self, is_white):
        self.is_white = is_white


    def move_possible(self, a:tuple,b:tuple, field, func_check) -> bool:
        if b in self.next_psb_moves(a, field, func_check): return True
        else: return False

    def next_psb_moves(self, a, field, func_check) -> list:
        moves_lst = []
        if func_check((a[0]+2, a[1]+1)):
            if field[a[0]+2][a[1]+1] == None:
                moves_lst.append([a[0]+2, a[1]+1])
            elif field[a[0]+2][a[1]+1].is_white != self.is_white:
                moves_lst.append([a[0]+2, a[1]+1])
        if func_check((a[0]+2, a[1]-1)):
            if field[a[0]+2][a[1]-1] == None:
                moves_lst.append([a[0]+2, a[1]-1])
            elif field[a[0]+2][a[1]-1].is_white != self.is_white:
                moves_lst.append([a[0]+2, a[1]-1])
        if func_check((a[0]-2, a[1]+1)):
            if field[a[0]-2][a[1]+1] == None:
                moves_lst.append([a[0]-2, a[1]+1])
            elif field[a[0]-2][a[1]+1].is_white != self.is_white:
                moves_lst.append([a[0]-2, a[1]+1])
        if func_check((a[0]-2, a[1]-1)):
            if field[a[0]-2][a[1]-1] == None:
                moves_lst.append([a[0]-2, a[1]-1])
            elif field[a[0]-2][a[1]-1].is_white != self.is_white:
                moves_lst.append([a[0]-2, a[1]-1])

        if func_check((a[0]+1, a[1]+2)):
            if field[a[0]+1][a[1]+2] == None:
                moves_lst.append([a[0]+1, a[1]+2])
            elif field[a[0]+1][a[1]+2].is_white != self.is_white:
                moves_lst.append([a[0]+1, a[1]+2])    
        if func_check((a[0]+1, a[1]-2)):
            if field[a[0]+1][a[1]-2] == None:
                moves_lst.append([a[0]+1, a[1]-2])
            elif field[a[0]+1][a[1]-2].is_white != self.is_white:
                moves_lst.append([a[0]+1, a[1]-2])
        if func_check((a[0]-1, a[1]+2)):
            if field[a[0]-1][a[1]+2] == None:
                moves_lst.append([a[0]-1, a[1]+2])
            elif field[a[0]-1][a[1]+2].is_white != self.is_white:
                moves_lst.append([a[0]-1, a[1]+2])
        if func_check((a[0]-1, a[1]-2)):
            if field[a[0]-1][a[1]-2] == None:
                moves_lst.append([a[0]-1, a[1]-2])
            elif field[a[0]-1][a[1]-2].is_white != self.is_white:
                moves_lst.append([a[0]-1, a[1]-2])

        return moves_lst
    

class Pawn:
    def __init__(self, is_white):
        self.is_white = is_white

    def move_possible(self, a:tuple,b:tuple, field, func_check) -> bool:
        if b in self.next_psb_moves(a, field, func_check): return True
        else: return False

    def next_psb_moves(self, a, field, func_check) -> list:
        moves_lst = []
        if self.is_white:
            move_dir = +1
            pos_spawn_pawn_line = 1 
        else:
            move_dir = -1
            pos_spawn_pawn_line = 6


        if func_check((a[0]+move_dir, a[1])): #forward 1 step
            if field[a[0]+move_dir][a[1]] == None: moves_lst.append([a[0]+move_dir, a[1]])
        if func_check((a[0]+move_dir*2, a[1])): #forward 2 steps
            if (field[a[0]+move_dir*2][a[1]] == None and a[0] == pos_spawn_pawn_line) and (field[a[0]+move_dir][a[1]] == None): moves_lst.append([a[0]+move_dir*2, a[1]])
        if func_check((a[0]+move_dir, a[1]+1)): #foward right
            if field[a[0]+move_dir][a[1]+1] != None: 
                if field[a[0]+move_dir][a[1]+1].is_white != self.is_white:
                    moves_lst.append([a[0]+move_dir, a[1]+1])
        if func_check((a[0]+move_dir, a[1]-1)): #forward left
            if field[a[0]+move_dir][a[1]-1] != None: 
                if field[a[0]+move_dir][a[1]-1].is_white != self.is_white:
                    moves_lst.append([a[0]+move_dir, a[1]-1])


        return moves_lst



class Board:
    def __init__(self, use_pre_field=True):
        self.dict = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
        self.dict_around = {1:'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F', 7:'G', 8:'H'}
        self.figures = [[] for _ in range(8)]
        if use_pre_field:
            self.figures[0] = [Rook(is_white=True), Knight(is_white=True), Bishop(is_white=True), Queen(is_white=True), King(is_white=True), Bishop(is_white=True), Knight(is_white=True), Rook(is_white=True)]
            self.figures[1] = [Pawn(is_white=True) for i in range(0,8)]
            for i in range(2,6):
                self.figures[i] = [None for _ in range(8)]
            self.figures[7] = [Rook(is_white=False), Knight(is_white=False), Bishop(is_white=False), Queen(is_white=False), King(is_white=False), Bishop(is_white=False), Knight(is_white=False), Rook(is_white=False)]
            self.figures[6] = [Pawn(is_white=False) for i in range(0,8)]
        else:
            for i in range(8):
                    self.figures[i] = [None for _ in range(8)]

        self.game_active = True
        self.white_turn = True
        self.white_is_winner = None
        self.pos_kings = [[0, 4], [7, 4]] #white = first Element
        self.return_codes = {0: 'Figure was placed', 1: 'Cannot move this figure that way', 2: 'Checkmate, white has won', 3: 'Checkmate, black has won', 4: 'Incorrect pos syntax!', 5: 'Game has already ended'}



    def add_element(self, pos:int, chess_obj):
        self.figures[pos[0]][pos[1]] = chess_obj

    def del_element(self, pos:int):
        self.figures[pos[0]][pos[1]] = None 

    def check_move(self, a:list, b:list) -> bool:
        if self.figures[a[0]][a[1]] == None: return False
        elif self.figures[a[0]][a[1]].move_possible(a, b, self.figures, self.check_coordinate_in_field_range) and ((self.figures[a[0]][a[1]].is_white == True and self.white_turn) or ((self.figures[a[0]][a[1]].is_white != True and self.white_turn == False))): return True
        else: return False
    

    def convert_chess_coordinates(self, str_pos:str) -> list:
        if self.check_right_str_coordinates(str_pos):
            return [int(str_pos[1])-1, self.dict[str_pos[0]]-1] #first element of list marks y-coordinate -> important for the list-field (more readable)
        else:
            return
    
    def convert_coordinates_in_str(self, pos:list) -> str:
        pos = pos.copy()
        pos[0] += 1
        pos[1] += 1
        return self.dict_around[pos[1]] + str(pos[0]) #Sicherheitsmechanismus einbauen, wenns nicht in dict_ist?



    def check_coordinate_in_field_range(self, pos:list) -> bool:
        if ((0<= pos[0] <= 7) and (0<= pos[1] <= 7)):
            return True
        else:
            return False
        
    def check_right_str_coordinates(self, str_pos:str) -> bool:
        if len(str_pos) == 2:
            if str_pos[0] in self.dict.keys() and 49 <= ord(str_pos[1]) <= 56: 
                return True
        else:
            return False

    def __change_pos_kings(self, b, is_white) -> None:
        if is_white:
            self.pos_kings[0] = b.copy()
        else:
            self.pos_kings[1] = b.copy() 



    def place_figure(self, a, b) -> None:
        if type(self.figures[a[0]][a[1]]) is King:
            self.__change_pos_kings(b, self.figures[a[0]][a[1]].is_white)
        self.figures[b[0]][b[1]] = self.figures[a[0]][a[1]]
        self.figures[a[0]][a[1]] = None


    def get_psb_moves(self, str_pos:str) -> list:
        pos = self.convert_chess_coordinates(str_pos)
        fig = self.figures[pos[0]][pos[1]]
        pos_lst = fig.next_psb_moves(pos, self.figures, self.check_coordinate_in_field_range)
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
                safed_pos_kings = self.pos_kings.copy()
                self.place_figure(*coordinates)
                if self.check_if_check(ref_king_is_white=self.white_turn): #check that your own move doesnt check your king
                    self.figures = check_field
                    self.pos_kings = safed_pos_kings
                    return 1

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
        if ref_king_is_white: curr_king = self.pos_kings[0]
        else: curr_king = self.pos_kings[1]

        psb_moves_opponent_element = []
        pos_opponent_elements = self.get_pos_all_elements(is_white=(not ref_king_is_white))


        for e in pos_opponent_elements:
            psb_moves_opponent_element.append(self.figures[e[0]][e[1]].next_psb_moves(e, self.figures, self.check_coordinate_in_field_range))

        for moves_per_figure in psb_moves_opponent_element:
            if curr_king in moves_per_figure:
                return True
        return False
    
    

    def check_checkmate(self, ref_king_is_white) -> list:
        if ref_king_is_white: curr_king = self.pos_kings[0].copy()
        else: curr_king = self.pos_kings[1].copy()

        if self.check_if_check(ref_king_is_white=ref_king_is_white):
            if ref_king_is_white:
                print("White is checked")
            else:
                print("Black is checked")
            psb_moves_king = self.figures[curr_king[0]][curr_king[1]].next_psb_moves(curr_king, self.figures, self.check_coordinate_in_field_range)
            n_possible_moves_king = len(psb_moves_king)

            if n_possible_moves_king > 0:
                for e in psb_moves_king:
                    check_field = copy.deepcopy(self.figures)
                    safed_pos_kings = copy.deepcopy(self.pos_kings)
                    self.place_figure(curr_king, e)
                    if self.check_if_check(ref_king_is_white=ref_king_is_white) is True:
                        n_possible_moves_king -= 1
                    self.figures = check_field
                    self.pos_kings = safed_pos_kings

            print(f'King has {n_possible_moves_king} moves')

            if n_possible_moves_king == 0:#when n_possible_moves_king = 0 and checked -> king cannot move
                #checking if any figure with same color as the threatened king can uncheck
                figure_can_unckeck = False
                pos_own_elements = self.get_pos_all_elements(is_white=ref_king_is_white)
                psb_moves_own_elements = []
                for pos_figure in pos_own_elements:
                    psb_moves_own_elements.append(self.figures[pos_figure[0]][pos_figure[1]].next_psb_moves(pos_figure, self.figures, self.check_coordinate_in_field_range))
                for i_moves_per_figure in range(len(psb_moves_own_elements)):
                    for move in psb_moves_own_elements[i_moves_per_figure]:
                        check_field = copy.deepcopy(self.figures)
                        safed_pos_kings = copy.deepcopy(self.pos_kings)
                        self.place_figure(pos_own_elements[i_moves_per_figure], move)
                        if self.check_if_check(ref_king_is_white=ref_king_is_white) is False:
                            figure_can_unckeck = True
                            print(f"Figure at {self.convert_coordinates_in_str(pos_own_elements[i_moves_per_figure])} can uncheck when going to {self.convert_coordinates_in_str(move)}!")
                        
                        self.figures = check_field
                        self.pos_kings = safed_pos_kings

                return not figure_can_unckeck #when figure_can_unckeck True, should return False, and other way around
            else:
                figure_can_unckeck = False
                for move in psb_moves_king:
                    check_field = copy.deepcopy(self.figures)
                    safed_pos_kings = copy.deepcopy(self.pos_kings)
                    #print(self.convert_coordinates_in_str(self.pos_kings[0]) + " " + self.convert_coordinates_in_str(self.pos_kings[1]))
                    self.place_figure(curr_king, move)
                    #print(self.convert_coordinates_in_str(self.pos_kings[0]) + " " + self.convert_coordinates_in_str(self.pos_kings[1]))
                    if self.check_if_check(ref_king_is_white=ref_king_is_white) is False:
                        figure_can_unckeck = True
                        print(f"King at {self.convert_coordinates_in_str(curr_king)} can escape, when going to {self.convert_coordinates_in_str(move)}!")                  
                    self.figures = check_field
                    self.pos_kings = safed_pos_kings
                return False

                
        else: return False



class Game:
    def __init__(self):
        self.board = Board(use_pre_field=True)

    def game(self):
        while self.board.game_active:
            str_a = input('Stelle der zu bewegenden Figur: ')
            str_b = input('Ziel der zu bewegenden Figur: ')
            pass


if __name__ == "__main__":
    game = Game()
    game.game()

#Code in chess_v02 sinngemäß überprüfen mit Logik
#bei gema_engine figurengröße ändern
#wenn figur angetippt, soll sei sich bewegen
#wenn könig im check, pwan schlägt Springer, andere Figuren bewegen sich auch 
#rochade einbauen

        