# This is a mini quiz game that i created in order to understand few concepts.
name = input("Enter your name: ")
print("Welcome to my quiz " + name + "!")
desire_play = input("Do you want to play the quiz game, " + name + "? ").lower() # .lower() makes our response case insensitive ex: YES,yEs,yes 
if(desire_play == "yes"):
    print("Let's do it! ")
else:
    print("Goodbye! ")
    quit()
score = 0 # This is to check our score points and begins from 0
question = input("What does AI stand for? ")
if question.lower() == "artificial intelligence":
    print('Correct!')
    score += 1 # For every Response, if it's TRUE, adds a point else adds nothing
else:
    print('Oops, wrong answer!')
    
question = input("Is Claude an example of AI? (yes/no) ")
if question.lower() == "yes":
    print('Correct!')
    score += 1
else:
    print('Oops, wrong answer!')
    
question = input("Will AI replace humans? (yes/no) ")
if question == "yes":
    print('Even though AI is a strong tool, Humans still hold the final say!')
else:
    print('Absolutely right ' + name+ '!' + " Even if AI becomes superintelligence, humans still has to reverify the decision")
    score += 1
    
print("Congrats " + name + "! " + "You earned " + str(score) + "%" + " points") # This is to check our final points gained
