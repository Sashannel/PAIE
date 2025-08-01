import random
import pygame

class Prey():

    preys = []

    def __init__(self):
        
        pass

    def create(self, screen, sprite):

        position = []
        x = random.randint(0, 1080)
        y = random.randint(0, 720)
        position = [x, y]

        print("New prey generated at:", position)
        Prey().preys.append([x, y, "invisible", 300])
        print("PREY", self.preys)

        for i in range(len(Prey().preys)):

            prey = Prey().preys[i]

            if prey[2] != "drawn":

                screen.blit(sprite, (prey[0], prey[1]))

                prey[2] = "drawn"

        return Prey().preys
    

    def energy(self, screen, size):

        for i in range(len(Prey().preys) - 1):

            prey = Prey().preys[i]
            prey[3] -= 1

            if prey[3] <= 0:

                Prey().destroy(screen, size, [prey[0], prey[1], prey[2], prey[3]])
    

    def destroy(self, screen, size, position):

        index = Prey().preys.index(position)

        del Prey().preys[index]

        pygame.draw.rect(screen, "lavender", (position[0], position[1], size, size))

        print("Deleted prey at:", position)