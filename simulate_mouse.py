import pyautogui
import random
import time

# defines the duration it should take to move mouse from a to b -> Gets choosen randomly between the min and max value
duration_range = (1, 10)

# defines the min/max duration the script should pause between mouse moves
sleep_range = (5, 100)

# get screen dimensions
display_width, display_height = pyautogui.size()


def simulate_mouse(width=display_width, height=display_height, duration=duration_range, sleep=sleep_range):
    """simulate mouse movement randomly across the screen"""
    while True:
        # adjust screen - 10% padding
        pyautogui.moveTo(random.randint(width*0.1, width*0.9),
                         random.randint(height*0.1, height*0.9),
                         random.randint(duration[0], duration[1])/10)
        time.sleep(random.randint(sleep[0], sleep[1]))


def simulate_keys_volume(sleep=sleep_range):
    """simulate key presses"""
    while True:

        # increase volume and then decrease it to get original value
        pyautogui.press('volumeup')
        time.sleep(1)
        pyautogui.press('volumedown')

        # make random break until next volume changement
        time.sleep(random.randint(sleep[0], sleep[1]))


if __name__ == "__main__":
    # simulate_mouse()
    simulate_keys_volume()