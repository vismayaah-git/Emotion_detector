# Emotion Detector

Repository: `https://github.com/vismayaah-git/Emotion_detector`

Emotion Detector is a Flask web application that analyzes text using the Watson NLP emotion model. It returns scores for anger, disgust, fear, joy, and sadness, then identifies the dominant emotion.

## Run locally

Open this folder in VS Code, then select **Terminal** > **New Terminal** and use the **PowerShell** profile. Create and activate a virtual environment if you have not already done so:

```powershell
cd "C:\Users\visma\OneDrive\Documents\Github_projects\Emotion_detector"
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install requests flask pylint
python server.py
```

If PowerShell blocks activation, run `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` in that terminal and then run `.venv\Scripts\Activate.ps1` again.

Open the local Flask address shown in the terminal and submit a sentence for analysis.

## Test and analyze

```powershell
python -m unittest test_emotion_detection.py
python -m pylint server.py
```

## Publish to GitHub

For first-time GitHub setup and publishing instructions, read [GITHUB_SETUP_GUIDE.md](GITHUB_SETUP_GUIDE.md).
