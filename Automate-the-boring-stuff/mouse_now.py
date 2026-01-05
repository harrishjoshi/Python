#! python3

# mouse_now.py - Displays the mouse cursor's current position.

import pyautogui

print("Press Ctrl-C to quit.")

# Get and print the mouse coordinates.
try:
    while True:
        # Get and print the mouse coordinates.
        x, y = pyautogui.position()
        position = f"X: {str(x).rjust(4)} Y: {str(y).rjust(4)}"
        pixel_color = pyautogui.screenshot().getpixel((x, y))
        position += f" RGB: ({str(pixel_color[0]).rjust(3)}"
        position += f", {str(pixel_color[1]).rjust(3)}"
        position += f", {str(pixel_color[2]).rjust(3)})"
        print(position, end="")
        print("\b" * len(position), end="", flush=True)
except KeyboardInterrupt:
    print("Ctrl-C pressed.")
