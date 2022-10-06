length = 0
width = 0
area = 0
guess = 0

length = int(input("Pick a number to be the lenght: "))
width = int(input("Pick a number to be the width: "))
guess = int(input("what do you think the answer will be ? "))

area = length * width

if guess != area:
  print("THAT IS VEERY WRONG,WHy Did YoU DroP OuT, the correct number was", area)
elif guess == area:
  print("Wow, thats right, you deserve a medal")
