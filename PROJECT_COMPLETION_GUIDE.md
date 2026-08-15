# Emotion Detector - Completion Guide

## Goal

Build and submit a Flask web application that accepts text, sends it to the Watson NLP emotion model, returns the five emotion scores and dominant emotion, handles invalid input, includes unit tests, and passes static analysis.

**Local project folder:** `C:\Users\visma\OneDrive\Documents\Github_projects\Emotion_detector`  
**GitHub repository:** `https://github.com/vismayaah-git/Emotion_detector`

## High-level data flow

```text
Browser
  |  text entered by user
  v
Flask route: server.py (/emotionDetector)
  |  validate blank/non-blank input
  v
EmotionDetection.emotion_detection.emotion_detector()
  |  HTTP POST with {"raw_document": {"text": "..."}}
  v
Watson NLP emotion endpoint
  |  JSON response: anger, disgust, fear, joy, sadness
  v
emotion_detector() formats scores + finds dominant emotion
  |  dictionary returned to Flask
  v
server.py creates display message
  |  HTML response
  v
Browser shows emotion scores and dominant emotion
```

## Delivery order

1. Sign in to GitHub and create the empty public `Emotion_detector` repository.
2. Install Git for Windows and confirm `git --version` works in a fresh VS Code terminal.
3. Connect this local project to GitHub and make the first commit.
4. Create the `EmotionDetection` package and implement the Watson NLP request.
5. Format the returned data and calculate the dominant emotion.
6. Make the package importable using `__init__.py`.
7. Add and run unit tests.
8. Add the Flask application and verify it in the browser.
9. Add error handling for the API status code `400` and for blank input.
10. Run Pylint, resolve issues, and save the final output.
11. Push each completed change and the required screenshots to the public GitHub repository.
12. Collect the exact code snippets, terminal output, URLs, and screenshots requested by the assessment.

## Suggested repository layout

```text
 C:\Users\visma\OneDrive\Documents\Github_projects\Emotion_detector/
|-- EmotionDetection/
|   |-- __init__.py
|   `-- emotion_detection.py
|-- static/
|   `-- mywebscript.js
|-- templates/
|   `-- index.html
|-- test_emotion_detection.py
|-- server.py
|-- requirements.txt
`-- README.md
```

## Submission evidence checklist

| Task | What to submit |
| --- | --- |
| 1 | Public GitHub repository URL, with a README that identifies the project. |
| 2 | `emotion_detection.py` code containing `emotion_detector`; terminal output showing import and a successful test call. |
| 3 | Updated formatting code in `emotion_detection.py`; terminal output confirming formatted results. |
| 4 | Public GitHub URL to `EmotionDetection/__init__.py`; terminal output showing `EmotionDetection` imports as a package. |
| 5 | `test_emotion_detection.py`; terminal output showing all tests pass. |
| 6 | `server.py`; screenshot saved as `6b_deployment_test.png` showing the working browser app. |
| 7 | Updated `emotion_detection.py` and `server.py`; screenshot saved as `7c_error_handling_interface.png` showing the blank-input message. |
| 8 | `server.py` configured to run Pylint; terminal output showing a 10.00/10 static-analysis score. |

See [GITHUB_SETUP_GUIDE.md](GITHUB_SETUP_GUIDE.md) for the complete first-time GitHub instructions, [IMPLEMENTATION_PLAN.md](IMPLEMENTATION_PLAN.md) for the development steps, and [SUBMISSION_CHECKLIST.md](SUBMISSION_CHECKLIST.md) for the final evidence collection process.
