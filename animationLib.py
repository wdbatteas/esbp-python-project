from terminalLib import *
import os
import random
import time

def loadingIntroRanTime():
    return random.uniform(0.0, 0.1)



def loadingIntro():
    printnl(color.BRIGHT_GREEN) 
    printnl(color.BRIGHT_CYAN)
    animateLetterByLetter("SYSTEM INITIALIZING")
    printnl(color.WHITE)
    animateLetterByLetter("....", 3)
    animateLetterByLetter(".........", 45)
    printnl(color.BRIGHT_GREEN)
    animateLetterByLetter("OK", sleep=loadingIntroRanTime())
    print()

    printnl(color.BRIGHT_CYAN)
    animateLetterByLetter(f"LOADING PYTHON MODULES", 1000)
    printnl(color.WHITE)
    animateLetterByLetter("..", 2)
    animateLetterByLetter("........", 45)
    printnl(color.BRIGHT_GREEN)
    animateLetterByLetter("OK", sleep=loadingIntroRanTime())
    print()

    printnl(color.BRIGHT_CYAN)
    animateLetterByLetter(f"LOADING STORAGE MODULES", 1000)
    printnl(color.WHITE)
    animateLetterByLetter(".........", 45)
    printnl(color.BRIGHT_GREEN)
    animateLetterByLetter("OK")
    print()

    printnl(color.BRIGHT_CYAN)
    animateLetterByLetter(f"LOADING INVENTORY MODULES", 1000)
    printnl(color.WHITE)
    animateLetterByLetter(".......", 45)
    printnl(color.BRIGHT_GREEN)
    animateLetterByLetter("OK")
    print()

    printnl(color.BRIGHT_CYAN)
    animateLetterByLetter(f"LOADING CUSTOMER MODULES", 1000)
    printnl(color.WHITE)
    animateLetterByLetter("........", 45)
    printnl(color.BRIGHT_GREEN)
    animateLetterByLetter("OK")
    print()

    printnl(color.BRIGHT_CYAN)
    animateLetterByLetter(f"LOADING OLLAMA MODULES", 1000)
    printnl(color.WHITE)
    animateLetterByLetter("..........", 45)
    printnl(color.BRIGHT_GREEN)
    animateLetterByLetter("OK")
    print()

    printnl(color.BRIGHT_CYAN)
    animateLetterByLetter(f"LOADING GAME MODULES", 1000)
    printnl(color.WHITE)
    animateLetterByLetter("............", 45)
    printnl(color.BRIGHT_GREEN)
    animateLetterByLetter("OK")
    print()

    printnl(color.BRIGHT_CYAN)
    animateLetterByLetter(f"LOADING TRANSLATION MODULES", 1000)
    printnl(color.WHITE)
    animateLetterByLetter(".....", 45)
    printnl(color.BRIGHT_GREEN)
    animateLetterByLetter("OK")
    print()

    printnl(color.BRIGHT_CYAN)
    animateLetterByLetter(f"LOADING ANIMATION MODULES", 1000)
    printnl(color.WHITE)
    animateLetterByLetter(".......", 45)
    printnl(color.BRIGHT_GREEN)
    printnl(format.HIDE_CURSOR)
    size = getTerminalSize()
    cols, rows = size.columns, size.lines
    if cols < 50 or rows < 50:
        printnl(color.BRIGHT_RED)
        printnl(format.BOLD)
        animateLetterByLetter("WARNING: ")
        printnl(format.RESET)
        printnl(color.BRIGHT_RED)
        animateLetterByLetter(f"Terminal is     x    . Please increase size")
        while True:
            cols, rows = getTerminalSize()
            format.gotoXY(54,9)
            printnl(f"{cols:>4}x{rows:>4}")
            if cols > 50 and rows > 50: 
                break
    printnl(format.SHOW_CURSOR)
    format.gotoXY(0,8)
    print(color.BRIGHT_GREEN)
    printnl(f"{color.BRIGHT_CYAN}LOADING ANIMATION MODULES{color.WHITE}.......                                                    ")
    format.gotoXY(33,9)
    printnl(color.BRIGHT_GREEN)
    animateLetterByLetter("OK")
    print()

    printnl(color.GREEN)
    animateLetterByLetter("ubuntu@linuz", 240, 0.1)
    printnl(color.WHITE)
    animateLetterByLetter(":", 240, 0.1)
    printnl(color.BLUE)
    animateLetterByLetter("~/Desktop", 240, 0.1)
    printnl(color.WHITE)
    animateLetterByLetter("$ sudo apt update", 240, 0.1)

    print()
    print("Hit:1 http://archive.ubuntu.com/ubuntu jammy InRelease")
    time.sleep(loadingIntroRanTime())
    
    print("Hit:2 http://security.ubuntu.com/ubuntu jammy-security InRelease")
    time.sleep(loadingIntroRanTime())
    
    print("Hit:3 http://archive.ubuntu.com/ubuntu jammy-updates InRelease")
    time.sleep(loadingIntroRanTime())
    
    print("Hit:4 http://archive.ubuntu.com/ubuntu jammy-backports InRelease")
    time.sleep(loadingIntroRanTime())
    
    print("Reading package lists... Done")
    time.sleep(loadingIntroRanTime())
    
    print("Building dependency tree       ")
    time.sleep(loadingIntroRanTime())
    
    print("Reading state information... Done")
    time.sleep(loadingIntroRanTime())
    
    print("All packages are up to date.")
    time.sleep(loadingIntroRanTime())
    




    
    animateRainbowText("STARTING PROGRAM IN ")
    for countdown, col in zip(["3...", "2...", "1..."], rainbow_colors):
        printnl(col)
        animateLetterByLetter(countdown, 6)
    print()
    

