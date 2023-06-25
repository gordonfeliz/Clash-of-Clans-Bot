from python_imagesearch.imagesearch import *
import pyautogui
import manageBuilderBase
import attackBuilderBase
import manageMainBase
import attackMainBase


def moveToBuilderBase():
    pyautogui.click(x=1320, y=414)
    pyautogui.scroll(-100)
    time.sleep(2)
    pos = imagesearch("images/MainBaseBoat.PNG", 0.8)
    if pos[0] > -1:
        pyautogui.click(x=pos[0], y=pos[1])
    else:
        print("could not find main boat :(")
    time.sleep(3)


def moveToMainBase():
    pyautogui.moveTo(x=733, y=416)
    pyautogui.scroll(100)
    time.sleep(2)
    pos = imagesearch("images/BuilderBaseBoat.PNG", 0.8)
    if pos[0] > -1:
        pyautogui.click(x=pos[0], y=pos[1])
    else:
        print("could not find builder boat :(")
    time.sleep(3)


def requestTroops():
    pyautogui.click(x=741, y=493)  # click on clan castle
    time.sleep(1)
    pyautogui.click(x=615, y=682)  # click request
    time.sleep(1)
    pyautogui.click(x=837, y=670)  # click send
    time.sleep(1)
    pyautogui.click(x=1281, y=104)  # close treasury/gem popup
    time.sleep(1)


def RemovePlants():
    pictures = ["images/GemBox.PNG", "images/Bush.PNG", "images/flowers.PNG", "images/pine.PNG", "images/sidewaysTrunk.PNG", "images/Tree.PNG", "images/Tree2.PNG", "images/Tree3.PNG", "images/Tree4.PNG", "images/trunk.PNG", "images/Trunk2.PNG", "images/Trunk3.PNG"]

    for x in range(0, len(pictures)):
        pos = imagesearch(pictures[x], 0.9)
        if pos[0] > -1:
            pyautogui.click(x=pos[0], y=pos[1])  # clicks on plants
            time.sleep(1)
            pyautogui.click(x=685, y=693)  # clicks on remove
            time.sleep(1)
            pyautogui.click(x=1324, y=105)  # closes gem popup
            time.sleep(1)


def checkIfLoggedOut():
    pos = imagesearch("images/LogInButton.PNG", 0.9)
    if pos[0] > -1:
        time.sleep(2) #180
        pyautogui.click(x=429, y=775) # clicks log in to supercell button
        time.sleep(30)
        #pyautogui.click(x=429, y=775)  # clicks log in to supercell button
        #time.sleep(2)

        pos = imagesearch("images/LogIn.PNG", 0.9)
        if pos[0] > -1:
            pyautogui.click(x=pos[0], y=pos[1])  # logs in to account
            time.sleep(30)
            pos = imagesearch("images/VillageAttackedOkay.PNG", 0.9)
            if pos[0] > -1:
                pyautogui.click(x=pos[0], y=pos[1])  # clicks okay if village was attacked

            return 1

        checkForAlreadyLoggedIn()
        pyautogui.click(x=1175, y=484) # clicks continue
        time.sleep(2)
        pyautogui.click(x=770, y=416) # clicks email box
        time.sleep(2)
        pyautogui.typewrite("jiff24680@gmail.com")
        time.sleep(2)
        pyautogui.click(x=1178, y=588)  # clicks log in
        time.sleep(2)
        pyautogui.click(x=509, y=870)  # open chrome with gmail on it
        time.sleep(60)
        pos = imagesearch("images/GmailBackArrow.PNG", 0.9)
        if pos[0] > -1:
            pyautogui.click(x=277, y=153)  # clicc bacc button
            time.sleep(2)
        pyautogui.click(x=349, y=155)  # refreshes email
        time.sleep(2)
        pyautogui.click(x=364, y=202)  # open email with code
        time.sleep(2)
        pyautogui.click(x=541, y=213)  # copies first half of code
        time.sleep(0.1)
        pyautogui.click(x=541, y=213)
        time.sleep(1)
        pyautogui.hotkey("ctrlleft", "c")
        time.sleep(1)
        pyautogui.click(x=711, y=882) #opens bluestacks
        time.sleep(1)
        checkForBlueStacks()
        checkForBlueStacks()
        pyautogui.click(x=758, y=484) #clicks on code box
        time.sleep(1)
        pyautogui.hotkey("ctrlleft", "v")
        time.sleep(1)
        pyautogui.click(x=509, y=870)  # open chrome with gmail on it
        time.sleep(1)
        pyautogui.click(x=565, y=216)  # copies second half of code
        time.sleep(0.1)
        pyautogui.click(x=565, y=216)  # copies second half of code
        time.sleep(1)
        pyautogui.hotkey("ctrlleft", "c")
        time.sleep(1)
        pyautogui.click(x=277, y=153) #clicc bacc button
        time.sleep(1)
        pyautogui.click(x=711, y=882) #opens bluestacks
        time.sleep(1)
        pyautogui.hotkey("ctrlleft", "v")
        time.sleep(1)
        pyautogui.click(x=1161, y=577) #clicks submit
        time.sleep(1)
        pyautogui.click(x=1161, y=499) #clicks confirm
        time.sleep(30)

        pos = imagesearch("images/VillageAttackedOkay.PNG", 0.9)
        if pos[0] > -1:
            pyautogui.click(x=pos[0], y=pos[1])  # clicks okay if village was attacked


