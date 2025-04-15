# 🧠 Emotion-Aware Daily Mood Journal

This project integrates **real-time emotion detection** using a webcam with a **mood journal** powered by **sentiment analysis**. It helps users track their daily emotions through facial expression recognition (OpenCV and CNN) and sentiment analysis (TextBlob), providing insights into their emotional well-being over time.

### 🛠 Software Used:
- Python 3.x
- OpenCV
- TensorFlow/Keras
- TextBlob
- Flask
- Streamlit
- SQLite

---

## 📁 Project Structure

```
emotion-aware-journal/
│
├── haarcascade/
│   └── haarcascade_frontalface_default.xml
│
├── model/
│   └── emotion_model.h5
│
├── app.py
├── database.py
├── frontend.py
├── main.py
├── requirements.txt
└── README.md
```

---

## 📦 Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/vanshjaggi/Emotion-aware-daily-mood-journal.git
cd Emotion-aware-daily-mood-journal
```

### Step 2: Create a Virtual Environment

```bash
python -m venv venv
# Activate it:
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🧠 Set Up the Database

```bash
python database.py
```

This will initialize the SQLite database for storing journal entries.

---

## ▶️ Run the Application

### Start Backend (Flask)

```bash
python app.py
```

### Start Frontend (Streamlit)

```bash
streamlit run frontend.py
```

---

## 📊 Emotion Detection

Real-time facial emotion detection uses a CNN model trained on the FER-2013 dataset:

- Happy
- Sad
- Angry
- Neutral
- Fear
- Surprise
- Disgust

Facial features are detected using Haar Cascades (`haarcascade_frontalface_default.xml`), and the CNN model (`emotion_model.h5`) classifies the emotion.

---

## 🧪 Dataset Used

- FER-2013: [Download from Kaggle](https://www.kaggle.com/datasets/msambare/fer2013)

---

## ✅ Use Cases

- Daily mood logging
- Early mental health detection
- Emotion-aware journaling
