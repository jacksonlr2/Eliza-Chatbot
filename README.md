# Eliza Chatbot

## Overview
This program is a simple Eliza implementation. Eliza plays the role of a
psychotherapist that is able to respond to the user's (patient) input.
She will initially greet the user and ask the user their name for a more
personalized experience. She will then take in any statement for the user
and produce a response.
She recognizes if the patient:
 - swears and will discourage it due to her standards of professionalism
 - is ready to go and will say goodbye as well and give the cost for the
   session to make it more realistic
 - talks about their family and will ask how their relationship with them is
   since family members are often brought up in therapy
 - asks a question since statements are different from questions in syntax
 - makes a statement using specific pronouns and helping verbs since and
   it can effect the syntax of the question eliza is able to formulate

## Example:
> **Eliza**: Hi, I'm a psychotherapist. What is your name?
> 
> **Patient (User)**: Lenice
> 
> **Eliza**: Hi Lenice. How can I help you today?
> 
> **Patient (User)**: I love my mom
> 
> **Eliza**: Tell me more about your relationship with your mom.
> 
> **Patient (User)**: Why do I feel this way
> 
> **Eliza**: Sorry, but I will be the one asking the questions.
> 
> **Patient (User)**: I feel sad today
> 
> **Eliza**: Why do you feel sad today?

## Algorithm Overview:
1) Eliza introduces herself and asks for your name. If the user leaves input empty, Eliza will ask again.
2) Eliza greets user and asks how she can help today.
3) User types a statement or question
4) Eliza takes in input and initially checks whether any specific keywords are found (regarding goodbyes, family,
   questions, or swear words). These words will cause Eliza to respond with a special response.
5) Otherwise, she will look at the given pronouns used in the sentence and reformulate it into a question that
   asks "Why ..... (the user's initial input)?"
6) Once a response is given the user can input another response
