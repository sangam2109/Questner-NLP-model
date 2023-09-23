from flask import Flask, request, jsonify, render_template
from main import QGen, BoolQGen

app = Flask(__name__)

qgen = QGen()  # Initialize your question generation class
bool_qgen = BoolQGen()  # Initialize your boolean question generation class

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_questions', methods=['GET', 'POST'])
def generate_questions():
    if request.method == 'POST':
        try:
            data = request.get_json()
            input_text = data['input_text']
            max_questions = data.get('max_questions', 4)
            question_type = data.get('question_type', 'mcq')  # Default to MCQ generation

            if question_type == 'mcq':
                questions = qgen.predict_mcq({"input_text": input_text, "max_questions": max_questions})
            elif question_type == 'boolean':
                questions = bool_qgen.predict_boolq({"input_text": input_text, "max_questions": max_questions})
            elif question_type == 'short':
                questions = qgen.predict_shortq({"input_text": input_text, "max_questions": max_questions})

            return jsonify({"questions": questions})

        except Exception as e:
            return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
