import time
import pyautogui
import pygetwindow


def window_get(title):
    windows = pygetwindow.getWindowsWithTitle(title)
    if windows:
        window = windows[0]
        window.activate()
        time.sleep(1)
    else:
        print(f"没有找到'{title}'.")


def information_click(image, s):
    moveto(image, 0, 55)
    pyautogui.click()
    time.sleep(s)


def c_click(image, s):
    location = pyautogui.locateCenterOnScreen(image=image, confidence=0.97)
    if location:
        pyautogui.click(location.x, location.y)
    time.sleep(s)


def click(image, s):
    max_attempts = 60
    attempts = 0
    location = None
    while attempts < max_attempts:
        try:
            location = pyautogui.locateCenterOnScreen(image=image, confidence=0.95)
        except Exception as e:
            print(f"{attempts + 1}次尝试: {e}")
        if location:
            time.sleep(0.3)
            pyautogui.click(location.x, location.y)
            time.sleep(s)
            return
        else:
            attempts += 1
            time.sleep(s)


def g_click(image):
    max_attempts = 30
    attempts = 0
    while attempts < max_attempts:
        try:
            location = pyautogui.locateCenterOnScreen(image=image, confidence=0.95)
        except Exception as e:
            print(f"{attempts + 1}次尝试关闭签到: {e}")
            location = None
        if location:
            time.sleep(0.3)
            pyautogui.click(location.x, location.y)
            time.sleep(0.5)
            try:
                pyautogui.locateCenterOnScreen(image=image, confidence=0.95)
            except Exception as e:
                print(f"已关闭签到: {e}")
                return
        else:
            attempts += 1
            time.sleep(1)


def h_click(image, s):
    max_attempts = 60
    attempts = 0
    location = None
    while attempts < max_attempts:
        try:
            location = pyautogui.locateCenterOnScreen(image=image, confidence=0.97)
        except Exception as e:
            print(f"{attempts + 1}次尝试: {e}")
        if location:
            time.sleep(0.3)
            pyautogui.click(location.x, location.y)
            time.sleep(s)
            return
        else:
            attempts += 1
            time.sleep(s)


def moveto(image, dx, dy):
    max_attempts = 60
    attempts = 0
    location = None
    while attempts < max_attempts:
        try:
            location = pyautogui.locateCenterOnScreen(image=image, confidence=0.9)
        except Exception as e:
            print(f"{attempts + 1}次尝试: {e}")
        if location:
            pyautogui.moveTo(location.x + dx, location.y + dy)
            return
        else:
            attempts += 1
            time.sleep(0.5)


def scroll(dpi, s):
    pyautogui.scroll(dpi)
    time.sleep(s)


def back(s):
    pyautogui.press('esc')
    time.sleep(s)


def gs_click(image, s, gd, gs):
    max_attempts = 30
    attempts = 0
    location = None
    while attempts < max_attempts:
        try:
            location = pyautogui.locateCenterOnScreen(image=image, confidence=0.95)
        except Exception as e:
            print(f"{attempts + 1}次尝试: {e}")
            if (attempts + 1) % 6 == 0:
                back(s)
                click(gd, 1)
                click(gs, 1)
        if location:
            pyautogui.click(location.x, location.y)
            time.sleep(s)
            return
        else:
            attempts += 1
            time.sleep(s)


def m_click(image, s):
    max_attempts = 30
    attempts = 0
    location = None
    while attempts < max_attempts:
        try:
            location = pyautogui.locateCenterOnScreen(image=image, confidence=0.95)
        except Exception as e:
            print(f"{attempts + 1}次尝试: {e}")
        if location:
            time.sleep(0.5)
            pyautogui.click(location.x, location.y)
            time.sleep(s)
            return
        else:
            attempts += 1
            time.sleep(s)


def match_click(image1, image2, image3, s):
    max_attempts = 60
    attempts = 0
    location1 = None
    location2 = None
    while attempts < max_attempts:
        try:
            location1 = pyautogui.locateCenterOnScreen(image=image1, confidence=0.95)
        except Exception as e:
            print(f"{attempts + 1}次尝试点击比赛: {e}")
        try:
            location2 = pyautogui.locateCenterOnScreen(image=image2, confidence=0.95)
        except Exception as e:
            print(f"{attempts + 1}次尝试点击正在比赛: {e}")
        if location1:
            time.sleep(0.3)
            pyautogui.click(location1.x, location1.y)
            time.sleep(s)
            return
        if location2:
            time.sleep(0.3)
            pyautogui.click(location2.x, location2.y)
            time.sleep(s)
            return
        else:
            if (attempts + 1) % 6 == 0:
                try:
                    c_click(image3, 2)
                except Exception as e:
                    print(f"尝试打开比赛失败{e}")
            attempts += 1
            time.sleep(s)
