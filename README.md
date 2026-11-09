# Smart Code Review and Bug Prediction System

An AI-assisted Python code review application that combines static analysis, rule-based bug categorization, and Google Gemini explanations to help developers identify potential problems and improve code quality.

**Live Application:** [Open Smart Code Review](https://smart-code-review-xznhvw5tvwz7yiw2u6hr59.streamlit.app/)

**GitHub Repository:** [Smart-Code-Review](https://github.com/sumasri-14/Smart-Code-Review)

**Developer:** [sumasri-14](https://github.com/sumasri-14)

---

## Project Overview

Manual code review can make it difficult for beginners to identify syntax errors, unsafe coding patterns, and exception-handling problems.

This project provides a simple web application where users can paste Python code or upload a Python file, run static analysis, view categorized findings, and receive AI-generated explanations and recommendations.

The application uses Streamlit for its interface, Python AST for static analysis, and Google's Gemini API for AI-powered code review.

## Key Features

- **Python Code Input:** Paste code or upload `.py` files.
- **Static Code Analysis:** Detect selected coding issues using Python AST.
- **Syntax Error Detection:** Identify syntax errors and their line numbers.
- **Security Risk Detection:** Flag potentially unsafe uses of `eval()` and `exec()`.
- **Code Quality Analysis:** Identify bare exception handlers.
- **Bug Categorization:** Categorize detected findings into readable bug types.
- **Gemini AI Code Review:** Explain issues, their impact, and possible solutions.
- **Improvement Suggestions:** Receive beginner-friendly recommendations.

## Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| Frontend and Application UI | Streamlit |
| Static Analysis | Python AST |
| AI Integration | Google Gemini API |
| Gemini SDK | google-genai |
| Version Control | Git and GitHub |
| Deployment | Streamlit Community Cloud |

Scikit-learn, Pandas, and NumPy are included as dependencies for potential future extensions. They are not currently used for model training in this implementation.

## How the System Works

1. The user enters Python code or uploads a `.py` file.
2. The application sends the code to the static analyzer.
3. Python AST checks for syntax errors, unsafe function calls, and bare exception handlers.
4. Detected issues are passed to the bug categorization module.
5. Gemini receives the source code and static-analysis findings.
6. The application displays the detected issues, bug categories, and AI-generated review.

## Project Structure

```text
Smart-Code-Review/
│
├── app.py
├── analyzer.py
├── ai_review.py
├── bug_prediction.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/sumasri-14/Smart-Code-Review.git
cd Smart-Code-Review
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Gemini API

Create a `.streamlit` folder in the project root and create a file named `secrets.toml` inside it.

Add:

```toml
GEMINI_API_KEY = "your-gemini-api-key"
```

Get your API key from [Google AI Studio](https://aistudio.google.com/apikey).

**Security:** Never upload your API key or `secrets.toml` file to GitHub.

### 5. Run the application

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal.

## Live Deployment

The application is deployed using Streamlit Community Cloud.

**Live Demo:**  
https://smart-code-review-xznhvw5tvwz7yiw2u6hr59.streamlit.app/

To deploy your own copy:

1. Push the project to GitHub.
2. Sign in to [Streamlit Community Cloud](https://share.streamlit.io/).
3. Create a new application.
4. Select the repository and branch.
5. Set `app.py` as the main file.
6. Add `GEMINI_API_KEY` in the application's Secrets settings.
7. Save and deploy.

## Current Implementation Scope

The current static analyzer checks a limited set of patterns:

- Python syntax errors.
- Calls to `eval()` and `exec()`.
- Bare `except:` blocks.

Bug categorization is currently rule-based. It does not use a separately trained machine-learning classifier.

Gemini provides additional natural-language explanations and suggestions. Its responses should be reviewed before applying changes.

## Future Enhancements

- Expand static analysis to identify more potential bugs.
- Develop and evaluate a machine-learning bug classification model.
- Add coding-standard recommendations.
- Introduce retrieval-augmented generation (RAG).
- Add code similarity detection using embeddings.
- Support additional programming languages.
- Generate downloadable code review reports.

## License

Refer to the [LICENSE](LICENSE) file for licensing information.

---

**Developed by [sumasri-14](https://github.com/sumasri-14)**

*Smart Code Review and Bug Prediction System Using AI and Large Language Models.*
