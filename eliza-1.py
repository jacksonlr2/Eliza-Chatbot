############################################################################
# eliza.java
############################################################################
#
# This program is a simple Eliza implementation. Eliza plays the role of a
# psychotherapist that is able to respond to the user's (patient) input.
# She will initially greet the user and ask the user their name for a more
# personalized experience. She will then take in any statement for the user
# and produce a response.
# She recognizes if the patient:
#  - swears and will discourage it due to her standards of professionalism
#  - is ready to go and will say goodbye as well and give the cost for the
#    session to make it more realistic
#  - talks about their family and will ask how their relationship with them is
#    since family members are often brought up in therapy
#  - asks a question since statements are different from questions in syntax
#  - makes a statement using specific pronouns and helping verbs since and
#    it can effect the syntax of the question eliza is able to formulate
#
# Example:
# Hi, I'm a psychotherapist. What is your name?
# Lenice
# Hi Lenice. How can I help you today?
# I love my mom
# Tell me more about your relationship with your mom.
# Why do I feel this way
# Sorry, but I will be the one asking the questions.
# I feel sad today
# Why do you feel sad today?
#
# Algorithm Overview:
# 1) Eliza introduces herself and asks for your name. If the user leaves input empty, Eliza will ask again.
# 2) Eliza greets user and asks how she can help today.
# 3) User types a statement or question
# 4) Eliza takes in input and initially checks whether any specific keywords are found (regarding goodbyes, family,
#    questions, or swear words). These words will cause Eliza to respond with a special response.
# 5) Otherwise, she will look at the given pronouns used in the sentence and reformulate it into a question that
#    asks "Why ..... (the user's initial input)?"
# 6) Once a response is given the user can input another response
# _____________________________________________________
# Lenice Jackson
# Last Modified: February 8, 2022
# CMSC 416 Section 001
############################################################################
import re

# global variables
patientName = ''
isIntro = True
isConsulting = True
done = False

swearWords = ["fuck", "shit", "cunt", "wanker", "bastard", "dick", "bitch", "ass"]
endWords = ["bye", "until tomorrow", "take care", "good night", "see you later"]
questionWords = ["who", "where", "when", "why", "what", "which", "how"]
familyWords = ["family", "mother", "father", "mom", "dad", "brother", "sister", "son", "daughter", "spouse", "husband",
               "wife", "sibling", "siblings", "brothers", "sisters", "sons", "daughters"]

# looks for name of patient
def get_name(string):
    global patientName
    if string:
        if re.search(r"am|I'm|is", string, re.IGNORECASE):
            patientName = re.search(r"(am|I'm|is)\s(\w+)", string, re.IGNORECASE).group(2)
        else:
            patientName = re.search(r"(\w+)", string).group(1)
    print_intro()

# print greeting to patient
def print_intro():
    global isIntro
    if patientName == "":
        print("Sorry, I didn't quite catch that. What is your name?")
    else:
        isIntro = False
        print("Hi " + patientName + ". How can I help you today?")

# flips the position of a helping verb with pronoun
def flip_pronoun_verb(updatedString):
    temp = updatedString[0]
    updatedString[0] = updatedString[1]
    updatedString[1] = temp.lower()
    return " ".join(updatedString)

# flips the position of a helping verb with possessive pronoun
def flip_possessive_verb(updatedString):
    temp = updatedString[0]
    updatedString[0] = updatedString[2]
    updatedString[2] = temp.lower()

    temp = updatedString[1]
    updatedString[1] = updatedString[2]
    updatedString[2] = temp.lower()
    return " ".join(updatedString)


# switch between first and second person (vice versa)
def changepronouns(updatedString):
    for i, word in enumerate(updatedString):
        if word.lower() == "i":
            updatedString[i] = "you"
        elif word.lower() == "you":
            updatedString[i] = "I"
        elif word.lower() == "my":
            updatedString[i] = "your"
        elif word.lower() == "your":
            updatedString[i] = "my"
        elif word.lower() == "me":
            updatedString[i] = "you"
        elif word.lower() == "mine":
            updatedString[i] = "yours"
        elif word.lower() == "yours":
            updatedString[i] = "mine"
        elif word.lower() == "myself":
            updatedString[i] = "yourself"
        elif word.lower() == "yourself":
            updatedString[i] = "myself"
        elif word.lower() == "we":
            updatedString[i] = "you guys"
        elif word.lower() == "us":
            updatedString[i] = "you guys"
        elif word.lower() == "our":
            updatedString[i] = "your"
        elif word.lower() == "ours":
            updatedString[i] = "yours"
        elif word.lower() == "ourselves":
            updatedString[i] = "yourselves"

    return " ".join(updatedString)

