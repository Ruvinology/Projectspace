import pygame
import random

pygame.init()


width = 800# THISis the width#
height = 800


rocket_height = 140
rocket_width = 110
rocket_x = width // 2
rocket_y = height // 2



screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Space Wars")


rocket_image = pygame.image.load(r'C:\Users\Windows 10\Videos\photo_2024-06-27_00-18-22.png')
rocket_image = pygame.transform.scale(rocket_image, (rocket_width, rocket_height))
rocket_direction = 0

astronaut_image = pygame.image.load(r'C:\Users\Windows 10\Videos\asteroid-planet-icon-cartoon-asteroid-planet-vector-icon-web-design-isolated-white-background_98402-48666.png')
astronaut_image = pygame.transform.scale(astronaut_image,(60,60))

background_image = pygame.image.load(r'C:\Users\Windows 10\Downloads\space-4984262_960_720 (1).jpg')
background_image = pygame.transform.scale(background_image, (width, height))

front_page_bg_image = pygame.image.load(r'D:\childs play page\656addcb903eb62d1eb7acf388024be9.jpeg')
front_page_bg_image = pygame.transform.scale(front_page_bg_image, (width, height))

game_over_bg_image = pygame.image.load(r'D:\childs play page\88d160224fa5e0388ceab5fd51148e63.jpeg')
game_over_bg_image = pygame.transform.scale(game_over_bg_image, (width, height))



pygame.mixer.music.load(r'C:\Users\Windows 10\Downloads\Untitled video - Made with Clipchamp (14).mp3')
pygame.mixer.music.play(-1)

collision_sound = pygame.mixer.Sound(r'C:\Users\Windows 10\Downloads\Untitled video - Made with Clipchamp (15).mp3')
destroy_sound = pygame.mixer.Sound(r'C:\Users\Windows 10\Downloads\Untitled video - Made with Clipchamp (17).mp3')
destroy_sound.set_volume(0.6)
laser_sound = pygame.mixer.Sound(r'C:\Users\Windows 10\Downloads\Untitled video - Made with Clipchamp (16).mp3')
laser_sound.set_volume(0.3)
boot_attack_sound = pygame.mixer.Sound(r'C:\Users\Windows 10\Downloads\Untitled video - Made with Clipchamp (18).mp3')
laser_sound.set_volume(0.6)
font_large = pygame.font.Font(None,74)
font_small = pygame.font.Font(None,42)
font_too_small = pygame.font.Font(None,28)
def get_rotated_image(image, angle):
    return pygame.transform.rotate(image, angle)

class Laser:
    def __init__(self,x,y,direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.speed = 10
        self.width = 5
        self.height = 20

    def move(self):
        if self.direction == 270:
            self.x += self.speed
        elif self.direction == 0:
            self.y -= self.speed
        elif self.direction == 90:
            self.x -= self.speed
        elif self.direction == 180:
            self.y += self.speed

    def draw(self,screen):
        laser_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen,(250,0,0), laser_rect)

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

