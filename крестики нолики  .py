import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Крестики-нолики")



board = [0, 0, 0,
         0, 0, 0,
         0, 0, 0]

current = 1        # чей ход: 1 = X, 2 = O
game_over = False
winner = 0         #0 = никто, 1 = X, 2 = O, 3 = ничья

running = True
while running:

    screen.fill("white")
    pygame.draw.line(screen, 'BLACK', (3, 3), (597, 3), 7)       # верх
    pygame.draw.line(screen, 'BLACK', (3, 597), (597, 597), 7)   # низ
    pygame.draw.line(screen, 'BLACK', (3, 3), (3, 597), 7)       # лево
    pygame.draw.line(screen, 'BLACK', (597, 3), (597, 597), 7)   # право
    pygame.draw.line(screen, 'BLACK', (200, 0), (200, 600), 5)
    pygame.draw.line(screen, 'BLACK', (400, 0), (400, 600), 5)
    pygame.draw.line(screen, 'BLACK', (0, 200), (600, 200), 5)
    pygame.draw.line(screen, 'BLACK', (0, 400), (600, 400), 5)
    if board[0] == 1:
        pygame.draw.line(screen, 'red', (40, 40), (160, 160), 8)
        pygame.draw.line(screen, 'red', (160, 40), (40, 160), 8)
    elif board[0] == 2:
        pygame.draw.circle(screen, 'blue', (100, 100), 60, 8)

    if board[1] == 1:
        pygame.draw.line(screen, 'red', (240, 40), (360, 160), 8)
        pygame.draw.line(screen, 'red', (360, 40), (240, 160), 8)
    elif board[1] == 2:
        pygame.draw.circle(screen, 'blue', (300, 100), 60, 8)

    if board[2] == 1:
        pygame.draw.line(screen, 'red', (440, 40), (560, 160), 8)
        pygame.draw.line(screen, 'red', (560, 40), (440, 160), 8)
    elif board[2] == 2:
        pygame.draw.circle(screen, 'blue', (500, 100), 60, 8)

    if board[3] == 1:
        pygame.draw.line(screen, 'red', (40, 240), (160, 360), 8)
        pygame.draw.line(screen, 'red', (160, 240), (40, 360), 8)
    elif board[3] == 2:
        pygame.draw.circle(screen, 'blue', (100, 300), 60, 8)

    if board[4] == 1:
        pygame.draw.line(screen, 'red', (240, 240), (360, 360), 8)
        pygame.draw.line(screen, 'red', (360, 240), (240, 360), 8)
    elif board[4] == 2:
        pygame.draw.circle(screen, 'blue', (300, 300), 60, 8)

    if board[5] == 1:
        pygame.draw.line(screen, 'red', (440, 240), (560, 360), 8)
        pygame.draw.line(screen, 'red', (560, 240), (440, 360), 8)
    elif board[5] == 2:
        pygame.draw.circle(screen, 'blue', (500, 300), 60, 8)

    if board[6] == 1:
        pygame.draw.line(screen, 'red', (40, 440), (160, 560), 8)
        pygame.draw.line(screen, 'red', (160, 440), (40, 560), 8)
    elif board[6] == 2:
        pygame.draw.circle(screen, 'blue', (100, 500), 60, 8)

    if board[7] == 1:
        pygame.draw.line(screen, 'red', (240, 440), (360, 560), 8)
        pygame.draw.line(screen, 'red', (360, 440), (240, 560), 8)
    elif board[7] == 2:
        pygame.draw.circle(screen, 'blue', (300, 500), 60, 8)

    if board[8] == 1:
        pygame.draw.line(screen, 'red', (440, 440), (560, 560), 8)
        pygame.draw.line(screen, 'red', (560, 440), (440, 560), 8)
    elif board[8] == 2:
        pygame.draw.circle(screen, 'blue', (500, 500), 60, 8)

    if game_over:
        font = pygame.font.SysFont("arial", 40, bold=False)
        if winner == 1:
            text = "Победил X заново R"
            color = 'red'
        elif winner == 2:
            text = "Победил O заново R"
            color = 'blue'
        else:
            text = "Ничья  заново R"
            color = (80, 80, 80)
        surf = font.render(text, True, color)
        screen.blit(surf, (60, 280))

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if not game_over:
                mx = event.pos[0]   #позция по иксу
                my = event.pos[1]   #по игрику
                cell = -1
                # верхний ряд
                if mx > 0 and mx < 200 and my > 0 and my < 200:
                    cell = 0
                elif mx > 200 and mx < 400 and my > 0 and my < 200:
                    cell = 1
                elif mx > 400 and mx < 600 and my > 0 and my < 200:
                    cell = 2
                    #среднйий ряд
                elif mx > 0 and mx < 200 and my > 200 and my < 400:
                    cell = 3
                elif mx > 200 and mx < 400 and my > 200 and my < 400:
                    cell = 4
                elif mx > 400 and mx < 600 and my > 200 and my < 400:
                    cell = 5
                    #нижний
                elif mx > 0 and mx < 200 and my > 400 and my < 600:
                    cell = 6
                elif mx > 200 and mx < 400 and my > 400 and my < 600:
                    cell = 7
                elif mx > 400 and mx < 600 and my > 400 and my < 600:
                    cell = 8

                #если нажал в клетку а она пустаея ставить знак
                if cell != -1 and board[cell] == 0:
                    board[cell] = current

                    #проверка победы
                    if board[0] == board[1] == board[2] != 0:
                        winner = board[0]
                        game_over = True
                    elif board[3] == board[4] == board[5] != 0:
                        winner = board[3]
                        game_over = True
                    elif board[6] == board[7] == board[8] != 0:
                        winner = board[6]
                        game_over = True
                    
                    elif board[0] == board[3] == board[6] != 0:
                        winner = board[0]
                        game_over = True
                    elif board[1] == board[4] == board[7] != 0:
                        winner = board[1]
                        game_over = True
                    elif board[2] == board[5] == board[8] != 0:
                        winner = board[2]
                        game_over = True
                    
                    elif board[0] == board[4] == board[8] != 0:
                        winner = board[0]
                        game_over = True
                    elif board[2] == board[4] == board[6] != 0:
                        winner = board[2]
                        game_over = True
                    #ничья
                    elif 0 not in board:
                        winner = 3
                        game_over = True
                    else:
                        #меняем игрока
                        if current == 1:
                            current = 2
                        else:
                            current = 1

        #рестарт по R
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                board = [0, 0, 0,
                         0, 0, 0,
                         0, 0, 0]
                current = 1
                game_over = False
                winner = 0
pygame.quit()