from python_imagesearch.imagesearch import *
import pyautogui


def collectGold():
    pos = imagesearch("images/BuilderBaseGold.PNG")
    if pos[0] > -1:
        pyautogui.click(x=pos[0], y=pos[1])
        print("collected builder base gold")
    time.sleep(1)


def collectElixir():
    pos = imagesearch("images/BuilderBaseElixir.PNG")
    if pos[0] > -1:
        pyautogui.click(x=pos[0], y=pos[1])
        print("collected builder base elixir")
    time.sleep(1)


def collectGems():
    pos = imagesearch("images/BuilderBaseGems.PNG")
    if pos[0] > -1:
        pyautogui.click(x=pos[0], y=pos[1])
        print("collected builder base gems")
    time.sleep(1)


def activateClockTower():
    pyautogui.click(x=555, y=398) #clicks cock tower
    time.sleep(1)
    pyautogui.click(x=760, y=707)  # clicks boost
    time.sleep(1)
    pyautogui.click(x=677, y=594)  # clicks boost again
    time.sleep(1)
    pyautogui.click(x=1328, y=101)  # closes menus
    time.sleep(1)
    pyautogui.click(x=1328, y=101)  # closes menus
    time.sleep(1)


def upgradeBuildings():
    pos = imagesearch("images/builder.PNG", 0.98)
    if pos[0] > -1:
        pyautogui.click(x=645, y=105) #opens list of upgrades
    time.sleep(1)

    for x in range(0, 7):
        pyautogui.click(x=613, y=237 + (x * 40))
        time.sleep(2)
        pos = imagesearch("images/upgradeHammer.PNG", 0.98)
        pos2 = imagesearch("images/smallUpgradeHammer.PNG", 0.98)
        pos3 = imagesearch("images/smallUpgradeHammer2.PNG", 0.98)
        pos4 = imagesearch("images/smallDoubleHammer.PNG", 0.98)
        posClose = imagesearch("images/closeShop.PNG", 0.9)

        if posClose[0] > -1:
            pyautogui.click(x=1323, y=115)  # closes shop
            time.sleep(3)
            pyautogui.click(x=645, y=105)  # opens list of upgrades
            time.sleep(1)

        if pos[0] > -1 or pos2[0] > -1 or pos3[0] > -1 or pos4[0] > -1:

            if pos[0] > -1 or pos2[0] > -1 or pos3[0] > -1 or pos4[0] > -1:
                if pos[0] > -1:
                    pyautogui.click(x=pos[0], y=pos[1])  # click hammer
                elif pos2[0] > -1:
                    pyautogui.click(x=pos2[0], y=pos2[1])  # click small hammer 1
                elif pos4[0] > -1:
                    pyautogui.click(x=pos4[0], y=pos4[1])  # click small double hammer
                else:
                    pyautogui.click(x=pos3[0], y=pos3[1])  # click small hammer 2

            time.sleep(1)
            pyautogui.click(x=682, y=740)
            time.sleep(1)
            pyautogui.click(x=1320, y=101)
            time.sleep(0.5)
            pyautogui.click(x=1320, y=101)
            time.sleep(1)
            pyautogui.click(x=615, y=105)  # opens list of upgrades
            time.sleep(1)
