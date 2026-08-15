# Detailed Implementation Plan

## 1. Set up GitHub and the local repository

First complete [GITHUB_SETUP_GUIDE.md](GITHUB_SETUP_GUIDE.md), Steps 1-9. This creates the public `https://github.com/vismayaah-git/Emotion_detector` repository and publishes the files from `C:\Users\visma\OneDrive\Documents\Github_projects\Emotion_detector`. Do not create a second repository or initialize a README on GitHub, because this project already includes one locally.

Then create and activate a virtual environment if the course environment does not already provide one. You are using Windows PowerShell, so use the PowerShell commands below.

In VS Code, select **Terminal** > **New Terminal**. In the terminal's profile selector, choose **PowerShell**. Verify that Python is available before continuing:

```powershell
python --version
```

If this command does not show a Python version, install Python for Windows from [python.org/downloads](https://www.python.org/downloads/windows/). During installation, select **Add python.exe to PATH**, then restart VS Code and open a new PowerShell terminal.

```powershell
cd "C:\Users\visma\OneDrive\Documents\Github_projects\Emotion_detector"
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install requests flask pylint
```

If PowerShell says that script execution is disabled, run the following command once in the same terminal, then activate again:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.venv\Scripts\Activate.ps1
```

After activation, the terminal prompt should begin with `(.venv)`. The project folder is already on your computer, so do not run `git clone` for this project. Use the exact `cd` command above whenever a terminal is not already in the project folder.

For reference only: `source .venv/bin/activate` is for macOS/Linux terminals and will not work in PowerShell.

Create the folders and files listed in the project guide. Keep `EmotionDetection` capitalized consistently because its import name is assessed.

## 2. Implement the Watson NLP client

In `EmotionDetection/emotion_detection.py`, import `requests` and define `emotion_detector(text_to_analyze)`.

Use the Watson NLP endpoint, headers, and JSON request body from the course lab:

```python
url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
json = {"raw_document": {"text": text_to_analyze}}
response = requests.post(url, headers=headers, json=json)
```

Do not substitute an endpoint or credentials from an unrelated service.

Before formatting the response, run a direct import-and-call check:

```text
python
>>> from EmotionDetection.emotion_detection import emotion_detector
>>> emotion_detector("I am glad this project is working.")
```

Save the successful terminal output for Task 2.

## 3. Format the return value

Read the JSON returned by the service from `response.json()['emotionPredictions'][0]['emotion']`. Extract the five emotion values: `anger`, `disgust`, `fear`, `joy`, and `sadness`. Determine `dominant_emotion` by selecting the key with the highest score.

Return a dictionary in this shape:

```python
{
    "anger": anger,
    "disgust": disgust,
    "fear": fear,
    "joy": joy,
    "sadness": sadness,
    "dominant_emotion": dominant_emotion,
}
```

Run the function again with text that has a clear emotion and save the terminal output. Check that all five score keys and `dominant_emotion` are present.

## 4. Make the module a package

Create `EmotionDetection/__init__.py` and expose the application module using the import format specified by the course, for example:

```python
from .emotion_detection import emotion_detector
```

Verify package import from the repository root:

```powershell
python -c "from EmotionDetection import emotion_detector; print(emotion_detector('I am happy'))"
```

Push this file to GitHub and copy its public URL for Task 4.

## 5. Add unit tests

Create `test_emotion_detection.py` with `unittest`. Use several short sentences whose expected dominant emotions are clear. For each test, call `emotion_detector()` and compare `result['dominant_emotion']` with the expected label.

Recommended cases:

| Input | Expected dominant emotion |
| --- | --- |
| `I am glad this happened.` | `joy` |
| `I am very sad about this.` | `sadness` |
| `I am afraid of the result.` | `fear` |
| `This makes me angry.` | `anger` |
| `That is disgusting.` | `disgust` |

Run:

```powershell
python -m unittest test_emotion_detection.py
```

Save the command output only after all tests pass.

## 6. Build the Flask interface

In `server.py`, create a Flask app. The `/` route should render `templates/index.html`. The `/emotionDetector` route should accept the text supplied by the existing JavaScript, call `emotion_detector`, and return a readable result.

The response should present the five emotion values followed by the dominant emotion, for example:

```text
For the given statement, the system response is 'anger': 0.01, 'disgust': 0.00,
'fear': 0.00, 'joy': 0.98 and 'sadness': 0.01. The dominant emotion is joy.
```

Use the starter `index.html` and `mywebscript.js` if supplied. Their job is to send the text to the Flask route and insert its response into the result area.

Start the server:

```powershell
python server.py
```

Open the local address printed by Flask, test a normal sentence, and capture the browser as `6b_deployment_test.png`.

## 7. Add error handling

If the Watson request returns status code `400`, `emotion_detector` should return a predictable null result rather than trying to read missing values:

```python
{
    "anger": None,
    "disgust": None,
    "fear": None,
    "joy": None,
    "sadness": None,
    "dominant_emotion": None,
}
```

In `server.py`, detect that null result and return the course-required message:

```text
Invalid text! Please try again!
```

Also handle empty or whitespace-only form input before sending it to the service. Restart Flask, submit a blank field in the browser, and save the result as `7c_error_handling_interface.png`.

## 8. Run static analysis

Run Pylint against `server.py`:

```powershell
python -m pylint server.py
```

Resolve the reported issues rather than hiding them. Common fixes are module/function docstrings, descriptive names, import ordering, spacing, and a final newline. The required final terminal output is a 10.00/10 score.

If the course requires Pylint from within the file, include the approved directive only when it matches the lab instructions; otherwise run it from the terminal.

## 9. Final GitHub and assessment submission

Check that the repository is public and includes the README. Commit and push all relevant source files and the two required screenshots. If this is your first push, follow the GitHub setup guide instead of running only these commands.

```powershell
git add .
git commit -m "Complete emotion detector project"
git push
```

Open the assessment only after all evidence is available. For each activity, submit exactly the requested URL, code snippet, terminal output, or image. Review the evaluator feedback after submission and correct any missed requirement before the deadline.
