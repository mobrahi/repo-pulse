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

---

