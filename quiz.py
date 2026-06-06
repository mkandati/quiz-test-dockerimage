from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# 1. Updated Data Structure to include choice options
QUIZ_DATA = [
    {
        "question": "What is the capital of France?", 
        "options": ["London", "Paris", "Berlin", "Madrid"],
        "answer": "Paris"
    },
    {
        "question": "What is 2 + 2?", 
        "options": ["3", "4", "5", "22"],
        "answer": "4"
    },
    {
        "question": "Which language is primarily used for Android App development?", 
        "options": ["Python", "Swift", "Kotlin", "C++"],
        "answer": "Kotlin"
    }
]

# 2. Updated HTML Template with Radio Buttons
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Multiple Choice Quiz App</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 40px; background: #f0f2f5; color: #333; }
        .card { background: white; padding: 30px; border-radius: 12px; box-shadow: 0 4px 8px rgba(0,0,0,0.05); max-width: 500px; margin: 0 auto; }
        h2 { margin-top: 0; color: #1a1a1a; }
        .option-container { margin: 15px 0; }
        
        /* Style the radio options to look modern */
        .option-label { 
            display: block; 
            padding: 12px; 
            margin: 8px 0; 
            background: #f8f9fa; 
            border: 2px solid #e9ecef; 
            border-radius: 8px; 
            cursor: pointer; 
            transition: all 0.2s ease;
        }
        .option-label:hover { background: #e8f4fd; border-color: #bde0fe; }
        input[type="radio"] { margin-right: 10px; transform: scale(1.2); }
        
        button { background: #007bff; color: white; border: none; padding: 12px 20px; border-radius: 6px; cursor: pointer; width: 100%; font-size: 16px; font-weight: bold; margin-top: 15px; }
        button:hover { background: #0056b3; }
        .score-board { margin-top: 20px; font-size: 14px; color: #6c757d; text-align: center; }
    </style>
</head>
<body>
    <div class="card">
        {% if game_over %}
            <h2 style="text-align: center;">🎉 Quiz Finished!</h2>
            <p style="text-align: center; font-size: 18px;">Your final score is: <strong>{{ score }} / {{ total }}</strong></p>
            <a href="/reset"><button>Play Again</button></a>
        {% else %}
            <h2>Question {{ q_index + 1 }} of {{ total }}</h2>
            <p style="font-size: 18px; font-weight: 500; margin-bottom: 20px;">{{ question }}</p>
            
            <form method="POST" action="/answer">
                <div class="option-container">
                    {% for option in options %}
                        <label class="option-label">
                            <input type="radio" name="user_answer" value="{{ option }}" required>
                            {{ option }}
                        </label>
                    {% endfor %}
                </div>
                <button type="submit">Submit Answer</button>
            </form>
            
            <div class="score-board">Current Score: {{ score }}</div>
        {% endif %}
    </div>
</body>
</html>
"""

game_state = {"q_index": 0, "score": 0}

@app.route('/')
def index():
    q_index = game_state["q_index"]
    if q_index >= len(QUIZ_DATA):
        return render_template_string(HTML_TEMPLATE, game_over=True, score=game_state["score"], total=len(QUIZ_DATA))
    
    current_q = QUIZ_DATA[q_index]
    return render_template_string(
        HTML_TEMPLATE, 
        game_over=False, 
        question=current_q["question"], 
        options=current_q["options"],
        q_index=q_index, 
        score=game_state["score"],
        total=len(QUIZ_DATA)
    )

@app.route('/answer', methods=['POST'])
def answer():
    # Retrieve the selected option
    user_ans = request.form.get('user_answer')
    q_index = game_state["q_index"]
    
    if q_index < len(QUIZ_DATA):
        # Case-sensitive matching ensures exact choice verification
        if user_ans == QUIZ_DATA[q_index]["answer"]:
            game_state["score"] += 1
        game_state["q_index"] += 1
        
    return redirect(url_for('index'))

@app.route('/reset')
def reset():
    game_state["q_index"] = 0
    game_state["score"] = 0
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)