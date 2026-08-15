"""Client for the Watson NLP emotion-prediction service."""

import requests


URL = (
    "https://sn-watson-emotion.labs.skills.network/v1/"
    "watson.runtime.nlp.v1/NlpService/EmotionPredict"
)
HEADERS = {
    "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
}


def _empty_emotion_result():
    """Return the result used when no emotion can be predicted."""
    return {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None,
    }


def emotion_detector(text_to_analyze):
    """Return emotion scores and the dominant emotion for supplied text."""
    payload = {"raw_document": {"text": text_to_analyze}}

    try:
        response = requests.post(URL, headers=HEADERS, json=payload, timeout=20)
    except requests.RequestException:
        return _empty_emotion_result()

    if response.status_code != 200:
        return _empty_emotion_result()

    try:
        emotion_data = response.json()["emotionPredictions"][0]["emotion"]
    except (KeyError, IndexError, TypeError, ValueError):
        return _empty_emotion_result()

    dominant_emotion = max(emotion_data, key=emotion_data.get)
    return {
        "anger": emotion_data["anger"],
        "disgust": emotion_data["disgust"],
        "fear": emotion_data["fear"],
        "joy": emotion_data["joy"],
        "sadness": emotion_data["sadness"],
        "dominant_emotion": dominant_emotion,
    }
