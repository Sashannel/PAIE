import random
import pygame

class Hunter():

    hunters = []

    def __init__(self):
        
        pass

    def create(self, screen, sprite):

        position = []
        x = random.randint(0, 1080)
        y = random.randint(0, 720)
        position = [x, y]

        print("New hunter generated at:", position)
        Hunter().hunters.append([x, y, "invisible", 300])
        print("HUNTER", self.hunters)

        for i in range(len(Hunter().hunters)):

            hunter = Hunter().hunters[i]

            if True:

                screen.blit(sprite, (hunter[0], hunter[1]))

                hunter[2] = "drawn"

        return Hunter().hunters
    

    def energy(self, screen, size):

        for i in range(len(Hunter().hunters) - 1):

            hunter = Hunter().hunters[i]
            hunter[3] -= 1

            if hunter[3] <= 0:

                Hunter().destroy(screen, size, [hunter[0], hunter[1], hunter[2], hunter[3]])
    

    def destroy(self, screen, size, position):

        index = Hunter().hunters.index(position)

        del Hunter().hunters[index]

        pygame.draw.rect(screen, "lavender", (position[0], position[1], size, size))

        print("Deleted hunter at:", position)


    def draw(self, screen, sprite):
        for hunter in Hunter.hunters:
            screen.blit(sprite, (hunter[0], hunter[1]))
            hunter[2] = "drawn"
