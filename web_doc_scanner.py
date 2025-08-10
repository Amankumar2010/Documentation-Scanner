import requests
from bs4 import BeautifulSoup
import language_tool_python
import sys
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

tool = language_tool_python.LanguageTool('en-US')

def fetch_text_from_url(url):
    """Download text from Markdown/raw text/HTML."""
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"❌ Failed to fetch {url}")

    content_type = response.headers.get("Content-Type", "")

    if "text/markdown" in content_type or url.endswith(".md"):
        return response.text
    elif "text/plain" in content_type or url.endswith(".txt"):
        return response.text
    else:
        # Assume HTML, extract visible text
        soup = BeautifulSoup(response.text, "html.parser")
        text = "\n".join(soup.stripped_strings)
        return text

def highlight_error(line_text, match):
    """Highlight the incorrect word in red within the line."""
    start = match.offsetInContext
    end = start + match.errorLength
    return (
        line_text[:start]
        + Fore.RED + line_text[start:end] + Style.RESET_ALL
        + line_text[end:]
    )

def scan_text(text, auto_fix=False):
    """Scan text for issues and optionally fix them."""
    lines = text.splitlines()
    matches = tool.check(text)

    if matches:
        print(f"🔍 Found {len(matches)} issue(s)")

        for match in matches[:5]:  # Show first 5
            line_num = text[:match.offset].count("\n") + 1
            line_text = lines[line_num - 1] if line_num <= len(lines) else ""
            highlighted_line = highlight_error(line_text, match)
            suggestion = match.replacements[0] if match.replacements else "(no suggestion)"

            print(f"\n🔹 Line {line_num}: {highlighted_line}")
            print(f"   ❌ Problem: {match.message}")
            print(f"   ✅ Suggestion: {Fore.GREEN}{suggestion}{Style.RESET_ALL}")

        if auto_fix:
            corrected_text = tool.correct(text)
            with open("corrected_from_web.txt", "w", encoding="utf-8") as f:
                f.write(corrected_text)
            print("\n✅ Corrected version saved as corrected_from_web.txt")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 web_doc_scanner.py <URL> [--fix]")
        sys.exit(1)

    url = sys.argv[1]
    auto_fix = "--fix" in sys.argv
    text = fetch_text_from_url(url)
    scan_text(text, auto_fix)
