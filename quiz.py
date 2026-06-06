from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello! Welcome to the quiz!"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

playing = input("Are you ready? ").lower()
if playing != "no":
    print ("Great! Let's get started.")
else:
    print ("Okay, maybe next time!")
    quit()
score = 0

print ("Question 1: What is the capital of France? ")
answer = input('a) Paris\nb) London\nc) Rome\nd) Berlin\n')
if answer == "a":
    print ("Correct!\n")
    score += 1
elif answer == "b":
    print ("Incorrect")
elif answer == " c":
    print ("Incorrect")
elif answer == "d":
    print ("Incorrect")    

print ("Question 2: What is the largest planet in our solar system?")
answer = input('a) Earth\nb) Jupiter\nc) Mars\nd) Saturn\n')
if answer == "a":
    print ("Incorrect")
elif answer == "b":
    print ("Correct!\n")
    score += 1
elif answer == "c":
    print ("Incorrect")
elif answer == "d":
    print ("Incorrect")

print ("Question 3: What is the capital of Japan? ")
answer = input('a) Beijing\nb) Seoul\nc) Tokyo\nd) Bangkok\n')
if answer == "a":
    print ("Incorrect")
elif answer == "b":
    print ("Incorrect")
elif answer == "c":
    print ("Correct!\n")
    score += 1
elif answer == "d":
    print ("Incorrect")    

print ("You got " + str(score) + " questions correct! ")
print (f"Your final score is: {score * 100 / 3:.2f} %")