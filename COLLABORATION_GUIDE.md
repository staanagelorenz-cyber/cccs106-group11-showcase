# CCCS 106: Collaborative Git Workflow & Branching Reference

Camarines Sur Polytechnic Colleges - College of Computer Studies  
**Course:** CCCS 106: Application Development and Emerging Technologies  
**Week 2 Reference Material**

---

## 1. Collaborative Git Architecture

In modern software development teams, developers never push untested code directly to the production branch (`main`). Instead, teams use **Feature Branching**:

```text
[Remote: origin/main]  ─────────────────────────────────────────────────────────────► (Production)
                               ▲                               ▲                    ▲
                               │ Merge (PR)                    │ Merge (PR)         │ Merge (PR)
[Branch: feature/dev1-profile] ┴──────────────                 │                    │
   (Dev 1: UI & Profile Cards)                                 │                    │
                                                               │                    │
[Branch: feature/dev2-state]   ────────────────────────────────┴──────────          │
   (Dev 2: Reactive State & Counters)                                               │
                                                                                    │
[Branch: feature/dev3-features]─────────────────────────────────────────────────────┴─
   (Dev 3: Sprint Goal Milestones & Theme)
```

### The Three Core Rules of Team Version Control:
1. **Never commit broken code to `main`:** The `main` branch must always remain runnable and testable.
2. **Work in dedicated feature branches:** Name branches descriptively using prefixes: `feature/<feature-name>`, `fix/<issue-name>`, `docs/<topic>`.
3. **Pull before you push:** Always synchronize with the upstream repository before beginning work or publishing changes (`git pull origin main`).

---

## 2. Conventional Commit Standards

Clear commit logs ensure auditability, make debugging straightforward, and facilitate peer review. Use the following structured commit syntax:

```text
<type>(<scope>): <short imperative summary>
```

### Approved Commit Types:

| Type | When to Use | Example Commit Message |
| :--- | :--- | :--- |
| **`feat`** | Adding a new feature or control | `feat(profile): add developer 1 profile card with avatar` |
| **`fix`** | Bug fix or resolving an error | `fix(counter): prevent negative integer counts on decrement` |
| **`docs`** | Documentation or README changes | `docs(readme): add environment setup instructions for macOS` |
| **`style`** | Code formatting, spacing, missing semicolons | `style(main): format code layout using black formatter` |
| **`refactor`** | Restructuring code without changing behavior | `refactor(team): extract card builder into reusable function` |
| **`chore`** | Updating configuration, `.gitignore`, packages | `chore(deps): update requirements.txt with flet 0.86.5` |

---

## 3. Team Triad Collaboration Protocol (3-Member Groups)

This section details the exact sequence of commands when three developers collaborate on a shared repository across different workstations.

> **GOLDEN RULE:** Only **Developer 1 (Lead)** runs `git init`. Developer 2 and Developer 3 join by running **`git clone`**.

---

### Step 1: Baseline Project Initialization (Partner A / Lead Developer)

```bash
# Initialize local repository (Developer 1 ONLY)
git init

# Verify default branch name is 'main'
git branch -M main

# Stage baseline files (ensuring .gitignore is respected)
git add .

# Create baseline commit
git commit -m "chore(init): baseline repository with modern flet app and verification tool"

# Check status and log
git status
git log --oneline
```

---

### Step 2: Create GitHub Remote & Invite Collaborators (Partner A / Lead Developer)

1. Create a new empty repo on GitHub: `cccs106-group01-showcase` (do NOT add README or .gitignore on GitHub).
2. Go to: **Settings > Collaborators > Add people** and invite Developer 2 and Developer 3.
3. Link the remote and push the initial `main` branch:
   ```bash
   git remote add origin https://github.com/<dev1-username>/cccs106-group01-showcase.git
   git push -u origin main
   ```

---

### Step 3: Clone Repository on Teammate PCs (Partner B & Partner C)

Developer 2 and Developer 3 accept their GitHub email invitations, open their terminals, and **CLONE** (do not run `git init`!):

```bash
# Clone the repository
git clone https://github.com/<dev1-username>/cccs106-group01-showcase.git
cd cccs106-group01-showcase

# Create and activate local virtual environment (.venv)
# (Windows CMD):
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt

# (macOS / Linux):
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Verify workstation diagnostic
python verify_setup.py
```

---

### Step 4: Feature Implementation - Developer 1 (Partner A)

Developer 1 implements the UI card feature in isolation:

```bash
# 1. Create and switch to Developer 1's feature branch
git switch -c feature/dev1-profile

# 2. Modify team_profiles.py (Enter Developer 1's real student profile details & optional photo_url)

# 3. Test your changes locally
flet run main.py

# 4. Stage and commit using Conventional Commits
git add team_profiles.py
git commit -m "feat(profile): integrate developer 1 profile card"

# 5. Switch to main, merge feature, and push to GitHub
git switch main
git merge feature/dev1-profile
git push origin main
```

---

### Step 5: Feature Implementation - Developer 2 (Partner B)

Developer 2 syncs the latest `main`, then implements reactive state logic:

```bash
# 1. Pull the latest main containing Developer 1's work
git switch main
git pull origin main

# 2. Create and switch to Developer 2's feature branch
git switch -c feature/dev2-state

# 3. Update team_profiles.py with Developer 2's profile details & optional photo_url
# 4. In main.py, review and test reactive counter event handlers

# 5. Test your changes locally
flet run main.py

# 6. Stage and commit changes
git add team_profiles.py main.py
git commit -m "feat(state): integrate developer 2 profile and task counter handlers"

# 7. Switch to main, merge, and push to GitHub
git switch main
git merge feature/dev2-state
git push origin main
```

---

### Step 6: Feature Implementation - Developer 3 (Partner C)

Developer 3 syncs the latest `main`, then implements sprint milestone tracker:

```bash
# 1. Pull latest main containing Developer 1 & 2's merged work
git switch main
git pull origin main

# 2. Create and switch to Developer 3's feature branch
git switch -c feature/dev3-features

# 3. Update team_profiles.py with Developer 3's profile details & optional photo_url
# 4. In main.py, test the sprint milestone logic (reaching 5 tasks)

# 5. Test your changes locally
flet run main.py

# 6. Stage and commit changes
git add team_profiles.py main.py
git commit -m "feat(milestone): integrate developer 3 profile and sprint goal milestone badge"

# 7. Switch to main, merge, and push to GitHub
git switch main
git merge feature/dev3-features
git push origin main
```

---

### Step 7: Final Team Sync & Unified Graph Audit

All three team members run `git pull` on their respective workstations to synchronize the completed triad project:

```bash
git switch main
git pull origin main

# Audit full 3-developer commit graph
git log --oneline --graph --all

# Commit and push laboratory verification screenshots
git add screenshots/
git commit -m "docs(screenshots): add laboratory verification proofs"
git push origin main
```

---

## 4. Handling & Resolving Merge Conflicts

A merge conflict occurs when two branches modify the **same line** of a file differently.

### How Git Highlights Conflicts:

```python
<<<<<<< HEAD (Current branch: main)
tasks_completed_count = 10
=======
tasks_completed_count = 25
>>>>>>> feature/dev2-stats (Incoming branch)
```

### Step-by-Step Conflict Resolution Workflow:

1. **Identify conflicted files:**
   ```bash
   git status
   ```
   Files marked as `both modified` contain conflict markers.

2. **Open the file in VS Code:**
   VS Code provides intuitive merge conflict buttons:
   - *Accept Current Change* (Keeps `HEAD`)
   - *Accept Incoming Change* (Keeps incoming branch)
   - *Accept Both Changes* (Combines both edits)

3. **Manually clean up the file:**
   Remove all marker lines (`<<<<<<<`, `=======`, `>>>>>>>`) and save the file.

4. **Verify application executes without syntax errors:**
   ```bash
   flet run main.py
   ```

5. **Stage and commit the resolution:**
   ```bash
   git add <resolved-file>
   git commit -m "fix(merge): resolve conflict in task counter between main and dev2"
   ```

---

## 5. Simulating Remote Collaboration (GitHub / GitLab)

> **First Time Using GitHub?**
> If you do not have an account yet, create one at [github.com/signup](https://github.com/signup) using your institutional email (`@cspc.edu.ph`) to qualify for free GitHub Student Developer Pack benefits.

When sharing the repository with remote teammates or pushing to GitHub:

### 1. Link Remote Repository:
```bash
git remote add origin https://github.com/<dev1-username>/cccs106-group01-showcase.git
git remote -v
```

### 2. Push Main Branch:
```bash
git push -u origin main
```

### 3. Teammate Clones and Pulls Updates:
```bash
# Clone on teammate's workstation (Developer 2 & 3)
git clone https://github.com/<dev1-username>/cccs106-group01-showcase.git
cd cccs106-group01-showcase

# Set up local environment
python3 -m venv .venv
source .venv/bin/activate     # (or .\.venv\Scripts\Activate.ps1 on Windows)
pip install -r requirements.txt

# Pull future updates from teammates
git pull origin main
```
