#we need to make a deep copy of the board for the AI, copy allows us to do it
import copy
def is_winner(b):
  #by rows
  for i in range(3):
    if (b[i*3]==b[i*3+1]) and (b[i*3]==b[i*3+2]):
      if b[i*3]!=" ":
          return b[i*3]
  #by columns
  for i in range(3):
    if (b[i]==b[i+3] and b[i]==b[i+6]):
      if b[i]!=" ":
          return b[i]
  #negative slope diagonal
  if b[0]==b[4] and b[0]==b[8] and b[0]!=" ":
      return b[0]
  #positive slope
  if b[2]==b[4] and b[2]==b[6] and b[2]!=" ":
      return b[2]
  return False  
def squares_used(b):
  count=0
  for i in range(9):
    if b[i]!=' ':
      count=count+1
  if count==9 and not is_winner(b):
    print("Draw!")
  return count
  
#could well combine drawing board
def draw_board(b):
  print(b[0]+ " | "+ b[1]+" | "+b[2])
  print("----------")
  print(b[3]+ " | "+ b[4]+" | "+b[5])
  print("----------")
  print(b[6]+ " | "+ b[7]+" | "+b[8])
  print("Squares Occupied:  "+str(squares_used(b)))
b=[" "," "," "," "," "," "," "," "," "]
draw_board(b)
def not_turn(turn):
  if turn=='o':
    return 'x'
  else:
     return 'o'
def make_computer_move(turn):
  for i in range(9):
    boardcopy=copy.deepcopy(b)
    if boardcopy[i]==' ':
      boardcopy[i]=turn
      if is_winner(boardcopy):
        b[i]=turn
        print("AI detected winning move.")
        draw_board(b)
        return is_winner(b)
  for i in range(9):
    boardcopy=copy.deepcopy(b)
    if boardcopy[i]==' ':
      boardcopy[i]=not_turn(turn)
      print("AI is processing...")
      if is_winner(boardcopy):
        b[i]=turn
        print("AI blocked a winner!")
        draw_board(b)
        return is_winner(b)
        # a simple strategy is to always take a corner if they take the 
        #center and visaversa
  if (b[0]=='x' or b[2]=='x' or b[6]=='x' or b[8]=='x') and squares_used(b)==1:
    b[4]='o'
    draw_board(b)
    return is_winner(b)
  if b[3] == ' ' and squares_used(b)==3:
    b[2]='o'
    draw_board(b)
    return is_winner(b)
# default is just take first available square if center is used
  if b[4]==' ':
    b[4] ='o'
    draw_board(b)
    return is_winner(b)
  print("AI made a random move.")
  for i in range(9):
    if b[i]==(" "):
      b[i]=turn
      draw_board(b)
      return is_winner(b)
def make_move(turn):
  x=input("Where does "+turn+" want to move?")
  if b[int(x)-1]!=' ':
    print ("Nice try, cheater!")
  else:
    b[int(x)-1]=turn
  draw_board(b)
  return is_winner(b)
is_done=False
while is_done==False and squares_used(b)<9:
  is_done=make_move("x")
  if is_done==False and squares_used(b)<9:
    is_done=make_computer_move("o")
  elif is_winner(b):
    print("x wins!")
if is_winner(b)=='o':
  print("o wins!")