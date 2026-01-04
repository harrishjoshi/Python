import threading
import time

print("Start of the program.")


def take_a_nap():
    time.sleep(5)
    print("Wake Up!")


thread_obj = threading.Thread(target=take_a_nap)
thread_obj.start()

print("End of the program.")
