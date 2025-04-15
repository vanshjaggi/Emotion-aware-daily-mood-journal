from flask import Flask, request, jsonify
from textblob import TextBlob
from datetime import datetime
import cv2
import numpy as np
from tensorflow.keras.models import load_model
from database import insert_entry
import os

app = Flask(__name__)

face_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')
model = load_model('model/emotion_model.h5')
emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

def predict_emotion():
    cap = cv2.VideoCapture(0)
    detected_emotion = "Unknown"
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray)
        for (x, y, w, h) in faces:
            roi_gray = gray[y:y+h, x:x+w]
            roi_gray = cv2.resize(roi_gray, (48, 48))
            roi = roi_gray.astype("float") / 255.0
            roi = np.reshape(roi, (1, 48, 48, 1))
            preds = model.predict(roi, verbose=0)
            detected_emotion = emotion_labels[np.argmax(preds)]
            break
        break
    cap.release()
    return detected_emotion

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    journal = data.get('journal', '')
    emotion = predict_emotion()
    sentiment = TextBlob(journal).sentiment.polarity
    sentiment_label = "Positive" if sentiment > 0 else "Negative" if sentiment < 0 else "Neutral"

    now = datetime.now()
    insert_entry(now.date().isoformat(), now.strftime("%H:%M:%S"), emotion, sentiment_label, journal)

    return jsonify({
        'emotion': emotion,
        'sentiment': sentiment_label
    })

if __name__ == '__main__':
    app.run(debug=True)
