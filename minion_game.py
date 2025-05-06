def minion_game(string):
    scorek = 0
    scores = 0
    check = 'AEIOU'
    collect = []
    for i in range(len(string)):
        if string[i] in check:
            scorek += len(string)- i
        else:
            scores += len(string) - i    
    if scorek > scores:
        print("Kevin",scorek)
    elif scorek < scores:
        print("Stuart",scores)
    else:
        print("Draw")                           

#https://www.hackerrank.com/challenges/the-minion-game/problem