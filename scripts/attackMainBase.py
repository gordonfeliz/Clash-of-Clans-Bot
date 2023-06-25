from python_imagesearch.imagesearch import *
import pyautogui
import generalFunctions


def beginAttack():
    pyautogui.click(x=82, y=734)  # opens attack menu
    time.sleep(2)
    pyautogui.click(x=1084, y=549)  # finds match
    time.sleep(15)

    searchForBase()

    attackAirDefense()
    positionForAttack()
    attackAirDefense()
    placeDragons()
    placeBarbKing()
    placeArcherQueen()
    placeClanCastle()
    attackAirDefense()
    useRemainingLightning()
    waitForReturnHome()
    zoomOut()


def searchForBase():
    count = 0
    while count < 200:
        count = count + 1
        #pos = imagesearch("TownHall9.PNG")
        pos2 = imagesearch("images/AirDefenseLevel7.PNG")
        pos3 = imagesearch("images/TownHall10.PNG")
        pos4 = imagesearch("images/AirDefenseLevel8.PNG")
        pos5 = imagesearch("images/TownHall11.PNG")
        if pos2[0] > -1 or pos3[0] > -1 or pos4[0] > -1 or pos5[0] > -1:
            pyautogui.click(x=1257, y=610)  # finds new match
        else:
            break
        time.sleep(15)


def placeBarbKing():
    pos = imagesearch("images/BarbKing.PNG")
    if pos[0] > -1:
        pyautogui.click(x=pos[0], y=pos[1]) #selects barb king
        time.sleep(1)
        pyautogui.click(x=936, y=323) #places tard king
        time.sleep(0.5)


def placeArcherQueen():
    pos = imagesearch("images/ArcherQueen.PNG")
    if pos[0] > -1:
        pyautogui.click(x=pos[0], y=pos[1]) #selects archer queen
        time.sleep(1)
        pyautogui.click(x=936, y=323) #places tard queen
        time.sleep(0.5)


def placeClanCastleSpell():
    pos = imagesearch("images/ClanCastleSpell.PNG")
    if pos[0] > -1:
        pyautogui.click(x=pos[0], y=pos[1]) #selects clan castle spell
        time.sleep(1)
        pyautogui.click(x=683, y=467)  # yeets spell onto air defense
        time.sleep(0.5)


def placeClanCastle():
    pos = imagesearch("images/ClanCastle.PNG")
    if pos[0] > -1:
        pyautogui.click(x=pos[0], y=pos[1]) #selects clan castle troops
        time.sleep(1)
        pyautogui.click(x=936, y=323) #places troops
        time.sleep(0.5)


def placeDragons():
    pos = imagesearch("images/Dragons.PNG")
    if pos[0] > -1:
        pyautogui.click(x=pos[0], y=pos[1])  # selects clan castle troops
    time.sleep(1)
    pyautogui.click(x=738, y=146) #places 1st dragon at top
    time.sleep(0.1)
    pyautogui.click(x=738, y=146) #places 2nd dragon at top
    time.sleep(0.6)
    pyautogui.click(x=1310, y=574) #places 3rd dragon at bottom
    time.sleep(0.1)
    pyautogui.click(x=1310, y=574) #places 4th dragon at bottom
    time.sleep(15)

    xPos = [817, 876, 910, 953, 1000, 1049, 953]
    yPos = [257, 281, 307, 332, 374, 392, 332]

    for x in range(0, 7):
        pyautogui.click(x=xPos[x], y=yPos[x])  # places 6 remaining dragons in middle
        time.sleep(0.1)


def positionForAttack():
    pyautogui.moveTo(639, 407) #positions mouse to scroll up
    time.sleep(1)
    pyautogui.scroll(100) #scrolls to top
    time.sleep(1)


def useRemainingLightning():
    pos = imagesearch("images/NewLightning.PNG")
    if pos[0] > -1:
        pyautogui.click(x=pos[0], y=pos[1]) #selects lightning

    for x in range(0, 10):
        pyautogui.click(x=683, y=467)  # yeets lightning onto air defense
        time.sleep(0.5)


def attackAirDefense():

    pos = imagesearch("images/NewLightning.PNG")
    if pos[0] > -1:
        pyautogui.click(x=pos[0], y=pos[1]) #selects lightning

        pos = imagesearch("images/AirDefenseLevel7.PNG")
        if pos[0] > -1:
            for x in range(0,5):
                pyautogui.click(x=pos[0], y=pos[1]) #yeets lightning onto air defense
                time.sleep(0.2)

        pos = imagesearch("images/AirDefenseLevel6.PNG")
        if pos[0] > -1:
            for x in range(0,4):
                pyautogui.click(x=pos[0], y=pos[1]) #yeets lightning onto air defense
                time.sleep(0.2)

        pos = imagesearch("images/AirDefenseLevel5.PNG")
        if pos[0] > -1:
            for x in range(0,4):
                pyautogui.click(x=pos[0], y=pos[1]) #yeets lightning onto air defense
                time.sleep(0.2)

        pos = imagesearch("images/AirDefenseLevel4.PNG")
        if pos[0] > -1:
            for x in range(0,4):
                pyautogui.click(x=pos[0], y=pos[1]) #yeets lightning onto air defense
                time.sleep(0.2)

        pos = imagesearch("images/AirDefenseLevel3.PNG")
        if pos[0] > -1:
            for x in range(0,4):
                pyautogui.click(x=pos[0], y=pos[1]) #yeets lightning onto air defense
                time.sleep(0.2)


def zoomOut():
    generalFunctions.checkForBlueStacks()
    pyautogui.moveTo(x=718, y=500) #moves mouse to zoom out
    pyautogui.keyDown('ctrlleft') #zooms back out
    time.sleep(1)
    pyautogui.scroll(-100)
    time.sleep(1)
    pyautogui.scroll(-100)
    time.sleep(1)
    pyautogui.scroll(-100)
    time.sleep(1)
    pyautogui.keyUp('ctrlleft')
    time.sleep(1)


def waitForReturnHome():
    count = 0
    while count < 200:
        count = count + 1
        time.sleep(1)
        pos = imagesearch("images/ReturnHome.PNG")
        if pos[0] > -1:
            time.sleep(1)
            pyautogui.click(x=pos[0], y=pos[1])  # selects return home
            time.sleep(5)
            break

    if count is 200:
        pyautogui.moveTo(515, 9)
        time.sleep(2)
        pyautogui.leftClick()
        time.sleep(5)
        pyautogui.click(x=175, y=195)
