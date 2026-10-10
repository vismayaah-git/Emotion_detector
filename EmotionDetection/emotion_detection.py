"""Emotion detection using a pretrained Hugging Face Transformer."""

from transformers import pipeline

# Load the pretrained emotion classification model
emotion_classifier = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    top_k=None,
)


def emotion_detector(text_to_analyze):
    """Detect emotions in the given text and return the predictions."""

    predictions = emotion_classifier(text_to_analyze)
    if predictions and isinstance(predictions[0], list):
        predictions = predictions[0]

    result = {}

    for prediction in predictions:
        emotion = prediction["label"].lower()
        score = prediction["score"]
        result[emotion] = score

    # Find the emotion with the highest confidence
    dominant_emotion = max(result, key=result.get)

    result["dominant_emotion"] = dominant_emotion

    return result