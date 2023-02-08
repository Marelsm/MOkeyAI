import pyautogui

MokeyCords = [("Hero", (1700,))]
pyautogui.click(100, 100)


def GrupRot(up_do):
    for _ in range(13):
        pyautogui.scroll(500 * up_do)
    return
