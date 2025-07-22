# Library Provides Clean Output for VS Code Terminal
# from https://stackoverflow.com/questions/2084508/clear-the-terminal-in-python
import os
import time
import sys

# google ai overview
def visibleLength(text):
    import re
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    return len(ansi_escape.sub('', text))


def clear():
    try:
        os.system('cls')
    except:
        print("error @ cleanLib.py @ clear()")
        sys.exit

def wait(seconds: int):
    try:
        time.sleep(seconds)
    except KeyboardInterrupt:
        sys.exit(0)

def waitIndef():
    """
    Waits indefinitely until the user presses Ctrl+C
    """
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        sys.exit(0)


def waitUntilEnter():
    """
    Waits until the user presses Enter. Does not print anything.
    """
    try:
        input()
    except KeyboardInterrupt:
        sys.exit(0)

def install(program):
    print(f"installing {program}")
    os.system(f'pip install {program}')

def clearV2(): # https://stackoverflow.com/questions/22885780/python-clear-the-screen/70387199#70387199
    print("\033c\033[3J", end = "") # use only when need to clear screen fully, menus will flicker if erased and overwritten



def printnl(text: str):
    print(text, end="", flush=True)

    

# basic askMenu
def askMenuDeprecated(menuList: list, recurse: bool = False): # takes in a list and outputs a menu and asks user for requested action; returns the menuList item
    mainLine = "" # store output
    
    mainLine += "|" # first slash

    for index, item in enumerate(menuList): # 
        mainLine += f" [{index+1}] {item} |"  # add values to string (index+1 because index starts at 0)
    
    mainLineLength = len(mainLine) # get string length to print
    if not recurse:
        for index in range(mainLineLength): # print top box cover
            print("■",end="")
        print("") # print newline

        print(f"{mainLine}") # print main line

        for index in range(mainLineLength): # print bottom box cover
            print("■",end="")
        print("") # print newline

    print("Please input your desired choice (number): ", end = "") # print asking line
    try:
        menuNum = int(float(input()))
        if menuNum <= 0:
            print("|You entered an invalid number|")
            return askMenuDeprecated(menuList, True)
    except:
        print("|You entered an invalid number|")
        return askMenuDeprecated(menuList, True)
    try:
        menuList[(menuNum-1)]
    except IndexError:
        print("|Number not valid|")
    else:
        return menuList[(menuNum-1)]

class border():
    top = "─"
    bottom = top
    dash = top
    side = "│"
    topLeft = "╭"
    topRight = "╮"
    bottomLeft = "╰"
    bottomRight = "╯"
    leftSplit = "├"
    rightSplit = "┤"
    topSplit = "┬"
    bottomSplit = "┴"
    crossSplit = "┼"
    forwardSlash = "╱"
    backwardSlash = "╲"
    cross = "╳"
    windowsMinimize = "_"
    windowsMaximize = "□"
    windowsClose = "X"


