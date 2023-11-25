# QuestGenerator NLP

QuestGenerator NLP is a natural language processing (NLP) based question generator using various Python libraries.

## Features

- **MCQ Generation:** Automatically generate multiple-choice questions.
- **Boolean Question Generation:** Create boolean questions.
- **Short Answer Questions:** Generate short-answer questions.

## Usage

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/sangam2109/Questner-NLP-model.git && Questner-NLP-model

2. Install Dependencies:
    ```bash
    pip install -r requirements.txt
3. Run the Application:
    ```bash
    python app.py


## Example

```
 from main import QGen, BoolQGen

qgen = QGen()
bool_qgen = BoolQGen()

input_text = "Your input text here."

mcq_questions = qgen.predict_mcq({"input_text": input_text, "max_questions": 5})
boolean_questions = bool_qgen.predict_boolq({"input_text": input_text, "max_questions": 3})

```

## Credits

Powered by spaCy, NLTK, Flask, and more.


## Comtributions 
Contributions are welcome! Submit issues or pull requests.




## 🚀 Happy Question Generating! 🚀


Feel free to copy and paste this code block into your README file or Markdown editor.
