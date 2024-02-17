import cv2
import numpy as np
import random

canvas = np.zeros((300, 800, 3), dtype=np.uint8)+255

x_pos = 50
y_pos = 150

velocity = 5

jump_velocity = 5

is_jumping = False
initial_y_pos = y_pos

obstacle_x = random.randint(100, 500)
obstacle_y = 120
obstacle_width = 10
obstacle_height = 50

game_start = False
font = cv2.FONT_HERSHEY_SIMPLEX

cv2.putText(canvas, 'Press S to start the Game!!', (200, 150), font, 1, (0, 0, 0), 2, cv2.LINE_AA)
cv2.putText(canvas, 'Bouncer Game', (300, 180), font, 1, (0, 0, 255), 2, cv2.LINE_AA)

cv2.imshow('Moving Circle', canvas)

if cv2.waitKey() == ord('s'):
    game_start = True

while game_start:
    x_pos += velocity
    
    if x_pos >= 780 or x_pos <= 20:
        velocity *= -1

    if is_jumping:
        y_pos -= jump_velocity
        if y_pos <= initial_y_pos - 50:
            is_jumping = False

    else:
        if y_pos < initial_y_pos:
            y_pos += jump_velocity
        else:
            y_pos = initial_y_pos

    canvas.fill(255)
    
    cv2.rectangle(canvas, (obstacle_x, obstacle_y), 
                  (obstacle_x + obstacle_width, obstacle_y + obstacle_height), 
                  (0, 0, 0), -1)
    
    cv2.rectangle(canvas, (obstacle_x + 200, obstacle_y), 
                  (obstacle_x + 200 + obstacle_width, obstacle_y + obstacle_height), 
                  (0, 0, 0), -1)
    
    cv2.circle(canvas, (x_pos, y_pos), 20, (0, 0, 0), -1)
    cv2.line(canvas,[50,170],[780,170],(0,0,0),2)

    cv2.imshow('Moving Circle', canvas)
    
    if (x_pos >= obstacle_x and x_pos <= obstacle_x + obstacle_width and
        y_pos >= obstacle_y and y_pos <= obstacle_y + obstacle_height):
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(canvas, 'Game Over', (300, 150), font, 1, (0, 0, 255), 2, cv2.LINE_AA)
        cv2.imshow('Moving Circle', canvas)
        cv2.waitKey(2000)
        break

    if (x_pos >= obstacle_x + 200 and x_pos <= obstacle_x + 200 + obstacle_width and
        y_pos >= obstacle_y and y_pos <= obstacle_y + obstacle_height):
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(canvas, 'Game Over', (300, 150), font, 1, (0, 0, 255), 2, cv2.LINE_AA)
        cv2.imshow('Moving Circle', canvas)
        cv2.waitKey(2000)
        break
    
    key = cv2.waitKey(30)
    if key == ord(' '): 
        is_jumping = True

    if key == ord('q'):
        break

cv2.destroyAllWindows()
