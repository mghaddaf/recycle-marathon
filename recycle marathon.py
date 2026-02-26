import pygame, random
pygame.init()
WIDTH = 864
LENGTH = 600
run = True
score = 0
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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                bin_sprite.rect.y = bin_sprite.rect.y - 1
            if event.key == pygame.K_DOWN:
                bin_sprite.rect.y = bin_sprite.rect.y + 1
            if event.key == pygame.K_LEFT:
                bin_sprite.rect.x = bin_sprite.rect.x - 1
            if event.key == pygame.K_RIGHT:
                bin_sprite.rect.x = bin_sprite.rect.x + 1
    Kb = pygame.key.get_pressed()
    if Kb[pygame.K_UP]:
        bin_sprite.rect.y = bin_sprite.rect.y - 1
    if Kb[pygame.K_DOWN]:
        bin_sprite.rect.y = bin_sprite.rect.y + 1
    if Kb[pygame.K_LEFT]:
        bin_sprite.rect.x = bin_sprite.rect.x - 1
    if Kb[pygame.K_RIGHT]:
        bin_sprite.rect.x = bin_sprite.rect.x + 1
    recycle.draw(screen)
    non_recycle.draw(screen)
    bin_group.draw(screen)
    if pygame.sprite.groupcollide(bin_group, recycle, False, True):
        score = score + 1
    if pygame.sprite.groupcollide(bin_group, non_recycle, False, True):
        score = score - 1
    
    font1 = pygame.font.SysFont("Comic Sans MC", 45)
    message1 = font1.render(("Score = " + str(score)), True, "white")
    screen.blit(message1, (10, 25))
    pygame.display.update()