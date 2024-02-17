import cv2
import numpy as np

img="image/bird.png"
bird_img=cv2.imread(img)
WINDOW_NAME = "Jumping Game"
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 300
CIRCLE_RADIUS = 20
CIRCLE_COLOR = (0, 0, 0)
OBSTACLE_WIDTH = 30
OBSTACLE_HEIGHT = 80
OBSTACLE_COLOR = (0, 0, 0)
JUMP_HEIGHT = 5

circle_x = 50
circle_y =  150
velocity_y = 0
gravity = 1
is_jumping = False
obstacle_x = WINDOW_WIDTH
obstacle_y = WINDOW_HEIGHT - OBSTACLE_HEIGHT

obstacle2_y=WINDOW_HEIGHT-300
obstacle_speed = 5
score = 0

def resize_img(image,height,width):
    return cv2.resize(image,(height,width))

def draw_circle(window):
    global circle_x, circle_y
    cv2.circle(window, (circle_x, circle_y), CIRCLE_RADIUS, CIRCLE_COLOR, -1, resize_img(bird_img,20,20))
   
   

def draw_obstacle(window):
    global obstacle_x, obstacle_y
    cv2.rectangle(window, (obstacle_x, obstacle_y), (obstacle_x + OBSTACLE_WIDTH, obstacle_y + OBSTACLE_HEIGHT), OBSTACLE_COLOR, -1)

def draw_obstacle2(window):
    global obstacle_x, obstacle2_y
    cv2.rectangle(window, (obstacle_x, obstacle2_y), (obstacle_x + OBSTACLE_WIDTH, obstacle2_y + OBSTACLE_HEIGHT), OBSTACLE_COLOR, -1)
def is_colliding():
    global circle_x, circle_y, obstacle_x, obstacle_y
    if circle_x + CIRCLE_RADIUS > obstacle_x and circle_x - CIRCLE_RADIUS < obstacle_x + OBSTACLE_WIDTH:
        if circle_y + CIRCLE_RADIUS > obstacle_y:
            return True
    return False

def main():
    global circle_x, circle_y, velocity_y, is_jumping, obstacle_x, obstacle_speed, score
    cv2.namedWindow(WINDOW_NAME)
    while True:
        frame = np.zeros((WINDOW_HEIGHT, WINDOW_WIDTH, 3), dtype=np.uint8) + 255
        draw_circle(frame)
       
        draw_obstacle(frame)
        draw_obstacle2(frame)
        cv2.putText(frame, f"Score: {score}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
        cv2.imshow(WINDOW_NAME, frame)
        key = cv2.waitKey(20)
        
        if key == ord(' '): 
            # if not is_jumping:
            is_jumping = True
            velocity_y = -10
                
        if key == ord('q'):
            break 
            
        if is_jumping:
            circle_y += velocity_y
            velocity_y += gravity
            
            if circle_y >= WINDOW_HEIGHT - CIRCLE_RADIUS:
                circle_y = WINDOW_HEIGHT - CIRCLE_RADIUS
                is_jumping = False
        
        obstacle_x -= obstacle_speed
        if obstacle_x < 0:
            obstacle_x = WINDOW_WIDTH
            score += 1
        
        if is_colliding():
            print("Game Over! Your score:", score)
            break
        
    cv2.destroyAllWindows()


main()
