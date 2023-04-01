# imports
import turtle
import time

# can customise
width = 1000
height = 800
############

# find canvas values
widthTrue = width/2
heightTrue = height/2
groundHeight = -heightTrue + heightTrue/4 #<---- Can customise for different ground height

# draw canvas
window = turtle.Screen()
window.setup(width, height)
window.tracer(0)

# player
class Player:
    heading = "stop"
    onGround = True
    jumping = False
    vy = 0
    
    # can customise
    jumpHeight = 25
    speed = 20
    gravity = 3
    width = 2
    height = 3
    ##########
    
    # drawing player square
    def drawPlayer(height, width):
        player = turtle.Turtle()
        player.shape("square")
        player.shapesize(height, width)
        player.penup()
        return player
    
    # creating instance
    player = drawPlayer(height, width)
    
    # functions for inputs
    def left():
        Player.heading="left"
    
    def right():
        Player.heading="right"
    
    def down():
        Player.heading="stop"
    
    def jump(player):
        Player.jumping = True
    
    def stopJump():
        Player.jumping = False
        Player.vy = Player.jumpHeight
        
    # gravity script
    def physics(player, gravity):
        if player.ycor() > groundHeight+(Player.height*10):
            player.sety(player.ycor()-gravity)
    
    # listening to inputs
    def handleInput(left, right, down, jump, stopJump):
        window.listen()
        window.onkeypress(left, "a")
        window.onkeypress(right, "d")
        window.onkeypress(down, "s")
        window.onkeypress(jump(Player.player), "w")
        window.onkeyrelease(stopJump, "w")

    # moving the player
    def move(player):
        if Player.heading == "left":
            player.setx(player.xcor()-Player.speed)
        if Player.heading == "right":
            player.setx(player.xcor()+Player.speed)
        
        if Player.jumping:
            player.sety(player.ycor()+Player.vy)
            Player.vy -= 1
        
        if player.ycor() <= groundHeight+(Player.height*10):
            player.sety(groundHeight+(Player.height*10))
            Player.vy = 0
        
    # keep player in bounds
    def borders(player):
        if player.xcor() < -widthTrue+(Player.width*10):
            player.setx(-widthTrue+(Player.width*10))
        if player.xcor() > widthTrue-(Player.width*10):
            player.setx(widthTrue-(Player.width*10))
        
    # loop
    def update():
        time.sleep(0.01)
        Player.handleInput(Player.left, Player.right, Player.down, Player.jump, Player.stopJump)
        Player.move(Player.player)
        Player.borders(Player.player)
        Player.physics(Player.player, Player.gravity)
    
# draw ground
turtle.hideturtle()
turtle.penup()
turtle.goto(-widthTrue, groundHeight)
turtle.pendown()
turtle.goto(widthTrue, groundHeight)

# main loop
while True:
    Player.update()
    window.update()