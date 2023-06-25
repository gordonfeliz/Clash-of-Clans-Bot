from python_imagesearch.imagesearch import *
import pyautogui
import generalFunctions


def Research():

    pyautogui.click(x=1146, y=442) #clicks on research lab
    time.sleep(1)
    pos = imagesearch("images/ResearchButton.PNG")
    if pos[0] > -1:
        time.sleep(1)
        pyautogui.click(x=pos[0], y=pos[1]) #clicks research button
        time.sleep(1)
        pyautogui.click(x=929, y=525) #clicks on dragons
        time.sleep(1)
        pyautogui.click(x=1050, y=738) #clicks on upgrade
        time.sleep(1)
        print("attempted main base research")

    time.sleep(1)
    pyautogui.click(x=1321, y=451)  # closes menu
    time.sleep(1)
    pyautogui.click(x=1321, y=451)  # closes menu
    time.sleep(3)


    pyautogui.click(x=1146, y=442) #clicks on research lab
    time.sleep(1)
    pos = imagesearch("images/ResearchButton.PNG")
    if pos[0] > -1:
        time.sleep(1)
        pyautogui.click(x=pos[0], y=pos[1]) #clicks research button
        time.sleep(1)
        pyautogui.click(x=610, y=683) #clicks on balloons
        time.sleep(1)
        pyautogui.click(x=1050, y=738) #clicks on upgrade
        time.sleep(1)
        print("attempted main base research")

    time.sleep(1)
    pyautogui.click(x=1321, y=451)  # closes menu
    time.sleep(1)
    pyautogui.click(x=1321, y=451)  # closes menu
    time.sleep(3)


    pyautogui.click(x=1146, y=442) #clicks on research lab
    time.sleep(1)
    pos = imagesearch("images/ResearchButton.PNG")
    if pos[0] > -1:
        time.sleep(1)
        pyautogui.click(x=pos[0], y=pos[1]) #clicks research button
        time.sleep(1)
        pyautogui.moveTo(1023, 605)
        pyautogui.dragTo(368, 602, 2, button='left')
        time.sleep(2)
        pyautogui.click(x=665, y=523) #clicks on lightning
        time.sleep(1)
        pyautogui.click(x=1050, y=738) #clicks on upgrade
        time.sleep(1)
        print("attempted main base research")

    time.sleep(1)
    pyautogui.click(x=1321, y=451)  # closes menu
    time.sleep(1)
    pyautogui.click(x=1321, y=451)  # closes menu
    time.sleep(3)


def upgradeTownHall():
    pyautogui.click(x=686, y=407)  # clicks on town hall
    time.sleep(1)
    pos = imagesearch("images/upgradeHammer.PNG", 0.98)
    if pos[0] > -1:
        print("upgrade attempted")
        pyautogui.click(x=pos[0], y=pos[1])  # click hammer
        time.sleep(1)
        pyautogui.click(x=698, y=738)  # clicks upgrade
        time.sleep(1)
        pyautogui.click(x=1322, y=410)  # closes popup
        time.sleep(1)
        pyautogui.click(x=1322, y=410)  # closes popup
        time.sleep(1)


def upgradeLab():
    pyautogui.click(x=1297, y=406)  # closes any menus
    time.sleep(1)
    pyautogui.click(x=1071, y=389) #clicks on research lab
    time.sleep(1)
    attemptUpgrade()


def upgradeBarbKing():
    pyautogui.click(x=1297, y=406)  # closes any menus
    time.sleep(1)
    pyautogui.click(x=865, y=218)  # clicks on tard king
    time.sleep(1)
    pos = imagesearch("images/upgradeHammer.PNG", 0.98)
    pos2 = imagesearch("images/smallUpgradeHammer.PNG", 0.98)
    pos3 = imagesearch("images/smallUpgradeHammer2.PNG", 0.98)
    if pos[0] > -1 or pos2[0] > -1 or pos3[0] > -1:
        print("upgrade attempted")
        if pos[0] > -1:
            pyautogui.click(x=pos[0], y=pos[1])  # click hammer
        elif pos2[0] > -1:
            pyautogui.click(x=pos2[0], y=pos2[1])  # click small hammer 1
        else:
            pyautogui.click(x=pos3[0], y=pos3[1])  # click small hammer 2


        time.sleep(1)
        pyautogui.click(x=1042, y=748)  # clicks upgrade
        time.sleep(1)
        pyautogui.click(x=1321, y=101)  # closes menu
        time.sleep(1)
        pyautogui.click(x=1321, y=101)  # closes menu
        time.sleep(1)
        pyautogui.click(x=1322, y=410)  # closes popup
        time.sleep(0.5)
        pyautogui.click(x=1322, y=410)  # closes popup
        time.sleep(1)


