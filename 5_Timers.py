import threading
import time

def timer_callback():
    print("Timer callback function is called!")
    with open("timer.txt", "a") as file:
        file.write("Timer callback function is called!\n")
    start_timer()

def start_timer():
    # Create a Timer that repeats every 2 seconds
    global timer
    timer = threading.Timer(2, timer_callback)
    # Start the timer
    timer.start()

if __name__ == "__main__":
    # Start the initial timer
    start_timer()

    try:
        while True:
            # Do something here
            time.sleep(1)
            # Main program logic goes here...
    except KeyboardInterrupt:
        # Stop the timer if the program is interrupted by a keyboard interrupt (Ctrl+C)
        timer.cancel()
        print("Timer canceled.")

    # Wait for the last timer to finish (though it's a repeating timer, so it won't actually finish until canceled)
    timer.join()
