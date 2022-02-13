import turtle

screen = turtle.Screen()
screen.setup(800, 600)
screen.title("Pong Game")
turtle.hideturtle()
turtle.speed(0)
turtle.tracer(0, 0)

# Constants
FPS = 60  # constant: refresh about 30 times per second
TIMER_VALUE = 1000 // FPS  # the timer value in milliseconds for timer events
SPEED = 500  # 100 units per second

# Variables
ball = turtle.Turtle()  # ball of the pong game
current_ball_xpos = 1  # current ball x coordinate
current_ball_ypos = 1  # current ball y coordinate
left_paddle = turtle.Turtle()
current_left_paddle_xpos = -350  # current left paddle x coordinate
current_left_paddle_ypos = 1  # current left y coordinate
right_paddle = turtle.Turtle()
current_right_paddle_xpos = 350  # current right paddle x coordinate
current_right_paddle_ypos = 1  # current right y coordinate
touch_upper_wall = False
touch_lower_wall = True
touch_rigth_wall = False
touch_left_wall = True


def initialze_game():
    ball.hideturtle()
    ball.up()
    left_paddle.up()
    right_paddle.up()


def update_position():
    global current_ball_xpos, current_ball_ypos, touch_upper_wall, touch_lower_wall, touch_rigth_wall, touch_left_wall

    # changes the current position of the ball based on collisions
    if touch_upper_wall and touch_rigth_wall:
        current_ball_xpos += SPEED / FPS * -1
        current_ball_ypos += SPEED / FPS * -1
    elif touch_upper_wall and touch_left_wall:
        current_ball_xpos += SPEED / FPS * 1
        current_ball_ypos += SPEED / FPS * -1
    elif touch_lower_wall and touch_rigth_wall:
        current_ball_xpos += SPEED / FPS * -1
        current_ball_ypos += SPEED / FPS * 1
    else:
        current_ball_xpos += SPEED / FPS * 1
        current_ball_ypos += SPEED / FPS * 1

    # collision with the upper wall
    if current_ball_ypos > 290:
        touch_upper_wall = True
        touch_lower_wall = False

    # collision with the lower wall
    if current_ball_ypos < -290:
        touch_lower_wall = True
        touch_upper_wall = False

    # collision with the left wall:
    if current_ball_xpos < -390:
        touch_left_wall = True
        touch_rigth_wall = False

    # collision with the righ wall:
    if current_ball_xpos > 390:
        touch_rigth_wall = True
        touch_left_wall = False


def update_states():
    global should_draw
    update_position()
    should_draw = True
    screen.ontimer(update_states, TIMER_VALUE)


def draw():
    global should_draw, current_ball_xpos, current_ball_ypos
    if not should_draw:  # There is no change. Don't draw and return immediately
        return

    ball.clear()  # clear the current drawing
    ball.color('white')
    ball.goto(current_ball_xpos, current_ball_ypos)
    ball.dot(30)

    left_paddle.clear()
    left_paddle.color('white')
    left_paddle.shape("square")
    left_paddle.shapesize(stretch_wid=5, stretch_len=1)
    left_paddle.goto(current_left_paddle_xpos, current_left_paddle_ypos)

    right_paddle.clear()
    right_paddle.color('white')
    right_paddle.shape("square")
    right_paddle.shapesize(stretch_wid=5, stretch_len=1)
    right_paddle.goto(current_right_paddle_xpos, current_right_paddle_ypos)

    should_draw = False  # just finished drawing, set should_draw to False


screen.bgcolor('black')
initialze_game()
update_states()
while True:
    draw()  # draw forever
    screen.update()
