# started from barebones tkinter starter code from CMU's 15-112 by David Kosbie

# new comment



# Global variables: canvas width and height
canvasWidth = 1280
canvasHeight = 720
buffer = 40

from tkinter import *
import random

def chooseTable(data):
    if (data.difficulty == 0):
        return random.choice([0,1])

####################################
# customize these functions
####################################

def init(data):
    # load the fish images
    loadFishImages(data)

    # splash screen, start with main menu
    # modes can be: mainMenu, playGame, incorrectMode, 
    # correctMode, blankMode, tooLong, gameOver
    data.mode = "mainMenu"
    data.round = 0

    # difficulty
    data.difficulty = 0
    data.maxDifficulty = 0
    data.timeMax = 2500 # milliseconds
                        # based on Davidson et al.
    data.timeRemaining = data.timeMax # starting out at timeMax, to be reset every attempt

    # probability table
    # data.tableTemplate = [NumberWidth, "Congruent"/"Incongruent", data.timeMax]
    data.tables = [
        # level 1
        [
            [1,"Congruent",2500]
        ],
        
        # level 2
        [
            [5,"Congruent",2500],
            [1,"Congruent",2000]
        ],

        # level 3
        [
            [5,"Incongruent",2500],
            [5,"Congruent",2000],
            [1, "Congruent",1500]
        ],

        # level 4
        [
            [5,"Incongruent",2000],
            [5,"Congruent",1500]
        ],

        # level 5
        [
            [5,"Incongruent",1500]
        ]
    ]
    data.level = -1

    # score
    data.correct = 0
    data.incorrect = 0
    data.leaderBoard = {'None':0}

    # misc
    data.paused = False
    data.pauseTime = 1

    #customization
    data.customize = 0
    data.bgColor = "white"
    data.fontColor = "black"
    data.correctColor = "green"
    data.incorrectColor = "red"
    data.tooLongColor = "yellow"
    data.timeLowColor = "red"
    data.useNotifs = True
    data.fonts = ["Helvetica", "Times"]
    data.font = 0
    data.maxRounds = 10
    data.showUI = True

def loadFishImages(data):
    data.images = []
    data.images.append(PhotoImage(file="CR.png"))
    data.images.append(PhotoImage(file="CL.png"))
    data.images.append(PhotoImage(file="NR.png"))
    data.images.append(PhotoImage(file="NL.png"))
    data.images.append(PhotoImage(file="ICR.png"))
    data.images.append(PhotoImage(file="ICL.png"))

########################
# mode dispatcher
########################

def mousePressed(event, data):
    if (data.mode == "mainMenu"):        mainMenuMousePressed(event, data)
    elif (data.mode == "customize"):     customizeMousePressed(event, data)
    elif (data.mode == "helpDDR"):       helpDDRMousePressed(event, data)
    elif (data.mode == "helpKey"):       helpKeyMousePressed(event, data)
    elif (data.mode == "playGame"):      playGameMousePressed(event, data)
    elif (data.mode == "incorrectMode"): incorrectModeMousePressed(event, data)
    elif (data.mode == "correctMode"):   correctModeMousePressed(event, data)
    elif (data.mode == "blankMode"):     blankModeMousePressed(event, data)
    elif (data.mode == "tooLong"):       tooLongMousePressed(event, data)
    elif (data.mode == "gameOver"):      gameOverMousePressed(event, data)

def keyPressed(event, data):
    if (data.mode == "mainMenu"):        mainMenuKeyPressed(event, data)
    elif (data.mode == "customize"):     customizeKeyPressed(event, data)
    elif (data.mode == "helpDDR"):       helpDDRKeyPressed(event, data)
    elif (data.mode == "helpKey"):       helpKeyKeyPressed(event, data)
    elif (data.mode == "playGame"):      playGameKeyPressed(event, data)
    elif (data.mode == "incorrectMode"): incorrectModeKeyPressed(event, data)
    elif (data.mode == "correctMode"):   correctModeKeyPressed(event, data)
    elif (data.mode == "blankMode"):     blankModeKeyPressed(event, data)
    elif (data.mode == "tooLong"):       tooLongKeyPressed(event, data)
    elif (data.mode == "gameOver"):      gameOverKeyPressed(event, data)

