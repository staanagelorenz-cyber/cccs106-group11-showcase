# Laboratory Verification Screenshots

This directory stores the official image proofs for CCCS 106 Laboratory Task 01. All screenshot files must be saved here, committed to the repository, and pushed to GitHub for academic verification.

## Required Screenshot Files

Save all captured images into this directory using the exact filenames listed below:

| Filename | Description | Captured From |
| :--- | :--- | :--- |
| `01_github_collaborators.png` | GitHub Settings > Collaborators showing Developer 1 (Owner), Developer 2, and Developer 3 with accepted statuses. | Browser (GitHub) |
| `02_diagnostic_audit.png` | Terminal output of `python verify_setup.py` showing all 6 checks with green `[PASS]` status. | Terminal / Command Prompt |
| `03_git_status_clean.png` | Terminal output showing `git status` clean working tree and empty `git ls-files .venv`. | Terminal / Command Prompt |
| `04_app_initial_state.png` | Flet desktop application window at startup with 3 cards, counter at 0, and status "In Progress (0/5)". | Flet App Window |
| `05_app_goal_reached.png` | Flet desktop application window with counter at 5, status "SPRINT GOAL MET (5/5)", and button disabled. | Flet App Window |
| `06_app_dark_mode.png` | Flet desktop application window with Dark Mode switch enabled. | Flet App Window |

## Git Commit Protocol

Once all screenshots are saved in this directory, commit and push them to GitHub:

```bash
git add screenshots/
git commit -m "docs(screenshots): add laboratory verification proofs"
git push origin main
```
