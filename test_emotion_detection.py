import unittest
from unittest.mock import Mock, patch

from EmotionDetection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Test formatted emotion results without relying on a live web service."""

    def setUp(self):
        """Replace the external Watson request with a predictable reply."""
        self.request_patcher = patch(
            "EmotionDetection.emotion_detection.requests.post",
            side_effect=self._mock_watson_response,
        )
        self.request_patcher.start()

    def tearDown(self):
        """Restore the real HTTP client after each test."""
        self.request_patcher.stop()

    @staticmethod
    def _mock_watson_response(_url, headers, json, timeout):
        """Create a Watson-shaped response with the expected dominant emotion."""
        del headers, timeout
        emotion_by_text = {
            "I am glad this happened.": "joy",
            "I am very sad about this.": "sadness",
            "I am afraid of the result.": "fear",
            "This makes me angry.": "anger",
            "That is disgusting.": "disgust",
        }
        dominant_emotion = emotion_by_text[json["raw_document"]["text"]]
        emotions = {
            "anger": 0.01,
            "disgust": 0.01,
            "fear": 0.01,
            "joy": 0.01,
            "sadness": 0.01,
        }
        emotions[dominant_emotion] = 0.96
        response = Mock(status_code=200)
        response.json.return_value = {"emotionPredictions": [{"emotion": emotions}]}
        return response

    def test_joy(self):
        result = emotion_detector("I am glad this happened.")
        self.assertEqual(result["dominant_emotion"], "joy")

    def test_sadness(self):
        result = emotion_detector("I am very sad about this.")
        self.assertEqual(result["dominant_emotion"], "sadness")

    def test_fear(self):
        result = emotion_detector("I am afraid of the result.")
        self.assertEqual(result["dominant_emotion"], "fear")

    def test_anger(self):
        result = emotion_detector("This makes me angry.")
        self.assertEqual(result["dominant_emotion"], "anger")

    def test_disgust(self):
        result = emotion_detector("That is disgusting.")
        self.assertEqual(result["dominant_emotion"], "disgust")


if __name__ == "__main__":
    unittest.main()