def timerFired(data):
    if (data.mode == "mainMenu"):        mainMenuTimerFired(data)
    elif (data.mode == "customize"):     customizeTimerFired(data)
    elif (data.mode == "helpDDR"):       helpDDRTimerFired(data)
    elif (data.mode == "helpKey"):       helpKeyTimerFired(data)
    elif (data.mode == "playGame"):      playGameTimerFired(data)
    elif (data.mode == "incorrectMode"): incorrectModeTimerFired(data)
    elif (data.mode == "correctMode"):   correctModeTimerFired(data)
    elif (data.mode == "blankMode"):     blankModeTimerFired(data)    
    elif (data.mode == "tooLong"):       tooLongTimerFired(data)
    elif (data.mode == "gameOver"):      gameOverTimerFired(data)

def redrawAll(canvas, data):
    if (data.mode == "mainMenu"):        mainMenuRedrawAll(canvas, data)
    elif (data.mode == "customize"):     customizeRedrawAll(canvas, data)
    elif (data.mode == "helpDDR"):       helpDDRRedrawAll(canvas, data)
    elif (data.mode == "helpKey"):       helpKeyRedrawAll(canvas, data)
    elif (data.mode == "playGame"):      playGameRedrawAll(canvas, data)
    elif (data.mode == "incorrectMode"): incorrectModeRedrawAll(canvas, data)
    elif (data.mode == "correctMode"):   correctModeRedrawAll(canvas, data)
    elif (data.mode == "blankMode"):     blankModeRedrawAll(canvas, data)
    elif (data.mode == "tooLong"):       tooLongRedrawAll(canvas, data)
    elif (data.mode == "gameOver"):      gameOverRedrawAll(canvas, data)

##################
# mainMenu Mode
##################

def mainMenuMousePressed(event, data):
    pass
def mainMenuKeyPressed(event, data):
    if (event.keysym == 'k'):
        data.mode = "helpKey"
    elif (event.char == 'p'):
        data.mode = "helpDDR"
    elif (event.char == 'c'):
        data.mode = "customize"
def mainMenuTimerFired(data):
    pass
def mainMenuRedrawAll(canvas, data):
    canvas.create_rectangle(0,0,data.width,data.height, fill=data.bgColor) # background
    canvas.create_text(data.width/2, data.height/3, text = "Flanker Task", 
                       font = "%s 36" %data.fonts[data.font])
    canvas.create_text(data.width/2, data.height*2/3, 
                       text = "If playing with a keyboard, press k to start", fill=data.fontColor, font = "%s 20" %data.fonts[data.font])
    canvas.create_text(data.width/2, data.height*2/3+70, 
                       text = "If playing with a dance pad , press p to start", fill=data.fontColor, font = "%s 20" %data.fonts[data.font])
    canvas.create_text(data.width/2, data.height*2/3+140,
                       text = "Press c to customize", fill=data.fontColor, font = "%s 20" %data.fonts[data.font])

##################
# customize Mode
##################

def customizeMousePressed(event, data):
    pass

