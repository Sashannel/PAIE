import random
import pygame
import math

class Hunter():

    hunters = []

    def __init__(self):
        
        self.speed = 0
        self.angle = 0

    def create(self, screen, sprite):

        position = []
        x = random.randint(0, 1080)
        y = random.randint(0, 720)
        position = [x, y]

        print("New hunter generated at:", position)
        Hunter.hunters.append([x, y, "invisible", 300, self.speed, self.angle]) #pos x, y, status, energy, velocity, angle
        print("HUNTER", self.hunters)

        for i in range(len(Hunter.hunters)):

            hunter = Hunter.hunters[i]

            if True:

                screen.blit(sprite, (hunter[0], hunter[1]))

                hunter[2] = "drawn"

        return Hunter.hunters
    

    def energy(self, screen, size):

        toRemove = []

        for hunter in Hunter.hunters:

            hunter[3] -= 1

            if hunter[3] <= 0:

                toRemove.append(hunter)

        for hunter in toRemove:

            self.destroy(screen, size, hunter)
    

    def destroy(self, screen, size, hunter):

        if hunter in Hunter.hunters:

            Hunter.hunters.remove(hunter)
            pygame.draw.rect(screen, "lavender", (hunter[0], hunter[1], size, size))
            print("Deleted hunter at:", hunter)


    def draw(self, screen, sprite):
        for hunter in Hunter.hunters:
            screen.blit(sprite, (hunter[0], hunter[1]))
            hunter[2] = "drawn"

    def move(self, hunter, angle, velocity):

        speed = hunter[4]
        angle = hunter[5]
        hunter[0] += (math.sqrt((velocity**2) - ((velocity * math.sin(angle))**2))) #change hunter's x position
        hunter[1] += (velocity * math.sin(angle)) #change hunter's y position


    def rotate(self, hunter, direction): #direction = 1 or -1 (turn left or right)

        hunter[5] += direction * 4 #change hunter's angle
        return hunter
