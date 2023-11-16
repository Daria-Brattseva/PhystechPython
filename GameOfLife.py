import pygame as pg
import random

pg.init()
fps = 30 #Количество кадров в секунду
width, height = 1000, 1000 # Высота и ширина поля
window = pg.display.set_mode((width, height))
finished = False
clock = pg.time.Clock()
c_height, c_width = 20, 20 # Высота и ширина клеток
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


# Создаем рандомные первые клетки
initial_cells = [[random.choice([0 , 1]) for j in range(window.get_width() // 20)] for i in range(window.get_height() // 20)]


# Создание сетки поля
def net():
    for i in range(0 , window.get_height() // 20): # Количесво строк от 0 до 500/20
        pg.draw.line(window , WHITE , (0 , i * 20) , (window.get_width() , i * 20))
    for j in range(0 , window.get_width() // 20): # Количество столбцов
        pg.draw.line(window , WHITE , (j * 20 , 0) , (j * 20 , window.get_height()))


# Считаем количество соседей у клетки
def near(pos: list , system=[[-1 , -1] , [-1 , 0] , [-1 , 1] , [0 , -1] , [0 , 1] , [1 , -1] , [1 , 0] , [1 , 1]]):
    count = 0
    for i in system:
        if initial_cells[(pos[0] + i[0]) % len(initial_cells)][(pos[1] + i[1]) % len(initial_cells[0])]:
            count += 1
    return count


# Просматриваем все клетки
def observe(initial_cells):
    for i in range(0 , len(initial_cells)):
        for j in range(0 , len(initial_cells[i])):
            if initial_cells[i][j] == 0:
                pg.draw.rect(window , BLACK , [i * 20 , j * 20 , c_height, c_width])
            else:
                pg.draw.rect(window , GREEN , [i * 20 , j * 20 , c_height, c_width])


# Основной код смены поколений
while not finished:
    clock.tick(fps)
    window.fill(BLACK)
    net()
    observe(initial_cells)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True
    pg.display.update()
    # Создаем следующее поколение
    new_cells = [[0 for j in range(len(initial_cells[0]))] for i in range(len(initial_cells))]
    for i in range(len(initial_cells)):
        for j in range(len(initial_cells[0])):
            if initial_cells[i][j]:
                if near([i , j]) != 2 and near([i,j]) != 3 :
                    new_cells[i][j] = 0
                    continue
                new_cells[i][j] = 1
                
            if near([i,j]) == 3:
                new_cells[i][j] = 1
    initial_cells = new_cells
pg.quit()