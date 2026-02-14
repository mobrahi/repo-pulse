import subprocess
import os
from pathlib import Path
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()


def analyze_repo() -> tuple[dict[str, str], str]:
    """Analyze repository health and return metrics report and insight."""
    report: dict[str, str] = {
        "docs": "✅ Found",
        "commits": "✅ Professional",
        "size": "✅ Lean"
    }
    points = 3  # Start with max points
    insight: str = "Your repo looks healthy and ready for contributors!"

    # 1. Check for README
    if not os.path.exists("README.md"):
        report["docs"] = "❌ Missing"
        insight = "Critical: Add a README.md to help others understand your project."
        points -= 1

    # 2. Check Git History
    try:
        log = subprocess.check_output(
            ["git", "log", "-n", "5", "--pretty=format:%s"],
            text=True,
            stderr=subprocess.DEVNULL
        )
        if len(log.splitlines()) < 3:
            report["commits"] = "⚠️ Sparse"
            insight = "Tip: Try to provide more context in your commit messages."
    except subprocess.CalledProcessError:
        report["commits"] = "❓ No Git Found"
        points -= 1


    # 3. Check Repository Size
    file_count: int = _count_files()
    if file_count > 100:
        report["size"] = "⚠️ Large"
        points -= 0.5
    elif file_count < 5:
        report["size"] = "❌ Too Small"
        points -= 1

    # Calculate percentage: (points earned / total possible points) * 100
    score = int((max(0, points) / 3) * 100)

    return report, insight


def _count_files() -> int:
    """Count total tracked files in repository, excluding hidden dirs and venv."""
    excluded_dirs: set[str] = {
        ".git", ".github", ".venv", "venv", "__pycache__", ".pytest_cache",
        "node_modules", ".env", ".idea", ".vscode", "dist", "build"
    }
    file_count: int = 0

    for path in Path(".").rglob("*"):
        if path.is_file():
            parts = path.parts
            if not any(part in excluded_dirs or part.startswith(".") for part in parts):
                file_count += 1

    return file_count


def main() -> None:
    """Display repository health report."""
    console.rule("[bold blue]Repo-Pulse Analysis[/]")

    with console.status("[bold green]Calculating Pulse...") as status:
        stats, ai_insight = analyze_repo()

        table = Table(title="Project Health Report")
        table.add_column("Metric", style="cyan")
        table.add_column("Status", style="magenta")
        for metric, status_value in stats.items():
            table.add_row(metric.capitalize(), status_value)

    console.print(table)
    console.print(f"\n[bold yellow]Pulse Insight:[/bold yellow] {ai_insight}")


if __name__ == "__main__":
    main()