def upgradeArcherQueen():
    pyautogui.click(x=1297, y=406)  # closes any menus
    time.sleep(1)
    pyautogui.click(x=903, y=246)  # clicks on archer bitch
    time.sleep(1)
    pos = imagesearch("images/upgradeHammer.PNG", 0.98)
    pos2 = imagesearch("images/smallUpgradeHammer.PNG", 0.98)
    pos3 = imagesearch("images/smallUpgradeHammer2.PNG", 0.98)
    if pos[0] > -1 or pos2[0] > -1 or pos3[0] > -1:
        print("upgrade attempted")
        if pos[0] > -1:
            pyautogui.click(x=pos[0], y=pos[1])  # click hammer
        elif pos2[0] > -1:
            pyautogui.click(x=pos2[0], y=pos2[1])  # click small hammer 1
        else:
            pyautogui.click(x=pos3[0], y=pos3[1])  # click small hammer 2


        time.sleep(1)
        pyautogui.click(x=1042, y=748)  # clicks upgrade
        time.sleep(1)
        pyautogui.click(x=1321, y=101)  # closes menu
        time.sleep(1)
        pyautogui.click(x=1321, y=101)  # closes menu
        time.sleep(1)
        pyautogui.click(x=1322, y=410)  # closes popup
        time.sleep(0.5)
        pyautogui.click(x=1322, y=410)  # closes popup
        time.sleep(1)


def collectGold():
    pos = imagesearch("images/MainBaseGold.PNG")
    if pos[0] > -1:
        pyautogui.click(x=pos[0], y=pos[1])
        print("collected main base gold")
    time.sleep(1)


def collectElixir():
    pos = imagesearch("images/MainBaseElixir.PNG")
    if pos[0] > -1:
        pyautogui.click(x=pos[0], y=pos[1])
        print("collected main base elixir")
    time.sleep(1)


def collectDarkElixir():
    pos = imagesearch("images/MainBaseDarkElixir.PNG")
    if pos[0] > -1:
        pyautogui.click(x=pos[0], y=pos[1])
        print("collected main base dark elixir")
    time.sleep(1)


def upgradeRecommendedBuildings():
    pyautogui.click(x=497, y=96) #open list of upgrades
    time.sleep(1)

    for x in range(0, 7):
        pyautogui.click(x=499, y=239 + (x * 42))
        time.sleep(2)
        if attemptUpgrade():
            pyautogui.click(x=497, y=96)  # open list of upgrades


def upgradeWalls():

    for x in range(0, 3):

        pyautogui.click(x=497, y=96) #open list of upgrades
        time.sleep(1)

        generalFunctions.checkForBlueStacks()
        for m in range(0, 11):
            pyautogui.moveTo(528, 379) # positions over list of upgrades to scroll down
            pyautogui.scroll(-100)
            time.sleep(1)

        pyautogui.click(x=414, y=478)  # clicks on wall in upgrade list
        time.sleep(1)

        pyautogui.click(x=664, y=687)  # selects row of walls
        time.sleep(1)

        pos = imagesearch("images/smallDoubleHammer.PNG", 0.98)
        if pos[0] > -1:
            pyautogui.click(x=pos[0], y=pos[1])  # selects upgrade
            time.sleep(1)
            pyautogui.click(x=838, y=563)  # tries to upgrade
            time.sleep(1)

        pyautogui.click(x=1322, y=410)  # closes popup
        time.sleep(1)
        pyautogui.click(x=1322, y=410)  # closes popup
        time.sleep(1)


def upgradeBuildings():
    upgradeRightSide(2)
    upgradeCampFires()
    moveLayout(2)
    generalFunctions.align()
    upgradeArcherQueen()
    upgradeBarbKing()
    upgradeBottom(4)
    upgradeRightSide(7)
    moveLayout(1)
    upgradeTownHall()
    #upgradeRecommendedBuildings()


def upgradeBottom(count):

    print("upgrade bottom side attempted")
    for x in range(0, count):
        pyautogui.click(x=1053 + (x * 37), y=568 + (x * -29))
        time.sleep(1)
        attemptUpgrade()
        pyautogui.click(x=1322, y=410)  # closes popup
        time.sleep(1)
        pyautogui.click(x=1322, y=410)  # closes popup
        time.sleep(1)


