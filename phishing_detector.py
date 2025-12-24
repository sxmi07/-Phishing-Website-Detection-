import re

def is_phishing(url):
    score = 0

    if len(url) > 75:
        score += 1

    if "@" in url or "-" in url:
        score += 1

    if not url.startswith("https"):
        score += 1

    if re.search(r"\d+\.\d+\.\d+\.\d+", url):
        score += 1

    suspicious_words = ["login", "verify", "bank", "free", "update"]
    for word in suspicious_words:
        if word in url.lower():
            score += 1

    return "PHISHING" if score >= 3 else "SAFE"
