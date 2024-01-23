import threading
import time

# Function to run in a thread
def print_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Thread 1: {i}")
        with open("threading.txt", "a") as file:
            file.write(f"Thread 1: {i}\n")

def print_letters():
    for letter in 'ABCDE':
        time.sleep(1)
        print(f"Thread 2: {letter}")
        with open("threading.txt", "a") as file:
            file.write(f"Thread 2: {letter}\n")

if __name__ == "__main__":
    # Create two threads
    thread1 = threading.Thread(target=print_numbers)
    thread2 = threading.Thread(target=print_letters)

    # Start the threads
    thread1.start()
    thread2.start()

    # Wait for both threads to finish
    thread1.join()
    thread2.join()
    print("Both threads have finished.")
