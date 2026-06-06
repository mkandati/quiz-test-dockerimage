from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello! Welcome to the quiz!"

def start_game():
    """All of your quiz game logic must live inside this function."""
    playing = input("Are you ready? ").lower()
    if playing == "no":
        print("Okay, maybe next time!")
        return  # Use return instead of quit() so it doesn't crash the test runner
        
    print("Great! Let's get started.")
    score = 0

    # Question 1
    print("Question 1: What is the capital of France? ")
    answer = input('a) Paris\nb) London\nc) Rome\nd) Berlin\n').strip().lower()
    if answer == "a":
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect\n")   

    # Question 2
    print("Question 2: What is the largest planet in our solar system?")
    answer = input('a) Earth\nb) Jupiter\nc) Mars\nd) Saturn\n').strip().lower()
    if answer == "b":
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect\n")

    # Question 3
    print("Question 3: What is the capital of Japan? ")
    answer = input('a) Beijing\nb) Seoul\nc) Tokyo\nd) Bangkok\n').strip().lower()
    if answer == "c":
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect\n")    

    print("You got " + str(score) + " questions correct! ")
    print(f"Your final score is: {score * 100 / 3:.2f} %")


# This block controls what happens when you run this script directly
if __name__ == "__main__":
    # Decide here what you want to happen when you type `python quiz.py`.
    # Currently, it will start the console quiz. If you want to start Flask instead, 
    # comment out start_game() and uncomment app.run().
    
    start_game()
    app.run(host="0.0.0.0", port=5000)