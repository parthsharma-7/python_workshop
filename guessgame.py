import random
def guess_no():
 return random.randint(1,100)
target_no=guess_no()
attempts=0
while True:
  user_guess=int(input("guess the no:-"))
  attempts+=1
  if user_guess==target_no:
   print("congrats yoou guess the no",attempts,"attempts")
   break
  elif user_guess>target_no:
    print("guess a lower no")
  else:
    print("guess a higher no")