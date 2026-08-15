# GitHub Setup Guide for This Project

Use this guide to publish the local project folder below to your GitHub account.

```text
C:\Users\visma\OneDrive\Documents\Github_projects\Emotion_detector
```

The GitHub username is `vismayaah-git`, so the repository address will be:

```text
https://github.com/vismayaah-git/Emotion_detector
```

## 1. Sign in to GitHub

1. Open [github.com](https://github.com/) in a browser.
2. Select **Sign in**.
3. Sign in to the account with the username `vismayaah-git`.
4. If GitHub asks for email verification or two-factor authentication, complete it before continuing.
5. Confirm the profile name in the upper-right menu says `vismayaah-git`.

## 2. Create an empty repository on GitHub

1. In the upper-right corner of GitHub, select the **+** icon.
2. Select **New repository**.
3. In **Repository name**, enter `Emotion_detector`.
4. Leave **Owner** set to `vismayaah-git`.
5. Optionally enter this description: `A Flask application that detects emotions in text using Watson NLP.`
6. Select **Public**. The Coursera rubric requires public GitHub URLs.
7. Do **not** select **Add a README file**, **Add .gitignore**, or **Choose a license**. These files already exist or will be added from the local project.
8. Select **Create repository**.
9. Keep the new repository page open. Its address should be `https://github.com/vismayaah-git/Emotion_detector`.

## 3. Install Git on Windows

Git is not currently available in the project terminal, so install it before publishing the project.

1. Open [git-scm.com/download/win](https://git-scm.com/download/win).
2. Download and run the current **64-bit Git for Windows Setup** installer.
3. Keep the default selections during installation unless a screen specifically offers to add Git to PATH. Choose the option that allows Git to be used from the command line and third-party software.
4. Finish the installation.
5. Close VS Code completely and reopen it. This refreshes its terminal environment.
6. Open a new PowerShell terminal in VS Code.
7. Run this command:

```powershell
git --version
```

8. Continue only when it prints a version such as `git version 2.x.x`.

9. If VS Code displays a terminal other than PowerShell, select the small arrow beside the **+** button in the terminal panel, choose **Select Default Profile**, select **PowerShell**, then create a new terminal.

## 4. Set your Git identity once

Run these commands in the PowerShell terminal. Replace the email address with the email connected to your GitHub account.

```powershell
git config --global user.name "vismayaah-git"
git config --global user.email "your-github-email@example.com"
```

Check the values:

```powershell
git config --global --list
```

Do not use a password in either command.

## 5. Open the project folder in the terminal

1. In VS Code, select **Terminal** then **New Terminal**.
2. Confirm the terminal path ends with `Emotion_detector`.
3. If it does not, run:

```powershell
cd "C:\Users\visma\OneDrive\Documents\Github_projects\Emotion_detector"
```

4. Confirm the files are visible:

```powershell
Get-ChildItem
```

You should see `README.md` and the project guide files. Later you will also see the Python source folders and files.

If you create the optional Python virtual environment in the implementation plan, activate it in PowerShell with:

```powershell
.venv\Scripts\Activate.ps1
```

Do not use `source .venv/bin/activate`; that command is for macOS/Linux, not Windows PowerShell.

## 6. Protect local-only files before uploading

Create a `.gitignore` file in the project folder before the first upload. It prevents virtual-environment files, Python cache files, and secrets from being published.

Its contents should include:

```gitignore
.venv/
__pycache__/
*.pyc
.env
```

Never upload passwords, API keys, tokens, or files containing them. The Watson endpoint used in this course does not require adding personal credentials to the repository.

## 7. Start Git tracking and make the first commit

Run every command below from the `Emotion_detector` folder, one command at a time.

```powershell
git init -b main
git status
git add .
git status
git commit -m "Initial project setup"
```

What each command does:

| Command | Purpose |
| --- | --- |
| `git init -b main` | Starts Git tracking in this project and names the first branch `main`. |
| `git status` | Shows which files Git sees and which ones are ready to save. |
| `git add .` | Selects all project files, except ignored files, for the next saved version. |
| `git commit -m "Initial project setup"` | Saves the selected files in local Git history. |

If Git says it cannot identify you, repeat Step 4 using the correct name and email, then run the commit command again.

## 8. Connect the local project to your GitHub repository

On the empty GitHub repository page, select the **HTTPS** tab and copy the repository URL. Then run:

```powershell
git remote add origin https://github.com/vismayaah-git/Emotion_detector.git
git remote -v
```

The final command should display the same URL twice: once for fetching and once for pushing.

## 9. Publish the project

Run:

```powershell
git push -u origin main
```

The first push may open a browser window asking you to sign in and authorize Git Credential Manager. Sign in to GitHub as `vismayaah-git`, approve the request, then return to the terminal. Do not enter your GitHub password into the terminal.

When the command finishes without an error, refresh the repository page in the browser. The project files should appear.

## 10. Verify the public repository and required links

1. Open `https://github.com/vismayaah-git/Emotion_detector` in a private/incognito browser window.
2. Confirm that the page opens without being signed in and that `README.md` is visible.
3. After creating the package, open `EmotionDetection/__init__.py` in GitHub.
4. Select the file's **Copy permalink** option, or copy the browser address. This is the URL needed for Task 4.
5. Keep the main repository URL for Task 1.

## 11. Publish later changes

Each time you finish a meaningful part of the project, run:

```powershell
git status
git add .
git commit -m "Describe the completed change"
git push
```

Suggested commit messages:

- `Add emotion detection package`
- `Add formatted emotion response`
- `Add unit tests`
- `Add Flask web interface`
- `Add error handling and static analysis fixes`
- `Add final project screenshots`

After the final push, refresh GitHub and make sure the two required screenshots are present: `6b_deployment_test.png` and `7c_error_handling_interface.png`.

## Common problems

| Problem | What to do |
| --- | --- |
| `git is not recognized` | Close and reopen VS Code after installing Git, then run `git --version` again. |
| `remote origin already exists` | Run `git remote -v`. If it points to the wrong URL, use `git remote set-url origin https://github.com/vismayaah-git/Emotion_detector.git`. |
| Push is rejected because the GitHub repository has a README | This happens if Step 2 was not followed. Use the GitHub page to delete the newly-created README, or ask for help before using any merge command. |
| Authentication fails | Run `git push -u origin main` again and complete browser sign-in. Make sure the browser is signed into `vismayaah-git`. |
| Repository shows as private | Open the repository **Settings**, select **General**, scroll to **Danger Zone**, select **Change visibility**, then choose **Make public** and confirm. |

Official GitHub instructions for these steps are available in [Creating a new repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository) and [Adding locally hosted code to GitHub](https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github).
