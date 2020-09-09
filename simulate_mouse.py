import pyautogui
import random
import time

# defines the duration it should take to move mouse from a to b -> Gets choosen randomly between the min and max value
duration_range = (1, 10)

# defines the min/max duration the script should pause between mouse moves
sleep_range = (5, 100)

# get screen dimensions
display_width, display_height = pyautogui.size()


# simulate mouse movement randomly across the screen
def simulate(width=display_width, height=display_height, duration=duration_range, sleep = sleep_range):
    while True:
        # adjust screen - 10% padding
        pyautogui.moveTo(random.randint(width*0.1, width*0.9),
                         random.randint(height*0.1, height*0.9),
                         random.randint(duration[0], duration[1])/10)
        time.sleep(random.randint(sleep[0], sleep[1]))


if __name__ == "__main__":
    simulate()