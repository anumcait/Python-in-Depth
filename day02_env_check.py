"""
Mission Python 100 — Day 02 Environment Verification Script
Run this script to verify your Python interpreter, virtual environment status, and active paths.
"""

import os
import sys


def verify_environment() -> dict:
    in_virtualenv = sys.prefix != sys.base_prefix

    return {
        "python_version": sys.version.split()[0],
        "executable_path": sys.executable,
        "is_virtual_environment": in_virtualenv,
        "base_interpreter": sys.base_prefix,
        "active_prefix": sys.prefix,
        "cwd": os.getcwd(),
    }


if __name__ == "__main__":
    report = verify_environment()
    print("=" * 65)
    print("🚀 PYTHON ENVIRONMENT DIAGNOSTIC REPORT (Mission Python 100 — Day 02)")
    print("=" * 65)
    for key, val in report.items():
        print(f"  {key:<25}: {val}")
    print("=" * 65)

    if report["is_virtual_environment"]:
        print("  Status: ✅ SUCCESS — Running inside an isolated virtual environment (.venv)!")
    else:
        print("  Status: ⚠️ WARNING — Running in global system Python. Activate your .venv!")
    print("=" * 65)

