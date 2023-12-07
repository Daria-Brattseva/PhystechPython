import pygame 
import random 
  
class Board: 
    def __init__(self, width, height): 
        self.width = width 
        self.height = height 
        self.board = [[0] * width for _ in range(height)] # Двумерный массив - поле с кнопка
        self.left = 0 # Отступ слева
        self.top = 0 # Отступ сверху
        self.cell_size = 30 # Размер клетки
  
    def set_view(self, left, top, cell_size): 
        self.left = left 
        self.top = top 
        self.cell_size = cell_size 
  
    def render(self, screen): # Создаем клетки-кнопки в поле
        white = pygame.Color('white') # Начальная заливка поля
        for y in range(self.height): 
            for x in range(self.width): 
                pos = (x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size, self.cell_size) # Координата клетки (сначала определяем верхний левый угол + отступы, потом смещаемся на размер одной клетки)
                pygame.draw.rect(screen, white, pos, 1) # Рисуем сами клетки (последнее - ширина контура)
  
  
    def get_cell(self, mouse_pos): # Возвращает координаты клетки в виде кортежа. Возвращает None, если координаты мыши оказались вне поля
        cell_x = (mouse_pos[0] - self.left) // self.cell_size 
        cell_y = (mouse_pos[1] - self.top) // self.cell_size 
        if cell_x < 0 or cell_x >= self.width or cell_y < 0 or cell_y >= self.height: 
            return None 
        return cell_x, cell_y 
  
    def on_click(self, cell): # Изменяет поле, опираясь на полученные координаты клетки — первоначально просто выводит координаты ячейки
        pass 
  
    def get_click(self, mouse_pos): # Получает событие нажатия и вызывает первые два метода
        cell = self.get_cell(mouse_pos) 
        if cell: 
            self.on_click(cell) 
  
class Sapper(Board): 
    def __init__(self, width, height, need): 
        super().__init__(width, height) # Обращение к родительскому классу
        self.board = [[-1] * width for inet in range(height)] # Новое поле, inet - ???
        bomb = 0 # Количество бомб на поле, заполняется, пока не достигнется необходимое значение
        while bomb < need: 
            x = random.randint(0, self.width - 1) 
            y = random.randint(0, self.height - 1) 
            if self.board[y][x] == -1: 
                self.board[y][x] = 10 
                bomb += 1 
  
    def open_click(self, cell): # Ищем бомбы-соседей
        x, y = cell 
        near =0
        if self.board[y][x] == 10:
            near = 11
        for dy in range(-1, 2): 
            for dx in range(-1, 2): 
                if x + dx < 0 or x + dx >= self.width or y + dy < 0 or y + dy >= self.height: # Проверка, что все соседи находятся внутри поля
                    continue 
                if self.board[y + dy][x + dx] == 10: 
                    near += 1 
        self.board[y][x] = near 
  
    def on_click(self, cell): 
        self.open_click(cell) 
  
    def render(self, screen):
        s = 0 
        red = pygame.Color('red')
        white = pygame.Color('white') 
        for y in range(self.height): 
            for x in range(self.width): 
                pos = (x * self.cell_size + self.left, y * self.cell_size + self.top, 
                        self.cell_size, self.cell_size) 
                pos1 = (x * self.cell_size + self.left + 2, y * self.cell_size + self.top + 2, 
                        self.cell_size, self.cell_size) 
                pygame.draw.rect(screen, white, pos, 1) # Выполняется, если игра продолжается (красным ничего не закрашивали)
                if self.board[y][x] >= 0 and self.board[y][x]!=10: 
                    font = pygame.font.Font(None, self.cell_size - 7) 
                    text = font.render(str(self.board[y][x]), 1, (100, 255, 100)) 
                    screen.blit(text, pos1) # Пишем текст
                    s += 1
                    if s == 216:
                        screen.fill((0, 222, 54))
                        font = pygame.font.Font(None, 72)
                        text = font.render("You win!", True, (0, 100, 0))
                        place = text.get_rect(center=(240, 150))
                        screen.blit(text, place)
                        pygame.display.update()
                    if  self.board[y][x] >= 10:
                        pygame.draw.rect(screen, red, pos) 
                        screen.fill((102, 0, 0))
                        font = pygame.font.Font(None, 72)
                        text = font.render("Game over...", True, (255, 0, 0))
                        place = text.get_rect(center=(240, 150))
                        screen.blit(text, place)
                        pygame.display.update()
                        return
  
  
def main(): 
    pygame.init() 
    size = 480, 480 
    screen = pygame.display.set_mode(size) 
    pygame.display.set_caption('Cапёр') 
    clock = pygame.time.Clock() 
    board = Sapper(16, 16, 40) 
    ticks = 0 
    running = True 
    while running: 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                running = False 
            if event.type == pygame.MOUSEBUTTONDOWN: 
                board.get_click(event.pos) 
        screen.fill((128, 128, 128)) 
        board.render(screen) 
        pygame.display.flip() 
        clock.tick(50) 
        ticks += 1 
    pygame.quit() 
  
main()

