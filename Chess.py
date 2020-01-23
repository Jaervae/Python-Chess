# Import the pygame library and initialise the game engine
import pygame, sys, os, time
from pygame.locals import *

pygame.init()
pygame.font.init()

# Define some colors
WHITE = (255, 255, 255)
DARKBROWN = (89, 54, 17)
LIGHTBROWN = (253, 198, 139)

# Define some sizes
SIZE_H = 1000
SIZE_V = 800
SQUARE_SIDE = SIZE_V / 8

SQUARE_LIST = []
CHARTER_LIST = []

SIZE = (SIZE_H, SIZE_V)
SCREEN = pygame.display.set_mode(SIZE)

#Define pieces
BLACK_KING = 'blackKing'
BLACK_QUEEN = 'blackQueen'
BLACK_ROOK = 'blackRook'
BLACK_KNIGHT = 'blackKnight'
BLACK_BISHOP = 'blackBishop'
BLACK_PAWN = 'blackPawn'

WHITE_KING = 'whiteKing'
WHITE_QUEEN = 'whiteQueen'
WHITE_ROOK = 'whiteRook'
WHITE_KNIGHT = 'whiteKnight'
WHITE_BISHOP = 'whiteBishop'
WHITE_PAWN = 'whitePawn'

PLAYING_WHITE = True
WHITE_TURN = True

HORIZONTAL_ROW = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
VERTICAL_ROW = ['8', '7', '6', '5', '4', '3', '2', '1']


class Squares:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

class Pawn:
    def __init__(self, image, xPos, yPos, pawn, squareID):
        self.image = image
        self.xPos = xPos
        self.yPos = yPos
        self.pawn = pawn
        self.squareID = squareID

def InitializeSquares():
    i = 8
    xRow = 0
    yRow = 0
    charterID = 0
    while i > 0:
        for x in HORIZONTAL_ROW:
            name = x + str(i)
            xPos = (xRow * SQUARE_SIDE)
            yPos = (yRow * SQUARE_SIDE)
            charter = 'none'
            if name[1] == '8' or name[1] == '7' or name[1] == '2' or name[1] == '1':
                charter = GetPlacement(name)
                image = load_image(charter + ".gif")
                CHARTER_LIST.append(Pawn(image,xPos,yPos,charter,name))
                charterID += 1

            name = Squares(name, xPos, yPos)
            SQUARE_LIST.append(name)
            xRow += 1
            
            #print('Name:' + name.name +', X=' + str(name.x) + ', Y=' + str(name.y))
        i -= 1
        xRow = 0
        yRow += 1

def GetPlacement(name):
    if name[1] == '7':
        if PLAYING_WHITE:
            return BLACK_PAWN
        else:
            return WHITE_PAWN

    elif name[1] == '2':
        if PLAYING_WHITE:
            return WHITE_PAWN
        else:
            return BLACK_PAWN

    elif name == 'a8' or name == 'h8':
        if PLAYING_WHITE:
            return BLACK_ROOK
        else:
            return WHITE_ROOK

    elif name == 'b8' or name == 'g8':
        if PLAYING_WHITE:
            return BLACK_KNIGHT
        else:
            return WHITE_KNIGHT

    elif name == 'c8' or name == 'f8':
        if PLAYING_WHITE:
            return BLACK_BISHOP
        else:
            return WHITE_BISHOP
    
    elif name == 'd8' :
        if PLAYING_WHITE:
            return BLACK_QUEEN
        else:
            return WHITE_KING

    elif name == 'e8' :
        if PLAYING_WHITE:
            return BLACK_KING
        else:
            return WHITE_QUEEN

    elif name == 'a1' or name == 'h1':
        if PLAYING_WHITE:
            return WHITE_ROOK
        else:
            return BLACK_ROOK

    elif name == 'b1' or name == 'g1':
        if PLAYING_WHITE:
            return WHITE_KNIGHT
        else:
            return BLACK_KNIGHT

    elif name == 'c1' or name == 'f1':
        if PLAYING_WHITE:
            return WHITE_BISHOP
        else:
            return BLACK_BISHOP
  
    elif name == 'd1':
        if PLAYING_WHITE:
            return WHITE_QUEEN
        else:
            return BLACK_KING

    elif name == 'e1':
        if PLAYING_WHITE:
            return WHITE_KING
        else:
            return BLACK_QUEEN
    else:
        return 'none'