rainbow_colors = [
    color.BRIGHT_RED,
    color.BRIGHT_YELLOW,
    color.BRIGHT_GREEN,
    color.BRIGHT_CYAN,
    color.BRIGHT_BLUE,
    color.BRIGHT_MAGENTA,
]

def animateRainbowText(text, charsPerSecond=120, sleep=0.0):
    for i, letter in enumerate(text):
        printnl(rainbow_colors[i % len(rainbow_colors)] + letter)
        time.sleep(1/charsPerSecond)
    time.sleep(sleep)
    printnl(color.RESET)

def animateLetterByLetter(text: str, charsPerSecond:float = 120, sleep: float = 0.0):
    for letter in text:
        printnl(letter)
        time.sleep(1/charsPerSecond)
    time.sleep(sleep)

# https://emojicombos.com/chocolate-ascii-art
chocolate = [
"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠶⠛⠻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠞⠋⣠⠴⠚⢦⡘⢷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡴⠾⣿⣄⠐⠋⠁⠀⠀⠀⠳⠈⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
"⠀⠀⠀⠀⠀⠀⠀⠀⣠⡴⠛⣡⠴⢶⣄⣿⣦⠀⠀⠀⠀⠀⠀⠀⠘⢿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
"⠀⠀⠀⠀⠀⣠⣴⣿⠁⠐⠋⠀⠀⠀⢻⡄⠹⣷⡀⠠⣤⠄⠀⢀⣤⠞⢻⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
"⠀⠀⣠⠴⠋⢁⣄⠻⣧⡀⠀⠀⠀⠀⠀⠉⠀⢛⣿⣄⣀⡤⠞⢋⡴⠷⣌⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
"⣴⠛⠁⠤⠚⠉⠈⢳⡙⣷⡄⠀⠀⠀⠀⠀⠀⣸⡿⣿⣿⠀⠘⠁⠀⠀⠈⠙⢿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
"⣿⣷⡀⠀⠀⠀⠀⠀⠑⠈⢻⣆⠈⠋⣀⡴⠚⣡⣤⡈⢻⣷⡀⠀⠀⠀⠀⠀⠈⠻⣿⡦⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
"⠘⣿⣷⡀⠀⡀⠀⠀⠀⠀⢀⣿⣷⡟⠁⠀⠋⠁⠀⠙⠀⢻⣷⡄⠳⠀⠀⢀⡠⠞⠉⠀⠀⠀⠉⠛⠛⠓⠒⠦⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀",
"⠀⠘⣿⣷⡄⠙⠒⢊⡠⢖⣋⡙⠛⣷⡄⠀⠀⠀⠀⠀⠀⠀⠙⢻⣀⡤⠚⠉⢧⣄⠀⠀⠘⢿⣦⣀⣤⠤⠔⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀",
"⠀⠀⠈⢿⣿⣶⠞⠉⠐⠋⠉⠻⡆⠈⣿⣄⠀⠦⠤⠀⢀⡠⠔⠛⠻⠷⡿⢶⠀⠉⢳⣄⣤⣤⡿⢿⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
"⠀⠀⠀⠈⢻⣿⣧⡀⠀⠀⠀⠀⠀⠀⠉⢿⣆⣀⣤⡒⠉⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⣽⣿⡿⠁⠈⢿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
"⠀⠀⠀⠀⠀⠹⣿⣷⡀⠱⣄⠀⠀⠀⣀⣴⠛⠁⢴⣿⣦⣄⣆⠤⣄⣀⠀⠀⠀⠀⡴⠛⠁⠀⠀⠀⠠⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
"⠀⠀⠀⠀⠀⠀⠙⣿⣿⡄⠀⣠⠔⠋⢀⣻⣤⣠⣴⡟⢿⣿⣭⣽⣿⣯⣷⡄⢀⡼⠁⠀⠀⠀⠀⣀⠈⠛⢻⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀",
"⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣫⣥⡴⠾⠟⠉⠿⠟⠋⠁⠇⠀⠉⠉⠉⠀⠈⠻⠛⠀⠀⠀⠀⢠⠜⠁⠀⠀⣼⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀",
"⠀⠀⠀⠀⠀⠀⢰⡇⠀⣼⣿⣿⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠖⠁⠀⣀⠤⠊⠉⠉⢿⣿⣆⠀⠀⠀⠀⠀⠀⠀",
"⠀⠀⠀⠀⠀⠀⠈⢻⣟⣻⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠃⢀⡠⠚⠁⠀⠀⠀⠀⠀⠻⣿⣆⠀⠀⠀⠀⠀⠀",
"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠋⢀⠔⠋⢀⠔⠂⠀⠀⠀⠀⠀⠀⠙⢻⣧⠀⠀⠀⠀⠀",
"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⡟⢁⠔⠁⣠⠖⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣧⠀⠀⠀⠀",
"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⣠⢊⣞⠔⠁⡠⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣧⠀⠀⠀",
"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣧⡀⠀⠀⠀⢀⠞⢡⠞⢁⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢷⡀⠀",
"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣷⡄⠀⠰⠁⡠⠃⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡄",
"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣆⠀⠀⠡⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣻",
"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠏",
"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡴⠟⠁⠀",
"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣤⣶⠶⠛⠉⠀⠀⠀⠀",
"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣼⣿⡿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀",
"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⢷⡄⠀⠀⠀⠀⠀⢀⣤⣾⣿⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⡄⠀⠀⡀⣴⣿⠿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣤⣴⡟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"
]


