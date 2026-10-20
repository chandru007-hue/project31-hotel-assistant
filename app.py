from flask import Flask, render_template, request
from graph import hotel_assistant

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None
    answer = None
    question = ""
    if request.method == "POST":
        action = request.form.get("action", "estimate")
        if action == "estimate":
            try:
                nightly_rate = float(request.form.get("nightly_rate", ""))
                checkout_time = request.form.get("checkout_time", "").strip()
                result = hotel_assistant({
                    "action": "calculate_late_checkout",
                    "nightly_rate": nightly_rate,
                    "checkout_time": checkout_time
                })
                if "error" in result:
                    error = result["error"]
                    result = None
            except (TypeError, ValueError):
                error = "Enter a valid positive nightly room rate."
        elif action == "ask":
            question = request.form.get("question", "").strip()
            response = hotel_assistant({"action": "ask_question", "question": question})
            answer = response.get("answer")
    return render_template("index.html", result=result, error=error, answer=answer, question=question)

if __name__ == "__main__":
    app.run(debug=True)
