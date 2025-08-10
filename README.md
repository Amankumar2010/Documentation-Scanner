# Documentation-Scanner
A simple python Document scanner which scans for spelling / punctuation errors.

# 📄 Web Docu Scanner  

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)](https://www.python.org/)  
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)  
[![Status](https://img.shields.io/badge/status-active-success)](#)  

> **Scan any webpage for grammar and spelling issues — fast and simple!** 🚀  

Web Docu Scanner fetches text from any public web page, checks it using **LanguageTool**, and shows you exactly what's wrong along with suggested fixes. Perfect for proofreading documentation, blogs, or articles directly from the web!  

---

## ✨ Features  

✅ Fetch content directly from a **URL**  
✅ Detect **grammar, spelling, and punctuation** errors  
✅ Show **exact problem lines** from the document  
✅ Provide **smart correction suggestions**  
✅ Works with **any public webpage** containing readable text  

---

## 📦 Requirements  

You’ll need **Python 3.7+** and the following libraries:  
```
pip install requests beautifulsoup4 language-tool-python
```

⚙️ Usage
Run the script with a webpage link:

```
python3 web_doc_scanner.py <URL>
```

Example:

```
python3 web_doc_scanner.py https://kubernetes.io/docs/tutorials/kubernetes-basics/
📊 Example Output
```

🔍 Issue found:
Line: Kubernetes is an open-sorce system for automating deployment.
❌ Problem: 'open-sorce' is a misspelling.
✅ Suggestion: open-source

📂 Project Structure
```
.
├── web_doc_scanner.py   # Main script
├── README.md            # Project documentation
```

⚠️ Notes
Works only with publicly accessible pages.

May not detect text inside JavaScript-rendered content.

Accuracy is based on LanguageTool's analysis.

📜 License
🆓 MIT License — use, modify, and share freely.
