# Nepali Sentiment Analyzer

This is a simple Flask web application that predicts the sentiment of Nepali text as Positive, Negative, or Neutral.
Note *** The model may make mistakes as it is trained on a relatively small dataset (~1000 samples)***

The model uses TF-IDF vectorization and Logistic Regression, trained on Nepali comments and posts collected from Facebook, YouTube, TikTok, news articles, and Twitter.


## Features

- Input Nepali text in the web form  
- Predict sentiment instantly  
- Shows result on the same page  

---

## Project Structure

├── app.py # Flask application code
├── requirements.txt # Python dependencies
├── README.md # documentation
├── model_files/ # Trained model and vectorizer files
│ ├── sentiment_model.pkl
│ └── tfidf_vectorizer.pkl
├── templates/ # HTML files for frontend
│ └── index.html


* Create a virtual environment and activate it:
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate

* Install required packages:
pip install -r requirements.txt
Start the Flask app:

python app.py
Open your browser and visit:

http://127.0.0.1:5000

* How to Use
Enter Nepali text into the input box

 Click Submit

 View the predicted sentiment on the page

* Requirements
  Flask
  scikit-learn
  joblib
