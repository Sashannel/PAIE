import random
import pygame
import math

class Prey():

    preys = []

    def __init__(self):
        
        self.speed = 0
        self.angle = 0

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

        toRemove = []

        for prey in Prey.preys:

            prey[3] -= 1

            if prey[3] <= 0:

                toRemove.append(prey)

        for prey in toRemove:

            self.destroy(screen, size, prey)
    

    def destroy(self, screen, size, prey):

        if prey in Prey.preys:

            Prey.preys.remove(prey)
            pygame.draw.rect(screen, "lavender", (prey[0], prey[1], size, size))
            print("Deleted hunter at:", prey)


    def draw(self, screen, sprite):
        for prey in Prey.preys:
            screen.blit(sprite, (prey[0], prey[1]))
            prey[2] = "drawn"


    def move(self, prey, angle, velocity):

        speed = prey[4]
        angle = prey[5]
        prey[0] += (math.sqrt((velocity**2) - ((velocity * math.sin(angle))**2))) #change prey's x position
        prey[1] += (velocity * math.sin(angle)) #change prey's y position


    def rotate(self, prey, direction): #direction = 1 or -1 (turn left or right)

        prey[5] += direction * 4 #change prey's angle
        return prey