def chocoIntro():
    import time
    import random
    
    terminal_width = getTerminalWidth()
    art_width = max(len(line) for line in chocolate)
    
    clearV2()
    format.hideCursor()
    
    try:
        for x_pos in range(-art_width, terminal_width + 1):
            # Build entire frame as string first
            frame_output = format.GOTO_00
            
            for y, line in enumerate(chocolate):
                # Position cursor for this line
                frame_output += f"\033[{y + 1};{max(1, x_pos + 1)}H"
                
                # Determine visible portion
                visible_line = ""
                if x_pos < 0:
                    visible_start = abs(x_pos)
                    if visible_start < len(line):
                        visible_line = line[visible_start:]
                elif x_pos + len(line) > terminal_width:
                    visible_end = terminal_width - x_pos
                    if visible_end > 0:
                        visible_line = line[:visible_end]
                else:
                    visible_line = line
                
                # Add colored characters to frame
                for char in visible_line:
                    if char != ' ':
                        random_color = random.choice(rainbow_colors)
                        frame_output += random_color + char + color.RESET
                    else:
                        frame_output += char
            
            # Print entire frame at once
            printnl(frame_output)
            time.sleep(0.001)
            
    except KeyboardInterrupt:
        pass
    finally:
        printnl(format.SHOW_CURSOR)

