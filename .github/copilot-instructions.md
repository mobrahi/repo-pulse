# Copilot Instructions for repo-pulse

## Project Overview

**repo-pulse** is a lightweight CLI tool that performs rapid health checks on GitHub repositories. It analyzes documentation, commit history, and repository size to generate a quick project health report.

## Architecture

The project follows a simple, single-file structure:

- **repo_pulse.py** - Main entry point containing two key functions:
  - `analyze_repo()` - Performs health checks (README presence, commit history quality, repo size) and returns a report dict and insight string
  - `main()` - Renders the report using the Rich library with formatted tables and panels

The tool uses the **Rich** library for terminal output formatting and **python-dotenv** for environment configuration.

## Setup & Running

### Installation
```bash
pip install -r requirements.txt
```

### Running
```bash
python repo_pulse.py
```

The script runs a health check on the current working directory (must be a git repository).

## Key Conventions

1. **Health Check Metrics** - The `analyze_repo()` function returns a dictionary with three main metrics: `docs`, `commits`, and `size`. Each maps to a status string with emoji indicators (✅, ❌, ⚠️, ❓).

2. **Status Format** - Status values follow the pattern: `"[emoji] [descriptor]"` (e.g., "✅ Found", "❌ Missing", "⚠️ Sparse")

3. **AI Insights** - The function generates a human-readable insight string that provides actionable guidance based on the analysis. Update the `insight` variable alongside any new health checks.

4. **Error Handling** - Git operations are wrapped in try-except blocks since the tool may run in non-git directories. Gracefully degrade with question mark emoji (❓).

5. **Dependencies** - Rich is used exclusively for terminal output. Console calls go through the global `console` object defined at module level.

## Quality Gate

- **PEP 8 Compliance** - All Python code must follow PEP 8 standards. Use consistent indentation (4 spaces), naming conventions (snake_case for functions/variables, PascalCase for classes), and line length limits.
- **Type Hinting** - Function signatures must include type hints for parameters and return types. Example: `def analyze_repo() -> tuple[dict, str]:`
- **Error Reporting** - All error messages and user-facing output must be reported through the Rich console object (`console.print()`, `console.rule()`, etc.), never via print() or standard output.

## Testing

Currently no automated tests exist. To manually verify changes:
1. Run the script: `python repo_pulse.py`
2. Test in a valid git repo to see full output
3. Test in a non-git directory to verify error handling

## Notes

- The `.env` file is configured for the project but currently unused
- The tool is designed to be run from the command line as a single-purpose utility
