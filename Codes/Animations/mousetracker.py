from graphics import Canvas
import time

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
PAUSE_TIME = 1/50

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    while True:
        mouse_x = canvas.get_mouse_x()
        mouse_y = canvas.get_mouse_y()
        time.sleep(PAUSE_TIME)
        print(f"Mouse Location: {str(mouse_x)}, {str(mouse_y)}")

if __name__ == '__main__':
    main()