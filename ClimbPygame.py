# Imports + Pygame Setup
import pygame, time, random, math

pygame.init()
clock = pygame.time.Clock()
run = True

# Define Colours
if True:
    black = (0, 0, 0)
    blue = (0, 0, 255)
    green = (0, 255, 0)
    cyan = (0, 255, 255)
    red = (255, 0, 0)
    pink = (255, 0, 255)
    yellow = (255, 255, 0)
    white = (255, 255, 255)

# Display
screensize = 1000
centrepoint = (screensize / 2, screensize / 2)
screen = pygame.display.set_mode((screensize, screensize))
armreach = 400


# Bg setup
class background():
    def __init__(self, screensize, gridsize):
        self.screensize = screensize
        self.gridsize = gridsize
        self.tilesize = screensize / gridsize

    def draw(self):
        for x in range(self.gridsize):
            for y in range(self.gridsize):
                if (x % 2 == 0 and y % 2 == 0) or (x % 2 == 1 and y % 2 == 1):
                    bgColour = (200, 200, 200)
                else:
                    bgColour = (170, 170, 170)

                bgX = self.tilesize * x
                bgY = self.tilesize * y

                pygame.draw.rect(screen, bgColour, (bgX, bgY, self.tilesize, self.tilesize))


screenbg = background(screensize, 10)  # Size, Gridbox amount


# Pointclass
class point():
    def __init__(self, linelength, point=centrepoint):
        self.cx, self.cy = point
        self.linelength = linelength
        self.goal = point

    def __length(self):
        length = (self.cx - self.gx) ** 2 + (self.cy - self.gy) ** 2
        length = math.sqrt(length)
        self.length = length

    def __change(self):
        dx = self.gx - self.cx
        dy = self.gy - self.cy
        self.dx = dx
        self.dy = dy

    def setgoal(self, point):
        self.gx, self.gy = point
        self.__length()
        self.__change()
        if self.length == 0:
            self.length = 0.00001
        self.goal = (self.cx + (self.dx / self.length) * self.linelength), (
                    self.cy + (self.dy / self.length) * self.linelength)
        return self.goal

    def getgoal(self):
        return self.goal

    def setcentre(self, point):
        self.cx, self.cy = point
        return point

    def getcentre(self):
        point = (self.cx, self.cy)
        return point


# Will return distance of 2 points
def distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    distance = (x2 - x1) ** 2 + (y2 - y1) ** 2
    distance = math.sqrt(distance)
    return distance


# limb
class limb():
    def __init__(self, segments=10, armlength=armreach, grabsize=10):
        segmentlength = armlength / segments
        self.points = [point(segmentlength) for _ in range(segments)]
        self.attach = attach(grabsize)

    def move(self, point1, point2=False):
        if point2 == False:
            newCentre = point1
            for segment in self.points:
                segment.setcentre(newCentre)
                segment.setgoal(segment.getgoal())
                newCentre = segment.getgoal()


        else:
            newCentre = point1
            for segment in self.points:
                segment.setcentre(newCentre)
                segment.setgoal(segment.getgoal())
                newCentre = segment.getgoal()
            newCentre = point2
            for segment in reversed(self.points):
                segment.setcentre(newCentre)
                segment.setgoal(segment.getgoal())
                newCentre = segment.getgoal()

    def draw(self, width=3, colour=pink):
        for point in self.points:
            pygame.draw.line(screen, colour, point.getcentre(), point.getgoal(), width)
        self.attach.draw()


class attach():
    def __init__(self, radius=10, vary = 100):
        self.x, self.y = centrepoint
        self.x = self.x + random.randint(-vary,vary)
        self.y = self.y + random.randint(-vary, vary)
        self.radius = radius

    def follow(self):
        self.x, self.y = cursor

    def draw(self, colour=red):
        pygame.draw.circle(screen, red, (self.x, self.y), self.radius, 0)

    def get(self):
        point = (self.x, self.y)
        return point

    def click(self):
        x, y = cursor
        cursor1 = pygame.Rect(x - 5, y - 5, 10, 10)
        radius = self.radius * 2
        hitbox = pygame.Rect(self.x - (radius / 2), self.y - (radius / 2), radius, radius)
        if cursor1.colliderect(hitbox):
            return True
        else:
            return False

class body():
    def __init__(self, armcount, armsD = ()):
        for i in range:
            item1
        self.arms = [limb(armD[0],armD[1],armD[2]) for _ in range(armcount)]
g = False
follow = False
body1 = body(1,(10,100))
cursor = pygame.mouse.get_pos()
# while run:
#     cursor = pygame.mouse.get_pos()
#     events = pygame.event.get()
#     for event in events:
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_SPACE:
#                 if g:
#                     g = False
#                 else:
#                     g = True
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             if arm2.attach.click():
#                 follow = True
#
#
#         elif event.type == pygame.MOUSEBUTTONUP:
#             if arm2.attach.click():
#                 follow = False
#     screenbg.draw()
#
#     # Draw Graphic Shapes
#     pygame.draw.line(screen, pink, centrepoint, cursor, 3)
#     pygame.draw.circle(screen, black, centrepoint, armreach, 3)
#     pygame.draw.circle(screen, yellow, centre.setgoal(cursor), 5, 0)
#     pygame.draw.line(screen, yellow, centrepoint, centre.setgoal(cursor), 3)
#     pygame.draw.circle(screen, red, centrepoint, 8, 0)
#     pygame.draw.circle(screen, pink, cursor, 5, 0)
#
#     if distance(centrepoint, arm2.attach.get()) > distance(centrepoint, centre.setgoal(arm2.attach.get())):
#         goal = centre.getgoal()
#     else:
#         goal = arm2.attach.get()
#
#     if g:
#         arm2.move(goal, centrepoint)
#     else:
#         arm2.move(goal)
#
#     if follow:
#         arm2.attach.follow()
#     arm2.draw(4, green)
#
#     clock.tick(60)
#     pygame.display.update()
#
# pygame.quit()