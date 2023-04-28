#trivia= {
#         "category": "Entertainment: Film",
#         "type": "multiple",
#         "question": "Which of the following is NOT a quote from the 1942 film Casablanca? ",
#         "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
#         "incorrect_answers": [
#             "&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
#             "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
#             "&quot;Round up the usual suspects.&quot;"
import html

trivia= {
        "category": "Entertainment: Television",
        "type": "multiple",
        "question": "What High School is Buffy Summers attend?",
        "correct_answer": "Sunnydale High School",
        "incorrect_answers": [
            "Edison High School;", "Vampire High School;", "Skyhigh High School;",
            ]
        }

question= trivia["question"]
correct= trivia["correct_answer"]
incorrect1= trivia['incorrect_answer'][0]
incorrect2= trivia["incorrect_answer"][1]
incorrect3= trivia["incorrect_answer"][2]

print(question)
print(correct)
print(incorrect1)
print(incorrect2)
print(incorrect3)
        

