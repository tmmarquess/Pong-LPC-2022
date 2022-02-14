import turtle
import winsound

# Initialize screen
screen = turtle.Screen()
screen.setup(800, 600)
screen.title('Pong Game')
turtle.hideturtle()
turtle.speed(0)
turtle.tracer(0, 0)

# Constants
FPS = 30  # constant: refresh about 30 times per second
TIMER_VALUE = 1000 // FPS  # the timer value in milliseconds for timer events
SPEED = 200  # ball speed

# Variables
ball = turtle.Turtle()  # ball of the pong game
current_ball_xpos = 1  # current ball x coordinate
current_ball_ypos = 1  # current ball y coordinate
speed_up_ball = False  # variable to control ball speed

left_paddle = turtle.Turtle()  # left paddle
current_left_paddle_xpos = -350  # current left paddle x coordinate
current_left_paddle_ypos = 1  # current left y coordinate

right_paddle = turtle.Turtle()  # right paddle
current_right_paddle_xpos = 350  # current right paddle x coordinate
current_right_paddle_ypos = 1  # current right y coordinate

player_1_hud = turtle.Turtle()  # player 1 head-up display
current_player_1_hud_xpos = -50  # current  player 1 head-up display x coordinate
current_player_1_ypos = 260  # current  player 1 head-up display x coordinate

player_2_hud = turtle.Turtle()  # player 2 head-up display
current_player_2_hud_xpos = 50  # current  player 2 head-up display x coordinate
current_player_2_ypos = 260  # current  player 2 head-up display x coordinate

player_1_score = 0  # player 1 score
player_2_score = 0  # player 2 score

dividing_line = []  # list which represents pong game dividing line
current_dividing_line_xpos = []  # list of dividing line current x coordinate
current_dividing_line_ypos = []  # list of dividing line current y coordinate
lines = 18  # number of lines

# Variables to control colissions
touch_upper_wall = False
touch_lower_wall = True
touch_rigth_wall = False
touch_left_wall = True


def initialize_game():
    ball.up()

    left_paddle.up()

    right_paddle.up()

    player_1_hud.hideturtle()
    player_1_hud.up()

    player_2_hud.hideturtle()
    player_2_hud.up()

    aux_ypos = -270
    for i in range(lines):
        dividing_line.append(turtle.Turtle())
        current_dividing_line_xpos.append(1)
        current_dividing_line_ypos.append(aux_ypos)
        aux_ypos += 32
    for d in dividing_line:
        d.up()


def left_paddle_up():
    global current_left_paddle_ypos

    if current_left_paddle_ypos < 250:
        current_left_paddle_ypos += 30
    else:
        current_left_paddle_ypos = 250


def left_paddle_down():
    global current_left_paddle_ypos

    if current_left_paddle_ypos > -250:
        current_left_paddle_ypos -= 30
    else:
        current_left_paddle_ypos = -250


def right_paddle_up():
    global current_right_paddle_ypos

    if current_right_paddle_ypos < 250:
        current_right_paddle_ypos += 30
    else:
        current_right_paddle_ypos = 250


def right_paddle_down():
    global current_right_paddle_ypos

    if current_right_paddle_ypos > -250:
        current_right_paddle_ypos -= 30
    else:
        current_right_paddle_ypos = -250


