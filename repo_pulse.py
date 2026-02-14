import subprocess
import os
import argparse
from pathlib import Path
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

# Templates for the --fix command
GITIGNORE_TEMPLATE = """# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# Environments
.venv/
venv/
ENV/
env/

# Distribution / packaging
dist/
build/
*.egg-info/
"""

MIT_LICENSE_TEMPLATE = """Copyright (c) 2026 Your Name

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
"""

def analyze_repo() -> tuple[dict[str, str], str, int]:
    """Analyze repository health and return metrics, insight, and health score."""
    report = {"docs": "✅ Found", "commits": "✅ Professional", "size": "✅ Lean", "hygiene": "✅ Excellent"}
    points = 4.0
    insight = "Your repo looks healthy and ready for contributors!"

    if not any(os.path.exists(f) for f in ["README.md", "README", "readme.md"]):
        report["docs"] = "❌ Missing README"; insight = "Tip: Add a README!"; points -= 1

    try:
        log = subprocess.check_output(["git", "log", "-n", "5", "--pretty=format:%s"], text=True, stderr=subprocess.DEVNULL)
        if len(log.splitlines()) < 3:
            report["commits"] = "⚠️ Sparse"; points -= 0.5
    except:
        report["commits"] = "❓ No Git Found"; points -= 1

    file_count = _count_files()
    if file_count > 100: report["size"] = "⚠️ Large"; points -= 0.5
    elif file_count < 5: report["size"] = "❌ Too Small"; points -= 1

    has_license = any(os.path.exists(f) for f in ["LICENSE", "LICENSE.txt", "license.md"])
    has_ignore = os.path.exists(".gitignore")
    if not has_license or not has_ignore:
        missing = [m for m, exists in [("LICENSE", has_license), (".gitignore", has_ignore)] if not exists]
        report["hygiene"] = f"⚠️ Missing {', '.join(missing)}"
        points -= 0.5 * len(missing)

    return report, insight, int((max(0, points) / 4) * 100)

def _count_files() -> int:
    excluded = {".git", ".github", ".venv", "venv", "__pycache__", "node_modules", "dist", "build"}
    return sum(1 for p in Path(".").rglob("*") if p.is_file() and not any(part in excluded or (part.startswith(".") and part != ".") for part in p.parts))

def apply_fixes():
    """Create missing hygiene files."""
    if not any(os.path.exists(f) for f in ["LICENSE", "LICENSE.txt", "license.md"]):
        with open("LICENSE", "w") as f:
            f.write(MIT_LICENSE_TEMPLATE)
        console.print("[bold green]✔ Created MIT LICENSE[/]")
    
    if not os.path.exists(".gitignore"):
        with open(".gitignore", "w") as f:
            f.write(GITIGNORE_TEMPLATE)
        console.print("[bold green]✔ Created .gitignore[/]")

def main():
    parser = argparse.ArgumentParser(description="Repo-Pulse: Check and fix project health.")
    parser.add_argument("--fix", action="store_true", help="Automatically generate missing hygiene files.")
    args = parser.parse_args()

    if args.fix:
        apply_fixes()
        return

    console.print(Panel("[bold blue]Repo-Pulse CLI[/bold blue]\n[italic]The 30-second Project Health Check[/italic]", expand=False))
    console.rule("[bold blue]Analysis Results[/]")
    
    stats, ai_insight, health_score = analyze_repo()
    color = "green" if health_score >= 90 else "yellow" if health_score >= 70 else "red"
    console.print(f"\n[bold]Overall Health Score:[/bold] [{color}]{health_score}%[/{color}]")

    table = Table(box=None, padding=(0, 2))
    table.add_column("Metric", style="cyan"); table.add_column("Status", style="magenta")
    for m, s in stats.items(): table.add_row(f"{m.capitalize()}:", s)
    
    console.print(table)
    console.print(f"\n[bold yellow]Pulse Insight:[/bold yellow]\n{ai_insight}\n")

if __name__ == "__main__":
    main()