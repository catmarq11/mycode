# Return unique answers based on the input provided... multiple results should be possible.
# AS BEST YOU'RE ABLE, control for user errors (suggested: methods, try/except, while loop)
# Use at least one while loop.
# Make all code "your own."
# ROUGH minimum of 40 lines of code... if code is spread out across multiple files, they are cumulative.


trivia = [
    {
        "question0": "What year was the Labyrinth released?",
        "options": ["1982", "1984", "1986", "1988"],
        "answer": "1986"
    },
    {
        "question1": "Who played the main character, Sarah?",
        "options": ["Jennifer Aniston", "Jennifer Lawrence", "Jennifer Tilly", "Jennifer Connelly"],
        "answer": "Jennifer Connelly"
    },
    {
        "question2": "David Bowie plays the Goblin King, what is his name?",
        "options": ["Jared", "Goblin King", "Sir Didymus", "Jareth"],
        "answer": "Jareth"
    },
    {
        "question3": "Who directed the film the Labyrinth",
        "options": ["Jim Henson", "Steven Spielberg", "George Lucas", "David Bowie"],
        "answer": "Jim Henson"
    },
    {
        "question4": "What is the name of Sarah's baby brother?",
        "options": ["Tommy", "Timmy", "Toby", "Tiny"],
        "answer": "Toby"
    },
    {
        "question5": "What is the name of the guide in the Labyrinth?",
        "options": ["Huggle", "Hogwart", "Hoggle", "Huggie"],
        "answer": "Hoggle"
    },
    {
        "question6": "Who is Merlin?",
        "options": ["A dog", "Magical Fairy", "Grand Wizard", "Teddy Bear"],
        "answer": "A dog"
    },
    {
        "question7": "How does Ludo help Sarah?",
        "options": ["Calls for help", "Calls for rocks", "Calls for peace", "Calls for backup"],
        "answer": "Calls for rocks"
    },
    {
        "question8": "What is the name of Sir Didymus's dog?",
        "options": ["Lancelot", "Merlin", "Guinevere", "Ambrosius"],
        "answer": "Ambrosius"
    },
    {
        "question9": "What does Sarah say to defeat the Goblin King?",
        "options": ["I will defeat you", "I will marry you", "You have no power over me", "You win, keep my brother"],
        "answer": "You have no power over me"
    },
]

def labyrinth_game(trivia) :
    score = 0
    # ask questions
    for question in trivia:
        print(question[list(question.keys())[0]])
        options = question["options"]
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")
        player_answer = int(input("Enter your answer (1-4): "))
        if options[player_answer-1] == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect! The correct answer is {question['answer']}")
    print(f"Your final score is {score} out of {len(trivia)}.")    

labyrinth_game(trivia)