def update_ball_position():
    global current_ball_xpos, current_ball_ypos, touch_upper_wall, touch_lower_wall, touch_rigth_wall, touch_left_wall,\
        current_left_paddle_xpos, current_left_paddle_ypos, current_right_paddle_xpos, current_right_paddle_ypos, \
        player_1_score, player_2_score, speed_up_ball, SPEED

    # changes the current position of the ball based on collisions
    if touch_upper_wall and touch_rigth_wall:
        if speed_up_ball:
            SPEED += SPEED * 0.001
        current_ball_xpos += SPEED / FPS * -1
        current_ball_ypos += SPEED / FPS * -1
    elif touch_upper_wall and touch_left_wall:
        if speed_up_ball:
            SPEED += SPEED * 0.001
        current_ball_xpos += SPEED / FPS * 1
        current_ball_ypos += SPEED / FPS * -1
    elif touch_lower_wall and touch_rigth_wall:
        if speed_up_ball:
            SPEED += SPEED * 0.001
        current_ball_xpos += SPEED / FPS * -1
        current_ball_ypos += SPEED / FPS * 1
    else:
        if speed_up_ball:
            SPEED += SPEED * 0.001
        current_ball_xpos += SPEED / FPS * 1
        current_ball_ypos += SPEED / FPS * 1

    # collision with the upper wall
    if current_ball_ypos > 290:
        winsound.PlaySound('pong_bounce.wav', winsound.SND_ASYNC)
        touch_upper_wall = True
        touch_lower_wall = False

    # collision with the lower wall
    if current_ball_ypos < -290:
        winsound.PlaySound('pong_bounce.wav', winsound.SND_ASYNC)
        touch_lower_wall = True
        touch_upper_wall = False

    # collision with the left wall:
    if current_ball_xpos < -390:
        winsound.PlaySound('258020__kodack__arcade-bleep-sound.wav', winsound.SND_ASYNC)
        current_ball_xpos = 1
        current_ball_ypos = 1
        touch_upper_wall = False
        touch_lower_wall = True
        touch_rigth_wall = False
        touch_left_wall = True
        player_2_score += 1
        player_2_hud.clear()
        player_2_hud.write('{}'.format(player_2_score), align='center', font=('Small Fonts', 24, 'normal'))
        speed_up_ball = False
        SPEED = 200

    # collision with the righ wall:
    if current_ball_xpos > 390:
        winsound.PlaySound('258020__kodack__arcade-bleep-sound.wav', winsound.SND_ASYNC)
        current_ball_xpos = 1
        current_ball_ypos = 1
        touch_upper_wall = False
        touch_lower_wall = True
        touch_rigth_wall = True
        touch_left_wall = False
        player_1_score += 1
        player_1_hud.clear()
        player_1_hud.write('{}'.format(player_1_score), align='center', font=('Small Fonts', 24, 'normal'))
        speed_up_ball = False
        SPEED = 200

    # collision with left paddle
    if current_ball_xpos < -330 and current_left_paddle_ypos + 40 > current_ball_ypos > current_left_paddle_ypos - 40:
        print('Bola tocou raquete esquerda!')
        print(f'Coordenada x da bola: {current_ball_xpos}')
        print(f'Coordenada y da bola: {current_ball_ypos}')
        print(f'Coordenada x da raquete: {current_left_paddle_xpos}')
        print(f'Coordenada y da raquete: {current_left_paddle_ypos}')
        winsound.PlaySound('pong_bounce.wav', winsound.SND_ASYNC)
        current_ball_xpos += SPEED / FPS * 1 + 50
        touch_left_wall = True
        touch_rigth_wall = False
        speed_up_ball = True

    # collision with right paddle
    if current_ball_xpos > 330 and current_right_paddle_ypos + 40 > current_ball_ypos > current_right_paddle_ypos - 40:
        print('Bola tocou raquete direita!')
        print(f'Coordenada x da bola: {current_ball_xpos}')
        print(f'Coordenada y da bola: {current_ball_ypos}')
        print(f'Coordenada x da raquete: {current_right_paddle_xpos}')
        print(f'Coordenada y da raquete: {current_right_paddle_ypos}')
        winsound.PlaySound('pong_bounce.wav', winsound.SND_ASYNC)
        current_ball_xpos += SPEED / FPS * -1 - 50
        touch_rigth_wall = True
        touch_left_wall = False
        speed_up_ball = True


def update_states():
    global should_draw
    update_ball_position()
    should_draw = True
    screen.ontimer(update_states, TIMER_VALUE)


def draw():
    global should_draw, current_ball_xpos, current_ball_ypos, player_1_score, player_2_score
    if not should_draw:  # There is no change. Don't draw and return immediately
        return

    ball.clear()  # clear the current drawing
    ball.color('white')
    ball.shape('square')
    ball.goto(current_ball_xpos, current_ball_ypos)

    left_paddle.clear()
    left_paddle.color('white')
    left_paddle.shape('square')
    left_paddle.shapesize(stretch_wid=5, stretch_len=1)
    left_paddle.goto(current_left_paddle_xpos, current_left_paddle_ypos)

    right_paddle.clear()
    right_paddle.color('white')
    right_paddle.shape('square')
    right_paddle.shapesize(stretch_wid=5, stretch_len=1)
    right_paddle.goto(current_right_paddle_xpos, current_right_paddle_ypos)

    player_1_hud.shape('square')
    player_1_hud.color('white')
    player_1_hud.goto(current_player_1_hud_xpos, current_player_1_ypos)
    player_1_hud.clear()
    player_1_hud.write('{}'.format(player_1_score), align='center', font=('Small Fonts', 24, 'normal'))

    player_2_hud.shape('square')
    player_2_hud.color('white')
    player_2_hud.goto(current_player_2_hud_xpos, current_player_2_ypos)
    player_2_hud.clear()
    player_2_hud.write('{}'.format(player_2_score), align='center', font=('Small Fonts', 24, 'normal'))

    for i in range(lines):
        dividing_line[i].clear()
        dividing_line[i].color('white')
        dividing_line[i].shape('square')
        dividing_line[i].goto(current_dividing_line_xpos[i], current_dividing_line_ypos[i])

    should_draw = False  # just finished drawing, set should_draw to False


# keyboard
screen.listen()
screen.onkeypress(left_paddle_up, 'w')
screen.onkeypress(left_paddle_down, 's')
screen.onkeypress(right_paddle_up, 'Up')
screen.onkeypress(right_paddle_down, 'Down')

screen.bgcolor('black')
initialize_game()
update_states()
while True:
    draw()  # draw forever
    screen.update()
