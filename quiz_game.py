print("Welcome to my Ultimate Warriors Quiz!")
print("You will be asked 5 questions, and you must answer them all correctly to win.")

playing = input("Do you want to play?Y/n ").lower()

if playing != "yes":
    quit()

print("Okay! Let's play :) ")
score = 0

# Question 1
answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print("correct!")
    score += 1
else:
    print("incorrect!")

# Question 2
answer = input("What does GPU stand for? ").lower()
if answer == "graphics processing unit":
    print("correct!")
    score += 1
else:
    print("incorrect!")

# Question 3
answer = input("What does RAM stand for? ").lower()
if answer == "random access memory":
    print("correct!")
    score += 1
else:
    print("incorrect!")

# Question 4
answer = input("What does ROM stand for? ").lower()
if answer == "read only memory":
    print("correct!")
    score += 1
else:
    print("incorrect!")

# Question 5
answer = input("What does PSU stand for? ").lower()
if answer == "power supply unit":
    print("correct!")
    score += 1
else:
    print("incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")