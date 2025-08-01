import random
import pygame
import math

class Food():

    foods = []

    def __init__(self):
        
        pass
    

    def create(self, screen, sprite):

        position = []
        x = random.randint(0, 1080)
        y = random.randint(0, 720)
        position = [x, y]

        print("New food generated at:", position)
        Food().foods.append([x, y, "invisible"])
        print("FOODS", self.foods)

        for i in range(len(Food().foods)):

            food = Food().foods[i]

            if True:

                screen.blit(sprite, (food[0], food[1]))

                food[2] = "drawn"

        return Food().foods
    

    def destroy(self, screen, sprite, position):

        del position[2]
        index = Food().foods.index(position)

        del Food().foods[index]

        pygame.draw.rect(screen, "lavender", (position[0], position[1], sprite, sprite))

        print("Deleted food at:", position)

    
    def draw(self, screen, sprite):
        for food in Food.foods:
            screen.blit(sprite, (food[0], food[1]))
            food[2] = "drawn"
