import numpy as np
import random
a = np.array(['1','2','3','4','5','6','7','8','9'])
choice = input("Play with Computer (c) or Player (p) : ")

count1 = 0
count2 = 0
p1 = 0
p2 = 1

# print board
def board(a):
    
    print()
    print("     |     |     ")
    print(" ",a[0]," | ",a[1]," | ",a[2]," ") 
    print("_____|_____|_____")
    print("     |     |     ")
    print(" ",a[3]," | ",a[4]," | ",a[5]," ") 
    print("_____|_____|_____")
    print("     |     |     ")
    print(" ",a[6]," | ",a[7]," | ",a[8]," ")

# check winning condition 
def win_condition(b):
    
    if b[0]=='X' and b[1]=='X' and b[2]=='X' or b[0]=='O' and b[1]=='O' and b[2]=='O':
        ret = True
    elif b[3]=='X' and b[4]=='X' and b[5]=='X' or b[3]=='O' and b[4]=='O' and b[5]=='O':
        ret = True
    elif b[6]=='X' and b[7]=='X' and b[8]=='X' or b[6]=='O' and b[7]=='O' and b[8]=='O':
        ret = True
    elif b[0]=='X' and b[3]=='X' and b[6]=='X' or b[0]=='O' and b[3]=='O' and b[6]=='O':
        ret = True
    elif b[1]=='X' and b[4]=='X' and b[7]=='X' or b[1]=='O' and b[4]=='O' and b[7]=='O':
        ret = True
    elif b[2]=='X' and b[5]=='X' and b[8]=='X' or b[2]=='O' and b[5]=='O' and b[8]=='O':
        ret = True
    elif b[0]=='X' and b[4]=='X' and b[8]=='X' or b[0]=='O' and b[4]=='O' and b[8]=='O':
        ret = True
    elif b[2]=='X' and b[4]=='X' and b[6]=='X' or b[2]=='O' and b[4]=='O' and b[6]=='O':
        ret = True
    else:
        ret = False

    return ret
   
board(a)  
while choice == 'c' or choice == 'p':
          
    if p1%2==0:    # turn of player 1
        count1 = 0 
        
        x = int(input("Player 1 enter number: "))
        for k in range(1,len(a)+1):
          if k==x:
            if a[x-1] == 'X' or a[x-1] == 'O':
                break
            else:
                a[x-1] = 'X'
                p1 = p1 + 1
                p2 = p2 + 1
                board(a)
        check = win_condition(a)
        if check == True:
             print("\nPlayer 1 Wins! 🎊🎉")
             break
        for c in a:
            if c=='X' or c=='O':
                count1 = count1 + 1        
            
    elif p2%2==0:  # turn of player 2
      count2 = 0
      
      if choice == 'p':  
        x = int(input("Player 2 enter number: "))
        for k in range(1,len(a)+1):
          if k==x:
            if a[x-1] == 'X' or a[x-1] == 'O':
                break
            else:
                a[x-1] = 'O'
                p1 = p1 + 1
                p2 = p2 + 1 
                board(a)
                
      if choice == 'c': 
        x = random.randint(1,9)
        for k in range(1,len(a)+1):
          if k==x:
            if a[x-1] == 'X' or a[x-1] == 'O':
                break
            else:
                print("\nComputer :",x)
                a[x-1] = 'O'
                p1 = p1 + 1
                p2 = p2 + 1
                board(a)
                
      check = win_condition(a)
      if check == True:
          if choice == 'p':
             print("\nPlayer 2 Wins! 🎊🎉")
             break
          if choice == 'c':
             print("\nComputer Wins! 🎊🎉")
             break
      for c in a:
            if c=='X' or c=='O':
                count2 = count2 + 1
 
    
    if count1 == 9 or count2 == 9:
        print("\nIt's a tie!")
        break