def customizeKeyPressed(event, data):
    if (data.customize == 0): # data.font
        if (event.char == '1'):
            data.font = 0
        elif (event.char == '2'):
            data.font = 1
        elif (event.keysym == 'space'):
            data.customize = 1
    elif (data.customize == 1): # data.fontColor
        if (event.char == '1'):
            data.fontColor = "Black"
        elif (event.char == '2'):
            data.fontColor = "Brown"
        elif (event.char == '3'):
            data.fontColor = "Purple"
        elif (event.char == '4'):
            data.fontColor = "Green"
        elif (event.char == '5'):
            data.fontColor = "Yellow"
        elif (event.char == '6'):
            data.fontColor = "Red"
        elif (event.keysym == 'space'):
            data.customize = 2
    elif (data.customize == 2): # data.bgColor
        if (event.char == '1'):
            data.bgColor = "White"
        elif (event.char == '2'):
            data.bgColor = "Brown"
        elif (event.char == '3'):
            data.bgColor = "Purple"
        elif (event.char == '4'):
            data.bgColor = "Green"
        elif (event.char == '5'):
            data.bgColor = "Yellow"
        elif (event.char == '6'):
            data.bgColor = "Red"
        elif (event.keysym == 'space'):
            data.customize = 3
    elif (data.customize == 3): # data.correctColor
        if (event.char == '1'):
            data.correctColor = "green"
        elif (event.char == '2'):
            data.correctColor = "yellow"
        elif (event.char == '3'):
            data.correctColor = "red"
        elif (event.char == '4'):
            data.correctColor = "black"
        elif (event.keysym == 'space'):
            data.customize = 4
    elif (data.customize == 4): # data.incorrectColor
        if (event.char == '1'):
            data.incorrectColor = "green"
        elif (event.char == '2'):
            data.incorrectColor = "yellow"
        elif (event.char == '3'):
            data.incorrectColor = "red"
        elif (event.char == '4'):
            data.incorrectColor = "black"
        elif (event.keysym == 'space'):
            data.customize = 5
    elif (data.customize == 5): # data.tooLongColor
        if (event.char == '1'):
            data.tooLongColor = "green"
        elif (event.char == '2'):
            data.tooLongColor = "yellow"
        elif (event.char == '3'):
            data.tooLongColor = "red"
        elif (event.char == '4'):
            data.tooLongColor = "black"
        elif (event.keysym == 'space'):
            data.customize = 6
    elif (data.customize == 6): # data.useNotifs
        if (event.char == '1'):
            data.useNotifs = True
        elif (event.char == '2'):
            data.useNotifs = False
        elif (event.keysym == 'space'):
            data.customize = 7
    elif (data.customize == 7): #data.timeLowColor
        if (event.char == '1'):
            data.timeLowColor = "red"
        elif (event.char == '2'):
            data.timeLowColor = "black"
        elif (event.char == '3'):
            data.timeLowColor = "green"
        elif (event.char == '4'):
            data.timeLowColor = "yellow"
        elif (event.keysym == 'space'):
            data.customize = 8
    elif (data.customize == 8): # data.showUI
        if (event.char == '1'):
            data.showUI = True
        elif (event.char == '2'):
            data.showUI = False
        elif (event.keysym == 'space'):
            data.customize = 9
    elif (data.customize == 9): #data.maxRounds
        if (event.char == '1'):
            data.maxRounds = 10
        elif (event.char == '2'):
            data.maxRounds = 15
        elif (event.char == '3'):
            data.maxRounds = 20
        elif (event.char == '4'):
            data.maxRounds = 30
        elif (event.char == '5'):
            data.maxRounds = 50
        elif (event.keysym == 'space'):
            data.customize = 10
    elif (data.customize == 10): # data.maxDifficulty
        if (event.char == '0'):
            data.maxDifficulty = 0
        elif (event.char == '1'):
            data.maxDifficulty = 1
        elif (event.char == '2'):
            data.maxDifficulty = 2
        elif (event.char == '3'):
            data.maxDifficulty = 3
        elif (event.char == '4'):
            data.maxDifficulty = 4
        elif (event.char == '5'):
            data.maxDifficulty = 5
        elif (event.keysym == 'space'):
            data.customize = 11
    elif (data.customize == 11): # data.difficulty
        if (event.char == '0'):
            data.difficulty = 0
        elif (event.char == '1'):
            data.difficulty = 1
        elif (event.char == '2'):
            data.difficulty = 2
        elif (event.char == '3'):
            data.difficulty = 3
        elif (event.char == '4'):
            data.difficulty = 4
        elif (event.char == '5'):
            data.difficulty = 5
        elif (event.keysym == 'space'):
            data.customize = 12
    elif (data.customize == 12):
        if (event.keysym == 'space'):
            data.mode = "mainMenu"
        
def customizeTimerFired(data):
    pass