# Generates Colored Output
# from https://stackoverflow.com/questions/73750465/color-print-in-python
# https://stackoverflow.com/questions/4842424/list-of-ansi-color-escape-sequences
class color():
    RED = '\033[31m'
    ORANGE = '\033[38;5;208m'      # True orange (extended color)
    YELLOW = '\033[33m'
    GREEN = '\033[32m'
    BLUE = '\033[34m'
    INDIGO = '\033[38;5;54m'       # Indigo (extended color)
    VIOLET = '\033[35m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    BLACK = '\033[30m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_ORANGE = '\033[38;5;214m' # Bright orange (extended color)
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_INDIGO = '\033[38;5;57m'  # Bright indigo (extended color)
    BRIGHT_VIOLET = '\033[95m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'
    RESET = '\033[0m'

# list of ansi characters https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797


class format():
    # underline does not work on vs code
    UNDERLINE = '\033[4' #https://stackoverflow.com/questions/35401019/how-do-i-print-something-underlined-in-python
    BOLD = '\033[1m' # https://stackoverflow.com/questions/4842424/list-of-ansi-color-escape-sequences
    HIDE_CURSOR = "\033[?25l" # https://stackoverflow.com/questions/50150552/how-to-get-set-cursor-visibility-without-using-libtinfo-libncurses
    SHOW_CURSOR = "\033[?25h"
    GOTO_00 = '\033[0;0f' # https://stackoverflow.com/questions/66522550/print-string-to-terminal-over-and-over-again-without-flickering-in-python
    CLEAR_SCREEN = '\033[2J'
    RESET = '\033[0m'

    def moveCursor(x):
        printnl(f"\033[{x}C")

    def hideCursor():
        printnl(f"{format.HIDE_CURSOR}")

    # print("\033[<2>;<2>H   - Put the cursor at line L and column C.")
    def gotoXY(x,y):
        printnl(f"\033[{y};{x}H")

def drawWindowBuffered(titleBar: str, windowLines: list, minWidth:int = 0, minHeight:int = 0, clearPreviousType: str|None|bool = "both", returnType: str = "print") -> str|list|None:
    """
    draws the window buffer style to avoid terminal flickering
    titleBar: title bar text
    windowLines: body text
    minWidth: will size window to this width (left to right) fif its not big enough, does not shrink
    minHeight: will size window to this height (top to bottom) if its not big enough, does not shrink
    clearPrevious: default: both: clears other characters of the screen. horizontal: clears rows but not text underneath. vertical: clears text underneath box. None: doesnt clear
    returnType: default: print: prints to terminal. list: returns list, str: returns string
    """
    # region example
    # example output:
    # titleBar = "Hello World"
    # windowLines = ["hello", "world", "123"]
    # ╭─────────────┬───┬───┬───╮
    # │ Hello World │ _ │ □ │ X │
    # ├─────────────┴───┴───┴───┤
    # │ hellosdjafhsjdhfkhakjsd │
    # │ world                   │
    # │ 123                     │
    # ╰─────────────────────────╯
    # titleBar = 11
    # topBar = 25 or titleBar + 14
    # buttonOffset = 13 or titleBar + 2
    # windowLine = 23
    # topBar = 25 or windowLine + 2
    # endregion example
    
    buttonLength = 12
    buttonWidth = 3
    # get the max length to size window appropriately
    maxLength = visibleLength(titleBar) + 2 + buttonLength
    for line in windowLines: # check for each line
        if ( visibleLength(line) + 2 ) > maxLength:
            maxLength += ((visibleLength(line) + 2) - maxLength)

    maxLength = minWidth - 2 if maxLength < minWidth else maxLength # only increase when window width is less then minWidth
    titleBarSpaceLength = maxLength - visibleLength(titleBar) - 2 - buttonLength

    
    outputLines = []

    outputLines.append(f"{color.BRIGHT_BLUE}{border.topLeft}{border.dash * (maxLength - buttonLength)}{ (border.topSplit + (border.dash * buttonWidth)) * 3}{border.topRight}{color.RESET}") 
    outputLines.append(f"{color.BRIGHT_BLUE}{border.side}{color.RESET} {titleBar} {' ' * titleBarSpaceLength}{color.BRIGHT_BLUE}{border.side} {color.RESET}{border.windowsMinimize} {color.BRIGHT_BLUE}{border.side}{color.RESET} {border.windowsMaximize} {color.BRIGHT_BLUE}{border.side}{color.RED} {border.windowsClose} {color.BRIGHT_BLUE}{border.side}{color.RESET}")
    outputLines.append(f"{color.BRIGHT_BLUE}{border.leftSplit}{border.dash * (maxLength - buttonLength)}{ (border.bottomSplit + (border.dash * buttonWidth)) * 3}{border.rightSplit}{color.RESET}")
    for line in windowLines:
        # get line length
        spacesToAdd = maxLength - 2 - visibleLength(line)
        outputLines.append(f"{color.BRIGHT_BLUE}{border.side}{color.RESET} {line}{' ' * spacesToAdd} {color.BRIGHT_BLUE}{border.side}{color.RESET}")

    if (len(outputLines)+1) < minHeight:
        remainingLines = minHeight - visibleLength(outputLines) - 1
        for index in range(remainingLines):
            spacesToAdd = maxLength - 2
            outputLines.append(f"{color.BRIGHT_BLUE}{border.side}{color.RESET} {' ' * spacesToAdd} {color.BRIGHT_BLUE}{border.side}{color.RESET}")
    
    outputLines.append(f"{color.BRIGHT_BLUE}{border.bottomLeft}{border.bottom * maxLength}{border.bottomRight}{color.RESET}")

    
    if clearPreviousType in ("both", True):
        clearExcessBuffered(outputLines)
    elif clearPreviousType == "horizontal":
        clearExcessBuffered(outputLines, vertical=False)
    elif clearPreviousType == "vertical":
        clearExcessBuffered(outputLines, horizontal=False)
    elif clearPreviousType in (None, "None", False):
        pass
    else:
        raise ValueError(f"Invalid returnType: {returnType}")

    outputString = '\n'.join(outputLines)
    if returnType == "print":
        printnl(outputString)
    elif returnType == "string":
        return outputString
    elif returnType == "list":
        return outputLines
    else:
        raise ValueError(f"Invalid returnType: {returnType}")

def clearExcessBuffered(frame, vertical: bool = True, horizontal: bool = True): 
    #https://www.w3schools.com/python/ref_os_get_terminal_size.asp
    columns = os.get_terminal_size().columns
    rows = os.get_terminal_size().lines
    rowsRemaining = rows
    if horizontal:
        for index, line in enumerate(frame):
            rowsRemaining -= 1
            remainder = columns - visibleLength(line)
            line += (f"{' ' * remainder}")
            frame[index] = line
    if vertical:
        for index in range(rowsRemaining):
            currentLine = rows - rowsRemaining
            frame.append(" " * columns)


def clearInputLine():
    """Clear the current input line without affecting the rest"""
    printnl("\r") 
    printnl(" " * os.get_terminal_size().columns)  
    printnl("\r")  

# region askForInput
"""
╭─────────────┬───┬───┬───╮
│ Hello World │ _ │ □ │ X │
├─────────────┴───┴───┴───┤
│ hellosdjafhsjdhfkhakjsd │
│ world                   │
│ 123                     │
╰─────────────────────────╯

"""
# endregion askForInput
def askForInput(titleBar, question: str = "Please type your response:", minWidth: int = 30, minHeight: int = 0, inputPrompt: str = ">"):
    question.append("")
    question.append(f"{inputPrompt}")
    question.append("")
    
    drawWindowBuffered(titleBar, question, minWidth=minWidth, minHeight=minHeight)
    
    xPos = visibleLength(inputPrompt) + 4
    format.gotoXY(xPos,6)
    userInput = input()
    
    return userInput
# testing askForInput
# titleBar = "My Game"
# user_response = askForInput(titleBar, "What's your name?")

# drawWindowBuffered(titleBar, [f"{user_response}"])


# askMenuV2
def askMenu( titleBar: str, choices: list, promptText: str|list = "Please choose an option:", askUntilValid: bool = True, validOptions: list[list[str]] = None, showNumbers: bool = True, returnIndex: bool = False, ignoreLetterCase: bool = True, minWidth: int = 0, minHeight: int = 0, warningMessage: str|None = None) -> int | str | None:
    """
    choices: the options the user can choose ex: ["Option 1", "Option 2"]
    titleBar: titleBar name (usually game name)
    promptText: default: adds "Please choose an option:" before the choices
    askUntilValid: default: ask until the user enters a valid option, if false, returns user input when invalid option is selected
    validOptions: valid accepted text that will route to the choice. ex: [ ["1", "Option 1","opt 1", etc...] , [], [] ] will allow Option 1 to route to index 0.
                  make sure that you implement it for all cases since this will override the default one.
    showNumbers: default: shows [1] before each choice
    returnIndex: default: returns choice text, if true, returns index.
    ignoreLetterCase: default: ignores lEtTeRcAsE
    minWidth: minimum window width
    minHeight: minimum window height
    """

    
    # https://discuss.python.org/t/why-do-my-lists-get-modified-when-passed-to-a-function/5036
    menuChoices = choices.copy()
    
    if showNumbers:
        for index, line in enumerate(menuChoices):
            menuChoices[index] = f"[{index + 1}] {line}"
    
    


    # https://stackoverflow.com/questions/21939652/insert-at-first-position-of-a-list-in-python
    if type(promptText) == str:
        menuChoices.insert(0, promptText)
    elif type(promptText) == list:
        menuChoices = promptText + menuChoices

    if warningMessage:
        menuChoices.insert(0, warningMessage)
    
    




    drawWindowBuffered(titleBar, menuChoices, minWidth, minHeight)
    printnl(format.GOTO_00)
    drawWindowBuffered(titleBar, menuChoices, minWidth, minHeight, clearPreviousType="horizontal")
    print("")
    # need to implement askUntilValid, validOptions, returnIndex, ignoreLetterCase
    if not validOptions:
        if askUntilValid:
            try:
                response = int(input())
                return choices[response - 1]
            except (ValueError, IndexError):
                clearInputLine
                warningMessage = f"{color.BRIGHT_RED}{format.BOLD}Invalid Choice{color.RESET}"
                return askMenu(titleBar, choices, promptText, askUntilValid, validOptions, showNumbers, returnIndex, ignoreLetterCase, minWidth, minHeight, warningMessage)


# menuTitle = "My Game"
# menuList = ["choice 1", "choice 2", "choice 3"]
# print(askMenu(menuTitle, menuList))
# time.sleep(1)
# print(askMenu(menuTitle, menuList))
    
    

# menuList = ["option 1"]



# for i in range(30, 37 + 1):
#     print("\033[%dm%d\t\t\033[%dm%d" % (i, i, i + 60, i + 60))

# print("\033[39m\\033[49m                 - Reset color")
# print("\033[2K                          - Clear Line")

# print("\033[<2>A                        - Move the cursor up N lines")
# print("\033[<2>B                        - Move the cursor down N lines")
# print("\033[2C                        - Move the cursor forward N columns")
# print("\033[<2>D                        - Move the cursor backward N columns\n")
# print("\033[2J                          - Clear the screen, move to (0,0)")
# print("\033[K                           - Erase to end of line")
# print("\033[s                           - Save cursor position")
# print("\033[u                           - Restore cursor position\n")
# print("\033[4m                          - Underline on")
# print("\033[24m                         - Underline off\n")
# print(f"\033[1m Bold on {color.RESET} OFFF")
# print("\033[21m                         - Bold off")





# testing
# clearV2()

# printnl(os.get_terminal_size().columns)
# format.moveCursor(5)
# printnl(os.get_terminal_size().lines)
# print("")
# time.sleep(1)
# clearV2()



# printnl(f"{format.HIDE_CURSOR}")
# windowIndex = 0
# isIncreasing = True
# i=0
# while windowIndex < (60*10):
#     windowIndex += 1
#     if isIncreasing:
#         i+=1
#         if i>=60:
#             isIncreasing = False
#     else:
#         i-=1
#         if i<=0:
#             isIncreasing = True
    
#     printnl(f"{format.GOTO_00}")
#     titleBar = "Please choose an option"
#     titleBar += " " * int(i)
#     windowLines = ["hello world", "world", "123"]
    
#     for index in range((i // 10)):
#         windowLines.append("")
#     drawWindowBuffered(titleBar, windowLines) 
#     time.sleep(1/60) # 60fps
# printnl(f"{format.SHOW_CURSOR}")



# # titleBar = "Hello World"
# titleBar = "1234"
# # windowLines = ["line 1", "line 2", "line 3"]
# windowLines = ["1","2","3"]
# drawWindowBuffered(titleBar,windowLines)





