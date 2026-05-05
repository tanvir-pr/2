## Cursor Cloud specific instructions

This is a minimal automation-support repository ("Daily Push Repo"). There is **no application code**, no dependencies, no build steps, and no services to run.

### Repository purpose

The repo exists solely for automated daily GitHub push activity. The file `GitHub-Push-Automation/daily-fullstop.txt` is updated (with a `.` character) by external automation when there are no other commits that day.

### Key facts for agents

- **No package manager / dependencies**: There is no `package.json`, `requirements.txt`, or any dependency file. No install step is needed.
- **No build / lint / test**: There are no build scripts, linters, or test suites. Standard commands like `npm test` or `make` do not apply.
- **No services**: There are no servers, databases, or background processes to start.
- **Automation runs externally**: The daily-push automation scripts live outside this repository (per `README.md`).
- **"Hello world" task**: The core action for this repo is appending to or updating `GitHub-Push-Automation/daily-fullstop.txt` and pushing the change — that is the entire workflow.
