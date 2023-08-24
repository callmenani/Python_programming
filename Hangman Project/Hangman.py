import random
print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/   ''')
steps = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["harsha", "rupesha", "eedharabhayya", "abhi"]
choosen_word = random.choice(word_list)
length = len(choosen_word)
lives = 7 
blank_list = []
for n in range(length):
        blank_list.append('_')

end_game = False
while not end_game:
    guess_list = input("Enter your guess letter : ")
    for i in range(0,length):
        if guess_list == choosen_word[i]:
            blank_list[i] = choosen_word[i]
    if guess_list not in choosen_word:
         lives -= 1
         print(steps[lives])
    if lives == 0:
        print("You Lost!")

    print(blank_list)
    if '_' not in blank_list:
        end_game = True
        print("Great You Won!")
    if lives == 0:
         end_game = True

