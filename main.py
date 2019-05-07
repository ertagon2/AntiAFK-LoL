import random
import time

import pyautogui
import keyboard


def my_role():
    print("1. I'm playing top")
    print("2. I'm playing jungle")
    print("3. I'm playing mid")
    print("4. I'm playing adc")
    print("5. I'm playing supp")
    choice = input("Choose: ")
    return int(choice)


def follow(role2):
    position = ["top", "jungle", "mid", "adc", "supp"]

    for i in range(1, 6):
        if i != role2:
            print(repr(i) + ". Follow " + position[i - 1])

    choice = int(input("Choose: "))

    if choice == role2 or choice > 5 or choice < 1:
        print("Wrong choice, try again !")
        choice = follow(role2)

    if choice < role2:
        choice += 1

    return choice


def click_center():
    randX = random.randrange(0, 5, 1)
    randY = random.randrange(0, 5, 1)

    pyautogui.moveTo(wCenter + randX, hCenter + randY, duration=0.2)
    pyautogui.rightClick()


def _run():
    keyboard.press(follow)
    click_center()


pyautogui.FAILSAFE = True
wCenter = pyautogui.size().width / 2
hCenter = pyautogui.size().height / 2
run = False

role = my_role()
follow = "f" + str(follow(role))

while True:  # making a loop
    if keyboard.is_pressed("home"):  # if key 'q' is pressed
        run = True
        print("Status: Active")
    if keyboard.is_pressed("end"):
        if run:
            run = False
            keyboard.release(follow)
            print("Status: Paused")
    if run:
        _run()