def customizeRedrawAll(canvas, data):
    canvas.create_rectangle(0,0,data.width,data.height, fill=data.bgColor) # background
    canvas.create_text(data.width/2, data.height/10, text = "Customizations", fill=data.fontColor, 
                       font = "%s 36" %data.fonts[data.font])
    canvas.create_text(data.width/2, data.height/9+50, text = "Press the corresponding number on the keyboard to customize or the spacebar to continue", fill=data.fontColor, font= "%s 24" %data.fonts[data.font])
    if (data.customize == 0):
        canvas.create_text(buffer, data.height/9+100, text = "Typeface: (1) Helvetica - Sans-serif  (2) Times New Roman - Serif", fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
    elif (data.customize == 1):
        canvas.create_text(buffer, data.height/9+100, text = "Typeface: (1) Helvetica - Sans-serif  (2) Times New Roman - Serif", fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+130, text = "Font Color: (1) Black  (2) Brown  (3) Purple  (4) Green  (5) Yellow  (6) Red", fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
    elif (data.customize == 2):
        canvas.create_text(buffer, data.height/9+100, text = "Typeface: (1) Helvetica - Sans-serif  (2) Times New Roman - Serif", fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+130, text = "Font Color: (1) Black  (2) Brown  (3) Purple  (4) Green  (5) Yellow  (6) Red", fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+160, text = "Background Color: (1) White  (2) Brown  (3) Purple  (4) Green  (5) Yellow  (6) Red", fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
    elif (data.customize == 3):
        canvas.create_text(buffer, data.height/9+100, text = "Typeface: (1) Helvetica - Sans-serif  (2) Times New Roman - Serif", fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+130, text = "Font Color: (1) Black  (2) Brown  (3) Purple  (4) Green  (5) Yellow  (6) Red", fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+160, text = "Background Color: (1) White  (2) Brown  (3) Purple  (4) Green  (5) Yellow  (6) Red", fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+190, text = '"Correct!" Color: (1) Green  (2) Yellow  (3) Red  (4) Black', fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
    elif (data.customize == 4):
        canvas.create_text(buffer, data.height/9+100, text = "Typeface: (1) Helvetica - Sans-serif  (2) Times New Roman - Serif", fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+130, text = "Font Color: (1) Black  (2) Brown  (3) Purple  (4) Green  (5) Yellow  (6) Red", fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+160, text = "Background Color: (1) White  (2) Brown  (3) Purple  (4) Green  (5) Yellow  (6) Red", fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+190, text = '"Correct!" Color: (1) Green  (2) Yellow  (3) Red  (4) Black', fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+220, text = '"Incorrect!" Color: (1) Green  (2) Yellow  (3) Red  (4) Black', fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
    elif (data.customize == 5):
        canvas.create_text(buffer, data.height/9+100, text = "Typeface: (1) Helvetica - Sans-serif  (2) Times New Roman - Serif", fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+130, text = "Font Color: (1) Black  (2) Brown  (3) Purple  (4) Green  (5) Yellow  (6) Red", fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+160, text = "Background Color: (1) White  (2) Brown  (3) Purple  (4) Green  (5) Yellow  (6) Red", fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+190, text = '"Correct!" Color: (1) Green  (2) Yellow  (3) Red  (4) Black', fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+220, text = '"Incorrect!" Color: (1) Green  (2) Yellow  (3) Red  (4) Black', fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+250, text = '"Took Too Long!" Color: (1) Green  (2) Yellow  (3) Red  (4) Black', fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
    elif (data.customize == 6):
        canvas.create_text(buffer, data.height/9+100, text = "Typeface: (1) Helvetica - Sans-serif  (2) Times New Roman - Serif", fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+130, text = "Font Color: (1) Black  (2) Brown  (3) Purple  (4) Green  (5) Yellow  (6) Red", fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+160, text = "Background Color: (1) White  (2) Brown  (3) Purple  (4) Green  (5) Yellow  (6) Red", fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+190, text = '"Correct!" Color: (1) Green  (2) Yellow  (3) Red  (4) Black', fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+220, text = '"Incorrect!" Color: (1) Green  (2) Yellow  (3) Red  (4) Black', fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+250, text = '"Took Too Long!" Color: (1) Green  (2) Yellow  (3) Red  (4) Black', fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+280, text = 'Show Correctness?: (1) Yes  (2) No', fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
    elif (data.customize == 7):
        canvas.create_text(buffer, data.height/9+100, text = "Typeface: (1) Helvetica - Sans-serif  (2) Times New Roman - Serif", fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+130, text = "Font Color: (1) Black  (2) Brown  (3) Purple  (4) Green  (5) Yellow  (6) Red", fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+160, text = "Background Color: (1) White  (2) Brown  (3) Purple  (4) Green  (5) Yellow  (6) Red", fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+190, text = '"Correct!" Color: (1) Green  (2) Yellow  (3) Red  (4) Black', fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+220, text = '"Incorrect!" Color: (1) Green  (2) Yellow  (3) Red  (4) Black', fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+250, text = '"Took Too Long!" Color: (1) Green  (2) Yellow  (3) Red  (4) Black', fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+280, text = 'Show Correctness?: (1) Yes  (2) No', fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+310, text = 'Time Warning Color: (1) Red  (2) Black  (3) Green  (4) Yellow', fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
    elif (data.customize == 8):
        canvas.create_text(buffer, data.height/9+100, text = "Typeface: (1) Helvetica - Sans-serif  (2) Times New Roman - Serif", fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+130, text = "Font Color: (1) Black  (2) Brown  (3) Purple  (4) Green  (5) Yellow  (6) Red", fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+160, text = "Background Color: (1) White  (2) Brown  (3) Purple  (4) Green  (5) Yellow  (6) Red", fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+190, text = '"Correct!" Color: (1) Green  (2) Yellow  (3) Red  (4) Black', fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+220, text = '"Incorrect!" Color: (1) Green  (2) Yellow  (3) Red  (4) Black', fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+250, text = '"Took Too Long!" Color: (1) Green  (2) Yellow  (3) Red  (4) Black', fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+280, text = 'Show Correctness?: (1) Yes  (2) No', fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+310, text = 'Time Warning Color: (1) Red  (2) Black  (3) Green  (4) Yellow', fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+340, text = 'Show UI Elements?: (1) Yes  (2) No', fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
    elif (data.customize == 9):
        canvas.create_text(buffer, data.height/9+100, text = "Typeface: (1) Helvetica - Sans-serif  (2) Times New Roman - Serif", fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+130, text = "Font Color: (1) Black  (2) Brown  (3) Purple  (4) Green  (5) Yellow  (6) Red", fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+160, text = "Background Color: (1) White  (2) Brown  (3) Purple  (4) Green  (5) Yellow  (6) Red", fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+190, text = '"Correct!" Color: (1) Green  (2) Yellow  (3) Red  (4) Black', fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+220, text = '"Incorrect!" Color: (1) Green  (2) Yellow  (3) Red  (4) Black', fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+250, text = '"Took Too Long!" Color: (1) Green  (2) Yellow  (3) Red  (4) Black', fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+280, text = 'Show Correctness?: (1) Yes  (2) No', fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+310, text = 'Time Warning Color: (1) Red  (2) Black  (3) Green  (4) Yellow', fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+340, text = 'Show UI Elements?: (1) Yes  (2) No', fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+370, text = 'Max Rounds: (1) 10  (2) 15  (3) 20  (4) 30  (5) 50', fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
    elif (data.customize == 10):
        canvas.create_text(buffer, data.height/9+100, text = "Typeface: (1) Helvetica - Sans-serif  (2) Times New Roman - Serif", fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+130, text = "Font Color: (1) Black  (2) Brown  (3) Purple  (4) Green  (5) Yellow  (6) Red", fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+160, text = "Background Color: (1) White  (2) Brown  (3) Purple  (4) Green  (5) Yellow  (6) Red", fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+190, text = '"Correct!" Color: (1) Green  (2) Yellow  (3) Red  (4) Black', fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+220, text = '"Incorrect!" Color: (1) Green  (2) Yellow  (3) Red  (4) Black', fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+250, text = '"Took Too Long!" Color: (1) Green  (2) Yellow  (3) Red  (4) Black', fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+280, text = 'Show Correctness?: (1) Yes  (2) No', fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+310, text = 'Time Warning Color: (1) Red  (2) Black  (3) Green  (4) Yellow', fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+340, text = 'Show UI Elements?: (1) Yes  (2) No', fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+370, text = 'Max Rounds: (1) 10  (2) 15  (3) 20  (4) 30  (5) 50', fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+400, text = 'Max Difficulty: (0) 0  (1) 1  (2) 2  (3) 3  (4) 4  (5) 5', fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
    elif (data.customize == 11):
        canvas.create_text(buffer, data.height/9+100, text = "Typeface: (1) Helvetica - Sans-serif  (2) Times New Roman - Serif", fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+130, text = "Font Color: (1) Black  (2) Brown  (3) Purple  (4) Green  (5) Yellow  (6) Red", fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+160, text = "Background Color: (1) White  (2) Brown  (3) Purple  (4) Green  (5) Yellow  (6) Red", fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+190, text = '"Correct!" Color: (1) Green  (2) Yellow  (3) Red  (4) Black', fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+220, text = '"Incorrect!" Color: (1) Green  (2) Yellow  (3) Red  (4) Black', fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+250, text = '"Took Too Long!" Color: (1) Green  (2) Yellow  (3) Red  (4) Black', fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+280, text = 'Show Correctness?: (1) Yes  (2) No', fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+310, text = 'Time Warning Color: (1) Red  (2) Black  (3) Green  (4) Yellow', fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+340, text = 'Show UI Elements?: (1) Yes  (2) No', fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+370, text = 'Max Rounds: (1) 10  (2) 15  (3) 20  (4) 30  (5) 50', fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+400, text = 'Max Difficulty: (0) 0  (1) 1  (2) 2  (3) 3  (4) 4  (5) 5', fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+430, text = 'Starting Difficulty: (0) 0  (1) 1  (2) 2  (3) 3  (4) 4  (5) 5', fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
    elif (data.customize == 12):
        canvas.create_text(buffer, data.height/9+100, text = "Typeface: (1) Helvetica - Sans-serif  (2) Times New Roman - Serif", fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+130, text = "Font Color: (1) Black  (2) Brown  (3) Purple  (4) Green  (5) Yellow  (6) Red", fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+160, text = "Background Color: (1) White  (2) Brown  (3) Purple  (4) Green  (5) Yellow  (6) Red", fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+190, text = '"Correct!" Color: (1) Green  (2) Yellow  (3) Red  (4) Black', fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+220, text = '"Incorrect!" Color: (1) Green  (2) Yellow  (3) Red  (4) Black', fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+250, text = '"Took Too Long!" Color: (1) Green  (2) Yellow  (3) Red  (4) Black', fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+280, text = 'Show Correctness?: (1) Yes  (2) No', fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+310, text = 'Time Warning Color: (1) Red  (2) Black  (3) Green  (4) Yellow', fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+340, text = 'Show UI Elements?: (1) Yes  (2) No', fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+370, text = 'Max Rounds: (1) 10  (2) 15  (3) 20  (4) 30  (5) 50', fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+400, text = 'Max Difficulty: (0) 0  (1) 1  (2) 2  (3) 3  (4) 4  (5) 5', fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(buffer, data.height/9+430, text = 'Starting Difficulty: (0) 0  (1) 1  (2) 2  (3) 3  (4) 4  (5) 5', fill=data.fontColor, font= "%s 18" %data.fonts[data.font], anchor=W)
        canvas.create_text(data.width/2, data.height/9+530, text = "Press Space again to go back to the Main Menu", fill=data.fontColor, font= "%s 28" %data.fonts[data.font])

##################
# helpDDR Mode
##################

def helpDDRMousePressed(event, data):
    data.tableNumber = chooseTable(data)
    data.timeMax = data.tables[data.tableNumber][2]
    data.mode = "playGame"
def helpDDRKeyPressed(event, data):
    data.tableNumber = chooseTable(data)
    data.timeMax = data.tables[data.tableNumber][2]
    data.mode = "playGame"
def helpDDRTimerFired(data):
    pass
def helpDDRRedrawAll(canvas, data):
    canvas.create_rectangle(0,0,data.width,data.height, fill=data.bgColor) # background
    canvas.create_text(data.width/2, data.height/8, text = "Instructions", fill=data.fontColor, 
                       font = "%s 36" %data.fonts[data.font])
    canvas.create_text(data.width/2, data.height*2/8, 
                       text = "A lot of fish with arrows in them are going to pop up.", fill=data.fontColor, font = "%s 18" %data.fonts[data.font])
    canvas.create_text(data.width/2, data.height*3/8, 
                       text = "Concentrate only on the middle fish.", fill=data.fontColor, font = "%s 18" %data.fonts[data.font])
    canvas.create_text(data.width/2, data.height*4/8, 
                       text = "Ignore any other fish!!", fill=data.fontColor, font = "%s 18" %data.fonts[data.font])
    canvas.create_text(data.width/2, data.height*5/8, 
                       text = "If the arrow is pointing left step on the left pad.", fill=data.fontColor, font = "%s 18" %data.fonts[data.font])
    canvas.create_text(data.width/2, data.height*6/8, 
                       text = "If the arrow is pointing right step on the right pad.", fill=data.fontColor, font = "%s 18" %data.fonts[data.font])
    canvas.create_text(data.width/2, data.height*7/8, 
                       text = "Ready? Press any key to play", fill=data.fontColor, font = "%s 24" %data.fonts[data.font])

#################
# helpKey Mode
#################

def helpKeyMousePressed(event, data):
    data.tableNumber = chooseTable(data)
    data.timeMax = data.tables[data.tableNumber][2]
    data.mode = "playGame"
def helpKeyKeyPressed(event, data):
    data.tableNumber = chooseTable(data)
    data.timeMax = data.tables[data.tableNumber][2]
    data.mode = "playGame"
def helpKeyTimerFired(data):
    pass
def helpKeyRedrawAll(canvas, data):
    canvas.create_rectangle(0,0,data.width,data.height, fill=data.bgColor) # background
    canvas.create_text(data.width/2, data.height/8, text = "Instructions", 
                       fill=data.fontColor, font = "%s 36" %data.fonts[data.font])
    canvas.create_text(data.width/2, data.height*2/8, 
                       text = "A lot of fish with arrows in them are going to pop up.", fill=data.fontColor, font = "%s 18" %data.fonts[data.font])
    canvas.create_text(data.width/2, data.height*3/8, 
                       text = "Concentrate only on the middle fish.", fill=data.fontColor, font = "%s 18" %data.fonts[data.font])
    canvas.create_text(data.width/2, data.height*4/8, 
                       text = "Ignore any other fish!!", fill=data.fontColor, font = "%s 18" %data.fonts[data.font])
    canvas.create_text(data.width/2, data.height*5/8, 
                       text = "If the arrow is pointing left press the letter e.", fill=data.fontColor, font = "%s 18" %data.fonts[data.font])
    canvas.create_text(data.width/2, data.height*6/8, 
                       text = "If the arrow is pointing right press the letter i.", fill=data.fontColor, font = "%s 18" %data.fonts[data.font])
    canvas.create_text(data.width/2, data.height*7/8, 
                       text = "Ready? Press any key to play", fill=data.fontColor, font = "%s 24" %data.fonts[data.font])

#################
# playGame Mode
#################

def getPauseTime(data):
    return 1

def checkAnswer(direction, data):
    if (direction == data.tables[data.tableNumber][3]):
        return True
    else: return False

def playGameMousePressed(event, data):
    pass

def playGameKeyPressed(event, data):
    if (event.char == 'e' or False):
        if (checkAnswer("Left",data)):
            data.correct += 1
            data.round += 1
            data.mode = "correctMode"
        else:
            data.incorrect += 1
            data.round += 1
            data.mode = "incorrectMode"
    if (event.char == "i" or False):
        if (checkAnswer("Right",data)):
            data.correct += 1
            data.round += 1
            data.mode = "correctMode"
        else:
            data.incorrect += 1
            data.round += 1
            data.mode = "incorrectMode"

def playGameTimerFired(data):
    data.timeRemaining -= 1
    if (data.timeRemaining < 1):
        data.incorrect += 1
        data.mode = "tooLong"

def drawFishLeft(canvas, x0, y0, x1, y1):
    canvas.create_text(x0,y0,x1,y1, text="E")

def drawFishRight(canvas, x0, y0, x1, y1):
    canvas.create_text(x0,y0,x1,y1, text="I")

def playGameRedrawAll(canvas, data):
    color = "black"
    if (data.timeRemaining > data.timeMax // 2):
        color = "black"
    else: color = data.timeLowColor
    canvas.create_rectangle(0,0,data.width,data.height, fill=data.bgColor) # background
    # UI elements
    canvas.create_text(data.width-buffer-112, data.height-buffer, text="Time Left: " + str(data.timeRemaining), fill=color, anchor=W)
    # always show the time remaning though

    if (data.showUI):
        canvas.create_text(buffer, buffer, text = "Number Correct: " + str(data.correct), fill=data.fontColor, anchor=W)
        canvas.create_text(buffer, buffer+40, text = "Number Incorrect: " + str(data.incorrect), fill=data.fontColor, anchor=W)

    ###############
    # Actual game
    ###############

    # if it's neutral (only 1 fish in the entire matrix)
    if (data.tables[data.level][0] == 1 and data.tables[data.tableNumber][1] == 1):
        if (data.tables[data.tableNumber][3] == "Left"):
            image = data.images[0]
        else: # direction is Right
            image = data.images[1]
        canvas.create_image(data.width/2, data.height/2, image=image)

#######################
# incorrectMode Mode
#######################

def incorrectModeMousePressed(event, data):
    pass
def incorrectModeKeyPressed(event, data):
    pass
def incorrectModeTimerFired(data):
    if (not (data.round <= data.maxRounds)):
        data.mode = "gameOver"
    else:
        data.pauseTime -= 1
        if (data.pauseTime < 1):
            data.pauseTime = getPauseTime(data)
            data.tableNumber = chooseTable(data)
            data.timeRemaining = data.timeMax
            data.mode = "playGame"

def incorrectModeRedrawAll(canvas, data):
    canvas.create_rectangle(0,0,data.width,data.height, fill=data.bgColor)
    text = "Incorrect!"
    if (data.useNotifs):
        canvas.create_text(data.width/2, data.height/2, text = text, fill=data.incorrectColor, font = "%s 72" %data.fonts[data.font])

###################
# correctMode Mode
###################

def correctModeMousePressed(event, data):
    pass
def correctModeKeyPressed(event, data):
    pass
def correctModeTimerFired(data):
    if (not (data.round < data.maxRounds)):
        data.mode = "gameOver"
    else:
        data.pauseTime -= 1
        if (data.pauseTime < 1):
            data.pauseTime = getPauseTime(data)
            data.tableNumber = chooseTable(data)
            data.timeRemaining = data.timeMax
            data.mode = "playGame"

def correctModeRedrawAll(canvas, data):
    canvas.create_rectangle(0,0,data.width,data.height, fill=data.bgColor)
    text = "Correct!"
    if (data.useNotifs):
        canvas.create_text(data.width/2, data.height/2, text = text, fill=data.correctColor, font = "%s 72" %data.fonts[data.font])

####################
# tooLong Mode
####################

def tooLongMousePressed(event, data):
    pass
def tooLongKeyPressed(event, data):
    pass
def tooLongTimerFired(data):
    if (not (data.round < data.maxRounds)):
        data.mode = "gameOver"
    data.pauseTime -= 1
    if (data.pauseTime < 1):
        data.pauseTime = 1
        data.timeRemaining = data.timeMax
        data.mode = "playGame"
def tooLongRedrawAll(canvas, data):
    canvas.create_rectangle(0,0,data.width,data.height, fill=data.bgColor)
    text = "Took Too Long!"
    if (data.useNotifs):
        canvas.create_text(data.width/2, data.height/2, text = text, fill=data.tooLongColor, font = "%s 72" %data.fonts[data.font])

###################
# gameOver Mode
###################

def gameOverMousePressed(event, data):
    data.mode = "mainMenu"
def gameOverKeyPressed(event, data):
    data.mode = "mainMenu"
def gameOverTimerFired(data):
    pass
def gameOverRedrawAll(canvas, data):
    canvas.create_text(data.width/2, data.height/3, text="Finished!", fill=data.fontColor, font = "%s 48" %data.fonts[data.font])
    canvas.create_text(data.width/2, data.height/2, text="Correct: " + str(data.correct), fill=data.fontColor, font = "%s 36" %data.fonts[data.font])
    canvas.create_text(data.width/2, data.height*2/3, text="Incorrect: " + str(data.incorrect), fill=data.fontColor, font = "%s 36" %data.fonts[data.font])


####################################
# use the run function as-is
####################################

def run(width=canvasWidth, height=canvasHeight):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    root = Tk()
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(canvasWidth, canvasHeight)