def GetClickedSquare(mouseX,mouseY):
    square = ''
  
    #Get matching alphabet
    if mouseX < 100:
        square += 'a'
    elif mouseX < 200:
        square += 'b'
    elif mouseX < 300:
        square += 'c'
    elif mouseX < 400:
        square += 'd'
    elif mouseX < 500:
        square += 'e'
    elif mouseX < 600:
        square += 'f'
    elif mouseX < 700:
        square += 'g'
    elif mouseX < 800:
        square += 'h'

    #Get matching number
    if mouseY < 100:
        square += '8'
    elif mouseY < 200:
        square += '7'
    elif mouseY < 300:
        square += '6'
    elif mouseY < 400:
        square += '5'
    elif mouseY < 500:
        square += '4'
    elif mouseY < 600:
        square += '3'
    elif mouseY < 700:
        square += '2'
    elif mouseY < 800:
        square += '1'

    return square

def load_image(name, colorkey=None):
    "loads an image, prepares it for play"
    fullname = os.path.join('data', name)
    try:
        surface = pygame.image.load(fullname)
    except pygame.error:
        raise SystemExit, 'Could not load image "%s" %s'%(file, pygame.get_error())
    if colorkey is not None:
        if colorkey is -1:
            colorkey = surface.get_at((0,0))
        surface.set_colorkey(colorkey, RLEACCEL)
    return surface.convert()

def DrawBoard():
    rowX = 0
    rowY = 0
    while rowY < 8:
        while rowX < 8:
            if (rowY % 2) == 0 and rowX == 0:
                pygame.draw.rect(SCREEN, LIGHTBROWN, [(rowX * SQUARE_SIDE), (rowY * SQUARE_SIDE), SQUARE_SIDE, SQUARE_SIDE], 0)
                rowX += 2
            elif rowX == 0:
                rowX += 1

            pygame.draw.rect(SCREEN, LIGHTBROWN, [(rowX * SQUARE_SIDE), (rowY * SQUARE_SIDE), SQUARE_SIDE, SQUARE_SIDE], 0)
            rowX += 2
        rowY += 1
        rowX = 0

def GetSuitablePlace(square):
    x = square[0]
    y = square[1]

    if x == 'a':
        x = 0
    elif x == 'b':
        x = 100
    elif x == 'c':
        x = 200
    elif x == 'd':
        x = 300
    elif x == 'e':
        x = 400
    elif x == 'f':
        x = 500
    elif x == 'g':
        x = 600
    else:
        x = 700

    if y == '8':
        y = 0
    elif y == '7':
        y = 100
    elif y == '6':
        y = 200
    elif y == '5':
        y = 300
    elif y == '4':
        y = 400
    elif y == '3':
        y = 500
    elif y == '2':
        y = 600
    else:
        y = 700

    return int(x), int(y)

def HighlightClickedSquare(squareID):
    x,y = GetSuitablePlace(squareID)
    pygame.draw.line(SCREEN, WHITE, [x, y], [(x + SQUARE_SIDE), y], 5) 
    pygame.draw.line(SCREEN, WHITE, [x, (y + SQUARE_SIDE)], [(x + SQUARE_SIDE), (y + SQUARE_SIDE)], 5)
    pygame.draw.line(SCREEN, WHITE, [x, y], [x, (y + SQUARE_SIDE)], 5)
    pygame.draw.line(SCREEN, WHITE, [(x + SQUARE_SIDE), y], [(x + SQUARE_SIDE), (y + SQUARE_SIDE)], 5)

