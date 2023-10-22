import pyautogui
import keyboard

def main():
    running = True

    # Create a function to stop the loop
    def stop_loop(e):
        nonlocal running
        if e.name == 'esc':
            running = False

    # Set up the key press event
    keyboard.on_press(stop_loop)

    while running:
        pyautogui.click()
        print("The loop is running...")

    # Clean up and stop listening to key events
    keyboard.unhook_all()

if __name__ == "__main__":k
    main()