def upgradeRightSide(count):

    print("upgrade right side attempted")
    for x in range(0, count):
        pyautogui.click(x=1146 + (x * -38), y=442 + (x * -26))
        time.sleep(1)
        attemptUpgrade()
        pyautogui.click(x=1322, y=410)  # closes popup
        time.sleep(1)
        pyautogui.click(x=1322, y=410)  # closes popup
        time.sleep(1)


def upgradeCampFires():
    campFiresX = [853, 905, 954, 1002]
    campFiresY = [705, 671, 630, 597]

    print("upgrade campfires attempted")
    for x in range(0, len(campFiresX)):
        pyautogui.click(x=campFiresX[x], y=campFiresY[x])
        time.sleep(1)
        attemptUpgrade()
        pyautogui.click(x=1322, y=410)  # closes popup
        time.sleep(1)
        pyautogui.click(x=1322, y=410)  # closes popup
        time.sleep(1)


def moveLayout(layout): #input 1 and it moves to main layout, anything else moves to second layout
    time.sleep(1)
    pyautogui.click(x=1322, y=533) #opens layout menu
    time.sleep(1)
    if layout is 1:
        pyautogui.click(x=257, y=493)  # clicks main layout
    else:
        pyautogui.click(x=1114, y=493) #clicks second layout
    time.sleep(1)
    pyautogui.click(x=939, y=779) #sets as active
    time.sleep(1)
    pyautogui.click(x=1325, y=113) #closes layout menu
    time.sleep(1)


def attemptUpgrade():
    upgraded = False
    pos = imagesearch("images/upgradeHammer.PNG", 0.98)
    pos2 = imagesearch("images/smallUpgradeHammer.PNG", 0.98)
    pos3 = imagesearch("images/smallUpgradeHammer2.PNG", 0.98)
    pos4 = imagesearch("images/smallDoubleHammer.PNG", 0.98)

    posClose = imagesearch("closeShop.PNG", 0.9)

    if posClose[0] > -1:
        pyautogui.click(x=1323, y=115)  # closes shop
        time.sleep(3)
        pyautogui.click(x=615, y=105)  # opens list of upgrades
        time.sleep(1)

    if pos[0] > -1 or pos2[0] > -1 or pos3[0] > -1 or pos4[0] > -1:
        upgraded = True
        if pos[0] > -1:
            pyautogui.click(x=pos[0], y=pos[1])  # click hammer
        elif pos2[0] > -1:
            pyautogui.click(x=pos2[0], y=pos2[1])  # click small hammer 1
        elif pos4[0] > -1:
            pyautogui.click(x=pos4[0], y=pos4[1])  # click small double hammer
        else:
            pyautogui.click(x=pos3[0], y=pos3[1])  # click small hammer 2
        time.sleep(1)
        pyautogui.click(x=687, y=733)  # tries to upgrade
        time.sleep(1)
        pyautogui.click(x=1322, y=410)  # closes popup
        time.sleep(1)
        pyautogui.click(x=1322, y=410)  # closes popup
        time.sleep(1)
        pyautogui.click(x=1322, y=410)  # closes popup
        time.sleep(1)
        pyautogui.click(x=1322, y=410)  # closes popup
        time.sleep(1)

    return upgraded


def trainTroops():
    trainingDone = False
    pyautogui.click(x=56, y=620)  # open training menu
    time.sleep(2)
    pos = imagesearch("images/EditArmyButton.PNG", 0.9)  # confirms bot is in training menu

    if pos[0] is not -1:

        time.sleep(1)
        pyautogui.click(x=1221, y=754)  # requests troops
        time.sleep(1)
        pyautogui.click(x=837, y=670)  # click send
        time.sleep(1)
        pyautogui.click(x=878, y=99)  # open quick train
        time.sleep(1)
        pyautogui.click(x=1228, y=416)  # train troops button
        time.sleep(1)
        pyautogui.click(x=173, y=101)  # view army tab
        time.sleep(1)
        pyautogui.click(x=173, y=101)  # view army tab
        time.sleep(14)
        pos = imagesearch("images/MainBaseTroopReady.PNG", 0.8)  # tries to find out if troop training is done
        pos2 = imagesearch("images/TroopsDone.PNG", 0.8)  # tries to find out if troop training is done
        pos3 = imagesearch("images/SpellsDone.PNG", 0.8)  # tries to find out if troop training is done
        time.sleep(2)

        if pos[0] is -1 and pos2[0] > -1 and pos3[0] > -1:
            print("TROOPS READY YAES")
            trainingDone = True
        pyautogui.click(x=1291, y=95)  # close button
        time.sleep(1)

    return trainingDone
