import random
import hangman_art
import hangman_words
chosen_word = random.choice(hangman_words.word_list)
user_input = []
lives = 5 
for _ in chosen_word:
    user_input += "-"
end_of_game = False
is_found = False
while not end_of_game:
    is_found = False
    guess = input("Guess a letter: ").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            is_found = True
            user_input[position] = letter
    if not is_found:
        print(hangman_art.stages[lives])
        lives -= 1
    print(user_input)
    if lives < 0:
        end_of_game = True
        print("You Lose!")
        print(f"That was {chosen_word}")
    if "-" not in user_input:
        end_of_game = True
        print("You Win!")
