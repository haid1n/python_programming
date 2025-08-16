#PythonGeeks- imports
import pygame
import requests

WIDTH = 550
Background_Color = (245,251,250)
buffer = 5

#PythonGeeks- making get request to the api
response_API = requests.get("https://sugoku.herokuapp.com/board?difficulty=easy")
grid_board = response_API.json()['board']
original_grid = [[grid_board[x][y] for y in range(len(grid_board[0]))] for x in range(len(grid_board))]

#PythonGeeks- Function to check if grid position is empty or not
def isEmpty(number):
    if number == 0:
        return True
    return False

#PythonGeeks- Function for checking if the entered value is valid
def isValid(place, number):
    #Check for Column, row and sub-grid
    
    #Checking row
    for i in range(0, len(grid_board[0])):
        if(grid_board[place[0]][i] == number):
            return False
    
    #Checking column
    for i in range(0, len(grid_board[0])):
        if(grid_board[i][place[1]] == number):
            return False
    
    #Check sub-grid  
    x = place[0]//3*3
    y = place[1]//3*3
    
    for i in range(0,3):
        for j in range(0,3):
            if(grid_board[x+i][y+j]== number):
                return False
    return True

#PythonGeeks- Solving Sudoku using Backtracking algorithm
solving = 0
def Sudoku_solver(window):
    Font = pygame.font.SysFont('Comic Sans MS', 35)
    for i in range(0,len(grid_board[0])):
        for j in range(0, len(grid_board[0])):
            if(isEmpty(grid_board[i][j])): 
                for k in range(1,10):
                    if isValid((i,j), k):                   
                        grid_board[i][j] = k
                        pygame.draw.rect(window, Background_Color, ((j+1)*50 + buffer, (i+1)*50+ buffer,50 -2*buffer , 50 - 2*buffer))
                        value = Font.render(str(k), True, (0,0,0))
                        window.blit(value, ((j+1)*50 +15,(i+1)*50))
                        pygame.display.update()
                        pygame.time.delay(10)
                        
                        Sudoku_solver(window)
                        
                        #Exit condition
                        global solving
                        if(solving == 1):
                            return
                        
                        #if sudoku_solver returns, there's a mismatch
                        grid_board[i][j] = 0
                        pygame.draw.rect(window, Background_Color, ((j+1)*50 + buffer, (i+1)*50+ buffer,50 -2*buffer , 50 - 2*buffer))
                        pygame.display.update()
                return               
    solving = 1
        


def main():    
    #initializing pygame
    pygame.init()

    #setting pygame window
    window = pygame.display.set_mode((WIDTH, WIDTH))

    #setting the caption
    pygame.display.set_caption("Sudoku using PythonGeeks")

    #filling background color
    window.fill(Background_Color)

    #declaring the font
    Font = pygame.font.SysFont('Comic Sans MS', 35)
    
    #PythonGeeks- creating grid
    for i in range(0,10):
        if(i%3 == 0):
            pygame.draw.line(window, (0,0,0), (50 + 50*i, 50), (50 + 50*i ,500 ), 4 )
            pygame.draw.line(window, (0,0,0), (50, 50 + 50*i), (500, 50 + 50*i), 4 )

        pygame.draw.line(window, (0,0,0), (50 + 50*i, 50), (50 + 50*i ,500 ), 2 )
        pygame.draw.line(window, (0,0,0), (50, 50 + 50*i), (500, 50 + 50*i), 2 )
    pygame.display.update()
    
    #PythonGeeks- placing elements on the board
    for i in range(0, len(grid_board[0])):
        for j in range(0, len(grid_board[0])):
            if(0<grid_board[i][j]<10):
                Value_board = Font.render(str(grid_board[i][j]), True,(52, 31, 151))
                window.blit(Value_board, ((j+1)*50 + 15, (i+1)*50 ))
    pygame.display.update()
            
    # Sudoku_solver(window)
    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
   
main()
