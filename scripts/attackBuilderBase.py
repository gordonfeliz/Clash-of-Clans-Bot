from python_imagesearch.imagesearch import *
import pyautogui
import generalFunctions

def beginAttack():
    pyautogui.click(x=89, y=735) # clicks attack button
    time.sleep(2)
    pyautogui.click(x=903, y=391)  # clicks Find Now button
    time.sleep(15)
    pyautogui.scroll(-100)
    time.sleep(1)
    pyautogui.scroll(-100)
    time.sleep(1)

    pyautogui.click(x=328, y=755) #select giants

    for x in range(0, 10): #place giants
        pyautogui.click(x=694, y=658)
        time.sleep(0.2)

    pyautogui.click(x=206, y=754)  # select archers
    time.sleep(4)

    for x in range(0, 12): #place archers
        pyautogui.click(x=694, y=658)
        time.sleep(0.2)

    count = 0

    while count < 200: #waits until battle is done, then clicks okay button
        count = count + 1
        pos = imagesearch("images/BuilderBaseOkayButton.PNG")
        if pos[0] > -1:
            pyautogui.click(x=pos[0], y=pos[1])
            print("finished builder base attack")
            break
        time.sleep(1)

    if count is 200:
        pyautogui.moveTo(515, 9)
        time.sleep(2)
        pyautogui.leftClick()
        time.sleep(10)
        generalFunctions.closeAppOfTheDay()
        pyautogui.click(x=175, y=195)
        time.sleep(20)
    else:
        count = 0
        time.sleep(5)
        while count < 200:  # waits until it sees okay button for when other player is done attacking
            count = count + 1
            pos = imagesearch("images/BuilderBaseAttackOkay2.PNG")
            if pos[0] > -1:
                pyautogui.click(x=pos[0], y=pos[1])
                print("finished builder base attack")
                time.sleep(1)
                pyautogui.click(x=84, y=745)
                break
            time.sleep(1)
        if count is 200:
            pyautogui.moveTo(515, 9)
            time.sleep(2)
            pyautogui.leftClick()
            time.sleep(5)
            generalFunctions.closeAppOfTheDay()
            pyautogui.click(x=175, y=195)
            time.sleep(8)


    time.sleep(2)
    generalFunctions.checkForBlueStacks()
    pyautogui.moveTo(x=718, y=500) #moves mouse to zoom out
    pyautogui.keyDown('ctrlleft') #zooms back out
    time.sleep(1)
    pyautogui.scroll(-100)
    time.sleep(1)
    pyautogui.scroll(-100)
    time.sleep(1)
    pyautogui.keyUp('ctrlleft')
    time.sleep(1)



