import pygame
from pygame.locals import *
import random
        
class Window:
    """ application window object """
    def __init__(self):

        self.width = 800
        self.height = 800
        self.window = pygame.display.set_mode((self.width, self.height))
        self.window.fill((60, 220, 0))
        

        self.road_width = int(self.width/1.6)
        self.roadmark_width = int(self.width/80)
        self.right_lane = self.width/2 + self.road_width/4
        self.left_lane = self.width/2 - self.road_width/4
        
    def draw_background(self):
    
        pygame.draw.rect(
            self.window,
            (50, 50, 50),
            (self.width/2-self.road_width/2, 0, self.road_width, self.height))

        pygame.draw.rect(
            self.window,
            (255, 240, 60),
            (self.width/2 - self.roadmark_width/2, 0, self.roadmark_width, self.height))

        pygame.draw.rect(
            self.window,
            (255, 255, 255),
            (self.width/2 - self.road_width/2 + self.roadmark_width*2, 0, self.roadmark_width, self.height))

        pygame.draw.rect(
            self.window,
            (255, 255, 255),
            (self.width/2 + self.road_width/2 - self.roadmark_width*3, 0, self.roadmark_width, self.height))

class CarGame:

    def __init__(self):
        self.player = Player()
        self.enemy_vehicle = EnemyVehicle()
        self.counter = 0
        self.running = False
        self.level = 0
        
        self.start_game()
        self.start_gameloop()
        
    def create_enemy(self):
     
        if self.enemy_vehicle.location[1] > window.height:

            if random.randint(0,1) == 0:
                self.enemy_vehicle.location.center = window.right_lane, -200
            else:
                self.enemy_vehicle.location.center = window.left_lane, -200  
            
    def level_up(self):

        self.counter += 1  


        if self.counter == 5000:
            self.enemy_vehicle.speed += 0.25
            self.level += 1

            self.counter = 0
            print("level up", self.level)
            
    def key_controls(self):

        for event in pygame.event.get():
            if event.type == QUIT:

                self.running = False
            if event.type == KEYDOWN:

                if event.key in [K_a, K_LEFT]:
                    self.player.location = self.player.location.move([-int(window.road_width/2), 0])
                if event.key in [K_d, K_RIGHT]:
                    self.player.location = self.player.location.move([int(window.road_width/2), 0])
             
            
    def start_game(self):
   
        pygame.display.set_caption("Mariya's car game")
        self.running = True
               
    def start_gameloop(self):
        
        while self.running:   
            self.create_enemy()
            self.level_up()
            self.enemy_vehicle.location[1] += self.enemy_vehicle.speed
            
            if self.player.location[0] == self.enemy_vehicle.location[0] and self.enemy_vehicle.location[1] > self.player.location[1] - self.enemy_vehicle.length:
                print("GAME OVER! YOU LOST!")
                break
            
            self.key_controls()
            window.draw_background()
            window.window.blit(self.player.car, self.player.location)
            window.window.blit(self.enemy_vehicle.car, self.enemy_vehicle.location)
            pygame.display.update()

        pygame.quit()   

class Player:
    def __init__(self):
        self.car = pygame.image.load("assets/car.png")
        self.location = self.car.get_rect()
        self.location.center = window.right_lane, window.height*0.8

class EnemyVehicle:
    def __init__(self):
        self.speed = 1
        self.length = 250
        self.img_path = "assets/otherCar.png"
        self.draw_car()
        
    def draw_car(self):
        self.car = pygame.image.load(self.img_path)
        self.location = self.car.get_rect()
        self.location.center = window.left_lane, window.height*0.2
 
if __name__ == "__main__":
    pygame.init()
    window = Window()
    game = CarGame()