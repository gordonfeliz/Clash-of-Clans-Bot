from python_imagesearch.imagesearch import *
import pyautogui
import threading

import manageBuilderBase
import attackBuilderBase
import manageMainBase
import attackMainBase
import generalFunctions


while True:
    time.sleep(5)
    generalFunctions.clickTeamViewerOk()  # closes teamviewer popup
    generalFunctions.checkForBlueStacks() #opens bluestacks if not already open
    generalFunctions.checkIfLoggedOut() #checks for logged out image, and logs in if sees
    generalFunctions.checkForNewBase()
    time.sleep(5)
    manageMainBase.upgradeWalls()
    generalFunctions.RemovePlants()
    manageMainBase.collectGold()
    manageMainBase.collectElixir()
    manageMainBase.collectDarkElixir()
    generalFunctions.checkIfLoggedOut() #checks for logged out image, and logs in if sees

    generalFunctions.align() #aligns camera for upgrading/research

    manageMainBase.Research() #researches dragons, balloons, and lightning
    generalFunctions.checkIfLoggedOut() #checks for logged out image, and logs in if sees
    manageMainBase.upgradeBuildings() #upgrades specific buildings

    if manageMainBase.trainTroops() is True: #checks if troops are done training
        attackMainBase.beginAttack()
        generalFunctions.checkIfLoggedOut()
        manageMainBase.trainTroops()

    generalFunctions.moveToBuilderBase()
    generalFunctions.checkIfLoggedOut()

    manageBuilderBase.collectGold()
    manageBuilderBase.collectElixir()
    manageBuilderBase.collectGems()
    #manageBuilderBase.activateClockTower()
    manageBuilderBase.upgradeBuildings()
    generalFunctions.checkIfLoggedOut()

    attackBuilderBase.beginAttack()
    generalFunctions.checkIfLoggedOut()

    generalFunctions.moveToMainBase()
