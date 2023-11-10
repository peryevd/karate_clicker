import pyautogui
import keyboard
import time


def main():
    """
    Clicks on the left or right side of the screen based on the color of the pixels.
    """
    # Define the left and right colors
    left_color = (195, 130, 80)
    right_color = (123, 61, 30)

    # Define the offset for the right pixel
    right_offset = 130

    # Define the initial click position
    x = 1881
    y = 965

    # Initialize the queue and set the initial position
    queue = ["left", "left"]
    position = "left"

    while True:
        # Pause for a short duration
        time.sleep(0.001)

        # Check if the 'Esc' key is pressed and exit if it is
        if keyboard.is_pressed('Esc'):
            exit()

        # Get the color of the left and right pixels
        left_pixel_color = pyautogui.pixel(x, y)
        right_pixel_color = pyautogui.pixel(x + right_offset, y)

        # Update the position based on the pixel colors
        if position == "left":
            if left_pixel_color == left_color:
                queue.append("left")
            else:
                queue.append("right")
                position = "right"
        else:
            if right_pixel_color == right_color:
                queue.append("right")
            else:
                queue.append("left")
                position = "left"

        # Click on the left or right side based on the queue
        if queue[0] == "left":
            pyautogui.click(x, y)
        else:
            pyautogui.click(x + right_offset, y)

        # Remove the first element from the queue
        queue.pop(0)


main()
