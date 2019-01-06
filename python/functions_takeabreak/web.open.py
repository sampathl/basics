import webbrowser
import time

def beak_time():
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/")


def main():
    print(time.ctime())
    num = input("enter number of breaks you need:")
    num = int(num)

    for i in range(num):
        beak_time()
main()
