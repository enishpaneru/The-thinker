import pygame
import time
import random
from entry import init_thinker,start_think
pygame.init()

display_width = 600
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

obstacles=20

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('I am the Thinker')
clock = pygame.time.Clock()


#######



#######
class main():
    def __init__(self):
        pygame.init()

        self.display_width = 800
        self.display_height = 600
        self.grid_range = range(8)
        self.obstacles=obstacles
        self.gameDisplay = pygame.display.set_mode((display_width, display_height))
        pygame.display.set_caption('I am the Thinker')
        self.clock = pygame.time.Clock()
        carImg = pygame.image.load('racecar.png')
        square = pygame.image.load('square.png')
        goal = pygame.image.load('goal.jpg')

        self.thinker = pygame.transform.scale(carImg, (int(
        display_width / len(self.grid_range)), int(display_height / len(self.grid_range))))
        self.obstacle = pygame.transform.scale(square, (
        int(display_width / len(self.grid_range)), int(display_height / len(self.grid_range))))
        self.goal = pygame.transform.scale(goal, (
        int(display_width / len(self.grid_range)), int(display_height / len(self.grid_range))))

    def things(self, color, start_pos, end_pos, width=1, ):
        pygame.draw.line(gameDisplay, color, start_pos, end_pos, width)

    def place_thinker(self, pos):
        gameDisplay.blit(self.thinker,
                         (display_width / len(self.grid_range) * pos[0], display_height / len(self.grid_range) * pos[1]))

    def place_obstacle(self, pos):
        gameDisplay.blit(self.obstacle,
                         (display_width / len(self.grid_range) * pos[0], display_height / len(self.grid_range) * pos[1]))

    def place_goal(self, pos):
        gameDisplay.blit(self.goal,
                         (display_width / len(self.grid_range) * pos[0], display_height / len(self.grid_range) * pos[1]))

    def text_objects(self, text, font):
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()

    def message_display(self, text, size=20,delay=0):
        largeText = pygame.font.Font('freesansbold.ttf', size)
        TextSurf, TextRect = self.text_objects(text, largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)

        pygame.display.update()
        time.sleep(delay)

    def run_menu(self):
        gameExit = False
        while not gameExit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.init_environment()

            gameDisplay.fill((30, 30, 30))
            self.message_display("press ENTER to wake up thinker", size=30)

            self.maintain_display()

    def get_random_pos(self):
        return (random.randint(0, 7),random.randint(0, 7))

    def start_think(self):
        pass

    def build_background(self):
        self.gameDisplay.fill(red)
        for each in self.grid_range:
            start_pos_ver = (display_width / len(self.grid_range) * each, 0)
            end_pos_ver = (display_width / len(self.grid_range) * each, display_width)
            self.things(black, start_pos_ver, end_pos_ver)
            start_pos_hor = (0, display_height / len(self.grid_range) * each)
            end_pos_hor = (display_height, display_height / len(self.grid_range) * each)
            self.things(black, start_pos_hor, end_pos_hor)

    def start_move(self,steps,goal_pos,obstacle_pos):
        print(steps)
        gamefin=False
        start_num=0
        while not gamefin:
            thinker_pos=steps[start_num]
            self.build_background()
            self.place_thinker(thinker_pos)
            self.place_goal(goal_pos)
            for each in obstacle_pos:
                self.place_obstacle(each)
            if thinker_pos==goal_pos:
                self.message_display("Congrats!!Goal Reached",30,2)
                gamefin=True
                return
            if start_num==len(steps)-1 and thinker_pos != goal_pos:
                self.message_display("Sorry Not Possible",30,2)
                gamefin=True
            start_num+=1
            self.maintain_display()
            time.sleep(0.5)
        return



    def init_environment(self):
        thinker_pos=self.get_random_pos()
        goal_pos=self.get_random_pos()
        while goal_pos==thinker_pos:
            goal_pos=self.get_random_pos()
        obstacle_pos=[]
        for each in range(self.obstacles):
            random_pos=self.get_random_pos()
            while random_pos  in obstacle_pos or random_pos==thinker_pos or random_pos==goal_pos:
                random_pos=self.get_random_pos()
            obstacle_pos.append(random_pos)
        gamestart = False

        thinker=init_thinker(goal_pos,thinker_pos,obstacle_pos)

        while not gamestart:

            self.build_background()
            self.place_thinker(thinker_pos)
            self.place_goal(goal_pos)
            for each in obstacle_pos:
                self.place_obstacle(each)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        steps=start_think(thinker)
                        self.start_move(steps[1:],goal_pos,obstacle_pos)
                        return

            self.message_display("press Enter to start thinking", 30)

            self.maintain_display()

    def maintain_display(self):
        pygame.display.update()
        clock.tick(60)


#
# def text_objects(text, font):
#     textSurface = font.render(text, True, black)
#     return textSurface, textSurface.get_rect()
#
#
# def message_display(text):
#     largeText = pygame.font.Font('freesansbold.ttf', 115)
#     TextSurf, TextRect = text_objects(text, largeText)
#     TextRect.center = ((display_width / 2), (display_height / 2))
#     gameDisplay.blit(TextSurf, TextRect)
#
#     pygame.display.update()
#
#     time.sleep(2)
#
#     game_loop()
#
#
# def crash():
#     message_display('You Crashed')
#
#
# def game_loop():
#     x = (display_width * 0.45)
#     y = (display_height * 0.8)
#
#     x_change = 0
#     ######
#     thing_startx = random.randrange(0, display_width)
#     thing_starty = -600
#     thing_speed = 7
#     thing_width = 100
#     thing_height = 100
#     ######
#     gameExit = False
#
#     while not gameExit:
#
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 quit()
#
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_LEFT:
#                     x_change = -5
#                 if event.key == pygame.K_RIGHT:
#                     x_change = 5
#
#             if event.type == pygame.KEYUP:
#                 if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
#                     x_change = 0
#
#         x += x_change
#         gameDisplay.fill((30, 30, 30))
#
#         ##########
#         # things(thingx, thingy, thingw, thingh, color)
#         things(thing_startx, thing_starty, thing_width, thing_height, black)
#         thing_starty += thing_speed
#         car(x, y)
#         ##########
#         if x > display_width - car_width or x < 0:
#             crash()
#
#         if thing_starty > display_height:
#             thing_starty = 0 - thing_height
#             thing_startx = random.randrange(0, display_width)
#
#         pygame.display.update()
#         clock.tick(60)
#
#
# game_loop()
newgame = main()
newgame.run_menu()
pygame.quit()
quit()
