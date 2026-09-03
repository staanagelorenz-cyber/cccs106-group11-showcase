#!/usr/bin/env python3
# ==============================================================================
# Camarines Sur Polytechnic Colleges - College of Computer Studies
# CCCS 106: Application Development and Emerging Technologies
# Laboratory Verification & Pre-flight Diagnostics Script
#
# Usage: python verify_setup.py
# ==============================================================================

import os
import sys
import shutil
import platform
import subprocess
from pathlib import Path

# Terminal ANSI Color Codes for readability
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"


def check_python_version() -> tuple[bool, str, str]:
    version_info = sys.version_info
    v_str = f"{version_info.major}.{version_info.minor}.{version_info.micro}"
    if version_info.major == 3 and version_info.minor >= 10:
        if version_info.minor == 12:
            return True, f"Python {v_str} (Target 3.12 Recommended)", ""
        return True, f"Python {v_str} (Compatible 3.10+)", ""
    return (
        False,
        f"Python {v_str} detected",
        "Python 3.10 to 3.12 LTS is required for Flet v0.86.5+. Please upgrade your Python version.",
    )


def check_virtual_environment() -> tuple[bool, str, str]:
    base_prefix = getattr(sys, "base_prefix", sys.prefix)
    in_venv = sys.prefix != base_prefix or hasattr(sys, "real_prefix")
    if in_venv:
        venv_path = Path(sys.prefix).name
        return True, f"Active Virtualenv: '{venv_path}' ({sys.prefix})", ""
    return (
        False,
        "Running in Global / Base Python",
        "Virtual environment is NOT active. Create and activate (.venv) before proceeding:\n"
        "  - Windows (CMD): python -m venv .venv && .venv\\Scripts\\activate\n"
        "  - macOS/Linux (Bash/Zsh): python3 -m venv .venv && source .venv/bin/activate",
    )


def check_flet_installation() -> tuple[bool, str, str]:
    try:
        import flet as ft
        try:
            import importlib.metadata
            version = importlib.metadata.version("flet")
        except Exception:
            version = getattr(getattr(ft, "version", None), "version", getattr(ft, "__version__", "unknown"))

        return True, f"Flet SDK v{version} installed and operational", ""
    except ImportError:
        return (
            False,
            "Flet module not found",
            "Flet SDK is not installed in the active environment. Run:\n"
            "  pip install 'flet[all]>=0.86.5'",
        )


def check_git_binary() -> tuple[bool, str, str]:
    git_path = shutil.which("git")
    if not git_path:
        return (
            False,
            "Git executable not found in system PATH",
            "Git is not installed or not added to PATH. Install it now:\n"
            "  - Windows (CMD): winget install --id Git.Git -e --source winget\n"
            "  - macOS (Terminal): xcode-select --install  (or: brew install git)\n"
            "  - Web Installer: https://git-scm.com/downloads\n"
            "  * Remember to close and reopen your terminal after installation finishes.",
        )

    try:
        result = subprocess.run(
            ["git", "--version"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True,
        )
        return True, result.stdout.strip(), ""
    except Exception as e:
        return False, "Failed to invoke git CLI", str(e)


def check_git_config() -> tuple[bool, str, str]:
    try:
        name_proc = subprocess.run(
            ["git", "config", "user.name"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        email_proc = subprocess.run(
            ["git", "config", "user.email"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        user_name = name_proc.stdout.strip()
        user_email = email_proc.stdout.strip()

        if user_name and user_email:
            return True, f"Configured as '{user_name}' <{user_email}>", ""

        missing = []
        if not user_name:
            missing.append("user.name")
        if not user_email:
            missing.append("user.email")

        return (
            False,
            f"Missing Git configuration: {', '.join(missing)}",
            "Set your Git user credentials (matching your GitHub account at https://github.com/signup):\n"
            '  git config --global user.name "Your Full Name"\n'
            '  git config --global user.email "your.email@cspc.edu.ph"',
        )
    except Exception as e:
        return False, "Unable to query git config", str(e)


def check_gitignore() -> tuple[bool, str, str]:
    current_dir = Path.cwd()
    gitignore_candidates = [
        current_dir / ".gitignore",
        current_dir.parent / ".gitignore",
        current_dir.parent.parent / ".gitignore",
    ]

    found_path = None
    for candidate in gitignore_candidates:
        if candidate.exists() and candidate.is_file():
            found_path = candidate
            break

    if not found_path:
        return (
            False,
            ".gitignore file NOT found",
            "A .gitignore file must exist to prevent committing .venv/ and __pycache__/.\n"
            "Create a .gitignore file in your repository root.",
        )

    content = found_path.read_text(encoding="utf-8", errors="ignore")
    lines = [line.strip() for line in content.splitlines()]

    has_venv = any(
        target in lines
        for target in [".venv", ".venv/", "venv", "venv/", "ENV/", "env/"]
    )

    if has_venv:
        return True, f".gitignore detected at {found_path.name} (blocks .venv/)", ""
    return (
        False,
        ".gitignore exists but DOES NOT ignore .venv/",
        "Add '.venv/' to your .gitignore file immediately to avoid committing thousands of binary files!",
    )


def main():
    print("=" * 76)
    print(f"{BOLD}{CYAN}      CAMARINES SUR POLYTECHNIC COLLEGES - COLLEGE OF COMPUTER STUDIES{RESET}")
    print(f"{BOLD}         CCCS 106: WORKSTATION & GIT ENVIRONMENT AUDIT TOOL{RESET}")
    print("=" * 76)
    print(f"Host Operating System : {platform.system()} {platform.release()} ({platform.machine()})")
    print(f"Current Working Dir   : {Path.cwd()}")
    print("-" * 76)

    checks = [
        ("1. Python Version (3.10 - 3.12)", check_python_version),
        ("2. Virtual Environment (.venv)", check_virtual_environment),
        ("3. Flet SDK (v0.86.5+)", check_flet_installation),
        ("4. Git CLI Installation", check_git_binary),
        ("5. Git User Configuration", check_git_config),
        ("6. Repository .gitignore Hygiene", check_gitignore),
    ]

    all_passed = True
    issues = []

    for label, check_func in checks:
        passed, summary, remediation = check_func()
        status_tag = f"{GREEN}[PASS]{RESET}" if passed else f"{RED}[FAIL]{RESET}"
        print(f"{status_tag} {BOLD}{label:<35}{RESET} : {summary}")
        if not passed:
            all_passed = False
            issues.append((label, remediation))

    print("=" * 76)
    if all_passed:
        print(f"{GREEN}{BOLD}🎉 ALL AUDIT CHECKS PASSED!{RESET}")
        print("Your workstation is properly configured and isolated.")
        print("You are fully ready to proceed with the Collaborative Git Workflow!")
        print("=" * 76)
        sys.exit(0)
    else:
        print(f"{RED}{BOLD}⚠️  {len(issues)} AUDIT CHECK(S) FAILED OR REQUIRE ATTENTION:{RESET}")
        for idx, (lbl, rem) in enumerate(issues, 1):
            print(f"\n{BOLD}{idx}. Remediation for {lbl}:{RESET}")
            for r_line in rem.splitlines():
                print(f"   {r_line}")
        print("\n" + "=" * 76)
        print("Please resolve the issues above and re-run: python verify_setup.py")
        print("=" * 76)
        sys.exit(1)


if __name__ == "__main__":
    main()
