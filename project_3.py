# Hangman game

import random
import hangman_stages
import word_list

#word_list=["apple", "beautiful", "potato", "cheese", "sugar"]
lives=6
chosen_word = random.choice(word_list.word) #take word from the word list 
#print(chosen_word)
display=[]
for i in chosen_word:
    display.append('_')

print(display)

game_over = False
while not game_over:
    guessed_letter= input("Guess a letter:").lower()
    for i in range(len(chosen_word)):
        letter = chosen_word[i]
        if letter==guessed_letter:
            display[i]=guessed_letter
    print(display)
            
    if guessed_letter not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("you lose")
    if '_' not in display:
        game_over = True
        print("you win")
    print(hangman_stages.stages[lives])