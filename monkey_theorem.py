import random
# write a program
def generateOne(strlen):
    alphabet = 'abcdefghijklmnopqrstuvwxyz '
    res=""
    for i in range(strlen):
        res = res+alphabet[random.randrange(27)]
    return res

def score(goal, teststring):
    numsame=0
    for i in range(len(goal)):
        if goal[i] == teststring[i]:
            numsame += 1
    
    return numsame/len(goal)

def main():
    goalstring = 'methinks it is like a weasel'
    newstring = generateOne(28)
    newscore = score(goalstring, newstring)
    best = 0
    while newscore < 1:
        if newscore > best:
            print(newscore, newstring)
            best = newscore
        newstring = generateOne(28)
        newscore = score(goalstring, newstring)

main()


        


