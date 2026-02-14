# ⚡ Repo-Pulse

**Repo-Pulse** is a lightweight CLI utility designed to give you a 30-second health check on any Python repository. It analyzes documentation, commit history, project size, and hygiene metrics to give you an actionable health score.

## ✨ Features
- 📊 **Instant Health Score:** Get a weighted percentage of your project's readiness.
- 🧹 **Auto-Fix:** Use `--fix` to automatically generate missing `LICENSE` and `.gitignore` files.
- 🎨 **Beautiful UI:** Powered by `Rich` for a terminal experience that doesn't hurt your eyes.
- 🚀 **Global Command:** Install it once and run it anywhere.

## 🚀 Installation

Clone the repo and install in editable mode:
```bash
git clone [https://github.com/your-username/repo-pulse.git](https://github.com/your-username/repo-pulse.git)
cd repo-pulse
pip install -e .
```

## 🛠 Usage

Check your project health:
```bash
repo-pulse
```
Automatically fix missing hygiene files:
```bash
repo-pulse --fix
```

## 📊 How it Scores

Docs: Checks for presence of README files.

Commits: Analyzes git history for professional patterns.

Size: Ensures the repo isn't bloated with unignored env folders.

Hygiene: Checks for vital LICENSE and .gitignore files.


## 🗺️ Future Roadmap: The Pulse Evolves

While the current version of **Repo-Pulse** provides a solid foundation, I have big plans for its evolution. My goal is to move from "Checking the Vitals" to "Predicting the Health."

#### 🟢 Phase 1: Deep Analysis (Near-Term)

* **Dependency Audit:** Integrate a check for outdated or vulnerable packages in `requirements.txt` or `pyproject.toml`.
* **Code Coverage Integration:** Automatically detect `pytest` or `unittest` suites and report the percentage of code covered by tests.
* **Linter Synergy:** Add a "Style" metric by running a fast linter like **Ruff** in the background.

#### 🟡 Phase 2: Automation & CI/CD (Mid-Term)

* **GitHub Actions Template:** A command like `repo-pulse --generate-action` to automatically create a `.github/workflows/pulse.yml` file.
* **Pre-Commit Hook:** Allow users to install Repo-Pulse as a pre-commit hook so they can never commit a "75% healthy" repo again.

#### 🔴 Phase 3: The Ecosystem (Long-Term)

* **Custom Rulebooks:** Allow teams to define their own `pulse.yaml` to set custom thresholds (e.g., "Documentation is required for 100% score, but hygiene is optional").
* **Multi-Language Support:** Expand beyond Python to detect health markers for JavaScript (npm/yarn) and Rust (cargo) projects.

---

## 💡 Closing Statement 

The ultimate goal for **Repo-Pulse** is to become the standard 'Pre-Flight Check' for every developer. Whether you're starting a weekend hobby project or maintaining a massive enterprise codebase, Repo-Pulse ensures your foundation is rock solid.

---


