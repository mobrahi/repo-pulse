# ⚡ Repo-Pulse


<img width="588" height="220" alt="Screenshot 2026-02-14 at 13 34 42" src="https://github.com/user-attachments/assets/740a2bc2-6c47-4232-a7cb-62ee92642b6b" />


> **Note:** This project was built for the [GitHub Copilot CLI Challenge](https://dev.to/challenges/github-2026-01-21). It showcases how AI-pair programming with GitHub Copilot (using the Claude 4.5 Haiku model) can accelerate the creation of robust developer tools.

**Repo-Pulse** is a lightweight CLI utility designed to give you a 30-second health check on any Python repository. It analyzes documentation, commit history, project size, and hygiene metrics to give you an actionable health score.

How do you know if your repository is "open-source ready"? Usually, it’s a manual checklist. I wanted to automate that "vibe check." Introducing **Repo-Pulse**, a CLI tool that gives your project a health score in seconds.

## **How I Built It (with GitHub Copilot + Claude 4.5 Haiku)**

This project was a collaboration between human intent and AI precision. I used the **GitHub Copilot CLI** powered by **Claude 4.5 Haiku** to:

* **Architect the Quality Gates:** The AI helped me enforce strict type-hinting and PEP 8 standards from the very first line.
* **Refine the Logic:** We used Copilot to brainstorm the `_count_files` algorithm, ensuring it accurately skips hidden environments like `.venv` and `node_modules` using `pathlib.parts`.
* **Iterative Debugging:** When I wanted to add a `--fix` flag, Copilot generated the boilerplate for `argparse` and the file templates instantly, allowing me to focus on the scoring logic.

## **The "Secret Sauce"**

The real power of **Claude 4.5 Haiku** in this challenge was its ability to maintain context. It didn't just write functions; it understood the "Quality Gate" requirements I was aiming for, ensuring every function had:

1. Proper return type signatures.
2. Clean docstrings.
3. Robust error handling for Git-less environments.

## **Features**

* 📊 **Scoring Engine:** A weighted algorithm (0–100%) checking Docs, Commits, Size, and Hygiene.
* 🛠 **Auto-Remediation:** `repo-pulse --fix` creates your missing `LICENSE` and `.gitignore` on the fly.
* 🎨 **Rich Terminal UI:** A beautiful, scannable dashboard for your project status.
* 🚀 **Global Command:** Install it once and run it anywhere.


## **Final Results**

I started with a sparse script and ended with a 100% health-rated, globally installable CLI tool. The combination of Copilot’s speed and Haiku’s logical reasoning turned a 3-hour task into a 30-minute sprint.

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

- Docs: Checks for presence of README files.

- Commits: Analyzes git history for professional patterns.

- Size: Ensures the repo isn't bloated with unignored env folders.

- Hygiene: Checks for vital LICENSE and .gitignore files.


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

## 🏁 Challenge Requirements Checklist

To ensure **Repo-Pulse** met the gold standard of the **GitHub Copilot CLI Challenge**, the following criteria were prioritized:

* **[x] Built with GitHub Copilot CLI:** Leveraged the CLI (Claude 3.5 Haiku) for architecture, logic refinement, and debugging.
* **[x] Productivity Focused:** Solves the manual "repo cleanup" bottleneck with a 30-second automated check.
* **[x] Quality Gates:** Implemented strict Python type-hinting, docstrings, and PEP 8 standards via AI-pair programming.
* **[x] Zero-Friction Testing:** No external API keys or login credentials required; works out of the box for judges.
* **[x] Auto-Remediation:** Includes a `--fix` flag to bridge the gap between "identifying a problem" and "solving it".

## 🤝 How to Contribute 

If you want to keep the momentum going after the challenge, add this:

```markdown
## 🤝 Contributing
I have big plans for the [Future Roadmap](#future-roadmap)! If you want to help add multi-language support or CI/CD templates:
1. Fork the repo.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

```

## 💡 Closing Statement 

The ultimate goal for **Repo-Pulse** is to become the standard 'Pre-Flight Check' for every developer. Whether you're starting a weekend hobby project or maintaining a massive enterprise codebase, Repo-Pulse ensures your foundation is rock solid.

---









