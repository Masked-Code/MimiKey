import time
import json
import random
import keyboard

FILENAME = "keystrokes.json"

def record_keystrokes():
    print("Recording... Press ESC to stop.")
    keystrokes = []
    last_time = time.time()

    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == "esc":
                break
            current_time = time.time()
            delay = current_time - last_time
            keystrokes.append((event.name, delay))
            last_time = current_time

    with open(FILENAME, "w") as f:
        json.dump(keystrokes, f)
    print("Keystrokes saved to", FILENAME)

def play_keystrokes():
    try:
        with open(FILENAME, "r") as f:
            keystrokes = json.load(f)
    except FileNotFoundError:
        print("No keystroke file found. Record first.")
        return
    
    print("Press Right Shift to start playback. Press ESC to exit.")
    while True:
        if keyboard.is_pressed("right shift"):
            print("Playing back...")
            for key, delay in keystrokes:
                if keyboard.is_pressed("esc"):
                    print("Playback stopped.")
                    return
                adjusted_delay = delay + random.uniform(-0.06, 0.06)
                time.sleep(max(0, adjusted_delay))
                keyboard.press_and_release(key)
            print("Playback finished. Press Right Shift again to replay.")
        time.sleep(0.1)

if __name__ == "__main__":
    mode = input("Enter 'r' to record or 'p' to playback: ")
    if mode.lower() == 'r':
        record_keystrokes()
    elif mode.lower() == 'p':
        play_keystrokes()
    else:
        print("Invalid option.")