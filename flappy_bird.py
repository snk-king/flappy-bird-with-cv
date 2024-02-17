import cv2
import numpy as np

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 300
bird_img_path = "image/bird.png"
bird_img = cv2.imread(bird_img_path)
pipe_path = "image/pipe.png"
pipe_img = cv2.imread(pipe_path)
bg_path = "image/bg.jpg"
bg_img = cv2.imread(bg_path)
bg = cv2.resize(bg_img, (WINDOW_WIDTH, WINDOW_HEIGHT))

WINDOW_NAME = "Jumping Game"
OBSTACLE_WIDTH = 30
OBSTACLE_HEIGHT = 80
OBSTACLE_COLOR = (0, 0, 0)
JUMP_HEIGHT = 5

bird_width = 40
bird_height = 30
pipe_width = 40
pipe_height = 80

bird_x = 50
bird_y = 150

velocity_y = 0
gravity = 1
is_jumping = False
obstacle_x = WINDOW_WIDTH
obstacle_y = WINDOW_HEIGHT - OBSTACLE_HEIGHT
obstacle2_y = WINDOW_HEIGHT - 300
obstacle_speed = 5
score = 0


def draw_bird(window):
    global bird_img, bird_width, bird_height, bird_x, bird_y, WINDOW_HEIGHT
    bird_resized = cv2.resize(bird_img, (bird_width, bird_height))

    if bird_y < 0:
        bird_y = 0
    elif bird_y + bird_height > WINDOW_HEIGHT:
        print(bird_y)
        bird_y = WINDOW_HEIGHT - bird_height

    window[bird_y: bird_y + bird_height, bird_x: bird_x + bird_width] = bird_resized


def draw_obstacle(window):
    global pipe_img, obstacle_x, obstacle_y
    obstacle_resize = cv2.resize(pipe_img, (pipe_width, pipe_height))
    cv2.rectangle(window, (obstacle_x, obstacle_y), (obstacle_x + OBSTACLE_WIDTH, obstacle_y + OBSTACLE_HEIGHT),
                  OBSTACLE_COLOR, -1)


def draw_obstacle2(window):
    global obstacle_x, obstacle2_y
    cv2.rectangle(window, (obstacle_x, obstacle2_y), (obstacle_x + OBSTACLE_WIDTH, obstacle2_y + OBSTACLE_HEIGHT),
                  OBSTACLE_COLOR, -1)


def is_colliding():
    global bird_x, bird_y, obstacle_x, obstacle_y
    if bird_x + bird_width > obstacle_x and bird_x < obstacle_x + OBSTACLE_WIDTH:
        if bird_y + bird_height > obstacle_y or bird_y < obstacle2_y + OBSTACLE_HEIGHT:
            return True

    return False


def main():
    global bird_x, bird_y, velocity_y, is_jumping, obstacle_x, obstacle_speed, score
    cv2.namedWindow(WINDOW_NAME)
    while True:
        frame = bg.copy()
        draw_bird(frame)
        draw_obstacle(frame)
        draw_obstacle2(frame)
        cv2.putText(frame, f"Score: {score}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
        cv2.imshow(WINDOW_NAME, frame)
        key = cv2.waitKey(20)

        if key == ord(' '):
            is_jumping = True
            velocity_y = -10

        if key == ord('q'):
            break

        if is_jumping:
            bird_y += velocity_y
            velocity_y += gravity

            if bird_y >= WINDOW_HEIGHT - bird_height:
                is_jumping = False

        obstacle_x -= obstacle_speed
        if obstacle_x < 0:
            obstacle_x = WINDOW_WIDTH
            score += 1

        if is_colliding():
            cv2.putText(frame, "Game Over", (300, 150), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 4)
            cv2.putText(frame, f"Score:{score}", (400, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            cv2.imshow(WINDOW_NAME, frame)
            cv2.waitKey()
            break

    cv2.destroyAllWindows()


main()
