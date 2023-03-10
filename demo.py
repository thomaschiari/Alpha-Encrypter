import time
# create a function that prints slow
def slow_print(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.1)
    print()

