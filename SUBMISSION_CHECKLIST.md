# Final Submission Checklist

**Local project folder:** `C:\Users\visma\OneDrive\Documents\Github_projects\Emotion_detector`  
**Public repository:** `https://github.com/vismayaah-git/Emotion_detector`

## Before submitting

- [ ] I completed [GITHUB_SETUP_GUIDE.md](GITHUB_SETUP_GUIDE.md) and can open the repository in a private/incognito browser window.
- [ ] Repository is public and opens without sign-in.
- [ ] `README.md` contains the project name and a short description.
- [ ] `EmotionDetection/emotion_detection.py` contains `emotion_detector`.
- [ ] The function returns five emotion values and `dominant_emotion`.
- [ ] `EmotionDetection/__init__.py` makes the module importable.
- [ ] `test_emotion_detection.py` completes successfully.
- [ ] `server.py` runs the Flask application.
- [ ] A normal browser request displays the formatted response.
- [ ] Empty input displays `Invalid text! Please try again!`.
- [ ] `6b_deployment_test.png` shows the working application.
- [ ] `7c_error_handling_interface.png` shows the invalid-input response.
- [ ] Pylint reports 10.00/10 for `server.py`.

## Evidence to paste into the assessment

1. Repository URL.
2. Code snippet and terminal proof for the initial Watson NLP function.
3. Code snippet and terminal proof for the formatted response.
4. Public URL to `EmotionDetection/__init__.py` and package-import output.
5. Unit test file and successful test output.
6. `server.py` code and `6b_deployment_test.png`.
7. Updated client and server code, plus `7c_error_handling_interface.png`.
8. `server.py` static-analysis evidence and the Pylint 10.00/10 output.

## Fast final verification

Run these from the repository root:

```powershell
python -m unittest test_emotion_detection.py
python -m pylint server.py
python server.py
```

With the server running, test one normal sentence and one blank submission in the browser before collecting screenshots.

Finally, publish the completed work:

```powershell
git status
git add .
git commit -m "Complete emotion detector project"
git push
```