# check patient input to formulate a reply
def check_string(statement):
    # global swearWords
    global isConsulting
    global done

    # check for swearing
    for swearWord in swearWords:
        regexStr = r".*" + re.escape(swearWord) + r".*"
        if re.search(regexStr, statement, re.IGNORECASE):
            done = True
            print("Please do not swear. Take a deep breathe and try again.")

    # check whether a question is asked
    for questionWord in questionWords:
        regexStr = r"^" + re.escape(questionWord) + r"\s(.*)"
        if not done and re.search(regexStr, statement, re.IGNORECASE):
            done = True
            print("Sorry, but I will be the one asking the questions.")

    # check for comment about family member
    for familyWord in familyWords:
        regexStr = r".*" + re.escape(familyWord) + r".*"
        if not done and re.search(regexStr, statement, re.IGNORECASE):
            done = True
            print("Tell me more about your relationship with your " + familyWord + ".")

    # check for goodbyes
    for endWord in endWords:
        regexStr = r".*" + re.escape(endWord) + r".*"
        if not done and re.search(regexStr, statement, re.IGNORECASE):
            isConsulting = False
            done = True
            print("See you next time. The cost for today's visit is $50.")

    # STANDARD TRANSFORMATIONS

    # if you is used, Eliza will shift focus
    if not done and re.search(r"You(.*)", statement, re.IGNORECASE):
        print("This session isn't about me. Let's focus on you.")

    # first person pronoun transformations
    elif not done and re.search(r"I am|I'm\s(.*)", statement, re.IGNORECASE):
        x = re.search(r"(I am|I'm)\s(.*)", statement, re.IGNORECASE).group(2)
        x = re.sub(r'[^\w\s]', '', x)
        x = changepronouns(x.split())
        print("Why are you " + x + "?")
    elif not done and re.search(r"I\s(.*)", statement, re.IGNORECASE):
        finalstatement = ""
        if not done and re.search(r"I\s(do|can|did|had|have|may|should|was|will|might|must|could|would)(.*)", statement, re.IGNORECASE):
            x = re.search(r"I\s(do|can|did|had|have|may|should|was|will|might|must|could|would)(.*)", statement, re.IGNORECASE)
            group1 = re.sub(r'[^\w\s]', '', x.group(1))
            group2 = re.sub(r'[^\w\s]', '', x.group(2))
            finalstatement = changepronouns(group1.split()) + " you " + changepronouns(group2.split())
        elif not done:
            x = re.search(r"I\s(.*)", statement, re.IGNORECASE).group(1)
            x = re.sub(r'[^\w\s]', '', x)
            x = changepronouns(x.split())
            finalstatement = "do you " + x

        print("Why " + finalstatement + "?")

    # Possessive pronoun transformations
    elif not done and re.search(r"(Our|My|His|Her|Their)\s(.*)", statement, re.IGNORECASE):
        x = re.search(r"(Our|My|His|Her|Their)\s(.*)", statement, re.IGNORECASE).group()
        x = re.sub(r'[^\w\s]', '', x)
        x = flip_possessive_verb(x.split())
        x = changepronouns(x.split())
        print("Why " + x + "?")

    # third person pronoun transformations
    elif not done and re.search(r"(She|He|It|They|We)\s(.*)", statement, re.IGNORECASE):
        x = re.search(r"(She|He|It|They|We)\s(.*)", statement, re.IGNORECASE).group()
        x = re.sub(r'[^\w\s]', '', x)
        x = flip_pronoun_verb(x.split())
        x = changepronouns(x.split())
        print("Why " + x + "?")

    # response for anything that eliza isn't able to process
    else:
        if not done:
            print("I didn't quite understand, can you say that another way?")

    done = False


# start of program
print("Hi, I'm a psychotherapist. What is your name?")

# Goes through initial introductions
while isIntro:
    firstString = input()
    get_name(firstString)

# takes in patient's response and generates a reply
while isConsulting:
    inputString = input()
    check_string(inputString)