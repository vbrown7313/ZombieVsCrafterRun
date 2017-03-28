
from gamelib import *

game = Game(1300,690,"ZombieRun")
bk = Image("images//background2.jpg",game)
game.setBackground(bk)
bar1= Image("images//bar1.PNG",game)
bar1.resizeBy(-87)
bar1.moveTo(game.width/2+20,game.height-35)

bar1.setSpeed(4,90)
bar2= Image("images//bar1.PNG",game)
bar2.resizeBy(-87)
bar2.moveTo(bar1.x+ bar1.width,game.height-35)
bar2.setSpeed(4,90)
crafter= Animation("images//crafterwalk.PNG",8,game,2835/3, 2610/3, 4)
crafter.resizeBy(-70)
crafter.moveTo(game.width/2+150,game.height-180)
zombie= Animation("images//zombiewalk.PNG",24,game,7500/5, 7500/5, 4)
zombie.resizeBy(-70)
zombie.moveTo(game.width/2-220,game.height-195) 
spider= Animation("images//spider3.PNG",7,game,2250/3, 2250/3, 5)
spider.resizeBy(-85)
spider.moveTo(game.width/2+690,game.height-105)
spider.setSpeed(5,90)
axe= Image ("images//axe.PNG",game)
axe.resizeBy(-45)
axe.visible = False
poison= Image ("images//poison.PNG",game)
poison.resizeBy(-50)
poison.moveTo(game.width/2+690,game.height-105)
poison.setSpeed(5,90)
#Sounds
eating = Sound ("sounds//eating.WAV",1)
end = Sound ("sounds//end.WAV",2)
jump = Sound ("sounds//jump.WAV",3)
start = Sound ("sounds//start.WAV",4)
attack = Sound ("sounds//Zombie Attack.WAV",5)
zjump = Sound ("sounds//zjump.WAV",6)
bite = Sound ("sounds//bite.WAV",7)

#List
jumping1 = False
jumping2 = False
landed1 = False
landed2 = False 
factor1 = 1
factor2 = 1
meat= []
brain=[]

for num in range(20):
    meat.append(Image("images//chicken.GIF",game))
for m in meat:
    m.resizeBy(-70)
    x = game.width + randint(100 ,10500)
    y = randint(275 ,320)
    s = randint(4,8)
    m.moveTo(x,y)
    m.setSpeed(s,90)
for num in range(20):
    brain.append(Image("images//brain.PNG",game,))
for b in brain:
    b.resizeBy(-45)
    x = game.width + randint(100 ,10500)
    y = randint(260 ,310)
    s = randint(4,8)
    b.moveTo(x,y)
    b.setSpeed(s,90)
#PreGame
game.drawBackground()
start.play()
text= Image("images//cooltext.png",game)
text.moveTo (game.width/2, game.height/4)
text.resizeBy(150)
game.drawText("Press[UP] to start",game.width/2, game.height/2+200, Font(white,55, yellow) )
game.update()
game.wait(K_UP)
text.visible= False
#Variables
speed = 3

