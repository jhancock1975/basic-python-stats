from random import randint

N = 1000

def simulate(N):
  K = 0;
  for i in range(N):
    
    # hide the prize
    doors = []
    prizeDoor = randint(0,2)
    for i in range(2):
      if i == prizeDoor:
        doors.append('p')
      else:
        doors.append(' ')
    
    # choose the door
    chosenDoor = randint(0,2)
    
    # select door to show
    if (chosenDoor == prizeDoor):
      nonPrizeDoor1 = (prizeDoor + 1)%3
      nonPrizeDoor2 = (prizeDoor + 2)%3
      coin = randint(0,1)
      if (coin == 0):
        shownDoor = nonPrizeDoor1
      else:
        shownDoor = nonPrizeDoor2
    
    elif chosenDoor == 0 and prizeDoor == 2:
      shownDoor = 1
    
    elif chosenDoor == 1 and prizeDoor == 2:
      shownDoor = 0
    
    elif chosenDoor == 2 and prizeDoor == 1:
      shownDoor = 0
    
    elif chosenDoor == 0 and prizeDoor == 1:
      shownDoor = 2
    
    elif chosenDoor == 1 and prizeDoor == 0:
      shownDoor = 2
    
    elif chosenDoor == 2 and prizeDoor == 0:
      shownDoor = 1
      
    if chosenDoor == 0 and shownDoor == 1:
      chosenDoor = 2
    
    elif chosenDoor == 0 and shownDoor == 2:
      chosenDoor = 1
    
    elif chosenDoor == 1 and shownDoor == 0:
      chosenDoor = 2
      
    elif chosenDoor == 1 and shownDoor == 2:
      chosenDoor = 0
    
    elif chosenDoor == 2 and shownDoor == 0:
      chosenDoor = 1
    
    elif chosenDoor == 2 and shownDoor == 1:
      chosenDoor = 0
      
    # check if we won
    if chosenDoor == prizeDoor:
      K = K + 1
        
  return float(K) / float(N)

print simulate(N)
