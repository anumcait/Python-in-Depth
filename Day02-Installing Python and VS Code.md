# 🐍 Python100 — Day 02

## Installing Python & VS Code: Building a Professional Development Environment

> **Goal:** Set up a clean, robust, reproducible Python development workstation. Master the operating system PATH variable, VS Code configuration, CPython interpreter resolution, and isolated virtual environments before writing complex multi-file applications.

| | |
|---|---|
| 📚 **Series** | Mission Python 100 |
| 🗓️ **Day** | 02 |
| 🎯 **Goal** | Build an enterprise-grade, reproducible Python development environment |
| 🧰 **You will build** | `.venv`, `.vscode/settings.json`, `day02_env_check.py`, `requirements.txt` |
| ✅ **Prerequisites** | Day 01: Python, Programming & the Developer Mindset |

---

## 📑 Contents

1. [Why Start with Environment Architecture?](#1-why-start-with-environment-architecture)
2. [Visual Architecture: The Professional Python Toolchain](#2-visual-architecture-the-professional-python-toolchain)
3. [Installing Python: Platform by Platform](#3-installing-python-platform-by-platform)
4. [The Critical Checkbox: "Add python.exe to PATH"](#4-the-critical-checkbox-add-pythonexe-to-path)
5. [Deep Dive: How the Operating System PATH Variable Works](#5-deep-dive-how-the-operating-system-path-variable-works)
6. [The Python Launcher for Windows (`py.exe`)](#6-the-python-launcher-for-windows-pyexe)
7. [Installing Visual Studio Code (VS Code)](#7-installing-visual-studio-code-vs-code)
8. [The Essential VS Code Extension Ecosystem](#8-the-essential-vs-code-extension-ecosystem)
9. [Configuring VS Code Workspace Settings (`.vscode/settings.json`)](#9-configuring-vs-code-workspace-settings-vscodesettingsjson)
10. [The Integrated Terminal & Shell Awareness](#10-the-integrated-terminal--shell-awareness)
11. [Selecting the Active Python Interpreter in VS Code](#11-selecting-the-active-python-interpreter-in-vs-code)
12. [Virtual Environments (`venv`): First Principles & Why They Exist](#12-virtual-environments-venv-first-principles--why-they-exist)
13. [Anatomy of a Virtual Environment Directory](#13-anatomy-of-a-virtual-environment-directory)
14. [Step-by-Step: Creating, Activating & Managing a `.venv`](#14-step-by-step-creating-activating--managing-a-venv)
15. [Package Management with `pip` and PyPI](#15-package-management-with-pip-and-pypi)
16. [Freezing and Reproducing Dependencies (`requirements.txt`)](#16-freezing-and-reproducing-dependencies-requirementstxt)
17. [Professional Project Directory Layout](#17-professional-project-directory-layout)
18. [First Interactive Debugging Session with Breakpoints](#18-first-interactive-debugging-session-with-breakpoints)
19. [Real-World Engineering Connection](#19-real-world-engineering-connection)
20. [Troubleshooting: The 8 Most Common Setup Bugs & Fixes](#20-troubleshooting-the-8-most-common-setup-bugs--fixes)
21. [Hands-On Practical Labs](#21-hands-on-practical-labs)
22. [Interview & Senior-Level Questions](#22-interview--senior-level-questions)
23. [Day 02 Golden Rules & Summary](#23-day-02-golden-rules--summary)

---

## 1. Why Start with Environment Architecture?

Many tutorials tell beginners:
> *"Download Python, click next, install VS Code, and start coding."*

In software engineering, this approach leads to major problems within days:
* Package version conflicts between different projects ("Dependency Hell").
* Scripts running on an unexpected Python version.
* Code working in the editor but crashing in the terminal with `ModuleNotFoundError`.
* The infamous error: `'python' is not recognized as an internal or external command`.

```text
The Amateur Approach:
Global Python ───> Install Package A (v1.0) ───> Install Package B (requires v2.0) ───> EVERYTHING BREAKS 💥

The Professional Approach:
System Python
     │
     ├── Project A Sandbox (.venv_a) ──> FastAPI 0.95 + Pydantic 1.10 (Isolated ✅)
     │
     └── Project B Sandbox (.venv_b) ──> FastAPI 1.0.0 + Pydantic 2.6.0 (Isolated ✅)
```

Today, we build a **reproducible, professional development workstation** from first principles.

---

## 2. Visual Architecture: The Professional Python Toolchain

Before touching installers, let's understand how the components of your workstation interact:

![Professional Python Development Environment Architecture](images/day-002-setup-architecture.svg)

### Three Layers of Your Workstation:
1. **Developer Experience Layer (VS Code & Extensions):** You write code, inspect errors via Pylance, format code automatically, and step through breakpoints.
2. **Command Resolution Layer (OS Shell & PATH):** Your terminal determines which exact `python.exe` binary executes when you type `python`.
3. **Runtime & Package Isolation Layer (`.venv`):** An isolated sandbox containing only the specific third-party libraries needed by your current project.

---

## 3. Installing Python: Platform by Platform

Always use modern **Python 3.12+** (64-bit).

### Windows Installation:
1. Download the official 64-bit installer from [python.org/downloads](https://www.python.org/downloads/).
2. Run the installer as Administrator.
3. ⚠️ **MANDATORY:** Check the box at the bottom: **"Add python.exe to PATH"**.
4. Click **Customize installation**:
   * Ensure `pip`, `tcl/tk and IDLE`, and `Python test suite` are checked.
   * Check **"Install py launcher for all users"**.
5. Advanced Options:
   * Check **"Install for all users"** (installs to `C:\Program Files\Python312` or user local app data).
   * Check **"Precompile standard library"** for faster startup.
6. Click **Install**. At the end, click **"Disable path length limit"** (avoids Windows 260-character path errors).

### macOS Installation:
macOS comes with a stub system Python that should never be modified. Use **Homebrew**:
```bash
# Install Homebrew if not already installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install modern Python
brew install python@3.12

# Verify
python3 --version
```

### Linux (Ubuntu / Debian):
```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv python3-dev
python3 --version
```

---

## 4. The Critical Checkbox: "Add python.exe to PATH"

Why is this checkbox so critical?

When you type a command in your terminal (such as `python` or `git`), the operating system doesn't know where that program lives on your hard drive. 

It consults an operating system variable called **PATH** — a semicolon-separated list of folder directories.

---

## 5. Deep Dive: How the Operating System PATH Variable Works

![Understanding the OS PATH Environment Variable](images/day-002-how-path-works.svg)

### What Happens Without PATH:
```text
User types: python main.py
   │
   ▼
OS checks: C:\Windows\System32 ────> Not found
OS checks: C:\Windows ─────────────> Not found
OS checks: End of PATH reached ────> ❌ CRASH:
"'python' is not recognized as an internal or external command"
```

### What Happens With PATH Configured:
```text
User types: python main.py
   │
   ▼
OS checks: C:\Users\Admin\AppData\Local\Programs\Python\Python312
   │
   └── FOUND python.exe! ──> Launches CPython runtime immediately ✅
```

### How to Inspect PATH in Your Terminal:

On Windows (PowerShell):
```powershell
# Show which python executable is chosen
where.exe python

# Print all directories in PATH
$env:PATH -split ';'
```

On Linux / macOS (Bash / Zsh):
```bash
which python3
echo $PATH | tr ':' '\n'
```

---

## 6. The Python Launcher for Windows (`py.exe`)

On Windows, the official installer provides `py.exe` located in `C:\Windows\py.exe`. 

`py.exe` automatically detects all installed Python versions and routes your execution to the desired one:

```powershell
# Show all installed Python versions on your computer
py --list

# Run specifically with Python 3.11
py -3.11 main.py

# Run specifically with Python 3.12
py -3.12 main.py
```

It also respects **shebang lines** at the top of Python files:
```python
#!/usr/bin/env python3.12
print("Running on Python 3.12!")
```

---

## 7. Installing Visual Studio Code (VS Code)

**Visual Studio Code** is the industry-standard code editor for Python developers worldwide:
* Lightweight, modular, and fast.
* Powered by the **Language Server Protocol (LSP)**.
* Integrated Git source control and integrated terminal.
* Industry-leading interactive debugger.

Download and install VS Code from [code.visualstudio.com](https://code.visualstudio.com/).
During Windows installation, check:
* ✅ **"Add 'Open with Code' action to Windows Explorer file context menu"**
* ✅ **"Add 'Open with Code' action to Windows Explorer directory context menu"**
* ✅ **"Add to PATH"**

---

## 8. The Essential VS Code Extension Ecosystem

Open VS Code, press `Ctrl + Shift + X` (or `Cmd + Shift + X` on macOS), and install these four essential extensions:

1. **Python (by Microsoft):** Core support for debugging, test discovery, and interpreter selection.
2. **Pylance (by Microsoft):** High-performance language server delivering type checking, IntelliSense, auto-imports, and docstring hovers.
3. **Python Debugger (`debugpy`):** Dedicated debugger supporting breakpoints, conditional watches, and call-stack stepping.
4. **Ruff (by Astral-sh) or Black Formatter:** Lightning-fast Python linting and code formatting conforming to PEP 8 standards.

---

## 9. Configuring VS Code Workspace Settings (`.vscode/settings.json`)

To ensure consistent behavior across team members, configure project settings inside `.vscode/settings.json`:

```json
{
  "python.defaultInterpreterPath": "${workspaceFolder}/.venv/Scripts/python.exe",
  "python.terminal.activateEnvironment": true,
  "editor.formatOnSave": true,
  "editor.defaultFormatter": "charliermarsh.ruff",
  "editor.codeActionsOnSave": {
    "source.organizeImports": "explicit"
  },
  "python.analysis.typeCheckingMode": "basic",
  "python.analysis.autoImportCompletions": true,
  "files.autoSave": "onFocusChange"
}
```

> **Why this matters:** When you or a teammate clone this repository, VS Code automatically targets the project's `.venv`, formats code on save, and organizes imports according to PEP 8 standards.

---

## 10. The Integrated Terminal & Shell Awareness

VS Code provides an integrated terminal (`Ctrl + ` ` ` or `` Ctrl + Shift + ` ``):
* On Windows: defaults to **PowerShell** (recommended).
* On macOS: defaults to **Zsh**.
* On Linux: defaults to **Bash**.

### Execution Policy on Windows PowerShell:
If you see the error:
`File ...\Activate.ps1 cannot be loaded because running scripts is disabled on this system.`

This is a Windows default security policy preventing unapproved script execution. Fix it safely for your user account:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

## 11. Selecting the Active Python Interpreter in VS Code

VS Code allows you to point directly to any Python runtime on your machine:
1. Press `Ctrl + Shift + P` (`Cmd + Shift + P` on macOS) to open the Command Palette.
2. Type and select: **`Python: Select Interpreter`**.
3. Choose the interpreter labeled **`('..venv': venv)`**.

Notice the bottom-right status bar in VS Code: it displays `3.12.x ('.venv': venv)`, confirming that your editor is bound to your project sandbox.

---

## 12. Virtual Environments (`venv`): First Principles & Why They Exist

![The Why Behind Virtual Environments: Eliminating Dependency Hell](images/day-002-virtualenv-internals.svg)

### The Dependency Collision Problem:
Suppose your company runs two services:
* **Service A (Fashion Marketplace):** Built 2 years ago using `FastAPI 0.95` and `pydantic 1.10`.
* **Service B (AI Ride Dispatch):** Built today using `FastAPI 1.0` and `pydantic 2.6` (which introduces breaking API changes).

If both projects use your computer's global Python, running `pip install` on Service B will overwrite Pydantic, breaking Service A immediately.

**The Solution:** A Virtual Environment gives each project its own isolated sandbox.

---

## 13. Anatomy of a Virtual Environment Directory

A virtual environment is **not** a heavy virtual machine like VMware or Docker. It is simply a directory containing lightweight symbolic links and isolated folders:

```text
my-project/
├── .venv/
│   ├── Include/           <-- C header files for C-extensions (numpy, cryptography)
│   ├── Lib/
│   │   └── site-packages/ <-- ALL third-party pip packages live HERE (isolated!)
│   ├── Scripts/           <-- Windows binaries (python.exe, pip.exe, activate.ps1)
│   │   └── (or bin/ on macOS/Linux)
│   └── pyvenv.cfg         <-- Configuration file pointing back to base Python
├── src/
│   └── main.py
└── requirements.txt
```

### The Magic of `pyvenv.cfg`:
```ini
home = C:\Users\Admin\AppData\Local\Programs\Python\Python312
include-system-site-packages = false
version = 3.12.2
executable = C:\Users\Admin\AppData\Local\Programs\Python\Python312\python.exe
command = C:\Python312\python.exe -m venv D:\project\.venv
```
Setting `include-system-site-packages = false` ensures that global computer packages are completely ignored.

---

## 14. Step-by-Step: Creating, Activating & Managing a `.venv`

### Step 1: Open Terminal in Your Project Directory
```powershell
cd D:\Python-in-Depth
```

### Step 2: Create the Virtual Environment
```powershell
# python -m venv <directory_name>
python -m venv .venv
```

### Step 3: Activate the Environment
On Windows PowerShell:
```powershell
.\.venv\Scripts\Activate.ps1
```

On Windows CMD:
```cmd
.venv\Scripts\activate.bat
```

On macOS / Linux:
```bash
source .venv/bin/activate
```

### How You Know It Worked:
Your terminal prompt changes to show the environment prefix:
```powershell
(.venv) PS D:\Python-in-Depth>
```

### What Activation Actually Does Internally:
When you run `Activate.ps1`, it temporarily modifies your session's `$env:PATH`:
```text
Old PATH: C:\Windows\System32;C:\Python312
New PATH: D:\Python-in-Depth\.venv\Scripts;C:\Windows\System32;C:\Python312
```
Because `.venv\Scripts` is at the very front of the list, typing `python` or `pip` routes directly to the sandbox!

### Step 4: Deactivate When Done
```powershell
deactivate
```

---

## 15. Package Management with `pip` and PyPI

With your `.venv` active, install packages securely from the **Python Package Index (PyPI)**:

```powershell
# Upgrade pip inside your virtual environment
python -m pip install --upgrade pip

# Install a specific package and version
pip install requests==2.31.0

# Inspect installed packages
pip list

# Inspect detailed metadata of a package
pip show requests
```

---

## 16. Freezing and Reproducing Dependencies (`requirements.txt`)

To ensure that any team member or deployment server can recreate your exact environment:

```powershell
# 1. Export exact pinned versions to requirements.txt
pip freeze > requirements.txt

# 2. Inspect requirements.txt
cat requirements.txt
```

Example output:
```text
certifi==2024.2.2
charset-normalizer==3.3.2
idna==3.6
requests==2.31.0
urllib3==2.2.1
```

### Recreating the Environment on Another Computer:
```powershell
# On the new machine:
git clone https://github.com/your-org/project.git
cd project
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```
Every dependency installs with identical versions!

---

## 17. Professional Project Directory Layout

Standard industry layout for production Python applications:

```text
fashion-service/
├── .venv/                     # Ignored by Git (Never commit this!)
├── .vscode/
│   ├── settings.json          # Workspace formatter & interpreter config
│   └── launch.json            # Debugger configurations
├── src/
│   └── fashion/
│       ├── __init__.py        # Marks directory as a Python package
│       ├── core/
│       │   ├── __init__.py
│       │   └── config.py      # Environment variables & secrets
│       ├── api/
│       │   ├── __init__.py
│       │   └── routes.py      # REST endpoints
│       └── main.py            # Application entrypoint
├── tests/
│   ├── __init__.py
│   └── test_pricing.py        # Automated pytest suite
├── .gitignore                 # Excludes .venv/, __pycache__/, .env
├── requirements.txt           # Production pinned dependencies
├── requirements-dev.txt       # Developer tooling (pytest, ruff, black)
└── README.md                  # Project setup documentation
```

### Essential `.gitignore` Rules:
```gitignore
# Byte-compiled / optimized files
__pycache__/
*.py[cod]

# Virtual environments
.venv/
env/
venv/

# Environment variables & secrets
.env
.env.local

# IDE configurations (personal)
.idea/
*.swp
```

---

## 18. First Interactive Debugging Session with Breakpoints

Create a verification script named `day02_env_check.py`:

```python
"""
Mission Python 100 — Day 02 Verification Script
Inspects active interpreter, virtual environment status, and system paths.
"""

import os
import sys


def verify_environment() -> dict:
    in_virtualenv = sys.prefix != sys.base_prefix
    
    env_info = {
        "python_version": sys.version.split()[0],
        "executable_path": sys.executable,
        "is_virtual_environment": in_virtualenv,
        "base_interpreter": sys.base_prefix,
        "active_prefix": sys.prefix,
        "cwd": os.getcwd()
    }
    return env_info


if __name__ == "__main__":
    report = verify_environment()
    print("=" * 60)
    print("🚀 PYTHON ENVIRONMENT DIAGNOSTIC REPORT")
    print("=" * 60)
    for key, val in report.items():
        print(f"  {key:<25}: {val}")
    print("=" * 60)

    if report["is_virtual_environment"]:
        print("✅ SUCCESS: Code is running inside an isolated .venv!")
    else:
        print("⚠️ WARNING: Code is running in GLOBAL System Python. Activate .venv!")
    print("=" * 60)
```

### Step-by-Step Debugging in VS Code:
1. Open `day02_env_check.py` in VS Code.
2. Click to the left of line 11 (`in_virtualenv = sys.prefix != sys.base_prefix`) to set a **Red Breakpoint** (or press `F9`).
3. Press **`F5`** (select *Python Debugger: Python File*).
4. Execution pauses on line 11!
5. Inspect the **Run & Debug** pane on the left:
   * **Variables:** View local variables and values in real time.
   * **Watch:** Type expressions like `sys.prefix` to evaluate on the fly.
   * **Call Stack:** Inspect the current execution frame.
6. Press **`F10`** to Step Over, or **`F5`** to continue execution.

---

## 19. Real-World Engineering Connection

How does today's setup directly power the enterprise architectures introduced in Day 01?

| Architecture | Local Environment Setup Pattern |
|---|---|
| **🏢 Enterprise ERP / Payroll** | Uses locked `pip-tools` or `Poetry` inside `.venv` to enforce strict deterministic package versions for multi-developer tax calculation compliance. |
| **🛍️ Fashion Marketplace** | Multiple microservices (`catalog-service`, `order-service`) each maintain independent `.venv` directories to avoid library collisions between legacy and modern APIs. |
| **🚗 Uber-Like Platform** | Docker containers mirror local `.venv` setups using identical `requirements.txt` to eliminate differences between local laptops and AWS ECS cloud clusters. |

---

## 20. Troubleshooting: The 8 Most Common Setup Bugs & Fixes

### 1. `'python' is not recognized as an internal or external command`
* **Root Cause:** Python was installed without checking "Add python.exe to PATH".
* **Instant Fix:** Re-run the installer, choose *Modify*, and check **"Add python.exe to PATH"**. Or manually add `C:\Users\<User>\AppData\Local\Programs\Python\Python312` to your user Environment Variables.

### 2. `ExecutionPolicy Error on Windows PowerShell`
* **Root Cause:** PowerShell restricts unsigned script execution by default.
* **Instant Fix:** Run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` in PowerShell.

### 3. VS Code uses Global Python instead of `.venv`
* **Root Cause:** Interpreter path not set in workspace settings.
* **Instant Fix:** Press `Ctrl + Shift + P` $\rightarrow$ `Python: Select Interpreter` $\rightarrow$ select `('..venv': venv)`.

### 4. `ModuleNotFoundError: No module named 'requests'`
* **Root Cause:** Package was installed in one environment, but the script is running in another.
* **Instant Fix:** Check `sys.executable` to verify the active interpreter, ensure `(.venv)` is active, and run `pip install requests` inside that environment.

### 5. `pip install` throws Access Denied / Permission Error
* **Root Cause:** Trying to install into global `C:\Program Files` without Admin rights.
* **Instant Fix:** Always use a virtual environment (`.venv`), where packages are installed into your user project directory with zero administrator restrictions.

### 6. Terminal prompt does not display `(.venv)`
* **Root Cause:** Script activation was bypassed.
* **Instant Fix:** Run `.\.venv\Scripts\Activate.ps1` explicitly.

### 7. Virtual environment broken after moving project folder
* **Root Cause:** `pyvenv.cfg` and scripts store absolute filesystem paths.
* **Instant Fix:** Delete the `.venv` folder (`rm -r .venv`) and re-create it in 10 seconds: `python -m venv .venv && .\.venv\Scripts\activate && pip install -r requirements.txt`.

### 8. Python opens the Windows Store instead of running
* **Root Cause:** Windows 10/11 "App Execution Aliases" intercepting `python.exe`.
* **Instant Fix:** Windows Settings $\rightarrow$ Search *Manage app execution aliases* $\rightarrow$ Turn OFF `App Installer (python.exe)` and `App Installer (python3.exe)`.

---

## 21. Hands-On Practical Labs

### Lab A — Verification:
Run `day02_env_check.py` and confirm that `is_virtual_environment` returns `True`.

### Lab B — Dependency Management:
1. Activate your `.venv`.
2. Install `requests` and `rich`:
   ```powershell
   pip install requests rich
   ```
3. Generate `requirements.txt`:
   ```powershell
   pip freeze > requirements.txt
   ```
4. Confirm that both libraries and their sub-dependencies appear in `requirements.txt`.

### Lab C — Deliberate Error Injection:
1. Open PowerShell **without activating `.venv`**.
2. Try importing `requests` using `python -c "import requests"`.
3. Observe the `ModuleNotFoundError`.
4. Now activate `.venv` and re-run. Observe how the error vanishes.

---

## 22. Interview & Senior-Level Questions

### 1. Junior Level: What does the PATH environment variable do, and what happens when it is misconfigured?
> **Answer:** PATH is an operating system environment variable containing an ordered list of directory paths. When an executable name is invoked in a shell without an absolute path, the OS traverses these directories from left to right until it finds a matching binary. If it reaches the end of the list without a match, it raises a command-not-found error.

### 2. Intermediate Level: How does Python determine whether it is running inside a virtual environment?
> **Answer:** Python compares `sys.prefix` (the current active execution prefix) with `sys.base_prefix` (the base interpreter path). When running in global Python, `sys.prefix == sys.base_prefix`. Inside a virtual environment, `sys.prefix` points to the `.venv` directory, while `sys.base_prefix` points to the root Python installation.

### 3. Senior Level: Why should `.venv` directories never be committed to Git or copied between different host operating systems?
> **Answer:** 
> 1. Virtual environments contain compiled platform-specific machine code binaries (e.g. `.exe` on Windows vs ELF binaries on Linux) in their `Scripts/` or `bin/` folders, which cannot run across different OS kernels.
> 2. `pyvenv.cfg` records hardcoded absolute filesystem paths specific to the developer's local machine.
> 3. C-extensions compiled for one architecture (e.g. x86_64 vs ARM64) will fail on another. Instead, commit only `requirements.txt` or `pyproject.toml` and rebuild the `.venv` natively on the host or inside a Docker container.

---

## 23. Day 02 Golden Rules & Summary

```text
╔══════════════════════════════════════════════════════════════════════════╗
║                    DAY 02 GOLDEN RULES TO LIVE BY                        ║
╠══════════════════════════════════════════════════════════════════════════╣
║ 1. One project, one virtual environment (.venv). Never install globally. ║
║ 2. Always verify your interpreter with sys.executable before debugging.  ║
║ 3. Never commit .venv/ or credentials to Git. Put them in .gitignore.    ║
║ 4. Always pin production dependencies using requirements.txt.            ║
║ 5. Treat environment setup as software architecture, not an afterthought.║
╚══════════════════════════════════════════════════════════════════════════╝
```

---

| ⬅️ Previous | ➡️ Next |
|---|---|
| [Day 01: Python, Programming & Developer Mindset](Day01-Python,%20Programming%20&%20the%20Developer%20Mindset.md) | [Day 03: Python REPL and First Programs](Day03-Python%20REPL%20and%20first%20programs.md) |
| 🏁 **Day 02 complete** | **Return to [README](README.md)** |
