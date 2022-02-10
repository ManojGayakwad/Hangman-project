from replit import clear
import random
stages=['''
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========
''','''
 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========
''','''
 +---+
 |   |
 O   |
/|\  |
     |
     |
=========
''','''
 +---+
 |   |
 O   |
/|   |
     |
     |
=========
''','''
 +---+
 |   |
 O   |
 |   |
     |
     |
=========
''','''
 +---+
 |   |
 O   |
     |
     |
     |
=========
''','''
 +---+
 |   |
     |
     |
     |
     |
=========
''']
end_of_game= False
word_list=["ardvark","baboon","camel"]
chosen_word=random.choice(word_list)
display=[]
word_length=len(chosen_word)
lives=6
for _ in range(word_length):
  display +="_"
print(display)
while not end_of_game:
  guess = input("Guess a letter:").lower()
  clear()
  for position in range(word_length):
    letter =chosen_word[position]
    if letter ==guess:
      display[position]=letter
  if guess not in chosen_word:
    lives-=1
    if lives==0:
      end_of_game=True
      print("You Lose") 
  print(display)
  if "_"not in display:
    end_of_game=True
    print("You Win.")
  print(stages[lives])