def CheckMove(pawn,squareID):
    horizontal = squareID[0]
    vertical = squareID[1]
    color = pawn [:5]
    pawnType = pawn[5:]
    avaibleSquares = []
    if pawnType == 'Pawn':
        if color == 'white' and PLAYING_WHITE:
            avaibleSquares.append(HORIZONTAL_ROW[(HORIZONTAL_ROW.index(horizontal) - 1)] + str(int(vertical) + 1))
            avaibleSquares.append(HORIZONTAL_ROW[HORIZONTAL_ROW.index(horizontal)] + str(int(vertical) + 1))
            avaibleSquares.append(HORIZONTAL_ROW[HORIZONTAL_ROW.index(horizontal)] + str(int(vertical) + 2))
            avaibleSquares.append(HORIZONTAL_ROW[(HORIZONTAL_ROW.index(horizontal) + 1)] + str(int(vertical) + 1))
            print(avaibleSquares)


def main(start):

    pygame.display.set_caption("Chess")

    myfont = pygame.font.SysFont('Comic Sans MS', 30)

    preparation = True
    playing = False

    pawnSelected = ""
    squareSelected = ""
    preClickedSquare = ""
    selected = ""
    whoseTurn = "White's"
    WHITE_TURN = True

    # The clock will be used to control how fast the screen updates
    clock = pygame.time.Clock()
    mx,my = pygame.mouse.get_pos()
    InitializeSquares()
    # -------- Main Program Loop -----------

    while preparation:
        preparation = False
        playing = True
    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                playing = False 
            elif event.type == event.type == KEYDOWN and event.key == K_q:
                playing = False 
                pass
            elif event.type == KEYDOWN and event.key == K_m:
                for x in CHARTER_LIST:
                    print(x)

            elif event.type == MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                clickedSquare = GetClickedSquare(mx,my)
                for x in SQUARE_LIST:
                    if x.name == clickedSquare:
                        preClickedSquare = clickedSquare


            elif event.type == MOUSEBUTTONUP:
                mx, my = pygame.mouse.get_pos()
                clickedSquare = GetClickedSquare(mx,my)
                for charter in CHARTER_LIST:
                    if  clickedSquare == preClickedSquare:
                        if charter.squareID == preClickedSquare:
                            if WHITE_TURN and charter.pawn[0] == 'w' or not WHITE_TURN and charter.pawn[0] == 'b':
                                if pawnSelected == "":
                                    print('selected: ' + charter.pawn)
                                    pawnSelected = charter.pawn
                                    squareSelected = clickedSquare
                                    selected = charter
                                    CheckMove(selected.pawn, selected.squareID)
                                    break
                                elif pawnSelected != "" and clickedSquare == squareSelected:
                                    pawnSelected = ""
                                    squareSelected = ""
                                    break
                        elif charter.squareID != preClickedSquare:
                            if clickedSquare != squareSelected and pawnSelected != "":
                                #Check if already pawn in square
                                for y in CHARTER_LIST:
                                    if y.squareID == clickedSquare:
                                        if y.pawn[0] != selected.pawn[0]:
                                            print(y.squareID)
                                            CHARTER_LIST.remove(y)
                                        else:
                                            clickedSquare = squareSelected
                                newX,newY = GetSuitablePlace(clickedSquare)
                                selected.xPos = newX
                                selected.yPos = newY
                                selected.squareID = clickedSquare
                                pawnSelected = ""
                                squareSelected = ""
                                WHITE_TURN = not WHITE_TURN
                                if WHITE_TURN:
                                    whoseTurn = "White's"
                                else:
                                    whoseTurn = "Black's"
                                break
                        

                          
        SCREEN.fill(WHITE)
        pygame.draw.rect(SCREEN, DARKBROWN, [0, 0, SIZE_H - 200, SIZE_V], 0)
        DrawBoard()
        for x in CHARTER_LIST:
            SCREEN.blit(x.image,(x.xPos, x.yPos))
        if pawnSelected != "":
            HighlightClickedSquare(squareSelected)
        textsurface = myfont.render(whoseTurn + " turn", False, (0, 0, 0))
        SCREEN.blit(textsurface,(800,0))
        clock.tick(60)
        pygame.display.flip()
        

    pygame.quit()

if __name__ == '__main__': main(0)
