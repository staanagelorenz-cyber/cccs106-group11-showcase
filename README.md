# Laboratory Task: Professional Development Environment Setup & Collaborative Git Workflow

**Institution:** Camarines Sur Polytechnic Colleges  
**College:** College of Computer Studies (CCS)  
**Program:** Bachelor of Science in Computer Science (BSCS)  
**Course Code & Title:** CCCS 106: Application Development and Emerging Technologies  
**Target Term & Week:** 1st Semester | Week 2  
**Lab Duration:** 4 Hours (Hands-On Lab Session)  
**Target Framework:** Python 3.10-3.12 & Flet SDK v0.86.5+ ([Official Docs](https://flet.dev/docs/))  

---

## 1. Laboratory Overview & Desired Learning Outcomes

Software development in modern professional engineering teams requires establishing reproducible, isolated workstations and adhering to disciplined version control practices. Writing production application code without virtual environment isolation risks dependency pollution, while writing code without version control invites catastrophic data loss and collaboration gridlocks.

In this laboratory exercise, you will:
1. Configure an isolated Python development workstation using virtual environments (`venv`).
2. Verify SDK installations using our automated diagnostics pre-flight tool (`verify_setup.py`).
3. Configure Visual Studio Code workspace settings and interpreter paths.
4. Establish repository hygiene by configuring `.gitignore` to prevent tracking virtual environments and binary artifacts.
5. Practice a real-world collaborative Git workflow (branching, conventional commits, merging, and conflict resolution) on a modern cross-platform **Flet v0.86.5** GUI application.

### Alignment with Course & Program Outcomes:
- **CO1 / CI1.1:** Articulate software development lifecycles, version control with Git, and reactive UI architecture in Python using Flet.
- **CO6 / CI6.1:** Utilize Git workflow repositories, code documentation standards, and collaborative team practices in software projects.
- **PO1 / PI1.1:** Formulate computing models and software abstractions using Python and cross-platform application frameworks.

---

## 2. Laboratory Prerequisites & Starter Pack Overview

### System Requirements:
- **Operating System:** Windows 10/11 (64-bit), macOS 12+ (Apple Silicon or Intel), or Ubuntu 20.04+ LTS.
- **Python:** Version 3.10 to 3.12 (Python 3.12 recommended).
- **Git:** Git 2.30+ installed and accessible from your terminal.
- **IDE:** Visual Studio Code with the Python extension installed.

### Workstation Setup: Installing Git (If Missing on Your Machine)

If your lab computer or personal laptop does not have Git installed (or typing `git` in your terminal returns an unrecognized command error), follow the instructions for your operating system:

---

#### Option A: Microsoft Windows (Command Prompt / CMD)

##### Method 1: Instant Installation via Windows Package Manager (Fastest)

Open Command Prompt (CMD) as Administrator and run:

```cmd
winget install --id Git.Git -e --source winget
```

> **IMPORTANT:**
> Once the installation completes, close Command Prompt and open a fresh Command Prompt window so the updated system PATH is recognized.

##### Method 2: Standard Git for Windows Graphical Installer

1. Navigate to: [git-scm.com/download/win](https://git-scm.com/download/win)
2. Download the **64-bit Git for Windows Setup** executable.
3. Run the installer and click **Next** through the setup wizard, ensuring these recommended settings are selected:
   - **Choosing the default editor:** Select *Use Visual Studio Code as Git's default editor*.
   - **Adjusting your PATH environment:** Select *Git from the command line and also from 3rd-party software* (CRITICAL: this makes `git` available in Command Prompt, PowerShell, and VS Code).
   - **Choosing the SSH executable:** Select *Use bundled OpenSSH*.
   - **Configuring the line ending conversions:** Select *Checkout Windows-style, commit Unix-style line endings* (`core.autocrlf = true`).
4. Click **Install**.
5. Close all open Command Prompt / VS Code windows and open a fresh Command Prompt window.

##### Verify Git on Windows:

```cmd
git --version
```

Expected output:
```text
git version 2.4x.x.windows.x
```

---

#### Option B: macOS (Terminal)

##### Method 1: Apple Command Line Developer Tools (Recommended)

macOS includes Git through Apple's developer tools. Open Terminal (`Cmd + Space`, type `Terminal`) and execute:

```bash
xcode-select --install
```

A software update dialog will appear on your screen. Click **Install** and agree to the license terms. macOS will automatically download and install Git.

##### Method 2: Homebrew Package Manager

If you have Homebrew installed on your Mac, run:

```bash
brew install git
```

##### Verify Git on macOS:

```bash
git --version
```

Expected output:
```text
git version 2.xx.x (Apple Git-xxx)
```

---

### Starter Pack Directory Contents:

```text
git_collaboration_workflow/
├── .gitignore                      # Repository exclusion rules (venv, bytecode, OS metadata)
├── .vscode/
│   └── settings.json               # VS Code workspace interpreter and formatting rules
├── assets/                         # Local application assets and student photos
│   ├── dev1.jpg                    # Developer 1 sample photo
│   ├── dev2.jpg                    # Developer 2 sample photo
│   └── dev3.jpg                    # Developer 3 sample photo
├── CCCS106_Lab01_Report_Template.docx # Official Word report template with placeholder boxes
├── COLLABORATION_GUIDE.md          # Quick-reference branching & conventional commit cheatsheet
├── README.md                       # This Laboratory Manual
├── requirements.txt                # Pinned project dependencies (flet>=0.86.5)
├── verify_setup.py                 # Automated pre-flight environment diagnostic tool
├── team_profiles.py                # Team data model & reusable Flet card component builder
├── main.py                         # Collaborative Flet v0.86.5 team showcase application
└── screenshots/                    # Verification screenshots committed and pushed to GitHub
    ├── .gitkeep                    # Directory preservation placeholder
    └── README.md                   # Screenshot naming specifications & commit instructions
```

### Team Distribution Architecture: Lead Inits & Pushes ➔ Teammates Clone

In a real engineering team, **only one developer initializes the repository**. Teammates never run `git init` independently.

```text
  Instructor (LMS / LeOnS / Starter Pack)
             │
             ▼
   [ Developer 1 (Group Lead) ]
      • Downloads starter pack & opens folder
      • Runs `git init` & baseline commit
      • Creates empty GitHub repository
      • Adds Dev 2 & Dev 3 as Collaborators on GitHub
      • Pushes baseline: git push -u origin main
             │
             ├──► PUSHED TO GITHUB ◄──┐
             │                        │
             ▼                        ▼
   [ Developer 2 ]              [ Developer 3 ]
   • Accepts GitHub invite      • Accepts GitHub invite
   • git clone <repo-url>       • git clone <repo-url>
   • Creates .venv & installs   • Creates .venv & installs
   • Works on feature/dev2      • Works on feature/dev3
```

> **IMPORTANT RULE FOR 3-MEMBER TEAMS:**
> - **Developer 1 (Lead)** is the ONLY student who downloads the starter folder from the LMS and runs `git init`.
> - **Developer 2 and Developer 3** must NOT run `git init`. They join the project by **cloning** Developer 1's repository using `git clone <repo-url>` once invited.
> - *(Alternative for Single-PC Lab: If your triad shares 1 physical computer, Developer 1 runs `git init`, and all 3 students take turns on the keyboard switching local branches).*

> [!TIP]
> **Parallel Work for Efficiency:** While Developer 1 completes Phases 4.3 and 4.4 (git init, GitHub repo creation, and push), Developer 2 and Developer 3 should independently complete **Phases 1-3** (venv setup, `verify_setup.py`, and VS Code configuration) on their own workstations. This way, they are immediately ready to clone once Developer 1 shares the repository URL.

---

## 3. Phase-by-Phase Step-by-Step Instructions

### Phase 1: Environment Isolation & Virtual Environment Creation

Select the instructions corresponding to your operating system:

#### Option A: Microsoft Windows (Command Prompt / CMD)

1. Open Command Prompt (CMD) and navigate to this laboratory directory:
   ```cmd
   cd "path\to\git_collaboration_workflow"
   ```

2. Create an isolated virtual environment named `.venv`:
   ```cmd
   python -m venv .venv
   ```

3. Activate the virtual environment (CMD activates instantly without script permission blocks):
   ```cmd
   .venv\Scripts\activate
   ```

4. Confirm that your command prompt begins with `(.venv)`. Then upgrade pip and install dependencies:
   ```cmd
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

---

#### Option B: macOS / Linux (Terminal / Zsh / Bash)

1. Open Terminal and navigate to this laboratory directory:
   ```bash
   cd /path/to/git_collaboration_workflow
   ```

2. Create an isolated virtual environment named `.venv`:
   ```bash
   python3 -m venv .venv
   ```

3. Activate the virtual environment:
   ```bash
   source .venv/bin/activate
   ```

4. Confirm that your terminal prompt begins with `(.venv)`. Then upgrade pip and install dependencies:
   ```bash
   python3 -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

---

### Phase 2: Automated Workstation Pre-flight Verification

Before proceeding, run the automated diagnostic script to verify that your workstation satisfies all engineering criteria:

```bash
python verify_setup.py
```

Expected Output:
```text
============================================================================
      CAMARINES SUR POLYTECHNIC COLLEGES - COLLEGE OF COMPUTER STUDIES
         CCCS 106: WORKSTATION & GIT ENVIRONMENT AUDIT TOOL
============================================================================
Host Operating System : macOS 15.2 (arm64)
Current Working Dir   : .../LearningTasks/git_collaboration_workflow
----------------------------------------------------------------------------
[PASS] 1. Python Version (3.10 - 3.12)     : Python 3.12.x (Target 3.12 Recommended)
[PASS] 2. Virtual Environment (.venv)      : Active Virtualenv: '.venv' (...)
[PASS] 3. Flet SDK (v0.86.5+)              : Flet SDK v0.86.5 installed and operational
[PASS] 4. Git CLI Installation             : git version 2.39.x
[PASS] 5. Git User Configuration           : Configured as 'Juan Dela Cruz' <...>
[PASS] 6. Repository .gitignore Hygiene    : .gitignore detected (blocks .venv/)
============================================================================
🎉 ALL AUDIT CHECKS PASSED!
Your workstation is properly configured and isolated.
You are fully ready to proceed with the Collaborative Git Workflow!
============================================================================
```

> **NOTE:**
> If any test fails, review the remediation guidance printed at the bottom of the report, execute the suggested fix, and re-run `python verify_setup.py`.

---

### Phase 3: Visual Studio Code Configuration

1. Launch VS Code in the project folder:
   ```bash
   code .
   ```
2. Open the Command Palette (`Ctrl+Shift+P` on Windows, `Cmd+Shift+P` on macOS).
3. Type and select: **`Python: Select Interpreter`**.
4. Select the interpreter labeled **`Python 3.12 (.venv): ./.venv/bin/python`** (or `.\.venv\Scripts\python.exe`).
5. Open `.vscode/settings.json` and verify that `python.defaultInterpreterPath` is set correctly.

---

### Phase 4: Git Repository Initialization & Baseline Commit

#### 4.1 First-Time Setup: Creating a GitHub Account (If You Don't Have One)

If you do not have a GitHub account yet, complete these setup steps before initializing Git:

1. **Sign Up at GitHub:**
   - Navigate to [github.com/signup](https://github.com/signup) in your browser.
   - Enter your email address and create a strong password.

> **TIP - Use Your CSPC Institutional Email:**
> Register using your official CSPC student email (`@cspc.edu.ph`). This automatically qualifies you for the **GitHub Student Developer Pack** (free GitHub Pro tier, GitHub Copilot access, cloud student credits, and free domain/tool vouchers).

2. **Choose a Professional Username:**
   - Select a clean handle suitable for academic audits and future software industry portfolios (e.g., `juandelacruz`, `jdelacruz-cspc`, or `maria-santos`).

3. **Verify Your Email:**
   - Check your CSPC student email inbox and click the verification link sent by GitHub.

4. **Authentication Note (Personal Access Tokens / Git Credential Manager):**
   - GitHub no longer permits using account passwords for terminal Git CLI pushes. When you push to GitHub (in Phase 6), you will authenticate seamlessly via **Git Credential Manager** (a browser popup) or a **Personal Access Token (PAT)** generated under *GitHub > Settings > Developer Settings > Personal Access Tokens*.

---

#### 4.2 Configure Local Git User Identity

Configure your Git user identity in your terminal. **Crucial:** Use the **exact same name and email address** registered on your GitHub account so that your commits are credited to your GitHub profile and activity heatmap:

```bash
# Set your full name
git config --global user.name "Your Full Name"

# Set your registered GitHub email (e.g. CSPC institutional email)
git config --global user.email "your.email@cspc.edu.ph"

# Set the default initial branch name to 'main'
git config --global init.defaultBranch main

# Verify your Git configuration
git config --list
```

---

#### 4.3 Developer 1 (Group Lead): Initialize Local Repository & Baseline Commit

> **REMINDER:** Only Developer 1 runs this initialization step!

Developer 1 initializes the repository and verifies `.gitignore` protections:

```bash
# 1. Initialize the local Git repository
git init

# 2. Set default branch to main
git branch -M main

# 3. Inspect status to confirm .venv/ is NOT being tracked
git status
```

> **CRITICAL RULE:**
> Under no circumstances should `.venv/` appear under "Untracked files". The `.gitignore` file must prevent `.venv/` from being tracked.

Create the baseline project commit:

```bash
# Stage all tracked and untracked files (excluding ignored files)
git add .

# Create initial commit using Conventional Commit standards
git commit -m "chore(init): baseline repository with modern flet app and verification tool"

# Inspect the commit log
git log --oneline
```

---

#### 4.4 Developer 1 (Group Lead): Create GitHub Repository & Invite Teammates

1. Open your browser and navigate to [GitHub: New Repository](https://github.com/new).
2. Name the repository: `cccs106-group01-showcase` (replace `01` with your team number).
3. **Leave "Add a README file" and ".gitignore template" UNCHECKED** (you already created them locally).
4. Click **Create repository**.
5. Add Developer 2 and Developer 3 as official team collaborators:
   - On your GitHub repo page, navigate to: **Settings > Collaborators > Add people**.
   - Search for Developer 2 and Developer 3 by their GitHub handles or CSPC email addresses and send invitations.
6. In your terminal, link your local repository to GitHub and push the initial `main` branch:
   ```bash
   git remote add origin https://github.com/<dev1-username>/cccs106-group01-showcase.git
   git push -u origin main
   ```

---

#### 4.5 Developer 2 & Developer 3: Accept Invitation & Clone Repository (`git clone`)

> **CRITICAL:** Developer 2 and Developer 3 do **NOT** run `git init`! Running `git init` creates disconnected repositories that cannot sync. Instead, teammates join by **cloning**.

1. **Accept GitHub Invitation:**
   - Developer 2 and Developer 3 check their email inbox or GitHub notifications bell and click **Accept invitation**.

2. **Clone the Shared Repository on Teammate PCs:**
   - On Developer 2 and Developer 3's workstations, open terminal in their desired folder (e.g., `~/Documents/CCCS_106/`):
   ```bash
   git clone https://github.com/<dev1-username>/cccs106-group01-showcase.git
   cd cccs106-group01-showcase
   ```

3. **Set Up Local Virtual Environment on Teammate PCs:**
   - Because `.venv` was intentionally excluded by `.gitignore` (as required by engineering best practices), each teammate creates their own local virtual environment:

   **Windows (Command Prompt / CMD):**
   ```cmd
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   ```

   **macOS / Linux (Terminal):**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

4. **Verify Workstation Diagnostic:**
   ```bash
   python verify_setup.py
   ```
   All checks should report `[PASS]`.

*(Note for Single-PC Lab: If your triad shares 1 physical computer, Developer 1 runs steps 4.3-4.4, and all 3 developers share the local repository on that computer, taking turns on the keyboard).*

---

### Phase 5: Hands-On Collaborative Feature Workflow (3-Member Team Triads)

In this phase, students collaborate in groups of three (Student 1, Student 2, and Student 3). Each developer is assigned a dedicated technical role and feature branch:

- **Developer 1 (Role A - Lead UI & Layout Engineer):** Branch `feature/dev1-profile`
- **Developer 2 (Role B - State & Event Logic Engineer):** Branch `feature/dev2-state`
- **Developer 3 (Role C - QA & Feature Engineer):** Branch `feature/dev3-features`

```text
                  COLLABORATIVE 3-DEVELOPER BRANCH WORKFLOW
 
  main:                  [Init Commit] ───● (Merge Dev 1) ───● (Merge Dev 2) ───● (Merge Dev 3)
                               │              ▲                   ▲                   ▲
                               │              │                   │                   │
  feature/dev1-profile:        └───► [Dev 1] ─┘                   │                   │
                                                                  │                   │
  feature/dev2-state:          ───────────────────► [Dev 2] ──────┘                   │
                                                                                      │
  feature/dev3-features:       ──────────────────────────────────────► [Dev 3] ───────┘
```

---

#### Step 1: Feature Branch 1 - Developer 1 Profile Integration & Remote Push

1. Developer 1 creates and switches to `feature/dev1-profile`:
   ```bash
   git switch -c feature/dev1-profile
   ```
   > **NOTE:** `git switch` requires Git 2.23+. If you encounter `git: 'switch' is not a git command`, use `git checkout -b feature/dev1-profile` as an equivalent.

2. Open `team_profiles.py` in VS Code. Locate the `[DEVELOPER 1 TASK]` section and update the first student profile with Developer 1's real details:
   - `student_id`: e.g., `"2024-10123"`
   - `full_name`: e.g., `"Maria Clara Santos"`
   - `role`: e.g., `"Lead Frontend UI Developer"`
   - `specialization`: e.g., `"Flet Reactive Widgets & Material 3 Layouts"`
   - `github_handle`: e.g., `"@mariaclara-cspc"`
   - `photo_url`: e.g., `"https://github.com/mariaclara-cspc.png"` *(optional: link to your GitHub avatar, web image URL, or leave `None` to display the default icon placeholder)*

3. Test your application in hot-reloading mode:
   ```bash
   flet run main.py -d
   ```
   > **NOTE:** If `flet run` is not recognized as a command, use `python main.py` instead.

   Confirm that Developer 1's profile card renders in the UI.

4. Stage and commit your changes using Conventional Commits:
   ```bash
   git add team_profiles.py
   git commit -m "feat(profile): integrate developer 1 profile card"
   ```

5. Switch to `main`, merge `feature/dev1-profile`, and push the updated `main` to GitHub:
   ```bash
   git switch main
   git merge feature/dev1-profile
   git push origin main
   ```

---

#### Step 2: Feature Branch 2 - Developer 2 Sync, State Logic & Remote Push

1. On Developer 2's PC, synchronize with GitHub to receive Developer 1's merge:
   ```bash
   git switch main
   git pull origin main
   ```

2. Create and switch to `feature/dev2-state`:
   ```bash
   git switch -c feature/dev2-state
   ```

3. Open `team_profiles.py` and locate the `[DEVELOPER 2 TASK]` section. Update Developer 2's details:
   - `student_id`: e.g., `"2024-10456"`
   - `full_name`: e.g., `"Juan Dela Cruz"`
   - `role`: e.g., `"Backend & State Engineer"`
   - `specialization`: e.g., `"State Mutation & Event Handlers"`
   - `github_handle`: e.g., `"@jdelacruz-cspc"`
   - `photo_url`: e.g., `"https://github.com/jdelacruz-cspc.png"` *(optional: link to your GitHub avatar or leave `None`)*

4. Open `main.py` and review Developer 2's event handlers (`handle_increment_task`, `handle_reset_counter`). You may adjust step sizes or add audio/haptic feedback hints.

5. Run the application to verify that clicks increment the counter and update both Developer 1 and Developer 2 cards:
   ```bash
   flet run main.py
   ```

6. Stage and commit your changes:
   ```bash
   git add team_profiles.py main.py
   git commit -m "feat(state): integrate developer 2 profile and task counter handlers"
   ```

7. Switch to `main`, merge `feature/dev2-state`, and push to GitHub:
   ```bash
   git switch main
   git merge feature/dev2-state
   git push origin main
   ```

---

#### Step 3: Feature Branch 3 - Developer 3 Sync, Milestone Feature & Remote Push

1. On Developer 3's PC, synchronize with GitHub to get Developer 1 and Developer 2's latest work:
   ```bash
   git switch main
   git pull origin main
   ```

2. Create and switch to `feature/dev3-features`:
   ```bash
   git switch -c feature/dev3-features
   ```

3. Open `team_profiles.py` and locate the `[DEVELOPER 3 TASK]` section. Update Developer 3's details:
   - `student_id`: e.g., `"2024-10789"`
   - `full_name`: e.g., `"Angelo Reyes"`
   - `role`: e.g., `"QA & Feature Engineer"`
   - `specialization`: e.g., `"Testing Diagnostics, Theme Engine & Controls"`
   - `github_handle`: e.g., `"@areyes-cspc"`
   - `photo_url`: e.g., `"https://github.com/areyes-cspc.png"` *(optional: link to your GitHub avatar or leave `None`)*

4. In `main.py`, test the sprint goal status milestone feature (`update_goal_progress()`). Click the "Complete Task" button until reaching 5 tasks to verify the celebration status badge (`🎉 SPRINT GOAL MET`) appears.

5. Stage and commit your changes:
   ```bash
   git add team_profiles.py main.py
   git commit -m "feat(milestone): integrate developer 3 profile and sprint goal milestone badge"
   ```

6. Switch to `main`, merge `feature/dev3-features`, and push to GitHub:
   ```bash
   git switch main
   git merge feature/dev3-features
   git push origin main
   ```

---

#### Step 4: Final Team Sync & Integrated Commit Tree Audit

1. All developers (Developer 1, Developer 2, and Developer 3) run `git pull` on their respective machines so all workstations have the identical final codebase:
   ```bash
   git switch main
   git pull origin main
   ```

2. Inspect the entire repository commit tree log:
   ```bash
   git log --oneline --graph --all
   ```

3. Launch the fully integrated application:
   ```bash
   flet run main.py
   ```

4. **Commit and Push Verification Screenshots:**
   Save all six (6) captured verification images directly into the `screenshots/` directory, then stage, commit, and push them to GitHub:
   ```bash
   git add screenshots/
   git commit -m "docs(screenshots): add laboratory verification proofs"
   git push origin main
   ```

---

## 4. Deliverables & Submission Checklist

### 4.1 Submission Protocol, Format & PDF Report Structure

All student triads must submit a single **Consolidated PDF Laboratory Report** to the **CSPC LeOnS LMS** portal under **Module 1: Laboratory Task 1 (Environment Setup & Collaborative Git Workflow)**.

#### Required Submission Format
- **Document Type:** PDF Document (`.pdf`)
- **Standardized File Name:** `CCCS106_Lab01_Group<XX>.pdf` *(e.g., `CCCS106_Lab01_Group03.pdf`)*

> **OFFICIAL SUBMISSION TEMPLATE PROVIDED:**
> To ensure uniformity, use the provided Microsoft Word template: [CCCS106_Lab01_Report_Template.docx](./CCCS106_Lab01_Report_Template.docx).
> Fill in your group metadata, paste your screenshots into the designated figure callout boxes, complete the reflection table, and export/save as **PDF** for submission on LeOnS.

> [!IMPORTANT]
> **Dual Verification Requirement for Screenshots:**
> All six (6) verification screenshots must be provided in **two locations**:
> 1. **Embedded in the PDF Report:** Pasted inside the corresponding figure boxes of the consolidated PDF submitted on LeOnS LMS.
> 2. **Committed & Pushed to GitHub:** Saved in the `screenshots/` folder with exact standardized filenames (`01_github_collaborators.png` through `06_app_dark_mode.png`), committed, and pushed to your GitHub repository for direct commit verification.

#### Standardized Report Structure
Every group PDF report must follow this exact section sequence:
1. **Cover Page:** Course Code (`CCCS 106`), Laboratory Title, Group Number, Full Names of all 3 students, Student IDs, and GitHub Handles.
2. **Section 1 - Repository & Collaborator Proof:** Public GitHub Repository link and screenshot of GitHub Collaborators (`01_github_collaborators.png`).
3. **Section 2 - Pre-Flight Diagnostics Audit:** Terminal screenshot of `verify_setup.py` displaying all 6 checks passing (`02_diagnostic_audit.png`).
4. **Section 3 - Git Working Tree Cleanliness:** Terminal screenshot of `git status` clean tree and empty `git ls-files .venv` (`03_git_status_clean.png`).
5. **Section 4 - Running Application Screenshots:**
   - Initial State (`04_app_initial_state.png`)
   - Goal Reached State (`05_app_goal_reached.png`)
   - Dark Mode State (`06_app_dark_mode.png`)
6. **Section 5 - Triad Contribution Matrix & Learning Reflections:** Completed contribution table and individual technical reflections.
7. **Appendix - Git Commit Tree History:** Verbatim text block of `git log --oneline --graph --all`.

---

#### Standardized Screenshot Labels and Captions inside the PDF

Embed each captured screenshot directly into its corresponding report section using the following standardized labels and captions:

| Figure # | Screenshot Reference | Screen Content & Caption Requirement |
| :-: | :--- | :--- |
| **Figure 1** | `01_github_collaborators.png` | GitHub **Settings > Collaborators** page displaying Developer 1 (Owner), Developer 2, and Developer 3 with accepted invitation statuses. |
| **Figure 2** | `02_diagnostic_audit.png` | Full terminal output of `python verify_setup.py` displaying all six (6) green `[PASS]` checks. |
| **Figure 3** | `03_git_status_clean.png` | Terminal output of `git status` showing `nothing to commit, working tree clean` and `git ls-files .venv` returning empty. |
| **Figure 4** | `04_app_initial_state.png` | Desktop GUI window upon startup showing CSPC header, green isolation chip, all 3 team member cards (with custom photos or placeholders), counter at `0`, and status `In Progress (0/5)`. |
| **Figure 5** | `05_app_goal_reached.png` | Desktop GUI window after 5 task completions showing counter at `5`, status badge `🎉 SPRINT GOAL MET (5/5)`, and the task button disabled. |
| **Figure 6** | `06_app_dark_mode.png` | Desktop GUI window with the **Dark Mode** toggle switch activated, demonstrating reactive Material 3 dark surface container rendering. |

---

- **LMS Submission Protocol (Lead-Only Submission):**
  - **Developer 1 (Lead ONLY):** Submits the consolidated group PDF report (`CCCS106_Lab01_Group<XX>.pdf`) on LeOnS on behalf of the triad.
  - **Developer 2 & Developer 3:** Do **NOT** submit on LeOnS. Their academic credit and individual grades are evaluated directly through the **Cover Page**, the **Triad Contribution Matrix (Section 5)**, and their verified GitHub commit history within the group's PDF report.

---

### 4.2 Comprehensive Itemized Deliverables

Review and prepare all six (6) required deliverables before final submission:

#### [ ] Deliverable 1: Public GitHub Repository URL & Collaborators Proof
- [ ] **Public Repository Link:** Ensure the GitHub repository visibility is set to **Public** (or add the course instructor `@allanibojr` as a collaborator if private).
  - Format: `https://github.com/<dev1-username>/cccs106-group<XX>-showcase`
- [ ] **Collaborators Screenshot:** Capture a screenshot of GitHub's repository page under:
  - **Settings > Collaborators** showing Developer 1 (Owner), Developer 2, and Developer 3 with accepted invitation statuses.
- [ ] **(Optional) GitHub Insights / Network Graph Screenshot:** If available, capture a screenshot under **Insights > Network** (`https://github.com/<dev1-username>/<repo-name>/network`) or the commit history page confirming commits authored by all three (3) distinct GitHub user accounts.

---

#### [ ] Deliverable 2: Automated Pre-flight Diagnostic Audit (`verify_setup.py`)
- [ ] Run the diagnostic tool in your active virtual environment:
  ```bash
  python verify_setup.py
  ```
- [ ] Capture a crisp terminal screenshot showing the green header and `[PASS]` on all six (6) audit checks:
  - `[PASS]` 1. Python Version (3.10 - 3.12 LTS)
  - `[PASS]` 2. Virtual Environment (`.venv` detected and active)
  - `[PASS]` 3. Flet SDK (`v0.86.5+` installed and operational)
  - `[PASS]` 4. Git CLI Installation (version 2.30+)
  - `[PASS]` 5. Git User Configuration (`user.name` and institutional `user.email`)
  - `[PASS]` 6. Repository `.gitignore` Hygiene (blocks `.venv/`)

---

#### [ ] Deliverable 3: Git Working Tree Cleanliness & `.gitignore` Audit Proof
- [ ] **Working Tree Cleanliness:** Capture a terminal screenshot of:
  ```bash
  git status
  ```
  Expected output:
  ```text
  On branch main
  Your branch is up to date with 'origin/main'.
  nothing to commit, working tree clean
  ```
- [ ] **Virtual Environment Exclusion Proof:** Run the following command to verify `.venv/` was never tracked:
  ```bash
  git ls-files .venv
  ```
  *The command output must return completely empty (no lines).* This confirms zero repository bloat.

---

#### [ ] Deliverable 4: Formatted Git Commit Tree History Log (`git_log_proof.txt`)
- [ ] Generate the ASCII commit graph log file:
  ```bash
  git log --oneline --graph --all > git_log_proof.txt
  ```
- [ ] Open `git_log_proof.txt` and confirm that it contains the complete historical lineage:
  1. Baseline initialization commit: `chore(init): baseline repository ...`
  2. Developer 1 feature branch and merge: `feat(profile): integrate developer 1 ...`
  3. Developer 2 feature branch and merge: `feat(state): integrate developer 2 ...`
  4. Developer 3 feature branch and merge: `feat(milestone): integrate developer 3 ...`
- [ ] Paste the complete, verbatim contents of `git_log_proof.txt` into the **Appendix** section of your group PDF report.

---

#### [ ] Deliverable 5: Running Flet v0.86.5 Application Screenshots (3 Application States)
Capture three (3) distinct desktop window screenshots of the application running (`flet run main.py`):

1. **Screenshot A - Initial Application State:**
   - Header with CSPC branding
   - Green `Env: ISOLATED (.venv) | Flet v0.86.5` status chip
   - All three (3) team member cards rendered with custom names, student IDs, roles, and photos (or default icon placeholders)
   - Task counter displaying: `Sprint Tasks Completed: 0`
   - Goal badge displaying: `Status: In Progress (0/5 tasks)`
2. **Screenshot B - Goal Reached Milestone State:**
   - After clicking "Complete Task (+1)" five times:
   - Task counter capped at: `Sprint Tasks Completed: 5`
   - Goal badge displaying: `Status: 🎉 SPRINT GOAL MET (5/5)` in green text
   - "Complete Task (+1)" button is visibly **disabled** (preventing count overflow)
3. **Screenshot C - Theme Mode Toggle:**
   - The dark mode toggle switch activated (`Dark Mode: True`)
   - Material 3 dark surface container styling applied across cards and canvas

---

#### [ ] Deliverable 6: Triad Contribution Matrix & Learning Reflection
Include the following completed matrix in your submission report:

| Student Name | Student ID | GitHub Username | Assigned Triad Role | Feature Branch | Commit SHA(s) | Primary Contributions |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Juan Dela Cruz** | `2024-10001` | `@jdelacruz-cspc` | Developer 1 (Lead UI) | `feature/dev1-profile` | `a1b2c3d` | Repo init, layout header, card 1 styling, remote setup |
| **Maria Clara Santos** | `2024-10002` | `@msantos-cspc` | Developer 2 (State) | `feature/dev2-state` | `d4e5f6g` | Task counter state, increment & reset logic, card 2 |
| **Angelo Reyes** | `2024-10003` | `@areyes-cspc` | Developer 3 (QA/Feature) | `feature/dev3-features` | `h7i8j9k` | Goal progress milestone badge, button bounds, card 3 |

**Individual Technical Reflections (3-4 sentences per student):**
- *Developer 1:* What did you learn about initial repository scaffolding, `.gitignore` configuration, and managing remote collaborators?
- *Developer 2:* What challenges did you encounter when syncing upstream changes (`git pull`) before creating your feature branch?
- *Developer 3:* How did feature branching protect the stability of the `main` branch while adding new milestone logic?

---

### 4.3 Final Pre-Submission Self-Audit Checklist

Before clicking Submit on LeOnS LMS, confirm:
- [ ] Does `python verify_setup.py` pass 100% of checks without errors?
- [ ] Is `.venv/` completely absent from your Git commit history?
- [ ] Did all three (3) students make at least one commit attributed to their GitHub username?
- [ ] Are all six (6) verification screenshots saved in `screenshots/`, committed, and pushed to GitHub?
- [ ] Is the GitHub repository link accessible by anyone without login restrictions?
- [ ] Does the application run smoothly with `flet run main.py` on Flet v0.86.5?

---

## 5. Analytic Evaluation Rubric (100 Points Total)

| Evaluation Criterion | Exemplary | Proficient | Developing | Unsatisfactory | Max Points |
| :--- | :--- | :--- | :--- | :--- | :---: |
| **1. Environment Isolation & Setup** | **20 pts:** Virtual environment (`.venv`) is correctly created, isolated, and active. All dependencies installed via `requirements.txt`. Diagnostic audit passes 100% of checks. | **16 pts:** Virtual environment configured but required manual intervention. Minor warning in diagnostics. | **12 pts:** Virtual environment created improperly or packages installed globally. | **0 pts:** No virtual environment used; global Python polluted; diagnostics tool failed. | **20 pts** |
| **2. Git Hygiene & `.gitignore`** | **15 pts:** Clean `.gitignore` accurately blocks `.venv/`, `__pycache__/`, and OS files. Zero binary or virtual environment bloat in Git history. | **12 pts:** `.gitignore` present with minor omissions that do not critically compromise repo size. | **9 pts:** Untracked artifacts or cache files accidentally committed and manually deleted. | **0 pts:** Committed `.venv/` or large binary build folders directly into Git history. | **15 pts** |
| **3. 3-Member Branching & Merge Workflow** | **25 pts:** Used all 3 dedicated feature branches (`feature/dev1-profile`, `feature/dev2-state`, `feature/dev3-features`). Clean fast-forward or 3-way merges into `main`. Clean graph structure. | **20 pts:** Feature branches created and merged, but naming conventions were irregular or only 2 branches used. | **15 pts:** Branches merged with messy or redundant commits; some direct commits on `main`. | **0 pts:** All commits made directly to `main` with no branching or collaboration workflow. | **25 pts** |
| **4. Conventional Commit Quality** | **15 pts:** Commit messages across all 3 developers strictly follow `<type>(<scope>): <summary>` standards. Messages are clear, descriptive, and imperative. | **12 pts:** Most commit messages follow conventions with minor syntax inconsistencies. | **9 pts:** Vague commit messages (e.g., "update", "changes", "fix code"). | **0 pts:** Single monolithic commit or empty/nonsense commit messages. | **15 pts** |
| **5. Application Execution & UI** | **20 pts:** Flet v0.86.5 app runs flawlessly without warnings. All three (3) team member cards display properly. Reactive counter, goal badge, and theme switch respond smoothly. | **16 pts:** App runs with minor visual imperfections or minor console warnings. All 3 profiles visible. | **12 pts:** App runs but has logic bugs in event handlers or incomplete profile fields. | **0 pts:** Application crashes on startup or fails to launch due to syntax/import errors. | **20 pts** |
| **6. Report Quality & Reflections** | **5 pts:** PDF report is well-formatted using the official template. All 6 figures are embedded with clear captions. Individual reflections are thoughtful, specific, and demonstrate genuine learning. | **4 pts:** Report uses the template with minor formatting issues. Reflections are adequate but generic. | **3 pts:** Report is disorganized or missing figures. Reflections are shallow or copied between members. | **0 pts:** No report submitted, or report is missing critical sections. No reflections provided. | **5 pts** |
| **TOTAL SCORE** | **100 pts** | **80 pts** | **60 pts** | **0 pts** | **100 pts** |

---

## 6. Summary & Key Takeaways

```text
+-------------------------------------------------------------------------------+
|                       KEY ENGINEERING TAKEAWAYS                               |
+-------------------------------------------------------------------------------+
| 1. Virtual environments (.venv) ensure project portability and reproducibility.|
| 2. Never commit .venv/ or cache files to Git; use .gitignore rigorously.      |
| 3. Feature branches protect the integrity of the main branch in team projects.|
| 4. Conventional commits make change histories readable, searchable, and clean.|
| 5. Modern Flet v0.86.5 provides reactive state and clean Material 3 design.  |
+-------------------------------------------------------------------------------+
```