#Loop
while not game.over:
    game.processInput()
    bk.draw()
    game.scrollBackground("left",4)
    bar1.move()
    bar2.move()
    spider.move()
    axe.move()
    poison.move()
    text.draw()
    

    for m in meat:
        m.move()
        if crafter.collidedWith(m):
            crafter.health+=3
            m.visible= False
            eating.play()
    for b in brain:
        b.move()
        if zombie.collidedWith(b):
            zombie.health+=3
            b.visible= False
            bite.play()
    if spider.isOffScreen("left"):
        spider.move()
        spider.moveTo(game.width/2+690,game.height-105)
        spider.setSpeed(speed,90)
        speed += 1
    if poison.isOffScreen("left"):
        poison.move()
        poison.moveTo(game.width/2+690,game.height-105)
        poison.setSpeed(speed,90)
        speed += 1
  
    #Scroll Bar
    if bar1.isOffScreen("left"):
        bar1.draw()
        bar1.moveTo(bar2.x+bar2.width,game.height-35)
        bar1.setSpeed(4,90)
    if bar2.isOffScreen("left"):
        bar2.draw()
        bar2.moveTo(bar1.x+bar1.width,game.height-35)
        bar2.setSpeed(4,90)

    #Zombie Control
    if keys.Pressed[K_a]:
        zombie.prevFrame()
        zombie.x -= 8
    elif keys.Pressed[K_d]:
        zombie.nextFrame()
        zombie.x += 1
    else:
        zombie.draw()

        
    if zombie.y < 500 :
        landed1 = False  
    else:
        landed1 = True
        
    if jumping1:
        zombie.y -= 27 * factor1
        factor1 *= .95
        if factor1 < .18 :
            jumping1 = False
            factor1 = 1        
    if keys.Pressed[K_w] and landed1 and not jumping1:
            jumping1 = True
            zjump.play()
    if not landed1:
        zombie.y += 9

    #Crafter Control
    if keys.Pressed[K_LEFT]:
        crafter.prevFrame()
        crafter.x -= 8
    elif keys.Pressed[K_RIGHT]:
        crafter.nextFrame()
        crafter.x += 8
    else:
        crafter.draw()
        
    if crafter.y < 500 :
        landed2 = False  
    else:
        landed2 = True
        
    if jumping2:
        crafter.y -= 27 * factor2
        factor2 *= .95
        landed2 = False
        if factor2 < .18:
            jumping2 = False
            factor2 = 1
    if keys.Pressed[K_UP] and landed2 and not jumping2:
            jumping2 = True
            jump.play()
    if not landed2:
        crafter.y += 9
    if keys.Pressed[K_SPACE]:
        axe.visible = True
        axe.moveTo(crafter.x,crafter.y)
        axe.setSpeed(10 ,90)
#Challenges       
    if zombie.collidedWith(spider):
        zombie.health-=5
        spider.visible= False
        spider.moveTo(game.width/2+690,game.height-105)
        spider.setSpeed(speed,90)
        speed += 1
        spider.visible=True
        attack.play()
    if crafter.collidedWith(poison):
        crafter.health-=5
        poison.visible= False
        poison.moveTo(game.width/2+690,game.height-105)
        poison.setSpeed(speed,90)
        speed += 1
        poison.visible=True
    if zombie.collidedWith(axe):
        zombie.moveTo (game.width/2-425,game.height-195)
        attack.play()
#Game Over
    if zombie.health < 0:
        game.over = True
        end.play()
    if crafter.health < 0:
        game.over = True
        end.play()
    if zombie.collidedWith(crafter):
        game.over = True
        end.play()

 
    
    
    game.drawText("Crafter: " + str(crafter.health),5,5,Font(white,24,black,"ZEN.ttf"))
    game.drawText("Zombie: " + str(zombie.health),200,5,Font(white,24,black,"ZEN.ttf"))
    

    game.update(60)


#Game over SCREENS
if zombie.health < 0:
    game.drawText("Crafter won",game.width/4,game.height/4, Font(black,100,black,"ZEN.ttf"))
    game.drawText("Press Space to Exit",game.width/5,game.height/6, Font(white,23,black,"ZEN.ttf"))

if crafter.health < 0:
    game.drawText("Zombie won",game.width/4,game.height/4, Font(blue,100,black,"ZEN.ttf"))
    game.drawText("Press Space to Exit",game.width/5,game.height/6, Font(white,23,black,"ZEN.ttf"))
if zombie.collidedWith(crafter):
    game.drawText("GAME OVER",game.width/4,game.height/4, Font(blue,100,black,"ZEN.ttf"))
    game.drawText("Press Space to Exit",game.width/5,game.height/6, Font(white,23,black,"ZEN.ttf"))

game.update()
game.wait(K_SPACE)
game.quit()