class Bootattack:
    def __init__(self,x,y,direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.speed = 15
        self.size = 30

    def move(self):
        if self.direction ==270:
            self.x += self.speed
        elif self.direction == 0:
            self.y -= self.speed
        elif self.direction == 90:
            self.x -= self.speed
        elif self.direction == 180:
            self.y += self.speed

    def draw(self,screen):
        boot_rect = pygame.Rect(self.x,self.y,self.size,self.size)
        pygame.draw.rect(screen,(250,0,0), boot_rect)

    def get_rect(self):
        return pygame.Rect(self.x,self.y,self.size,self.size)

class Astronaut:
    def __init__(self,rocket_x,rocket_y,safe_radius =200):
        while True:
            self.x = random.randint(0,width - 50)
            self.y = random.randint(0,height - 50)
            distance_to_rocket = ((self.x - rocket_x) ** 2 + (self.y - rocket_y) ** 2) ** 0.5
            if distance_to_rocket > safe_radius:
                break
        self.speed_x = random.choice([-1,1]) * random.randint(1,3)
        self.speed_y = random.choice([-1,1]) * random.randint(1,3)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        if self.x < 0 or self.x > width - 50:
            self.speed_x  *= -1
        if self.y < 0 or self.y > height - 50:
            self.speed_y *= -1


    def draw(self,screen):
        screen.blit(astronaut_image,(self.x,self.y))

    def get_rect(self):
        return pygame.Rect(self.x,self.y,50,50)
    def reset_position(self):
        self.x = random.randint(0,width - 50)
        self. y = random.randint(0,height - 50)

def show_game_over_screen():
    screen.blit(game_over_bg_image,(0,0))
    text = font_large.render("Game Over",True,(255,0,0))
    screen.blit(text,(width// 2 - text.get_width()//2,height//2 - text.get_height()//2))
    text_small = font_small.render("Press R to Restart or Q to Quit", True,(255,255,255))
    screen.blit(text_small,(width// 2 -text_small.get_width()//2,height// 2 + text.get_height()))
    pygame.display.flip()

def show_front_page():
    screen.blit(front_page_bg_image,(0,0))
    title = font_large.render("Space Wars", True,(255,255,255))
    play_button = font_small.render("Play",True,(0,255,0))
    quit_button = font_small.render("Quit",True,(255,0,0))
    creater_button = font_too_small.render("By Dark Might",True,(255,255,255,))

    title_rect = title.get_rect(center =(width //2,height //3+60))
    play_rect = play_button.get_rect(center =(width //2 , height //2+20))
    quit_rect = quit_button.get_rect(center =(width //  2, height // 2+70))
    creater_rect = creater_button.get_rect(center= (width // 2+ 70,height // 3+90 ))
    pygame.display.flip()



    screen.blit(title,title_rect)
    screen.blit(play_button, play_rect)
    screen.blit(quit_button, quit_rect)
    screen.blit(creater_button,creater_rect)

    pygame.display.flip()

    return play_rect,quit_rect


def main():
    lasers = []
    boot_attacks =[]
    astronauts = [Astronaut(rocket_x,rocket_y) for _ in range(5)]
    global rocket_x,rocket_y,rocket_direction


    running = True
    game_over = False
    front_page = True

    while running:
        if front_page:
            play_rect,quit_rect = show_front_page()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and front_page:
                if play_rect.collidepoint(event.pos):
                    front_page = False
                elif quit_rect.collidepoint(event.pos):
                    running = False

            if event.type == pygame.KEYDOWN and game_over:
                if event.key == pygame.K_r:
                    game_over = False
                    rocket_x,rocket_y = width //2,height // 2
                    lasers.clear()
                    boot_attacks.clear()
                    astronauts =[Astronaut(rocket_x,rocket_y) for _ in range(5)]
                elif event.key == pygame.K_q:
                    running = False


        if not front_page and not game_over:
            keys = pygame.key.get_pressed()

            if keys[pygame.K_a]:
                rocket_x -= 10
                rocket_direction = 90
            if keys[pygame.K_d]:
                rocket_x += 10
                rocket_direction = 270
            if keys[pygame.K_w]:
                rocket_y -= 10
                rocket_direction = 0
            if keys[pygame.K_s]:
                rocket_y += 10
                rocket_direction = 180


            rocket_x = max(0, min(width - rocket_width, rocket_x))
            rocket_y = max(0, min(height - rocket_height, rocket_y))

            if keys[pygame.K_SPACE]:
                if rocket_direction == 270:
                    laser_x = rocket_x + rocket_width
                    laser_y = rocket_y + rocket_height // 2 -10
                elif rocket_direction == 0:
                    laser_x = rocket_x + rocket_width  // 2
                    laser_y = rocket_y
                elif rocket_direction == 90:
                    laser_x = rocket_x
                    laser_y = rocket_y + rocket_height // 2 - 10
                elif rocket_direction == 180:
                    laser_x = rocket_x + rocket_width // 2
                    laser_y = rocket_y + rocket_height
                lasers.append(Laser(laser_x,laser_y,rocket_direction))
                laser_sound.play()

            if keys[pygame.K_e]:
                if rocket_direction == 270:
                    boot_x = rocket_x + rocket_width // 1 -10
                    boot_y = rocket_y + rocket_height // 3 +10
                elif rocket_direction == 0:
                    boot_x = rocket_x + rocket_width // 3 + 5
                    boot_y = rocket_y + rocket_height // 3 -40
                elif rocket_direction == 90:
                    boot_x = rocket_x + rocket_width // 6 - 35
                    boot_y = rocket_y + rocket_height // 3 + 8
                elif rocket_direction == 180:
                    boot_x = rocket_x + rocket_width // 3 +4
                    boot_y = rocket_y + rocket_height // 1 - 30
                boot_attacks.append(Bootattack(boot_x,boot_y,rocket_direction))
                boot_attack_sound.play()


            for laser in lasers:
                laser.move()


            for boot in boot_attacks:
                boot.move()


            lasers = [laser for laser in lasers if 0 <= laser.x <= width and 0 <= laser.y <= height]
            boot_attacks = [boot for boot in boot_attacks if 0 <= boot.x <= width and 0 <= boot.y <= height]

            for laser in lasers:
                for astronaut in astronauts:
                    if laser.get_rect().colliderect(astronaut.get_rect()):
                        astronaut.reset_position()
                        lasers.remove(laser)
                        destroy_sound.play()
                        break

            for boot in boot_attacks:
                for astronaut in astronauts:
                    if boot.get_rect().colliderect(astronaut.get_rect()):
                        astronaut.reset_position()
                        boot_attacks.remove(boot)
                        destroy_sound.play()
                        break

            screen.blit(background_image,(0,0))


            rotated_rocket = get_rotated_image(rocket_image, rocket_direction)
            rocket_rect = rotated_rocket.get_rect(center=(rocket_x + rocket_width // 2, rocket_y + rocket_height // 2))
            screen.blit(rotated_rocket, rocket_rect.topleft)


            for laser in lasers:
                laser.draw(screen)

            for boot in boot_attacks:
                boot.draw(screen)


            for astronaut in astronauts:
                astronaut.move()
                astronaut.draw(screen)

                if rocket_rect.colliderect(astronaut.get_rect()):
                    collision_sound.play()
                    game_over = True

        if game_over:
           show_game_over_screen()



        pygame.display.flip()
        pygame.time.Clock().tick(30)

    pygame.quit()


if __name__ == "__main__":
    main()