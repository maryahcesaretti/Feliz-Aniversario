from flask import Flask, render_template, request

app = Flask(__name__)

# Keep ONE dictionary of codes (all in one place)
CODES = {
    "DINNER01": "🍽️ Dinner date unlocked! You choose the place (plsss), I choose the dessert!",
    "COFFEE02": "☕ Coffee and a sweet treat!",
    "LOVE": "You found the secret❤️",
    "PIGEON": "This is a special code for you! 🕊️",
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/letter")
def letter():
    return render_template("letter.html")

@app.route("/secret", methods=["GET", "POST"])
def secret():
    ok = False
    message = ""
    perfill_code = ""
    tried = False   # 👈 NEW (this fixes your problem)

    if request.method == "POST":
        tried = True
        perfill_code = request.form.get("code", "").strip()
        code = perfill_code.upper()

        if code in CODES:
            ok = True
            message = CODES[code]
        else:
            message = "❌ Invalid code. Try again!"

    return render_template(
        "secret.html",
        ok=ok,
        message=message,
        perfill_code=perfill_code,
        tried=tried
    )

@app.route("/pigeon")
def pigeon():
    return render_template("pigeon.html")

if __name__ == "__main__":
    app.run(debug=True)
