# Emotion Detector

## Project Overview

This project analyzes text with a pretrained Hugging Face deep-learning model and the interface uses Streamlit and Python.

Enter text to see the predicted dominant emotion and scores for all emotions.

## Model

The project uses the pretrained `j-hartmann/emotion-english-distilroberta-base` model from Hugging Face.

The model analyzes the given text and predicts the most likely emotion.

## Emotion Detection

The application can detect emotions such as:

- Joy
- Sadness
- Anger
- Fear
- Disgust
- Surprise
- Neutral

## Application

The Streamlit application allows users to:

- Enter a passage
- See the dominant emotion
- View the model's emotion scores

## Testing

The project uses Pytest for automated testing.

Tests are included for:

- Joy
- Sadness
- Anger
- Fear
- Disgust

## Technologies Used

- Python
- Streamlit
- Hugging Face Transformers
- PyTorch
- Pytest

## Project Structure

```text
Emotion_detector/
│
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
│
├── requirements.txt
├── README.md
├── app.py
├── test_emotion_detection.py
└── .gitignore
```

## How to Run

1. Create a virtual environment

```powershell
python -m venv .venv
```

2. Activate the virtual environment

```powershell
.venv\Scripts\Activate.ps1
```

3. Install the required libraries

```powershell
pip install -r requirements.txt
```

4. Run the Streamlit application

```powershell
streamlit run app.py
```

5. Streamlit opens the application in your browser. Enter text and choose **Analyze**.

## Testing

Run the automated tests using:

```powershell
pytest
```

## Project Outcome

Built a Python Streamlit application that uses deep learning with a pretrained Transformer model to classify text into seven emotion categories. The app displays the dominant emotion and a score chart for all categories, and the emotion detection function is covered by five automated tests.
```
