import random
choice = ['rock','paper','scissors']

while True:
    
  times = int(input("Enter number of times you want to play : "))
  tab = {'Player':0, 'Computer':0}
  for i in range(0,times):
      
    x = input("Enter choice [rock (r), paper (p), scissors (s)] : ")
    rng = random.randint(0,2)
    comp = choice[rng]
    
    print("\nYour choice :",x)
    print("Computer :",comp)
    print()
    
    if x == 'r' and rng == 0 or x == 'p' and rng == 1 or x == 's' and rng == 2:
        print("Result : It's a tie!")
             
    if x == 'r' and rng == 1 or x == 'p' and rng == 2 or x == 's' and rng == 0:
        tab['Computer'] = tab['Computer'] + 1
        print("Result : Computer wins!")
        
    if x == 'r' and rng == 2 or x == 'p' and rng == 0 or x == 's' and rng == 1:
        tab['Player'] = tab['Player'] + 1
        print("Result : You win!")
            
    for i in tab:
        print(i,tab[i])
        
  again = input("Play again? (Y/N) : ")
  if again == 'N' or again == 'n':
        break
    