def closeAppOfTheDay():
    pos = imagesearch("images/AppOfTheDayX.PNG", 0.9)
    if pos[0] > -1:
        pyautogui.click(x=pos[0], y=pos[1])  # clicks X
        time.sleep(2)


def clickTeamViewerOk():
    pos = imagesearch("images/TeamviewerOk.PNG", 0.9)
    if pos[0] > -1:
        pyautogui.click(x=pos[0], y=pos[1])  # clicks ok


def align():
    checkForBlueStacks()
    attackMainBase.zoomOut()
    moveToBuilderBase()
    attackMainBase.zoomOut()
    moveToMainBase()
    time.sleep(1)


def checkForBlueStacks():
    pos = imagesearch("images/BlueStacksLogo.PNG", 0.9)
    if pos[0] is -1:
        pyautogui.click(x=705, y=878)  # clicks bluestacks
        time.sleep(1)


def checkForAlreadyLoggedIn():
    pos = imagesearch("images/AlreadyLoggedIn.PNG", 0.9)
    if pos[0] > -1:
        pyautogui.click(x=836, y=587)  # clicks cancel
        time.sleep(1)


def checkForNewBase():
    pos = imagesearch("images/NewBaseText.PNG", 0.9)
    if pos[0] > -1:
        pyautogui.click(x=58, y=101)  # opens settings
        time.sleep(1)
        pyautogui.click(x=841, y=517)  # opens settings
        time.sleep(1)
        checkForAlreadyLoggedIn()
        pyautogui.click(x=1175, y=484) # clicks continue
        time.sleep(2)
        pyautogui.click(x=770, y=416) # clicks email box
        time.sleep(2)
        pyautogui.typewrite("jiff24680@gmail.com")
        time.sleep(2)
        pyautogui.click(x=1178, y=588)  # clicks log in
        time.sleep(2)
        pyautogui.click(x=509, y=870)  # open chrome with gmail on it
        time.sleep(60) #60
        pyautogui.click(x=349, y=155)  # refreshes email
        time.sleep(2)
        pyautogui.click(x=564, y=254)  # open email with code
        time.sleep(2)
        pyautogui.click(x=541, y=213)  # copies first half of code
        time.sleep(0.1)
        pyautogui.click(x=541, y=213)
        time.sleep(1)
        pyautogui.hotkey("ctrlleft", "c")
        time.sleep(1)
        pyautogui.click(x=705, y=878)  #opens bluestacks
        time.sleep(1)
        checkForBlueStacks()
        checkForBlueStacks()
        pyautogui.click(x=758, y=484) #clicks on code box
        time.sleep(1)
        pyautogui.hotkey("ctrlleft", "v")
        time.sleep(1)
        pyautogui.click(x=509, y=870)  # open chrome with gmail on it
        time.sleep(1)
        pyautogui.click(x=565, y=216)  # copies second half of code
        time.sleep(0.1)
        pyautogui.click(x=565, y=216)  # copies second half of code
        time.sleep(1)
        pyautogui.hotkey("ctrlleft", "c")
        time.sleep(1)
        pyautogui.click(x=277, y=153) #clicc bacc button
        time.sleep(1)
        pyautogui.click(x=705, y=878) #opens bluestacks
        time.sleep(1)
        pyautogui.hotkey("ctrlleft", "v")
        time.sleep(1)
        pyautogui.click(x=1161, y=577) #clicks submit
        time.sleep(1)
        pyautogui.click(x=1161, y=499) #clicks confirm
        time.sleep(30)

        pos = imagesearch("images/VillageAttackedOkay.PNG", 0.9)
        if pos[0] > -1:
            pyautogui.click(x=pos[0], y=pos[1])  # clicks okay if village was attacked
