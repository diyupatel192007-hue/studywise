from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load trained model
model = joblib.load("model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    study_hours = float(request.form["study_hours"])
    sleep_hours = float(request.form["sleep_hours"])
    phone_hours = float(request.form["phone_hours"])
    breaks = float(request.form["breaks"])
    exercise_hours = float(request.form["exercise_hours"])
    focus_level = float(request.form["focus_level"])
    stress_level = float(request.form["stress_level"])
    attendance = float(request.form["attendance"])

    input_data = [[
        study_hours,
        sleep_hours,
        phone_hours,
        breaks,
        exercise_hours,
        focus_level,
        stress_level,
        attendance
    ]]

    prediction = model.predict(input_data)[0]

    # Keep score between 0 and 100
    prediction = max(0, min(100, prediction))

    prediction = round(prediction, 2)

    if prediction >= 75:
        category = "High Efficiency"
    elif prediction >= 50:
        category = "Moderate Efficiency"
    else:
        category = "Low Efficiency"

    return render_template(
        "result.html",
        prediction=prediction,
        category=category,
        study_hours=study_hours,
        sleep_hours=sleep_hours,
        phone_hours=phone_hours,
        focus_level=focus_level,
        stress_level=stress_level
    )


if __name__ == "__main__":
    app.run(debug=True)