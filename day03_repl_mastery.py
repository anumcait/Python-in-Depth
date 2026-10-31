"""
Day 03 Companion Script: Python REPL and First Programs Mastery
==============================================================
Demonstrates core concepts covered in Day 03:
1. Script vs Interactive execution detection (sys.flags.interactive).
2. Dynamic prompt customization (sys.ps1, sys.ps2).
3. Expression evaluation vs statement side-effects.
4. Exit status codes and system diagnostics.
5. Launching an in-process interactive REPL console with custom context.

Usage:
    python day03_repl_mastery.py
    python -i day03_repl_mastery.py
"""

import sys
import platform
import code

def display_runtime_environment() -> None:
    """Print architectural diagnostic information about the current Python session."""
    print("=" * 60)
    print("  PYTHON REPL & SCRIPT RUNTIME INSPECTOR")
    print("=" * 60)
    print(f"Python Version    : {platform.python_version()} ({platform.python_implementation()})")
    print(f"Executable Path   : {sys.executable}")
    print(f"Interactive Mode  : {'YES (-i or REPL)' if sys.flags.interactive else 'NO (Normal Script)'}")
    print(f"Optimization Flag : {sys.flags.optimize} (0=Normal, 1=-O, 2=-OO)")
    print(f"Default Encoding  : {sys.getdefaultencoding()}")
    print("-" * 60)

class ApplicationConfig:
    """Simulated application configuration loaded into memory for REPL inspection."""
    def __init__(self, app_name: str, environment: str, debug: bool):
        self.app_name = app_name
        self.environment = environment
        self.debug = debug
        self.request_count = 0

    def record_request(self) -> int:
        self.request_count += 1
        return self.request_count

    def __repr__(self) -> str:
        return f"ApplicationConfig(app_name={self.app_name!r}, env={self.environment!r}, debug={self.debug}, requests={self.request_count})"

def start_custom_repl() -> None:
    """Start an embedded interactive Python console pre-populated with variables."""
    print("\n[+] Launching embedded interactive Python console...")
    print("[+] Variables 'config' and 'runtime_info' are preloaded!")
    print("[+] Type 'exit()' or press Ctrl+Z / Ctrl+D to leave the console.\n")

    local_context = {
        "config": ApplicationConfig("ECommerceEngine", "development", True),
        "runtime_info": {
            "os": platform.system(),
            "release": platform.release(),
            "cpu_architecture": platform.machine(),
        },
        "calculate_tax": lambda amount, rate=0.07: round(amount * (1 + rate), 2)
    }

    # Start interactive REPL
    code.interact(banner="--- Day 03 Embedded Python REPL Console ---", local=local_context)

if __name__ == "__main__":
    display_runtime_environment()

    # If user ran script normally, demonstrate execution and optionally offer REPL
    print("\nDemonstrating script-mode calculations:")
    prices = [19.99, 45.50, 102.00]
    taxed_prices = [round(p * 1.08, 2) for p in prices]
    print(f"Raw prices:   {prices}")
    print(f"With 8% tax:  {taxed_prices}")

    print("\nTip: To inspect variables interactively after script finish, run:")
    print("    python -i day03_repl_mastery.py")
    
    # If explicitly requested with argument '--repl', launch in-process REPL
    if "--repl" in sys.argv:
        start_custom_repl()

