import pyautogui
import random
import time

# defines the duration it should take to move mouse from a to b -> Gets choosen randomly between the min and max value
duration_range = (1, 100)

# defines the min/max duration the script should pause between mouse moves
sleep_range = (20, 300)

# get screen dimensions
display_width, display_height = pyautogui.size()


# simulate mouse movement randomly across the screen
def simulate(width=display_width, height=display_height, duration=duration_range, sleep = sleep_range):
    while True:
        pyautogui.moveTo(random.randint(0, width), random.randint(0, height), random.randint(duration[0], duration[1]))
        time.sleep(random.randint(sleep[0], sleep[1]))


if __name__ == "__main__":
    simulate()