import pygame
import chess

class ChessVisualizer:
    def __init__(self, board:chess.Board):
        self.width, self.height = 800, 800
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.playground = pygame.Surface((self.width, self.height))
        self.board = board
        self.playgound_surfaces = []

        self.bishop_w = pygame.image.load("figures/white-bishop.png").convert_alpha()
        self.bishop_b = pygame.image.load("figures/black-bishop.png").convert_alpha()
        self.rook_w = pygame.image.load("figures/white-rook.png").convert_alpha()
        self.rook_b = pygame.image.load("figures/black-rook.png").convert_alpha()
        self.queen_w = pygame.image.load("figures/white-queen.png").convert_alpha()
        self.queen_b = pygame.image.load("figures/black-queen.png").convert_alpha()
        self.knight_w = pygame.image.load("figures/white-knight.png").convert_alpha()
        self.knight_b = pygame.image.load("figures/black-knight.png").convert_alpha()
        self.pawn_w = pygame.image.load("figures/white-pawn.png").convert_alpha()
        self.pawn_b = pygame.image.load("figures/black-pawn.png").convert_alpha()
        self.king_w = pygame.image.load("figures/white-king.png").convert_alpha()
        self.king_b = pygame.image.load("figures/black-king.png").convert_alpha()
        self.size_figures = (90, 90)

        self.bishop_w = pygame.transform.scale(self.bishop_w, self.size_figures)
        self.bishop_b = pygame.transform.scale(self.bishop_b, self.size_figures)
        self.rook_w = pygame.transform.scale(self.rook_w, self.size_figures)
        self.rook_b = pygame.transform.scale(self.rook_b, self.size_figures)
        self.queen_w = pygame.transform.scale(self.queen_w, self.size_figures)
        self.queen_b = pygame.transform.scale(self.queen_b, self.size_figures)
        self.knight_w = pygame.transform.scale(self.knight_w, self.size_figures)
        self.knight_b = pygame.transform.scale(self.knight_b, self.size_figures)
        self.pawn_w = pygame.transform.scale(self.pawn_w, self.size_figures)
        self.pawn_b = pygame.transform.scale(self.pawn_b, self.size_figures)
        self.king_w = pygame.transform.scale(self.king_w, self.size_figures)
        self.king_b = pygame.transform.scale(self.king_b, self.size_figures)
        self.create_rect_fields()


    def create_rect_fields(self):
        for i in range(8):
            list = []
            for j in range(8):
                list.append(pygame.Rect((self.width/8*j), self.height-(self.height/8*i)-self.height/8, self.width/8, self.height/8))
            self.playgound_surfaces.append(list)


    def draw_field(self):
        for i in range(8):
            for j in range(8):
                if (i+j)%2 == 0:
                    pygame.draw.rect(self.playground, (0,170,102), self.playgound_surfaces[i][j])
                else:
                    pygame.draw.rect(self.playground, (236,236,215), self.playgound_surfaces[i][j])
        self.screen.blit(self.playground, (0,0))


    def draw_figures(self, except_figures:list=None):
        for i in range(8):
            for j in range(8):
                match type(self.board.figures[i][j]):
                    case chess.Rook:
                        if except_figures is None or [i,j] not in except_figures:
                            if self.board.figures[i][j].is_white:
                                self.screen.blit(self.rook_w, ((j*(self.width/8)-self.size_figures[0]//2)+(self.width/8)/2, (self.height-(i*self.height/8)-(self.height/8)-self.size_figures[1]//2)+(self.height/8)/2))
                            else:
                                self.screen.blit(self.rook_b, ((j*(self.width/8)-self.size_figures[0]//2)+(self.width/8)/2, (self.height-(i*self.height/8)-(self.height/8)-self.size_figures[1]//2)+(self.height/8)/2))
                    case chess.Bishop:
                        if except_figures is None or [i,j] not in except_figures:
                            if self.board.figures[i][j].is_white:
                                self.screen.blit(self.bishop_w, ((j*(self.width/8)-self.size_figures[0]//2)+(self.width/8)/2, (self.height-(i*self.height/8)-(self.height/8)-self.size_figures[1]//2)+(self.height/8)/2))
                            else:
                                self.screen.blit(self.bishop_b, ((j*(self.width/8)-self.size_figures[0]//2)+(self.width/8)/2, (self.height-(i*self.height/8)-(self.height/8)-self.size_figures[1]//2)+(self.height/8)/2))

                    case chess.Knight:
                        if except_figures is None or [i,j] not in except_figures:
                            if self.board.figures[i][j].is_white:
                                self.screen.blit(self.knight_w, ((j*(self.width/8)-self.size_figures[0]//2)+(self.width/8)/2, (self.height-(i*self.height/8)-(self.height/8)-self.size_figures[1]//2)+(self.height/8)/2))
                            else:
                                self.screen.blit(self.knight_b, ((j*(self.width/8)-self.size_figures[0]//2)+(self.width/8)/2, (self.height-(i*self.height/8)-(self.height/8)-self.size_figures[1]//2)+(self.height/8)/2))
                    case chess.Queen:
                        if except_figures is None or [i,j] not in except_figures:
                            if self.board.figures[i][j].is_white:
                                self.screen.blit(self.queen_w, ((j*(self.width/8)-self.size_figures[0]//2)+(self.width/8)/2, (self.height-(i*self.height/8)-(self.height/8)-self.size_figures[1]//2)+(self.height/8)/2))
                            else:
                                self.screen.blit(self.queen_b, ((j*(self.width/8)-self.size_figures[0]//2)+(self.width/8)/2, (self.height-(i*self.height/8)-(self.height/8)-self.size_figures[1]//2)+(self.height/8)/2))

                    case chess.King:
                        if except_figures is None or [i,j] not in except_figures:
                            if self.board.figures[i][j].is_white:
                                self.screen.blit(self.king_w, ((j*(self.width/8)-self.size_figures[0]//2)+(self.width/8)/2, (self.height-(i*self.height/8)-(self.height/8)-self.size_figures[1]//2)+(self.height/8)/2))
                            else:
                                self.screen.blit(self.king_b, ((j*(self.width/8)-self.size_figures[0]//2)+(self.width/8)/2, (self.height-(i*self.height/8)-(self.height/8)-self.size_figures[1]//2)+(self.height/8)/2))

                    case chess.Pawn:
                        if except_figures is None or [i,j] not in except_figures:
                            if self.board.figures[i][j].is_white:
                                self.screen.blit(self.pawn_w, ((j*(self.width/8)-self.size_figures[0]//2)+(self.width/8)/2, (self.height-(i*self.height/8)-(self.height/8)-self.size_figures[1]//2)+(self.height/8)/2))
                            else:
                                self.screen.blit(self.pawn_b, ((j*(self.width/8)-self.size_figures[0]//2)+(self.width/8)/2, (self.height-(i*self.height/8)-(self.height/8)-self.size_figures[1]//2)+(self.height/8)/2))



    def get_image_from_obj(self, obj):
        match type(obj):
            case chess.Rook:
                if obj.is_white:
                    return self.rook_w
                else:
                    return self.rook_b
            case chess.Bishop:
                if obj.is_white:
                    return self.bishop_w
                else:
                    return self.bishop_b
                
            case chess.Knight:
                if obj.is_white:
                    return self.knight_w
                else:
                    return self.knight_b
                
            case chess.Queen:
                if obj.is_white:
                    return self.queen_w
                else:
                    return self.queen_b
                
            case chess.King:
                if obj.is_white:
                    return self.king_w
                else:
                    return self.king_b
            
            case chess.Pawn:
                if obj.is_white:
                    return self.pawn_w
                else:
                    return self.pawn_b
                     

    def main(self):
        running = True
        self.draw_field()
        self.draw_figures()
        pygame.display.flip()
        a = None
        b = None
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEMOTION and a is not None:
                    self.draw_field()
                    self.draw_figures(except_figures=[a])
                    mouse_pos = pygame.mouse.get_pos()
                    self.screen.blit(self.tageted_image, (mouse_pos[0]-self.size_figures[0]//2, mouse_pos[1]-self.size_figures[1]//2))

                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if event.button == 1: 
                        for i in range(8):
                            for j in range(8):
                                if self.playgound_surfaces[i][j].collidepoint(mouse_pos) and self.board.figures[i][j] is not None:
                                    a = [i, j]
                                    self.tageted_image = self.get_image_from_obj(self.board.figures[i][j])
                                    
                                    
                if event.type == pygame.MOUSEBUTTONUP:
                    mouse_pos = pygame.mouse.get_pos()
                    for i in range(8):
                        for j in range(8):
                            if self.playgound_surfaces[i][j].collidepoint(mouse_pos):
                                if a is not None:
                                    b = [i, j]
                                    self.figs_old = self.board.figures
                                    match self.board.main(a,b):
                                        case 0: #move was successful
                                            self.draw_field()
                                            self.draw_figures()
                                        case 1 | 4: #cannot move this way
                                            self.draw_field()
                                            self.draw_figures()
                                            print(f"Cannot move {self.board.convert_coordinates_in_str(a)} to {self.board.convert_coordinates_in_str(b)}")
                                        case 2: #checmkate, white won
                                            self.draw_field()
                                            self.draw_figures()
                                            print("White has won the game")
                                            
                                        case 3: #checkmate, black has won
                                            self.draw_field()
                                            self.draw_figures()
                                            print("Black has won the game")
                                        
                                        case 5: #game over
                                            print("Game is over")

                                    self.figs_new = self.board.figures 
                                    a,b = None, None

                
                pygame.display.flip()

board = chess.Board()
game = ChessVisualizer(board)
game.main()