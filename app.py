from flask import Flask, request, render_template
import os
import joblib

app = Flask(__name__)

MODEL_DIR = 'model_files'
model_path = os.path.join(MODEL_DIR, 'sentiment_model.pkl')
vectorizer_path = os.path.join(MODEL_DIR, 'tfidf_vectorizer.pkl')

model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)

@app.route('/', methods=['GET', 'POST'])
def index():
    sentiment = None
    input_text = ""
    if request.method == 'POST':
        input_text = request.form['text']
        if input_text.strip():
            text_tfidf = vectorizer.transform([input_text])
            prediction = model.predict(text_tfidf)[0]
            sentiment = prediction
    return render_template('index.html', sentiment=sentiment, input_text=input_text)

if __name__ == '__main__':
    app.run(debug=True)
