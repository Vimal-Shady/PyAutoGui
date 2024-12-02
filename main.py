import pyautogui
import time
from time import sleep

def delay():
    sleep(0.75)

def clk(x,y,duration=0.50):
    pyautogui.moveTo(x,y,duration)
    pyautogui.click()

def drag_scroll_1():
    pyautogui.moveTo(1036,650)
    pyautogui.dragTo(1042,351, duration=0.35)

def drag_scroll_2():
    pyautogui.moveTo(1030,650,duration=0.50)
    pyautogui.dragTo(1040,350, duration=1)

def password():
    clk(1015,318)
    print("pass: ",end="")
    for i in range(1,9):
        print(str(i),end="")
        pyautogui.keyDown(str(i))
        pyautogui.keyUp(str(i))
    print()
    pyautogui.click()

def confirm():
    #confirm
    clk(1138,797)
    clk(1113,666)
    #spec
    clk(861,741)
    clk(936,564)
    clk(1078,625)
    sleep(1.2)
    #invite shady
    clk(877,800)
    clk(1557,363)
    print("Room Created Successfully!")

def room_create():
    #BR button
    clk(1375,756)
    delay()
    #custom button
    clk(984,803)
    delay()
    #create button:
    clk(1511,798)
    #pass
    password()
    #mode selection
    clk(1254,561)

def config():
    clk(392,375)
    #store
    clk(891,327)
    #round
    clk(994,484)
    clk(990,564)
    #coin
    clk(1485,484)
    clk(1416,606)
    drag_scroll_1()
    #config
    #tier
    clk(880,539)
    #limited ammo
    clk(1367,445)
    #air
    clk(1367,490)
    #skill
    clk(1367,636)
    #gunattributes
    clk(1367,683)

def advanced():
    #advanced
    clk(393,529)
    clk(1555,278)
    sleep(1)
    gunselect()

def gunselect():
    guns = [
    [1142, 476], [579, 561], [1145, 650], 'drag',
    [1030, 650], [1145, 446], [585, 447], 'drag',
    [1030, 650], [1144, 481], [1144, 658], 'drag',
    [1030, 650], [579, 512], [1144, 682], 'drag',
    [1030, 650], [579, 454], [579, 545], [1144, 454], 'drag',
    [1030, 650], 'drag', [1030, 650],
    [1142, 517], [579, 605], [1145, 608], [1144, 690], 'drag',
    [1030, 650], [579, 461], 'drag',
    [1030, 650], [1144, 573], 'drag',
    [1030, 650], 'drag', [1030, 650], 'drag', [1030, 650],
    [1090, 460], [579, 631], 'drag',
    [1030, 650], [579, 652], [1090, 652], 'drag',
    [1030, 650], 'drag', [1030, 650],
    [580, 478], [580, 564], [580, 648], [1144, 564], [1144, 643]
]
    for i in guns:
        print(i)
        if i=='drag':
            drag_scroll_2()
        else:
            clk(i[0],i[1])
def main():
    pyautogui.FAILSAFE=True
    print("Initializing..")
    sleep(4)
    pyautogui.moveTo(1051, 849,duration=1)
    sleep(1)
    room_create()
    sleep(1)
    config()
    sleep(1)
    advanced()
    sleep(0.50)
    confirm()

if __name__ == "__main__":
    main()