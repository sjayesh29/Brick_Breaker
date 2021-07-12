import pygame
# importing pygame module fro accessing all functions of pygame
pygame.init()
# initialising
screen = pygame.display.set_mode((400,500))
green = (0, 255, 0)
blue = (0, 0, 128)
# setting height and width of screen to be shown
x=200
y=490

# initialising co-ordinates of bar
a=x+75
b=y
# initialising center of ball
dirb=1
dira=1
# initialising direction of movement of ball
font = pygame.font.Font('freesansbold.ttf', 32)# setting font
text = font.render('Victory', True, green, blue)# setting text
textRect = text.get_rect()# making rectangle for the the text to be displayed in
textRect.center = (400 // 2, 500 // 2)# setting center of rectangle
# setting text to be visible after completion it's size,place and font
vel=10
# initialising velocity of bar
done=False
finish = False
flag=0
# for identifying whether ball has fallen in pit or not
shoot=0
# for deciding when to shoot the ball
arr = [[0 for i in range(20)] for j in range(25)]
# initialising map
empty_arr=[[0 for i in range(20)] for j in range(25)]
# creating an empty array to know whether all bricks are broken or not

for i in range(15):
    arr[i][0]=1
for i in range(20):
    arr[0][i]=1
for i in range(20):
    arr[14][i]=1
for i in range(15):
    arr[i][19]=1
for i in range(8):
    arr[i][i]=1
    arr[14-i][i]=1
    arr[i][19-i]=1
    arr[14-i][19-i]=1

for i in range(8,13):
    arr[7][i]=1
# setting map

while not done:# starting an infinite loop
    pygame.time.delay(20)# setting time delay
    for event in pygame.event.get():# getting next event in game
        if event.type == pygame.QUIT:# quitting game if closed
            done = True
    if(flag): # if ball has fallen in pit
        a=x+35
    if (shoot):# shooting ball if pressed space bar
       dirb=-1
       dira=1
       flag=0
       shoot=0
    b=b+dirb*5
    a=a+dira*5
    # updating center of ball
    if(a>=390):
        dira=-1
    if(a<=0):
        dira=1
    if(b<=0):
        dirb=1
    # boundary conditions
    if(b>=490):
        if(a>=x and a<=x+70):
            dirb=-1
        # if ball striked the bar reversing the direction of ball
        else:
            a=x+35
            b=y-10
            dira=0
            dirb=0
            flag=1
        # if ball has fallen in pit then placing the ball on center of the bar making it ready to launch

    if(arr[(int)(b/20)][(int)(a/20)]==1):
        arr[(int)(b/20)][(int)(a/20)]=0
        dirb=dirb*-1
    # checking if ball stricked a brick if yes then break the brick i.e. setting it's value to 0
    else:
        if((int)(a/20)+1<20 and arr[(int)(b/20)][(int)(a/20)+1]==1 and a>a/20+10):
            arr[(int)(b/20)][(int)(a/20)+1]=0
            dirb=dirb*-1
        if((int)(a/20)-1>0 and arr[(int)(b/20)][(int)(a/20)-1]==1 and a<a/20+10):
            arr[(int)(b/20)][(int)(a/20)-1]=0
            dirb=dirb*-1
        if((int)(b/20)-1>0 and arr[(int)(b/20)-1][(int)(a/20)]==1 and b<b/20+10):
            arr[(int)(b/20)-1][(int)(a/20)]=0
            dira=dira*-1
        if((int)(b/20)+1<25 and arr[(int)(b/20)+1][(int)(a/20)]==1 and b>b/20+10):
            arr[(int)(b/20)+1][(int)(a/20)]=0
            dira=dira*-1
        if(arr==empty_arr):
            finish=True
    # checking if ball has striked neighouring bricks
    keys = pygame.key.get_pressed()
    # if key is pressed or not

    if keys[pygame.K_LEFT]:
        x -= vel

    if keys[pygame.K_RIGHT]:
        x += vel
    # moving bar using left and right key
    if keys[pygame.K_SPACE]:
        shoot=1
    # shooting ball if pressed space
    if x>=330:
        x=330
    if x<=0:
        x=0
    # boundary condition for bar
    screen.fill((0,0,0))
    # refreshing screen
    for i in range(15):
        for j in range(20):
            if arr[i][j]==1:
                pygame.draw.rect(screen, (0, 125, 255),[j*20,i*20,20,20])

    # drawing map
    pygame.draw.rect(screen, (0, 125, 255), pygame.Rect(x, y, 70, 10))
    # drawing bar
    pygame.draw.circle(screen,(0, 125, 255),[a,b],10)
    # drawing ball
    if(finish):
        screen.fill((0,0,0))
        screen.blit(text, textRect)
    #displaying victory after completion



    pygame.display.flip()
    pygame.display.update()
    # updating event

