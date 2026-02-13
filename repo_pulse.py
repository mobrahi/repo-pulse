import subprocess
import os
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

def run_copilot(prompt):
    try:
        result = subprocess.run(["copilot", "-p", prompt], capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except:
        return "[red]Error: Check Copilot CLI auth.[/red]"

def main():
    console.print(Panel("[bold blue]Repo-Pulse CLI[/bold blue]\n[italic]The 30-second Project Health Check[/italic]", expand=False))
    
    # Example logic: Commit Check
    with console.status("[bold green]Analyzing project pulse...") as status:
        # Mocking the prompt for the demo
        feedback = run_copilot("Summarize why a clear README is important for open source in 1 sentence.")
        
        table = Table(title="Project Health Report")
        table.add_column("Metric", style="cyan")
        table.add_column("Status", style="magenta")
        table.add_row("Documentation", "Scan Complete")
        table.add_row("Commit History", "Professional")
        
    console.print(table)
    console.print(f"\n[bold]Copilot Insight:[/bold] {feedback}")

if __name__ == "__main__":
    main()