banner = """
/ $$   /$$  /$$$$$$  /$$      /$$ /$$$$$$$  /$$     /$$ /$$                                                  
| $$  | $$ /$$__  $$| $$  /$ | $$| $$__  $$|  $$   /$$/| $$                                                  
| $$  | $$| $$  \ $$| $$ /$$$| $$| $$  \ $$ \  $$ /$$/ | $$                                                  
| $$$$$$$$| $$  | $$| $$/$$ $$ $$| $$  | $$  \  $$$$/  | $$                                                  
| $$__  $$| $$  | $$| $$$$_  $$$$| $$  | $$   \  $$/   |__/                                                  
| $$  | $$| $$  | $$| $$$/ \  $$$| $$  | $$    | $$                                                          
| $$  | $$|  $$$$$$/| $$/   \  $$| $$$$$$$/    | $$     /$$                                                  
|__/  |__/ \______/ |__/     \__/|_______/     |__/    |__/                                                                                                                            
 /$$                   /$$                                                                                   
| $$                  | $$                                                                                   
| $$        /$$$$$$  /$$$$$$   /$$$$$$$       /$$$$$$/$$$$   /$$$$$$  /$$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$ 
| $$       /$$__  $$|_  $$_/  /$$_____/      | $$_  $$_  $$ |____  $$| $$__  $$ |____  $$ /$$__  $$ /$$__  $$
| $$      | $$$$$$$$  | $$   |  $$$$$$       | $$ \ $$ \ $$  /$$$$$$$| $$  \ $$  /$$$$$$$| $$  \ $$| $$$$$$$$
| $$      | $$_____/  | $$ /$$\____  $$      | $$ | $$ | $$ /$$__  $$| $$  | $$ /$$__  $$| $$  | $$| $$_____/
| $$$$$$$$|  $$$$$$$  |  $$$$//$$$$$$$/      | $$ | $$ | $$|  $$$$$$$| $$  | $$|  $$$$$$$|  $$$$$$$|  $$$$$$$
|________/ \_______/   \___/ |_______/       |__/ |__/ |__/ \_______/|__/  |__/ \_______/ \____  $$ \_______/
                                                                                          /$$  \ $$          
                                                                                         |  $$$$$$/          
                                                                                          \______/                                                                                          
 /$$   /$$  /$$$$$$  /$$   /$$  /$$$$$$        /$$$$$$$   /$$$$$$  /$$  /$$  /$$                             
| $$  | $$ /$$__  $$| $$  | $$ /$$__  $$      | $$__  $$ /$$__  $$| $$ | $$ | $$                             
| $$  | $$| $$  \ $$| $$  | $$| $$  \__/      | $$  \ $$| $$$$$$$$| $$ | $$ | $$                             
| $$  | $$| $$  | $$| $$  | $$| $$            | $$  | $$| $$_____/| $$ | $$ | $$                             
|  $$$$$$$|  $$$$$$/|  $$$$$$/| $$            | $$  | $$|  $$$$$$$|  $$$$$/$$$$/                             
 \____  $$ \______/  \______/ |__/            |__/  |__/ \_______/ \_____/\___/                              
 /$$  | $$                                                                                                   
|  $$$$$$/                                                                                                   
 \______/                                                                                                    
  /$$$$$$  /$$$$$$$$ /$$$$$$  /$$$$$$$  /$$$$$$$$ /$$                                                        
 /$$__  $$|__  $$__//$$__  $$| $$__  $$| $$_____/| $$                                                        
| $$  \__/   | $$  | $$  \ $$| $$  \ $$| $$      | $$                                                        
|  $$$$$$    | $$  | $$  | $$| $$$$$$$/| $$$$$   | $$                                                        
 \____  $$   | $$  | $$  | $$| $$__  $$| $$__/   |__/                                                        
 /$$  \ $$   | $$  | $$  | $$| $$  \ $$| $$                                                                  
|  $$$$$$/   | $$  |  $$$$$$/| $$  | $$| $$$$$$$$ /$$                                                        
 \______/    |__/   \______/ |__/  |__/|________/|__/                                                        
                                                                                                             
                                                                                                             
                                                                                                             
  """

# Split the banner into lines and store in a list
banner_list = banner.strip().split('\n')

def neon_sign(logo_lines, flicker_count=3):
    clearV2()
    format.hideCursor()
    
    neon_colors = [color.BRIGHT_MAGENTA, color.BRIGHT_CYAN, color.BRIGHT_WHITE]
    
    for flicker in range(flicker_count):
        # Flicker effect
        for flash in range(random.randint(2, 5)):
            printnl(format.GOTO_00)
            
            if flash % 2 == 0:
                # On
                for line in logo_lines:
                    outline = ""
                    for char in line:
                        if char != ' ':
                            outline += f"{random.choice(neon_colors)}{format.BOLD}{char}{color.RESET}"
                        else:
                            outline += ' '
                    print(outline)
            else:
                # Off
                for line in logo_lines:
                    print(' ' * len(line))
            
            time.sleep(0.1)
        
        time.sleep(0.2)


def hologram_logo(logo_lines):
    clearV2()
    format.hideCursor()
    
    # Show logo with scan lines moving across
    for scan_line in range(len(logo_lines) + 5):
        printnl(format.GOTO_00)
        
        for i, line in enumerate(logo_lines):
            if i == scan_line:
                # Bright scan line
                print(f"{color.BRIGHT_WHITE}{format.BOLD}{line}{color.RESET}")
            elif abs(i - scan_line) <= 2:
                # Dimmer lines near scan
                print(f"{color.BRIGHT_MAGENTA}{line}{color.RESET}")
            else:
                # Normal lines
                print(f"{color.RED}{line}{color.RESET}")
        
        time.sleep(0.03)


def matrix_rain(duration=3):
    columns = os.get_terminal_size().columns
    rows = os.get_terminal_size().lines
    
    # Initialize columns with random starting positions
    drops = [0] * columns
    
    for _ in range(int(duration * 60)):  # 60 FPS
        printnl(format.GOTO_00)
        
        for col in range(columns):
            if drops[col] > rows:
                drops[col] = 0
            
            # Draw the "rain" character
            if drops[col] < rows:
                print(f"\033[{drops[col]};{col}H{color.BRIGHT_GREEN}{random.choice('01')}{color.RESET}")
                drops[col] += 1
        
        time.sleep(1/60)


def playIntro():
    loadingIntro()
    chocoIntro()
    hologram_logo(banner_list)
    neon_sign(banner_list, 1)

if __name__ == "__main__":
    # playIntro()
    # testFireworks()
    pass




   