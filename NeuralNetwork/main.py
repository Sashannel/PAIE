import time
import pygame
import random
import NN
import foodHandler
import preyHandler
import hunterHandler


width = 1080
height = 720
fps = 60

images = []

images.append(pygame.transform.scale(pygame.image.load("NeuralNetwork/data/sprites/food.png"), (50, 50)))
images.append(pygame.transform.scale(pygame.image.load("NeuralNetwork/data/sprites/prey.png"), (50, 50)))
images.append(pygame.transform.scale(pygame.image.load("NeuralNetwork/data/sprites/hunter.png"), (50, 50)))


def main():

    pygame.init()

    icon = pygame.image.load("NeuralNetwork/data/sprites/icon.jpg")

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Pablo's AI Ecosystem")
    pygame.display.set_icon(icon)

    clock = pygame.time.Clock()

    screen.fill(pygame.Color("lavender"))

    running = True

    while running:

        for e in pygame.event.get():

            if e.type == pygame.QUIT:

                running = False

        attempt = random.randint(0, 100) #generates objects randomly

        if attempt == 69: #nice

            foodHandler.Food().create(screen, images[0])

        if attempt == 42: #nice

            preyHandler.Prey().create(screen, images[1])

        if attempt == 16: #nice

            hunterHandler.Hunter().create(screen, images[2])

            


        preyHandler.Prey().energy(screen, 50)
        hunterHandler.Hunter().energy(screen, 50)
        
        clock.tick(fps)
        pygame.draw.rect(screen, "lavender", (0, 0, width, height))

        foodHandler.Food().draw(screen, images[0])
        preyHandler.Prey().draw(screen, images[1])
        hunterHandler.Hunter().draw(screen, images[2])
        
        pygame.display.flip()



if __name__ == "__main__":

    main()
