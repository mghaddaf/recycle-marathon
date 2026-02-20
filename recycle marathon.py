import pygame, random
pygame.init()
WIDTH = 864
LENGTH = 600
run = True
bin = pygame.image.load(r"Pygame Developer\Images\bin.png")
bin = pygame.transform.scale(bin, (50, 70))
box = pygame.image.load(r"Pygame Developer\Images\box.png")
box = pygame.transform.scale(box, (50, 50))
eco_circle = pygame.image.load(r"Pygame Developer\Images\eco_circle.png")
eco_circle = pygame.transform.scale(eco_circle, (864, 600))
paper_bag = pygame.image.load(r"Pygame Developer\Images\paper_bag.png")
paper_bag = pygame.transform.scale(paper_bag, (50, 50))
pencil = pygame.image.load(r"Pygame Developer\Images\pencil.png")
pencil = pygame.transform.scale(pencil, (50, 50))
plastic_bag = pygame.image.load(r"Pygame Developer\Images\plastic_bag.png")
plastic_bag = pygame.transform.scale(plastic_bag, (50, 50))
screen = pygame.display.set_mode((WIDTH, LENGTH))

class Recyclables(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.images = [pencil, paper_bag, box]
        self.image = random.choice(self.images)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
recycle = pygame.sprite.Group()
for i in range(30):
    recyclable_sprites = Recyclables(random.randint(0, 864), random.randint(0, 600))
    recycle.add(recyclable_sprites)

class NonRecyclables(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = plastic_bag
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
non_recycle = pygame.sprite.Group()
for i in range(30):
    non_recyclable_sprites = NonRecyclables(random.randint(0, 864), random.randint(0, 600))
    non_recycle.add(non_recyclable_sprites)

class Bin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = bin
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
bin_group = pygame.sprite.Group()
bin_sprite = Bin(10, 10)
bin_group.add(bin_sprite)


while run:
    screen.blit(eco_circle, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    recycle.draw(screen)
    non_recycle.draw(screen)
    bin_group.draw(screen)
    pygame.display.update()