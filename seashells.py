import random
import tkinter as tk 
import sys

picked = 0 # yeAh I should fix this
    
def getPipeOp(startseq, endseq):
    operation = [startseq.index(symbol) + 1 for symbol in endseq]   
    return operation

def performPipeOp(startseq, operation):
    endSeq = [startseq[position - 1] for position in operation]
    return endSeq

def generateSOpE():
    start = ["+", "○", "△", "□"]
    end = ["+", "○", "△", "□"]
    random.shuffle(start)
    random.shuffle(end)
    operator = getPipeOp(start, end)
    return start, end, operator

def generateMultiPipePuzzle():
    pass

def randomOperator(correctOp, otherOp = None):
    roperator = [1, 2, 3, 4]
    random.shuffle(roperator)
    while roperator == correctOp:
        random.shuffle(roperator)
    return roperator

def trickierOperator(correctOp, otherOp = None):
    index1 = random.randint(0, 3)
    index2 = random.randint(0, 3)

    while index1 == index2:
        index2 = random.randint(0, 3)

    roperator = correctOp.copy()
    roperator[index1] = correctOp[index2]
    roperator[index2] = correctOp[index1]

    while roperator == otherOp or roperator == correctOp:
        random.shuffle(roperator)
    
    return roperator

def generateOnePipePuzzle():
    start, end, correctOperator = generateSOpE()
    falseO1 = trickierOperator(correctOperator)
    falseO2 = trickierOperator(correctOperator, falseO1)
    options = [falseO1, correctOperator, falseO2]
    random.shuffle(options)
    
    return start, end, correctOperator, options
# 1 point for a correct answer
# -1/2 for a wrong one
# This gives an expected value of 0 for random guesses

def play():
    start, end, correctOperator, options = generateOnePipePuzzle()
    curr_picked = graphicPipe(start, end, options)
    if options[curr_picked] == correctOperator:
        print("Yes! Correct!\n")
        return 1
    else:
        print("Noo, that's wrong.\n")
        return -0.5

def graphicPipe(start, end, options):
    window = tk.Tk()

    startField = tk.Label(
        window,
        text=start,
        width=25,
        height=5,
        bg="blue",
        fg="yellow"
        )
    startField.grid(row =0, column=1, padx=5,pady=5)

    operatorFrame = tk.Frame(window)
    operatorFrame.grid(row=1, column=0, columnspan=3) 
    
    button1 = tk.Button(
        operatorFrame,
        text=options[0],
        width=25,
        height=5,
        bg="blue",
        fg="yellow",
        command = lambda:[choose(0), window.destroy()]
    ).grid(row=0, column=0)

    button2 = tk.Button(
        operatorFrame,
        text=options[1],
        width=25,
        height=5,
        bg="blue",
        fg="yellow",
        command = lambda:[choose(1), window.destroy()]
    ).grid(row=0, column=1)

    button3 = tk.Button(
        operatorFrame,
        text=options[2],
        width=25,
        height=5,
        bg="blue",
        fg="yellow",
        command=lambda:[choose(2), window.destroy()], 
    ).grid(row=0, column=2)

    endField = tk.Label(
        window,
        text=end,
        width=25,
        height=5,
        bg="blue",
        fg="yellow"
        )
    endField.grid(row =2, column=1, padx=5,pady=5)

    window.mainloop()

    return picked

def choose(value):
    global picked
    picked = value

def main():
    #greeting = tk.Label(text="Hello, Tkinter")
    
    points = 0
    playmore = True
    #timeleft = 5*60
    #time = 0 #starttime
    # window = initWindow()
    # initButtons()
    while playmore:# and timeleft > 0:
        turnscore = play()
        points += turnscore
        if turnscore == 0:
            playmore = False
        # time
        #timeleft -= time
    print("You got", points, "points!")


main()