import random
import pygame
import time
import os

can_up = True
can_down = True
can_left = True
can_right = True
run = True
size = 1
direction = "None"
x = 100
y = 100
position = (x, y, 25, 25)
pygame.init()
fruit_x = random.randint(0,9)
fruit_y = random.randint(0,9)
fruit_pos = (fruit_x*25, fruit_y*25, 25, 25)
parts = [position] * 100

screen = pygame.display.set_mode((250, 250))
while run:
    pygame.draw.rect(screen, (0, 0, 0), (0,0,500,500))
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and can_up:
                direction = "Up"
            if event.key == pygame.K_s and can_down:
                direction = "Down"
            if event.key == pygame.K_a and can_left:
                direction = "Left"
            if event.key == pygame.K_d and can_right:
                direction = "Right"


    if direction == "Up" and can_up:
        y = y - 25
        can_down = False
        can_up = True
        can_left = True
        can_right = True

    if direction == "Down" and can_down:
        y = y + 25
        can_down = True
        can_up = False
        can_left = True
        can_right = True

    if direction == "Left" and can_left:
        x = x - 25
        can_down = True
        can_up = True
        can_left = True
        can_right = False

    if direction == "Right" and can_right:
        x = x + 25
        can_down = True
        can_up = True
        can_left = False
        can_right = True


    if x < 0:
        run= False
    if y < 0:
        run = False
    if x > 225:
        run = False
    if y > 225:
        run = False

    position = (x, y, 25, 25)
    pygame.draw.rect(screen, (255, 0, 0), fruit_pos)


    i = len(parts) - 1
    while i > 0:
        parts[i] = parts[i-1]
        parts[0] = position
        i = i - 1

    size_store = size
    snake_colour = (0,200,0)
    snake_colour_choice = 0
    while size_store > 0:
        pygame.draw.rect(screen, (snake_colour), parts[size_store])
        size_store = size_store - 1

        if snake_colour_choice == 0:
            snake_colour = (50, 255, 50)
            snake_colour_choice = 1
        else:
            snake_colour = (0, 200, 0)
            snake_colour_choice = 0



    if position == fruit_pos:
        size = size + 1
        # successful_place = False
        # add_fruit = True
        # while add_fruit:
        fruit_x = random.randint(0,9)
        fruit_y = random.randint(0,9)
        fruit_pos = (fruit_x * 25, fruit_y * 25, 25, 25)
    #         size_store = size
    #         print(size)
    #         print(size_store)
    #         check = True
    #
    #         while check:
    #
    #             if parts[size_store] == fruit_pos:
    #                 check = False
    #
    #
    #             if size_store > 0:
    #                 successful_place = True
    #                 check = False
    #
    #
    #             size_store = size_store - 1
    #
    #     if successful_place:
    #         add_fruit = False


    size_store = size
    while size_store > 1:
        if position == parts[size_store]:
            run = False
        size_store = size_store - 1

    pygame.display.update()
    time.sleep(0.55-(0.01*size))

