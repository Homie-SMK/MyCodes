import pygame
import random


# 배경 화면 사각형 클래스
class BackgroundSquareClass(pygame.sprite.Sprite):
    def __init__(self, color, location):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.draw.rect(screen, color, location)
        self.location = location


# 캔디 클래스
class CandyClass(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.location = location


# 자동차 클래스
class CarClass(pygame.sprite.Sprite):
    def __init__(self, image_file, speed, location=[0, 120]):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.location = location

    def move(self):
        if event.key == pygame.K_UP:
            self.location[1] = self.location[1] - 5
            self.image = pygame.image.load("car_u.png")
            self.rect = self.image.get_rect()
            self.rect.left, self.rect.top = self.location
        elif event.key == pygame.K_DOWN:
            self.location[1] = self.location[1] + 5
            self.image = pygame.image.load("car_d.png")
            self.rect = self.image.get_rect()
            self.rect.left, self.rect.top = self.location
        elif event.key == pygame.K_RIGHT:
            self.location[0] = self.location[0] + 5
            self.image = pygame.image.load("car_r.png")
            self.rect = self.image.get_rect()
            self.rect.left, self.rect.top = self.location
        elif event.key == pygame.K_LEFT:
            self.location[0] = self.location[0] - 5
            self.image = pygame.image.load("car_l.png")
            self.rect = self.image.get_rect()
            self.rect.left, self.rect.top = self.location


pygame.init()
pygame.font.init()
screen = pygame.display.set_mode([650, 500])
screen.fill([120, 120, 120])

# 배경 사각형 객체 9개 생성
s1 = BackgroundSquareClass([0, 200, 200], [0, 0, 650, 50])
s2 = BackgroundSquareClass([0, 200, 200], [0, 50, 500, 50])
s3 = BackgroundSquareClass([0, 200, 200], [150, 100, 200, 100])
s4 = BackgroundSquareClass([0, 200, 200], [300, 200, 50, 100])
s5 = BackgroundSquareClass([0, 200, 200], [0, 200, 50, 100])
s6 = BackgroundSquareClass([0, 200, 200], [0, 300, 200, 100])
s7 = BackgroundSquareClass([0, 200, 200], [450, 200, 150, 200])
s8 = BackgroundSquareClass([0, 200, 200], [600, 150, 50, 250])
s9 = BackgroundSquareClass([0, 200, 200], [0, 400, 650, 100])

myCar = CarClass("car_r.png", 0)
score = 0
lives = 3
width = screen.get_rect().width
carWidth = myCar.image.get_width()
done = False

squareGroup = pygame.sprite.Group()
candyGroup = pygame.sprite.Group()
carGroup = pygame.sprite.Group()
squareGroup.add(s1, s2, s3, s4, s5, s6, s7, s8, s9)

# 점수폰트 생성
score_font = pygame.font.Font(None, 50)
score_surf = score_font.render(str(score), 1, (0, 0, 0))
score_pos = [10, 10]

# 캔디 50개를 화면에 무작위 위치에 생성하고 캔디 그룹에 추가
for countOfCandy in range(50):
    candy = CandyClass("candy.png", [random.randint(0, 650), random.randint(0, 500)])
    candyGroup.add(candy)

# 배경 사각형에 닫는 캔디들을 그룹에서 삭제
for square in squareGroup:
    pygame.sprite.spritecollide(square, candyGroup, True)

# 도로 위에만 캔디를 블릿
for candy in candyGroup:
    screen.blit(candy.image, candy.rect)

# 자동차를 초기 위치에 블릿
screen.blit(myCar.image, myCar.rect)
# 초기 점수를 화면에 블릿
screen.blit(score_surf, score_pos)
# 생명수 만큼 오른쪽 상단에 자동차 블릿
for life in range(lives):
    screen.blit(pygame.image.load("car_r.png"), [width - 40 * life, 20])
# 화면에 플립
pygame.display.flip()

# 방향키 누르고 있으면 연속 인식
delay = 100
interval = 50
pygame.key.set_repeat(delay, interval)

# 이벤트 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            pygame.draw.rect(screen, [120, 120, 120], [myCar.location[0], myCar.location[1], 40, 40])
            myCar.move()
    # 자동차가 움직일 때마다 캔디전체를 지우고
    for candy in candyGroup:
        pygame.draw.rect(screen, [120, 120, 120], [candy.location[0], candy.location[1], 20, 20])
    # 최신화 하여 다시 블릿
    if pygame.sprite.spritecollide(myCar, candyGroup, True):    # 자동차에 닿은 캔디 제거후 점수 50점 추가
        for candy in candyGroup:
            screen.blit(candy.image, candy.rect)
        score = score + 50
        pygame.draw.rect(screen, [0, 200, 200], [10, 10, 65, 65])
        score_surf = score_font.render(str(score), 1, (0, 0, 0))    # 점수에 변동이 있을 때마다 점수폰트를 최신화
    else:
        for candy in candyGroup:
            screen.blit(candy.image, candy.rect)

    # 자동차가 벽에 부딪힐 경우 자동차정보를 초기화 하고 생명과 점수를 깎음
    if pygame.sprite.spritecollide(myCar, squareGroup, False):
        if not done:
            myCar.__init__("car_r.png", 0, [0, 120])
            lives = lives - 1
            if lives == 0:
                finalText1 = "Game Over"
                finalText2 = "Your final score is : " + str(score)
                fT1Font = pygame.font.Font(None, 70)
                fT1Surf = fT1Font.render(finalText1, 1, (0, 0, 0))
                fT2Font = pygame.font.Font(None, 50)
                fT2Surf = fT2Font.render(finalText2, 1, (0, 0, 0))
                screen.blit(fT1Surf, [width / 2 - fT1Surf.get_width() / 2, 100])
                screen.blit(fT2Surf, [width / 2 - fT2Surf.get_width() / 2, 200])
                pygame.display.flip()
                done = True
            score = score - 100
            pygame.draw.rect(screen, [0, 200, 200], [10, 10, 65, 65])
            score_surf = score_font.render(str(score), 1, (0, 0, 0))
            if score < 0:
                score = 0
                pygame.draw.rect(screen, [0, 200, 200], [10, 10, 65, 65])
                score_surf = score_font.render(str(score), 1, (0, 0, 0))

    # 남은 생명 수만큼 오른쪽 상단에 자동차 이미지로 표시
    pygame.draw.rect(screen, [0, 200, 200], [0, 0, 650, 50], 0)

    for life in range(lives):
        screen.blit(pygame.image.load("car_r.png"), [width - 40 * life, 20])

    # 자동차가 목적지에 도착했을 경우 결과 표시
    if myCar.rect.left + carWidth > 650:
        finalText3 = "Success!!"
        finalText4 = "Your final score is : " + str(score)
        fT3Font = pygame.font.Font(None, 70)
        fT3Surf = fT3Font.render(finalText3, 1, (0, 0, 0))
        fT4Font = pygame.font.Font(None, 50)
        fT4Surf = fT4Font.render(finalText4, 1, (0, 0, 0))
        screen.blit(fT3Surf, [width / 2 - fT3Surf.get_width() / 2, 100])
        screen.blit(fT4Surf, [width / 2 - fT4Surf.get_width() / 2, 200])
        done = True
    if not done:
        screen.blit(score_surf, score_pos)
        screen.blit(myCar.image, myCar.rect)

    pygame.display.flip()

pygame.quit()
