from flask import Flask, request, jsonify
from models import db, TelemetrySession

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///comparison.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return {"message": "Motorsport Telemetry Comparison API is running"}


@app.route("/sessions", methods=["GET"])
def get_sessions():
    driver = request.args.get("driver")
    track = request.args.get("track")

    query = TelemetrySession.query

    if driver:
        query = query.filter_by(driver_name=driver)
    if track:
        query = query.filter_by(track=track)

    sessions = query.all()
    return jsonify([session.to_dict() for session in sessions])


@app.route("/compare", methods=["GET"])
def compare_drivers():
    driver1 = request.args.get("driver1")
    driver2 = request.args.get("driver2")

    if not driver1 or not driver2:
        return jsonify({"error": "Both driver1 and driver2 are required"}), 400

    laps1 = TelemetrySession.query.filter_by(driver_name=driver1).all()
    laps2 = TelemetrySession.query.filter_by(driver_name=driver2).all()

    if not laps1 or not laps2:
        return jsonify({"error": "One or both drivers have no data"}), 404

    avg1 = sum(l.lap_time for l in laps1) / len(laps1)
    avg2 = sum(l.lap_time for l in laps2) / len(laps2)
    fastest1 = min(l.lap_time for l in laps1)
    fastest2 = min(l.lap_time for l in laps2)

    return jsonify({
    "driver1": driver1,
    "driver2": driver2,
    "driver1_avg_lap": round(avg1, 3),
    "driver2_avg_lap": round(avg2, 3),
    "driver1_fastest_lap": round(fastest1, 3),
    "driver2_fastest_lap": round(fastest2, 3),
    "faster_driver_average": driver1 if avg1 < avg2 else driver2,
    "faster_driver_fastest_lap": driver1 if fastest1 < fastest2 else driver2
})

@app.route("/driver/average", methods=["GET"])
def average_lap_time():
    driver = request.args.get("driver")

    if not driver:
        return jsonify({"error": "Driver parameter is required"}), 400

    laps = TelemetrySession.query.filter_by(driver_name=driver).all()

    if not laps:
        return jsonify({"error": "No data found for this driver"}), 404

    avg = sum(l.lap_time for l in laps) / len(laps)

    return jsonify({
        "driver": driver,
        "average_lap_time": round(avg, 3)
    })

if __name__ == "__main__":
    app.run(debug=True)

