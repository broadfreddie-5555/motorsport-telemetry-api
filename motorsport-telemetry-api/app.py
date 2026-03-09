from flask import Flask, request, jsonify
from models import db, Telemetry

app = Flask(__name__)

# SQLite database file will be created in this folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///telemetry.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

# Create tables once on startup
with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return {"message": "Motorsport Telemetry API is running"}

@app.route("/telemetry", methods=["GET"])
def get_telemetry():
    driver = request.args.get("driver")

    if driver:
        telemetry = Telemetry.query.filter_by(driver_name=driver).all()
    else:
        telemetry = Telemetry.query.all()

    return jsonify([t.to_dict() for t in telemetry])

@app.route("/telemetry", methods=["POST"])
def create_telemetry():
    data = request.get_json() or {}

    required = [
        "driver_name",
        "track",
        "lap_number",
        "tyre_compound",
        "sector1",
        "sector2",
        "sector3",
        "top_speed",
    ]

    missing = [field for field in required if field not in data]
    if missing:
        return jsonify({"error": f"Missing fields: {', '.join(missing)}"}), 400

    telemetry = Telemetry(
        driver_name=data["driver_name"],
        track=data["track"],
        lap_number=int(data["lap_number"]),
        tyre_compound=data["tyre_compound"],
        sector1=float(data["sector1"]),
        sector2=float(data["sector2"]),
        sector3=float(data["sector3"]),
        top_speed=float(data["top_speed"]),
    )

    db.session.add(telemetry)
    db.session.commit()

    return jsonify(telemetry.to_dict()), 201

@app.route("/telemetry/best", methods=["GET"])
def get_best_lap():
    driver = request.args.get("driver")

    if not driver:
        return jsonify({"error": "Driver parameter is required"}), 400

    best_lap = (
        Telemetry.query
        .filter_by(driver_name=driver)
        .order_by((Telemetry.sector1 + Telemetry.sector2 + Telemetry.sector3).asc())
        .first()
    )

    if not best_lap:
        return jsonify({"error": "No laps found for this driver"}), 404

    return jsonify(best_lap.to_dict())

@app.route("/track/fastest", methods=["GET"])
def fastest_driver_on_track():
    track = request.args.get("track")

    if not track:
        return jsonify({"error": "Track parameter is required"}), 400

    fastest = (
        Telemetry.query
        .filter_by(track=track)
        .order_by((Telemetry.sector1 + Telemetry.sector2 + Telemetry.sector3).asc())
        .first()
    )

    if not fastest:
        return jsonify({"error": "No telemetry found for this track"}), 404

    return jsonify(fastest.to_dict())

if __name__ == "__main__":
    app.run(debug=True)