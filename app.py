from flask import Flask, render_template, request

app = Flask(__name__)

# Simple phishing logic (rule-based for diploma level)
def detect_phishing(url):
    suspicious_words = ["login", "verify", "secure", "bank", "account", "update"]
    if not url.startswith("https"):
        return "PHISHING"
    if any(word in url.lower() for word in suspicious_words):
        return "PHISHING"
    return "SAFE"

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    score = None
    features = None
    url = None

    if request.method == "POST":
        url = request.form["url"]
        result = detect_phishing(url)

        score = 20 if result == "SAFE" else 85

        features = {
            "HTTPS Enabled": "Yes" if url.startswith("https") else "No",
            "URL Length": len(url),
            "Suspicious Keywords": "Detected" if result == "PHISHING" else "None",
            "IP Address Used": "Yes" if url.replace(".", "").isdigit() else "No"
        }

    return render_template(
        "index.html",
        result=result,
        score=score,
        features=features,
        url=url
    )

if __name__ == "__main__":
    app.run(debug=True)
