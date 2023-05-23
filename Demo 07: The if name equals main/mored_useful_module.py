import time

def some_function():
    print("Doing useful stuff")
    for i in range(5):
        print(i)
        time.sleep(1)


if __name__ == "__main__":
    some_function()