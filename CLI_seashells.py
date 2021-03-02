import random

# She steals seashells by the seashore
# and the shells she steals are seascales, I'm sure.

# Here's a "talent test" which allows you to test how
# quickly you can figure out which operator that's 
# needed to convert one sequence of symbols into 
# another sequence. 

# Run it by typing 'python3 CLI_seashells.py'
# into your terminal.

# GUI (hopefully) to come.

def getPipeOp(startseq, endseq):
    operation = [startseq.index(symbol) + 1 for symbol in endseq]   
    return operation

def performPipeOp(startseq, operation):
    endSeq = [startseq[position - 1] for position in operation]
    return endSeq

def generateOnePipePuzzle():
    start = ["+", "○", "△", "□"]
    end = ["+", "○", "△", "□"]
    random.shuffle(start)
    random.shuffle(end)
    operator = getPipeOp(start, end)
    return start, end, operator

# TODO: 
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

    if roperator == otherOp:
        random.shuffle(roperator)
    
    return roperator

# 1 point for a correct answer
# -1/2 for a wrong one
# This gives an expected value of 0 for random guesses

def play():
    s, e, o = generateOnePipePuzzle()
    print(s)
    print("         ---")
    print(e)
    falseo = trickierOperator(o)
    options = [falseo, o, trickierOperator(o, falseo)]
    random.shuffle(options)
    print(" 1:", options[0], "\n 2:", options[1], "\n 3:", options[2])
    picked = input("Pick one of the operators 1, 2 or 3. \n")
    
    if picked.lower() == "q":
        return 0

    elif options[int(picked) - 1] == o:
        print("Yes! Correct!\n")
        return 1
    else:
        print(options[int(picked) - 1])
        print("Noo, that's wrong.\n")
        return -0.5


def main():
    # TODO: Add timer
    print("You can exit the game at any time by pressing q.")
    points = 0
    playmore = True
    while playmore:
        turnscore = play()
        points += turnscore
        if turnscore == 0:
            playmore = False
        
    print("You got", points, "points!")


main()
