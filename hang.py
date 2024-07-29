import random

topics = {
    "fruits": ["apple", "banana", "cherry", "date", "berry", "fig", "grape", "melon", "kiwi", "plum"],
    "vegetables": ["pea", "bean", "carrot", "corn", "onion"],
    "animals": ["ant", "lion", "cat", "dog", "goat", "frog", "rat", "horse", "bear", "pig"],
    "countries": ["italy", "brazil", "canada", "japan", "egypt", "france", "uk", "russia", "usa"],
    "birds": ["crow", "eagle", "dove", "duck", "sparrow", "owl", "parrot", "bee"]
}

hangman_stages = [
    """
     ------
     |    |
     |
     |
     |
     |
     |
    ---
    """,
    """
     ------
     |    |
     |    O
     |
     |
     |
     |
    ---
    """,
    """
     ------
     |    |
     |    O
     |    |
     |
     |
     |
    ---
    """,
    """
     ------
     |    |
     |    O
     |   /|
     |
     |
     |
    ---
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |
     |
     |
    ---
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   /
     |
     |
    ---
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   / \\
     |
     |
    ---
    """
]

def get_word(topics):
    topic = random.choice(list(topics.keys()))
    word = random.choice(topics[topic])
    return topic, word

def print_dash(word_length):
    return '_' * word_length

def is_found(word, dash):
    if word == dash:
        print("""
     ------
     |            
     |
     |
     |   \O/
     |    |
     |   / \\
    ---
    """)
        print("You won!")
        return True
    return False

def user_guess(guess, word, dash):
    new_dash = list(dash)
    for i in range(len(word)):
        if word[i] == guess:
            new_dash[i] = guess
    return ''.join(new_dash)

def display_hangman(tries):
    print(hangman_stages[tries])

# Main game loop
topic, word = get_word(topics)
word_length = len(word)
max_wrong_guesses = 6
wrong_guesses = 0

print('Topic:', topic)
dash = print_dash(word_length)
print(dash)

while not is_found(word, dash):
    display_hangman(wrong_guesses)
    if wrong_guesses >= max_wrong_guesses:
        print("The word was:", word)
        print("You lost!")
        break

    guess = input('Guess a letter: ').lower()
    if len(guess) == 1 and guess.isalpha():
        if guess in word:
            dash = user_guess(guess, word, dash)
        else:
            wrong_guesses += 1
            print(f"Incorrect guess. You have {max_wrong_guesses - wrong_guesses} guesses left.")
        print(dash)
    else:
        print("Please enter a single alphabetic character.")
